import urllib
import tkMessageBox
import tkSimpleDialog
import tarfile
import Tkinter
import time
import os
import os.path
import tkFileDialog
root = Tkinter.Tk()
root.withdraw()

if not os.path.isfile("steamcmd.sh"): 
    tkMessageBox.showinfo("First Time Setup", "Downloading and extracting steamcmd. Please wait.")
    urllib.urlretrieve ("https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz", "steamcmd.tar.gz")
    time.sleep(0.5)
    tar = tarfile.open("steamcmd.tar.gz", "r:gz")
    tar.extractall()
    tar.close()
username = tkSimpleDialog.askstring("Username Entry", "Please enter your Steam Username")
password = tkSimpleDialog.askstring("Password Entry", "Please enter your Steam Password", show="*")
appid = tkSimpleDialog.askinteger("Enter App Id", "Enter the app id for the app that you wish to download (eg. 282440 for Quake Live)")
installdir = tkFileDialog.askdirectory()
os.system("sudo ./steamcmd.sh +@sSteamCmdForcePlatformType windows " + "+login " + username + " " + password + " +force_install_dir '" + installdir + "' " +  "+app_update " + str(appid) + " -validate"+ " +quit")
