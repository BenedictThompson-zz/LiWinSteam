#!/usr/bin/env python3
# coding: utf-8
import urllib
import tkMessageBox
import tkSimpleDialog
import tarfile
import Tkinter
import time
from subprocess import Popen
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
dir_opt = {}
dir_opt['title'] = 'Please select a download location'
installdir = tkFileDialog.askdirectory(**dir_opt)
authkey = tkSimpleDialog.askstring("Auth Key", "If an Auth Key is required, please enter it below.")
if not authkey == "":
	authkey = (" "+authkey)
Popen("./steamcmd.sh +@sSteamCmdForcePlatformType windows " + "+login " + username + " " + password + authkey + " +force_install_dir '" + installdir + "' " +  "+app_update " + str(appid) + " -validate"+ " +quit", shell=True)

