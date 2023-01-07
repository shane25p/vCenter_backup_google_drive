#!/usr/bin/env python3

#
# apt-get install python3-pip -y
# pip install pydrive
# pip install PyDrive2    <==== For Large files

from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
   
# For using listdir()
import os
    
# Below code does the authentication
# part of the code
gauth = GoogleAuth()
  
# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)

vc_directory = '<google drive directory id>' ## File ID can be obtained from the we browser when you select the Google drive directory (The Directory ID will be in last on the URL)

### Move Old files to Trash ###

fileList = drive.ListFile({'q': "'<google drive directory id>' in parents and trashed=false"}).GetList()
for file in fileList:
  file_id = file['id']
  gfile_in = drive.CreateFile({'id': file_id})
  gfile_in.Trash()

### vCenter Backup Upload to Google Drive ###

local_vc_directory = "<directory of the file locally"
for f in os.listdir(local_vc_directory):
  filename = os.path.join(local_vc_directory, f)
  gfile = drive.CreateFile({'parents' : [{'id' : vc_directory}], 'title' : f})
  gfile.SetContentFile(filename)
  gfile.Upload()
