import sys
import os
from scipy.interpolate import RectBivariateSpline
from datetime import datetime
font = {'size'   : 7}

import numpy as np
import argparse
from data.version import version
from data.data_table import data_table

def printHeader():
    print("   __                 _       ___      _                              ")
    print("  / /  ___  __ _  ___| |__   / __\__ _| | ___                         ")
    print(" / /  / _ \/ _` |/ __| '_ \ / /  / _` | |/ __|                        ")
    print("/ /__|  __/ (_| | (__| | | / /__| (_| | | (__    Version: v"+version+"      ")
    print("\____/\___|\__,_|\___|_| |_\____/\__,_|_|\___|   Created: "+datetime.today().strftime("%d-%b-%Y")+" ")
    print("----------------------------------------------------------------------")
    print("Leaching Calculator for Assessing Mobility (c) D. Skodras             ")
    print("Internet: software.ime.fraunhofer.de                                  ")
    print("Contact:  dimitrios.skodras@ime.fraunhofer.de                         ")
    print("----------------------------------------------------------------------")
    print("")

leachability_path = None
if getattr(sys, 'frozen', False):
    leachability_path = os.path.dirname(sys.executable)
else:
    leachability_path = os.path.dirname(os.path.abspath(__file__))

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class LeachCalc_CLI():
    def __init__(self,input_array):
        printHeader()
        self.dt50_a = [1,2,3,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,95,100,105,115,120,125,135,145,155,165,175,185,205,225,245,265,285,305,325,345,365]
        self.koc_a = [0,2,4,6,8,10,20,40,60,80,100,200,400,600,800,1000,2000,4000,6000,8000,10000]  
        self.koc_setRange = [min(self.koc_a), 10000]
        self.dt50_setRange = [min(self.dt50_a), max(self.dt50_a)]

        if len(input_array.input)==3:
            self.subst_name = [input_array.input[0]]
            if self.koc_setRange[0] <= float(input_array.input[1]) <= self.koc_setRange[1] and\
                self.dt50_setRange[0] <= float(input_array.input[2])  <= self.dt50_setRange[1]:
                koc = [float(input_array.input[1])]
                dt50 = [float(input_array.input[2])]
                print("Valid Input: Substance name = "+input_array.input[0] + ", Koc = "+str(koc[0]) + " mL/g, DegT50 (@12°C) = " + str(dt50[0]) + " d.")
            else:
                print(input_array.input[0]+"'s input not in valid range: Koc in [0;10,000] mL/g, DegT50 (@12°C) in [1;365] d")
                print("type LEACHCALC_CLI.exe -h or python3 LeachCalc.py -h, respectively, for help")
                sys.exit()

        elif len(input_array.input)==1:
            filename = input_array.input[0]
            try:
                self.subst_name, koc, dt50 = self.readInputFile(filename)
            except ValueError:
                sys.exit()
        try:
            os.mkdir(leachability_path+"/results/")
        except FileExistsError:
            pass

        rep_file = "results/reports.txt"
        with open(rep_file,'w') as f:
            f.write("# Report file created "+datetime.now().strftime("%d.%m.%y - %H:%M")+"\n")
            f.write("# Substance name\tKoc\tDegT50(@12°C)\tLeaching\tMobility\n")
            print("------------------------------ Results -------------------------------")
            print("Substance name\t\tKoc\tDegT50(@12°C)\tLeaching   Mobility")

        self.dataTable()
        self.interpolated = RectBivariateSpline(self.koc_a, self.dt50_a, self.data_table)
        if input_array.plot:

            self.plotInit( width=3.5, height=3.0,dpi=100)

        #calls
        newdt50 = np.linspace(min(self.dt50_a),max(self.dt50_a),1000)
        newkoc = np.logspace(0,4.00,1000)
        newdata = self.interpolated(newkoc,newdt50)
        for isub in range(len(self.subst_name)):
            res_perc, mobility, res_report = self.result(koc[isub],dt50[isub],self.subst_name[isub])
            with open(rep_file,'a') as f:
                if self.koc_setRange[0] <= float(koc[isub]) <= self.koc_setRange[1] and\
                    self.dt50_setRange[0] <= float(dt50[isub]) <= self.dt50_setRange[1]:

                    f.write(self.subst_name[isub] + "\t" + str(koc[isub]) + "\t" + str(dt50[isub]) + "\t" + str(round(res_perc*100,2)) + "\t" + mobility + "\n")
                    if len(self.subst_name[isub]) > 20:
                        substname = self.subst_name[isub][:20]+"..."
                    else:
                        substname = self.subst_name[isub]
                    print(substname.ljust(22) + "\t" + str(koc[isub]) + "\t" + str(dt50[isub]) + "\t\t" + str(round(res_perc*100,2)).ljust(8) + "   " + mobility + "")
                    if input_array.report:
                        f.write(res_report+"\n\n")
                    if input_array.plot:
                        
                        self.plot(newdt50, newkoc, newdata)
                        self.setCross(koc[isub],dt50[isub],self.subst_name[isub])
                        self.saveFig(self.subst_name[isub]+"_"+str(koc[isub])+"_"+str(dt50[isub])+".png")

                else:
                    f.write(self.subst_name[isub] + "\t" + str(koc[isub]) + "\t" + str(dt50[isub]) + "\n")
                    print(self.subst_name[isub].ljust(22) + "\t" + str(koc[isub]) + "\t" + str(dt50[isub]) + "")

 
        
        print("----------------------------------------------------------------------")
        if input_array.plot:
            print("Plots created in results folder")
        if input_array.report:
            print("Full reports created in results folder")
        else:
            print("Reports created in results folder")


    def readInputFile(self,filename):
        lines = None
        substances = []
        kocs = []
        dt50s = []
        with open(filename,"r") as f:
            lines = f.readlines()
        for line in lines:
            if line[0] == "#":
                continue
            try:
                data = line.replace("\n","").split("\t")
                a,b,c = (data[0],float(data[1]),float(data[2]))
            except Exception as e:
                print(e)
                continue
            if self.koc_setRange[0] <= float(data[1]) <= self.koc_setRange[1] and\
                self.dt50_setRange[0] <= float(data[2]) <= self.dt50_setRange[1]:
                substances.append(data[0])
                kocs.append(float(data[1]))
                dt50s.append(float(data[2]))
            else:
                substances.append(data[0]+"'s values are not in valid ranges: Koc in [0;10,000] mL/g, DegT50 (@12°C) in [1;365] d")
                kocs.append(data[1])
                dt50s.append(data[2])

        return substances,kocs,dt50s
        

    def saveFig(self,savename):
        self.fig.savefig("results/"+savename,dpi=300)
        pass

    def dataTable(self):
        """
            dt50-koc table calculated with FOCUS PELMO
        """
        self.data_table = data_table
        return

    def result(self,koc,dt50,subst):
        result_perc = max(0.0,self.interpolated(koc,dt50)[0][0])
        mobility = None
        reason = None
        color = None
        if result_perc < 0.01:
            mobility = "not mobile"
            reason = "lower than 1%"
            color = "rgb(0,255,0)"
        elif 0.01 <= result_perc <= 0.1:
            mobility = "mobile"
            reason = "between 1% and 10%"
            color = "rgb(255,255,0)"
        else:
            mobility = "very mobile"
            reason = "larger than 10%"
            color = "rgb(255,0,0)"
        
        if subst =="":
            subst = "..."
        
        result_text = "With a Koc of "+str(koc) + " mL/g and a DegT50_soil of " + str(dt50) + " d " + str(round(result_perc*100,2)) + "% of the substance mass was calculated" \
                              +" to reach a soil depth of 1 m. Since the leachability is "+reason+" "+ subst+" is considered "+mobility + "."

        return result_perc, mobility, result_text




    def plotInit(self, width=5, height=4, dpi=100):
        import matplotlib
        matplotlib.rc('font', **font)
        import matplotlib.pyplot as plt

        self.fig,self.axes = plt.subplots(1,1,figsize=(width, height), dpi=dpi)
        self.fig.tight_layout()


    def plot(self,x,y,data):
        self.xarr = np.array(x)
        self.yarr = np.array(y)

