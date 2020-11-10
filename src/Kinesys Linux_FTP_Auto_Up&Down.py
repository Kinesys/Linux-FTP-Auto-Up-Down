#Kinesys FTP_Auto_Up & Down.py
from ftplib import FTP
import os
import sys

#ftp의 파일리스트와 디렉토리 리스트 가져오기
def get_list_ftp(ftp, cwd, files = [], diretories = []):
    data = []

    ftp.cwd(cwd)

    #파일의 정보를 확인함
    ftp.dir(data.append)

    for item in data:
        pos = item.rfind(' ')

        name = cwd + item[pos + 1:]

        if item.find('<DIR>') > -1:
            diretories.append(name)

            get_list_ftp(ftp, name + '/', files, diretories)
        else:
            files.append(name)
        return files, diretories

def get_list_local(path, files = [], diretories = []):
    for files in os.listdir(path):
        item = path + file

    if os.path.isdir(item):
        diretories.append(item + "\\")

        get_list_local(item + "\\", files, diretories)
    else:
        files.append(item)

    return files, diretories
#FTP 부분
with FTP('localhost') as ftp:

    ftp.set_debuglevel(1)

    ftp.login('ID', 'PW')

    files, diretories = get_list_ftp(ftp, '/')

    diretories = diretories[::-1]

    for file in files:
        ftp.delete(file)

    for dir in diretories:
        ftp.rmd(dir)

#업로드 부분
with FTP('localhost') as ftp:

    ftp.set_debuglevel(1)

    ftp.login('ID', 'PW')
#파일을 업로드할 로컬 디렉터리 선택
    upload_path = ""

    files, diretories = get_list_local(upload_path)

    for diretory in diretories:

            path = diretory.replace(upload_path,  "").replace("\\", "/")

with open(file, 'rb') as localfile:
    ftp.storybinary('STOR' + path, localfile)

#콘솔 출력
print("upload files is " + path)

#다운로드

#서버에서 파일을 다운로드 할 로컬 디렉터리 지정
download_path = ""

files, diretories = get_list_ftp(ftp, '/')

for diretory in diretories:

    dir = download_path + diretory

    if os.path.isdir(dir) is False:
        os.mkdir(dir)

    #파일 다운로드
    for file in files:

        with open(download_path + file, 'wb') as localfile:

            ftp.retrbinary('RETR' + file, localfile.write)

#콘솔 출력
print('Download File in' + file)
