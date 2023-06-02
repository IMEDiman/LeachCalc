import sys
import os
import traceback
from datetime import datetime
import requests

leachability_path = None
if getattr(sys, 'frozen', False):
    leachability_path = os.path.dirname(sys.executable)
else:
    leachability_path = os.path.dirname(os.path.abspath(__file__))
    # utils in src, leachcalc.py one above
    leachability_path = os.path.dirname(os.path.abspath(__file__))+"\\.."

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def handler(_exception_type, _value, t):
    exc = traceback.TracebackException(_exception_type, _value, t)
    for frame_summary in exc.stack:
        frame_summary.filename = os.path.relpath(frame_summary.filename)

    with open(leachability_path+"\\LeachCalc.err", "a") as f:
        f.write(datetime.now().strftime("%d.%m.%y - %H:%M") + "\n")
        f.write("".join(exc.format()))
        f.write("### Please contact the author via https://github.com/IMEDiman/LeachCalc/issues ###\n")
    return 

def checkVersion():
    url = "https://software.ime.fraunhofer.de/Leaching_Calculator/"
    try:
        req = requests.get(url).text
    except Exception as e:
        handler(type(e),e,e.__traceback__)
        return 2

    req = req.split("href=")
    print(req)
    url_version_mod_date = ""
    for r in req:
        if "leachcalc.exe" in r.lower():
            url_version_mod_date = datetime.strptime(r.split('"right">')[1][:16],"%Y-%m-%d %H:%M")
            break
    print("mod date",[url_version_mod_date])
    if not url_version_mod_date:
        return 3

    try:
        local_version_mod_date = datetime.fromtimestamp(os.path.getmtime(leachability_path+"\\LeachCalc.exe"))
        if url_version_mod_date > local_version_mod_date:
            return 0
        else: 
            return 1

    except FileNotFoundError:
        try:
            local_version_mod_date = datetime.fromtimestamp(os.path.getmtime(leachability_path+"\\dist\\LeachCalc.exe"))
            if url_version_mod_date > local_version_mod_date:
                return 0
            else: 
                return 1

        except FileNotFoundError:
            pass

    return 4
