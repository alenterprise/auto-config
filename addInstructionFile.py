import requests
import csv 
import sys


requests.packages.urllib3.disable_warnings()


############# VARIABLES A REMPLIR (IP OV , user et password) ###########

OmniVistaIP = "192.168.115.251"
userOV = "admin"
passwordOV = "switch"

#########################################################################

filename = sys.argv[1]

url0 = "https://"+OmniVistaIP+"/rest-api/login"  # Remplacez l'URL par celle de l'API que vous souhaitez appeler
headers0 = {
    "Content-Type": "application/json"  # Spécifiez le type de contenu de la requête
}

data0 = {
    "userName": userOV,
    "password": passwordOV
}

response = requests.post(url0, headers=headers0, json=data0, verify=False)

if response.status_code == 200:
    data = response.json()
    token= response.json().get("accessToken")
else:
    print("Erreur :", response.status_code)


url = "https://"+OmniVistaIP+"/api/resourcemanager/switchinstructionfiles"

headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer {}".format(token)
}

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        switchLocation = row['switchLocation']
        #print(f"location : {switchLocation}")

        data =   {
        "switchInstructionFile": {
        "filePath": "home/autoconfig",
        "fileName": switchLocation+".alu",
        "fileHeader": "OS6360",
        "primaryIp": "192.168.115.252",
        "primaryProtocol": "FTP",
        "primaryUserName": "admin",
        "secondaryIp": "",
        "secondaryIpValid": True,
        "secondaryProtocol": None,
        "secondaryProtocolValid": True,
        "secondaryUserName": "",
        "secondaryUserNameValid": True,
        "fwVersion": "OS_8_9_107_R02",
        "fwVersionValid": True,
        "fwLocation": "/file",
        "fwLocationValid": True,
        "cfgFileName": switchLocation+".cfg",
        "cfgFileNameValid": True,
        "cfgFileLocation": "/file/config",
        "cfgFileLocationValid": True,
        "dbgFileName": "",
        "dbgFileNameValid": True,
        "dbgFileLocation": "",
        "dbgFileLocationValid": True,
        "scrFileName": "",
        "scrFileNameValid": True,
        "scrFileLocation": "",
        "scrFileLocationValid": True,
        "fileLicenseLocation": "",
        "fileLicenseLocationValid": True,
        "fileLicenseName": "",
        "fileLicenseNameValid": True
    }
}
       
        
        response = requests.post(url, headers=headers, json=data, verify=False)
        print(switchLocation ,":",response.json().get("status"))