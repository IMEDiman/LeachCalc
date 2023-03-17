import sys
import os
from scipy.interpolate import RectBivariateSpline
from datetime import datetime
font = {'size'   : 7}

import numpy as np
import argparse
from data.version import version


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

        print("valid input")
        self.dt50_a = [1,2,3,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,95,100,105,115,120,125,135,145,155,165,175,185,205,225,245,265,285,305,325,345,365]
        self.koc_a = [0,2,4,6,8,10,20,40,60,80,100,200,400,600,800,1000,2000,4000,6000,8000,10000]  
        self.koc_setRange = [min(self.koc_a), 10000]
        self.dt50_setRange = [min(self.dt50_a), max(self.dt50_a)]

        if len(input_array.input)==3:
            self.subst_name = [input_array.input[0]]
            if self.koc_setRange[0] < float(input_array.input[1]) < self.koc_setRange[1] and\
                self.dt50_setRange[0] < float(input_array.input[2])  < self.dt50_setRange[1]:
                koc = [float(input_array.input[1])]
                dt50 = [float(input_array.input[2])]
            else:
                print(input_array.input[0]+"'s input not in valid range: Koc in [0;10,000] mL/g, DegT50 in [0;365] d")
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
            f.write("# Substance name\tKoc\tDegT50\tLeaching\tMobility\n")
            print("### Results ###")
            print("Substance name\t\tKoc\tDegT50\tLeaching   Mobility")

        self.dataTable()
        self.interpolated = RectBivariateSpline(self.koc_a, self.dt50_a, self.data_table)
        if input_array.plot:

            self.plotInit( width=3.5, height=3.0,dpi=100)
            #self.pdf = backend_pdf.PdfPages("./.pdf")
       # self.plot(newdt50, newkoc, newdata)


        #calls
        newdt50 = self.dt50_a
        newdt50 = np.linspace(min(self.dt50_a),max(self.dt50_a),1000)
        newkoc = self.koc_a
        newkoc = np.logspace(0,2.85,1000)
        newkoc = np.logspace(0,4.00,1000)
        newdata = self.data_table
        newdata = self.interpolated(newkoc,newdt50)
        for isub in range(len(self.subst_name)):
            res_perc, mobility, res_report = self.result(koc[isub],dt50[isub],self.subst_name[isub])
            with open(rep_file,'a') as f:
                f.write(self.subst_name[isub] + "\t" + str(koc[isub]) + "\t" + str(dt50[isub]) + "\t" + str(round(res_perc*100,2)) + "\t" + mobility + "\n")
                if len(self.subst_name[isub]) > 20:
                    substname = self.subst_name[isub][:20]+"..."
                else:
                    substname = self.subst_name[isub]
                print(substname.ljust(22) + "\t" + str(koc[isub]) + "\t" + str(dt50[isub]) + "\t" + str(round(res_perc*100,2)).ljust(8) + "   " + mobility + "")
                if input_array.report:
                    f.write(res_report+"\n\n")

 
            if input_array.plot:
                
                self.plot(newdt50, newkoc, newdata)
                self.setCross(koc[isub],dt50[isub],self.subst_name[isub])
                self.saveFig(self.subst_name[isub]+"_"+str(koc[isub])+"_"+str(dt50[isub])+".png")
        
        print("###############")
        if input_array.plot:
            print("plots created in results folder")
        if input_array.report:
            print("reports created in results folder")

    def readInputFile(self,filename):
        lines = None
        substances = []
        kocs = []
        dt50s = []
        with open(filename,"r") as f:
            lines = f.readlines()
        for line in lines:
            print([line])
            if line[0] == "#":
                continue
            try:
                data = line.replace("\n","").split("\t")
                a,b,c = (data[0],float(data[1]),float(data[2]))
            except Exception as e:
                print(e)
                continue
            if self.koc_setRange[0] < float(data[1]) < self.koc_setRange[1] and\
                self.dt50_setRange[0] < float(data[2]) < self.dt50_setRange[1]:
                #substances.append(data[0].replace("/","-").replace("\\","-"))
                substances.append(data[0])
                kocs.append(float(data[1]))
                dt50s.append(float(data[2]))
            else:
                print(data[0]+"'s input not in valid range: Koc in [0;10,000] mL/g, DegT50 in [0;365] d")

                print("substances",substances,kocs,dt50s)

        print("return")
        return substances,kocs,dt50s
        

    def saveFig(self,savename):
        self.fig.savefig("results/"+savename,dpi=300)
        pass

    def dataTable(self):
        """
            dt50-koc table calculated with FOCUS PELMO with 
            dt50 =  [1,2,3,10,20,30,40,50,60,70,80,100,120]
            koc =  [0,2,4,6,8,10,20,40,60,80,100,200,400]
            freundlich exponent = 1.0
        """
        
        self.data_table = [[0.00462634,0.006528688,0.009556599,1.60E-02,0.036047824,6.02E-02,0.086214769,0.111732917,0.137577778,0.165461574,0.192853704,0.218583796,0.242362037,0.264701852,0.286775463,0.308496759,0.32989537,0.350017593,0.369511111,0.387417593,0.420681481,0.436383796,0.452689815,0.482143519,0.495490741,0.508416667,0.533106481,0.556166667,0.577990741,0.598333333,0.617694444,0.636550926,0.675634259,0.710564815,0.742412037,0.772263889,0.80075463,0.828490741,0.85437963,0.877986111,0.900481481],\
[0.002317244,0.003738617,0.005834387,1.06E-02,0.027593287,4.84E-02,0.071379722,9.44E-02,0.117616204,0.143381944,0.169956481,0.195133333,0.21873287,0.240741204,0.262003704,0.283130093,0.304148611,0.324948611,0.344962037,0.363535185,0.397387037,0.413050926,0.428413889,0.45887037,0.473365741,0.486981481,0.512916667,0.536782407,0.558962963,0.580023148,0.599773148,0.618462963,0.653138889,0.687078704,0.718689815,0.746930556,0.774189815,0.799828704,0.824615741,0.849296296,0.873185185],\
[0.001260637,0.002173573,0.003570866,7.14E-03,0.020959491,3.92E-02,0.059800648,8.10E-02,0.102481481,0.125687963,0.150450463,0.174536574,0.197315278,0.218934722,0.239762963,0.259726852,0.279359259,0.299383333,0.319086574,0.338216667,0.373868981,0.390048148,0.405640278,0.435000463,0.449592593,0.463819444,0.490694444,0.515240741,0.53837037,0.560259259,0.581097222,0.600564815,0.635787037,0.667685185,0.698486111,0.727384259,0.754949074,0.780263889,0.804675926,0.828125,0.850296296],\
[0.000700707,0.001288937,0.002180849,4.92E-03,0.016168009,3.20E-02,0.050161944,6.98E-02,0.089897917,0.110717222,0.133794444,0.156799537,0.179157407,0.200303241,0.220706019,0.240357407,0.259191667,0.277298611,0.296019907,0.314946296,0.351082407,0.368295833,0.384272685,0.414016204,0.428342593,0.44250463,0.469226852,0.494222222,0.517412037,0.538990741,0.559912037,0.579828704,0.616643519,0.650486111,0.681555556,0.710115741,0.736787037,0.761574074,0.785402778,0.808578704,0.830851852],\
[0.000397249,0.000780857,0.001366816,3.47E-03,0.012638264,2.61E-02,0.042272639,6.00E-02,0.079149815,9.80E-02,0.119187037,0.140673148,0.162262037,0.183169444,0.203058796,0.222384259,0.241053704,0.259406944,0.276937037,0.293789352,0.32895,0.346040741,0.362669444,0.393536574,0.407850463,0.421687963,0.448944444,0.474486111,0.498347222,0.520712963,0.541518519,0.561296296,0.598537037,0.632805556,0.664032407,0.692652778,0.719865741,0.745009259,0.768300926,0.790166667,0.810884259],\
[0.000229635,0.000483159,0.000881264,2.50E-03,0.010023204,0.021519213,0.035709954,5.17E-02,0.069535,8.73E-02,0.106036296,0.126043056,0.146437963,0.166619907,0.18615463,0.205403241,0.224079167,0.241970833,0.259452778,0.276043981,0.309071296,0.325430556,0.341358333,0.372856481,0.387969907,0.40186713,0.428452315,0.45437963,0.478726852,0.501546296,0.523050926,0.543240741,0.580509259,0.614685185,0.646402778,0.675569444,0.702527778,0.727587963,0.751638889,0.774027778,0.795314815],\
[1.84E-05,5.41E-05,0.000142954,6.17E-04,0.003504556,8.63E-03,0.015798144,2.51E-02,0.036450463,4.91E-02,0.062684213,7.72E-02,0.091717593,0.106587731,0.122079259,0.13744537,0.153016204,0.168437963,0.183767593,0.198871296,0.228727778,0.243350463,0.257499537,0.284381481,0.297675926,0.310695833,0.33602963,0.360815741,0.384683796,0.407143519,0.42817963,0.447912963,0.486217593,0.521435185,0.553972222,0.585046296,0.613805556,0.640421296,0.66625463,0.690476852,0.712949074],\
[3.24E-07,2.19E-06,9.77E-06,6.69E-05,0.0005972,1.81E-03,0.003858134,6.91E-03,0.01100894,1.62E-02,0.022484583,2.97E-02,0.037787917,4.64E-02,0.055637083,6.53E-02,0.075468009,8.59E-02,0.096199213,0.106673102,0.12816912,0.139088889,0.150108796,0.172371759,0.183351852,0.194237963,0.215813889,0.23627037,0.255728241,0.274565741,0.292601389,0.310498611,0.344618056,0.376554167,0.405885648,0.433371296,0.459439815,0.484115741,0.508097222,0.531064815,0.552078704],\
[1.85E-08,2.05E-07,1.19E-06,1.05E-05,0.000129056,4.54E-04,0.001107114,2.22E-03,0.003926056,6.31E-03,0.009340403,1.30E-02,0.017235417,2.20E-02,0.027223704,3.29E-02,0.039031944,4.55E-02,0.052300185,5.95E-02,7.46E-02,0.082549028,9.07E-02,0.107177454,0.115572037,0.1240775,0.141276806,0.158496759,0.1755625,0.192343519,0.208959259,0.225348611,0.256999074,0.286753704,0.314164815,0.340124074,0.365232407,0.389575,0.412746296,0.434864815,0.456258796],\
[1.96E-09,2.84E-08,1.92E-07,2.03E-06,3.10E-05,1.34E-04,0.000371635,8.21E-04,0.00156328,2.67E-03,0.004175668,0.006026125,0.008284292,1.10E-02,0.01400981,0.01744,0.021231472,2.54E-02,0.029788977,3.45E-02,4.47E-02,0.050112685,5.58E-02,6.79E-02,0.074128843,8.05E-02,9.35E-02,0.106977546,0.120776852,0.134641296,0.14851,0.162354352,0.19043287,0.217775,0.244443056,0.269956019,0.294761574,0.318327778,0.341091667,0.363077315,0.384223611],\
[3.03E-10,5.11E-09,3.80E-08,4.77575E-07,8.62E-06,4.41E-05,0.000137316,3.34E-04,0.000673903,1.18E-03,1.90E-03,2.89E-03,4.16E-03,5.73E-03,7.57E-03,9.69E-03,1.21E-02,1.48E-02,1.77E-02,2.08E-02,2.79E-02,3.17E-02,3.58E-02,0.044402662,0.049059648,5.39E-02,6.39E-02,7.43E-02,8.52E-02,9.63E-02,0.10758662,0.119048287,0.142603796,0.166133657,0.189173194,0.212283796,0.235268981,0.257533333,0.279515741,0.301203241,0.321806019],\
[3.88E-13,8.35E-12,7.71E-11,1.20E-09,5.29E-08,4.48E-07,1.94E-06,6.76E-06,1.83E-05,4.08E-05,7.97E-05,1.41E-04,0.000232807,3.64E-04,0.000537487,7.63E-04,0.001046737,1.39E-03,0.001808908,2.30E-03,3.50E-03,0.004224246,5.03E-03,6.90E-03,0.007960601,9.11E-03,1.17E-02,1.45E-02,1.78E-02,2.13E-02,2.50E-02,2.91E-02,3.82E-02,4.81E-02,5.90E-02,7.06E-02,8.29E-02,9.57E-02,0.108721435,0.122070741,0.135471204],\
[1.17E-16,3.12E-15,3.33E-14,8.22E-13,4.51E-11,6.92E-10,5.39E-09,2.62E-08,9.84E-08,2.96E-07,7.71E-07,1.76E-06,3.55E-06,6.49E-06,1.11E-05,1.79E-05,2.76E-05,4.09E-05,5.88E-05,8.23E-05,1.49E-04,1.95E-04,2.51E-04,3.95E-04,0.000485417,5.89E-04,8.38E-04,1.15E-03,1.54E-03,2.01E-03,2.56E-03,3.20E-03,4.74E-03,6.66E-03,8.94E-03,1.16E-02,1.46E-02,1.80E-02,2.17E-02,2.58E-02,3.01E-02],\
[6.10E-19,1.70E-17,2.03E-16,6.55E-15,3.61E-13,7.25E-12,7.33E-11,4.97E-10,2.24E-09,8.03E-09,2.38E-08,5.96E-08,1.34E-07,2.76E-07,5.34E-07,9.52E-07,1.60E-06,2.56E-06,3.96E-06,5.97E-06,1.23E-05,1.70E-05,2.30E-05,4.00E-05,5.15E-05,6.54E-05,1.01E-04,1.50E-04,2.16E-04,2.99E-04,4.03E-04,0.000529419,8.60E-04,1.31E-03,1.89E-03,2.61E-03,3.49E-03,4.54E-03,5.74E-03,7.11E-03,8.62E-03],\
[1.17E-20,3.38E-19,4.36E-18,1.69E-16,8.91E-15,2.23E-13,2.78E-12,2.11E-11,1.08E-10,4.37E-10,1.41E-09,4.00E-09,1.02E-08,2.24E-08,4.51E-08,8.59E-08,1.55E-07,2.66E-07,4.40E-07,6.99E-07,1.60E-06,2.32E-06,3.28E-06,6.13E-06,8.18E-06,1.07E-05,1.77E-05,2.76E-05,4.13E-05,5.99E-05,8.43E-05,1.15E-04,2.02E-04,3.29E-04,5.04E-04,7.36E-04,1.03E-03,1.40E-03,1.85E-03,2.38E-03,3.00E-03],\
[4.91E-22,1.45E-20,2.00E-19,8.76E-18,4.49E-16,1.34E-14,1.91E-13,1.54E-12,8.66E-12,3.83E-11,1.38E-10,4.26E-10,1.10E-09,2.57E-09,5.56E-09,1.13E-08,2.17E-08,3.95E-08,6.83E-08,1.13E-07,2.79E-07,4.18E-07,6.11E-07,1.22E-06,1.66E-06,2.23E-06,3.86E-06,6.32E-06,9.88E-06,1.49E-05,2.17E-05,3.07E-05,5.71E-05,9.80E-05,1.58E-04,2.41E-04,3.52E-04,4.96E-04,6.76E-04,8.97E-04,1.16E-03],\
[0,1.79E-25,7.65E-24,4.40E-22,2.68E-20,1.19E-18,2.35E-17,2.27E-16,1.66E-15,8.57E-15,3.55E-14,1.35E-13,4.48E-13,1.33E-12,3.57E-12,8.85E-12,2.00E-11,4.15E-11,8.17E-11,1.53E-10,4.69E-10,7.76E-10,1.25E-09,2.96E-09,4.41E-09,6.42E-09,1.28E-08,2.40E-08,4.28E-08,7.22E-08,1.17E-07,1.85E-07,4.18E-07,8.60E-07,1.63E-06,2.90E-06,4.89E-06,7.85E-06,1.21E-05,1.80E-05,2.59E-05],\
[0,0,0,0,4.55E-26,6.62E-23,1.67E-21,1.78E-20,1.14E-19,6.21E-19,3.30E-18,1.51E-17,5.92E-17,2.02E-16,6.09E-16,1.66E-15,4.13E-15,9.59E-15,2.11E-14,4.36E-14,1.62E-13,2.95E-13,5.18E-13,1.48E-12,2.40E-12,3.82E-12,9.01E-12,1.98E-11,4.06E-11,7.92E-11,1.47E-10,2.62E-10,7.39E-10,1.85E-09,4.19E-09,8.79E-09,1.72E-08,3.17E-08,5.56E-08,9.35E-08,1.51E-07],\
[0,0,0,0,0,0,3.29E-24,5.32E-23,3.41E-22,1.99E-21,1.18E-20,5.57E-20,2.21E-19,7.55E-19,2.36E-18,6.55E-18,1.68E-17,4.05E-17,9.19E-17,1.97E-16,8.03E-16,1.53E-15,2.85E-15,8.97E-15,1.52E-14,2.51E-14,6.42E-14,1.53E-13,3.43E-13,7.26E-13,1.45E-12,2.76E-12,8.94E-12,2.53E-11,6.40E-11,1.48E-10,3.17E-10,6.36E-10,1.21E-09,2.17E-09,3.76E-09],\
[0,0,0,0,0,0,0,0,3.99E-24,2.98E-23,2.02E-22,9.59E-22,3.82E-21,1.33E-20,4.14E-20,1.14E-19,2.98E-19,7.23E-19,1.65E-18,3.60E-18,1.51E-17,2.99E-17,5.72E-17,1.86E-16,3.23E-16,5.50E-16,1.49E-15,3.74E-15,8.76E-15,1.93E-14,4.05E-14,8.12E-14,2.87E-13,8.78E-13,2.39E-12,5.92E-12,1.35E-11,2.88E-11,5.77E-11,1.10E-10,1.99E-10],\
[0,0,0,0,0,0,0,0,0,0,7.38E-24,3.63E-23,1.59E-22,5.57E-22,1.74E-21,4.84E-21,1.25E-20,3.03E-20,6.94E-20,1.51E-19,6.52E-19,1.32E-18,2.50E-18,8.34E-18,1.47E-17,2.52E-17,7.05E-17,1.84E-16,4.44E-16,1.01E-15,2.19E-15,4.52E-15,1.69E-14,5.46E-14,1.57E-13,4.09E-13,9.79E-13,2.18E-12,4.56E-12,9.04E-12,1.71E-11]]


        return

    def writeTable(self):
        tableStr = "KOC\\DT50"
        for dt50 in self.dt50_a:
            tableStr += "\t" + str(dt50)
        
        for i in range(len(self.koc_a)):
            tableStr += "\n" + str(self.koc_a[i])
            for j in range(len(self.dt50_a)):
                tableStr += "\t" + str(self.data_table[i][j])

        return

    def result(self,koc,dt50,subst):