#        yarr = np.array(y)
        self.data = np.array(data)
        self.data = self.data.T
        self.setCross(0,1)

    def setCross(self,x,y,subst="..."):
        from matplotlib.lines import Line2D
        from matplotlib.patches import Rectangle

        try:
            self.fig.delaxes(self.axes)
        except AttributeError:
            pass

        self.axes = self.fig.add_subplot(111)

        self.axes.contourf(self.yarr,self.xarr,self.data,levels=[-1,0.01,0.1,1],colors=['green','yellow','red'])
        if x<=900:
            self.axes.set_xlim(0,1000)
        elif 900<x<=2500:
            self.axes.set_xscale("log")
            self.axes.set_xlim(1,3000)
        elif 2500 < x <= 5500:
            self.axes.set_xscale("log")
            self.axes.set_xlim(1,6000)
        else:
            self.axes.set_xscale("log")

        if subst == "":
            subst = "..."
        self.axes.set_title("Mobility of "+subst)
        self.axes.set_xlabel("Koc in mL/g")
        self.axes.set_ylabel(r"DegT50$_{\rm soil}$ in d", fontstyle='normal')
        self.axes.plot([x],[y],marker="x",color='purple',markersize=8)
        legend_elements = [\
            Rectangle((-1,-1),.1,.1,color=('green'),label="not mobile"),\
            Rectangle((-1,-1),.1,.1,color=('yellow'),label="mobile"),\
            Rectangle((-1,-1),.1,.1,color=('red'),label="very mobile"),\
            Line2D([0], [0], marker = "x", color="purple", label=subst, ls="")
                ]
        self.axes.legend(handles = legend_elements, bbox_to_anchor=(0.98,0.98), ncol=1 )
        self.fig.tight_layout()
        self.axes.margins(-0.001)


