import os
import sys
import subprocess
import time


def readEnvVar(): #Reads Environment variables from specified file.
    envVar = open('envVar.txt', 'r').read()
    return envVar

# def execContract(script):
#     execute contract on cmdline


# def callContract(action,var,*args):
#     if action == 1:
#         id = args[0]
#         readEnvVar(userFile)

def execCom(): #Executes shell commands to retrieve data and display in terminal
    cmd = ["chmod", "+x", "script"]
    subprocess.run(cmd)
    print("\n\n\n")
    subprocess.run('./script', shell=True)
    print("\n\n\n")
    os.remove('script')
    
def execComTrans(): #Executes shell commands to retrieve data, display in terminal and save to output file
    cmd = ["chmod", "+x", "script"]
    subprocess.run(cmd)
    print("\n\n\n")
    with open('text.txt', 'w') as outfile:
        subprocess.run('./script', stdout=outfile)
    subprocess.run('./script', shell=True)
    print("\n\n\n")
    os.remove('script')


def readAsset(id): #get asset by ID
    cmd = """peer chaincode query -C testchannel -n basic -c '{"function":"ReadAsset","Args":[\"""" + id + """\"]}'"""
    return cmd


def getAllAssets(): #get all assets
    cmd = """peer chaincode query -C testchannel -n basic -c '{"Args":["GetAllAssets"]}'"""
    return cmd

def createAsset(id, name, price, origin): #create a new asset
    cmd = """peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" -C testchannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" --peerAddresses localhost:9051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" -c '{"function":"CreateAsset","Args":[\"""" + id + """\",\"""" + name + """\",\"""" + price + """\",\"""" + origin + """\"]}'"""
    return cmd

def updateAsset(id, name, price, origin): #update an asset
    cmd = """peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" -C testchannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" --peerAddresses localhost:9051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" -c '{"function":"UpdateAsset","Args":[\"""" + id + """\",\"""" + name + """\",\"""" + price + """\",\"""" + origin + """\"]}'"""
    return cmd

def deleteAsset(id): #delete an asset
    cmd = cmd = """peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" -C testchannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" --peerAddresses localhost:9051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" -c '{"function":"DeleteAsset","Args":[\"""" + id + """\"]}'"""
    return cmd

# def transferAsset():
#     toFile = getAsset()
#     return

# def transferAllAssets():
#     toFile = getAllAssets()
    

def checkIsNum(num): #check if input is a number and is from 1 to 8
    while not num.isnumeric() or int(num) not in range(1,9):
        print('Wrong value entered. Please renter a value between 1 and 8\n')
        num = input('Enter a number:')
    return(int(num))   

def takeAction(action): #Takes action based on value entered by user
    envV = readEnvVar()
    if int(action) == 8:
        sys.exit()

    elif int(action) == 1:
        id = input('Enter asset ID to get:')
        toFile = readAsset(id)
        with open('script','w') as f:
            f.write(envV)
            f.write('\n')
            f.write(toFile)
        execCom()

    elif int(action) == 2:
        toFile = getAllAssets()
        with open('script','w') as f:
            f.write(envV)
            f.write('\n')
            f.write(toFile)
        execCom()

    elif int(action) == 3:
        id = input('Enter asset ID to create:')
        name = input('\nEnter asset Name:')
        price = input('\nEnter asset price (e.g. GHS 20):')
        origin = input('\nEnter asset country of Origin:')
        toFile = createAsset(id,name,price,origin)
        with open('script','w') as f:
            f.write(envV)
            f.write('\n')
            f.write(toFile)
        execCom()

    elif int(action) == 4:
        id = input('Enter asset ID to update:')
        name = input('\nEnter asset New Name:')
        price = input('\nEnter asset New Price (e.g. GHS 20):')
        origin = input('\nEnter asset New country of Origin:')
        toFile = updateAsset(id,name,price,origin)
        with open('script','w') as f:
            f.write(envV)
            f.write('\n')
            f.write(toFile)
        execCom()

    elif int(action) == 5:
        id = input('Enter asset ID to delete:')
        toFile = deleteAsset(id)
        with open('script','w') as f:
            f.write(envV)
            f.write('\n')
            f.write(toFile)
        execCom()

    elif int(action) == 6:
        id = input('Enter asset ID to get:')
        toFile = readAsset(id)
        with open('script','w') as f:
            f.write(envV)
            f.write('\n')
            f.write(toFile)
        execComTrans()
        #transferAsset()

    elif int(action) == 7:
        toFile = getAllAssets()
        with open('script','w') as f:
            f.write(envV)
            f.write('\n')
            f.write(toFile)
        execComTrans() 
    
    


if __name__== '__main__':
    n = 0
    while True: #Run till user exits program
        if n == 0:
            print("Select an option from the numbers below\n")
            print("1. Read Asset by Id","\t\t\t\t","2. Get all Assets\n")
            print("3. Create an Asset","\t\t\t\t","4. Update an Asset\n")
            print("5. Delete an Asset","\t\t\t\t","6. Transfer an Asset to another blockchain/app\n")
            print("7. Transfer all Assets to another blockchain/app","\t\t\t\t","8. Quit\n")
            inp = input('enter option: ')[0]
            inp = checkIsNum(inp)
            print('You entered:', inp)
            action = takeAction(inp)
            n+=1

        else:
            print("Select another option from the numbers below\n")
            print("1. Read Asset by Id","\t\t\t\t","2. Get all Assets\n")
            print("3. Create an Asset","\t\t\t\t","4. Update an Asset\n")
            print("5. Delete an Asset","\t\t\t\t","6. Transfer an Asset to another blockchain/app\n")
            print("7. Transfer all Assets to another blockchain/app","\t\t\t\t","8. Quit\n")
            inp = input('enter option: ')[0]
            inp = checkIsNum(inp)
            print('You entered:', inp)
            action = takeAction(inp)