#        self.interpolated = RectBivariateSpline(self.koc_a, self.dt50_a, self.data_table)
#        interpolated = RectBivariateSpline(self.dt50_a,self.koc_a,  self.data_table)
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
        result_text = ("With a KOC of "+str(koc) + " mL/g and a DT50 of " + str(dt50) + " d "\
        + str(round(result_perc*100,2))+" % of the substance could probably leach to a depth of 1m.\nSince the leaching is "+reason+" " + subst + " is considered "+mobility + ".")
        return result_perc, mobility, result_text




    def plotInit(self, width=5, height=4, dpi=100):
        import matplotlib
        matplotlib.rc('font', **font)
        import matplotlib.pyplot as plt

        self.fig,self.axes = plt.subplots(1,1,figsize=(width, height), dpi=dpi)
        self.fig.tight_layout()


    def plot(self,x,y,data):
        self.xarr = np.linspace(min(x),max(x),len(x))
        self.xarr = np.array(x)
#        self.xarr = np.logspace(np.log10(min(x)),np.log10(max(x)),1000)
        self.yarr = np.linspace(min(y),max(y),len(y))
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
#        if x<=100:
#            self.axes.set_xlim(0,150)
#        elif x<=900:
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

#        if y<= 50:
#            self.axes.set_ylim(0,70)

