from posixpath import relpath
import dropbox
import random
import os

from dropbox import files

class TransferData:

    def __init__(self,access_token):
          self.access_token = access_token

    def uploadFile(self,file_from,file_to):
    
         dbx=dropbox.Dropbox(self.access_token)

         for root,dirs,files,os.walk(file_from):
             for fileName in files:
                 localPath=os.path.join(root,fileName)
                 RelPath=os.path.relpath(localPath,file_from)
                 
                 dbxPath=os.path.join(file_to,RelPath)
                 with open(localPath,"rb") as f:
                    dbx.files_upload(f.read(),dbxPath,mode=dropbox.files.WriteMode.overwrite)      

        
def main():
    access_token="rScs3iFsAVAAAAAAAAAAAbI3tGyoEdvadOWeD6VnD2I_bAc7sqnuyMKpUP1dTQ0L"
    transferData=TransferData(access_token) 
    file_from=input("Enter The Folder Path To Upload")
    file_to=input("Enter The Path To DropBox")  

    transferData.UploadFiles(file_from,file_to) 
    print("Your File Has Been Uploaded! Check DropBox")   

main()
