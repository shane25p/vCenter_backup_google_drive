# vCenter_backup_google_drive
This Script will upload the VMware backup to Google Drive

Please note this will NOT directly upload the backups from vCenter appliance, you will have to setup a Linux SFTP server. The files will be backed up from the SFTP server to Google Drive

### Pre-Requisite - Linux SFTP Server ###

Install the below packages on the server

$ apt-get install python3-pip -y
$ pip install PyDrive2

### Pre-Requisite - Google Drive ###

Create a google account and configure Google Drive API service
- Enable the Google Drive API: https://developers.google.com/drive/api/guides/enable-drive-api
- Please follow this Medium link to configure and download the json file: https://medium.com/@chingjunetao/simple-way-to-access-to-google-service-api-a22f4251bb52

Create settings.yaml file to avoid browser prompting for Google Drive Autherization
- example file added to the repository

