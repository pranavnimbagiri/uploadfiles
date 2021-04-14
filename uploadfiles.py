import dropbox

class TransferData :
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,fileform,fileto):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(fileform,'rb')
        dbx.files_upload(f.read(),fileto)


def main():
    access_token='sl.Auzg57-C87IxEn9k0J0YYk3a1gVy9ugHBL4gZp0BhhyNVeMvocCKabwT5824L1Nfw2zIIeoWDoHouEmDr_zdKi52ll6gxkJZ6r6AUmBZR2xQ5PEJacv2wlZWvHKsaVXX47p1bPMG'
    transferdata=TransferData(access_token)   
    fileform=r'C:/Users/PRANAV/OneDrive/Desktop/python/sample.txt'
    fileto='/Dropbox/sample.txt'
    transferdata.upload_file(fileform,fileto)
    print("file has been moved")

main()