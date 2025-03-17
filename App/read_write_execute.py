import subprocess,os


def readEnvVar(file:str): #Reads Environment variables from specified file.
    '''Enter the full location of the file containing the environment variables to set in the terminal'''
    information = open(file, 'r').read()
    return information

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