import os
#import sys
#sys.path.append("**Put here the directory where you have the file with your function**")
import read_write_execute as rwe

class LedgerAccess(object):
    def __init__(self,env_file):
        self.envVar = rwe.readEnvVar(env_file)
        #cert_location

    def readAsset(self,id):
        cmd = """peer chaincode query -C testchannel -n basic -c '{"function":"ReadAsset","Args":[\"""" + id + """\"]}'"""
        return cmd
print(os.getcwd())
file = 'envVar.txt'    
la = LedgerAccess(file)
print(la.envVar)