import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'ybSl6l68L60AAAAAAAAAAdmikpHEGxuWLE-Hu5sM4Wsp-7V1Ot9-AhSJ73ve_NMx'
    transferData = TransferData(access_token)

    file_from = input("Enter the file to be transfered : ")
    file_to = input("Enter the full path of the file to be uploaded : ")

    # API v2
    transferData.upload_file(file_from, file_to)

main()