if __name__ == "__main__":

    if "-h" in sys.argv:
        printHeader()

    parser = argparse.ArgumentParser(description="Calculate the mobility of a substance in soil",prog='LeachCalc_CLI')
    parser.add_argument('input', nargs='+', help="input: either a list consisting of a substance's name, its Koc in mL/g and DegT50 (@12°C) in d, or a file name")
    parser.add_argument('-p','--plot',action='store_true',help="if set, plot(s) are created")
    parser.add_argument('-r','--report',action='store_true',help="if set, report text(s) are created")
    parser.add_argument('-v','--version',action='version',version='%(prog)s '+version,help="show version and exit")
    args = parser.parse_args()

    correct_input = True
    if len(args.input) == 3:
        # input is a list with a name and two floats
        name = args.input[0]
        try:
            float1 = float(args.input[1])
            float2 = float(args.input[2])
        except ValueError:
            printHeader()
            parser.print_help()
            print("\n#### You need to pass floats for Koc and DegT50 (@12°C)")
            correct_input = False
    elif len(args.input) == 1:
        # input is a file name
        file_name = args.input[0]
        try:
            with open(file_name,'r') as f:
                pass
        except FileNotFoundError:
            printHeader()
            parser.print_help()
            print("\n#### You need to pass an existing file")
            correct_input = False
    else:
        printHeader()
        parser.print_help()
        print("\n#### Not a valid input style. Possible calls:\n#### python3 leachCalc_CLI.py -r -p subst1 200 200 \n#### or\n#### python3 leachCalc_CLI.py -r -p data\\testfile.txt")
        correct_input = False

    if correct_input:
        args = parser.parse_args()
#        print("args",args)
        app = LeachCalc_CLI(args)
    else:
        pass