#        if x <= 900:
#            self.axes.set_xlim(0,1000)
#        if 900<x<=2500:
#            self.axes.set_xlim(0,3000)
#            self.axes.set_xscale("log")
#        elif 2500 < x <= 5500:
#            self.axes.set_xlim(0,6000)
#
#        print(self.xarr)
#        print(np.log(self.yarr))
#        self.axes.contourf(self.yarr,self.xarr,self.data,levels=[-1,0.01,0.1,1],colors=['green','yellow','red'])
        if subst == "":
            subst = "..."
        self.axes.set_title("Mobility of "+subst)
        self.axes.set_xlabel("KOC in mL/g")
        self.axes.set_ylabel("DegT50 in d")
#        self.axes.add_patch(Rectangle((-1,-1),.1,.1,color=('green'),label="immobile"))
#        self.axes.add_patch(Rectangle((-1,-1),.1,.1,color=('yellow'),label="mobile"))
#        self.axes.add_patch(Rectangle((-1,-1),.1,.1,color=('red'),label="very mobile"))
        self.axes.plot([x],[y],marker="x",color='purple',markersize=8)
        legend_elements = [\
            Rectangle((-1,-1),.1,.1,color=('green'),label="not mobile"),\
            Rectangle((-1,-1),.1,.1,color=('yellow'),label="mobile"),\
            Rectangle((-1,-1),.1,.1,color=('red'),label="very mobile"),\
            Line2D([0], [0], marker = "x", color="purple", label=subst, ls="")
                ]
       # if x > 400 and y > 200:
       #     self.axes.legend(bbox_to_anchor=(0.98,0.28), ncol=1 )
       # else:
       #     self.axes.legend(bbox_to_anchor=(0.98,0.98), ncol=1 )
        self.axes.legend(handles = legend_elements, bbox_to_anchor=(0.98,0.98), ncol=1 )
        self.fig.tight_layout()
##
        self.axes.margins(-0.001)
        #self.draw()


if __name__ == "__main__":
#    try:
#        with open("version.txt",'r') as f:
#            version = f.readline()
#    except FileNotFoundError:
#        version = "version not found"
    parser = argparse.ArgumentParser(description="Calculate the mobility of a substance in soil",prog='LEACHCALC')
    parser.add_argument('input', nargs='+', help="input: either a list consisting of a substance's name, its Koc in mL/g and DegT50 in d, or a file name")
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
            parser.print_help()
            print("\n#### You need to pass floats for Koc and DegT50")
            correct_input = False
    elif len(args.input) == 1:
        # input is a file name
        file_name = args.input[0]
        try:
            with open(file_name,'r') as f:
                pass
        except FileNotFoundError:
            parser.print_help()
            print("\n#### You need to pass an existing file")
            correct_input = False
    else:
        parser.print_help()
        print("\n#### Not a valid input style. Possible calls:\n#### python3 leachCalc_CLI.py -r -p subst1 200 200 \n#### or\n#### python3 leachCalc_CLI.py -r -p data\\testfile.txt")
        correct_input = False

    if correct_input:
        args = parser.parse_args()
        print("args",args)
        app = LeachCalc_CLI(args)
    else:
        pass
