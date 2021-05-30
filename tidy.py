#::Toolx::
#::WiP::
#
#   tidy.py         (Ver: 1.00a)            Paul Mann 20210530
#
#       Script to tidy up directories (download etc) from a cfg file (tidy.cfg) which is what will
#       need the most upkeep.  Just run it - most of the items will be sorted after a while.
#
#       Todo:
#       =====
#
#       Help page & man page 
#       choose a cfg file in options
#

import os
import sys
import subprocess
import time
import shutil

base=os.path.dirname(os.path.realpath(__file__))
pwd=os.getcwd()
#print(pwd)

cfg=base+"\\tidy.cfg"
#print(cfg)

def in_name(file, str, dest):
    
    file=file.lower()
    str=str.lower()
    
    if(file.find(str) != -1):        
        
        source=pwd+"\\"+file
        dst=dest+file
        try:
            shutil.move(source, dest)
        except:
            pass

def in_ext(file, str, dest):

    sp_name=file.split(".")

    if(sp_name[-1].lower()==str.lower()):

        source=pwd+"\\"+file
        dst=dest+file
        shutil.move(source, dest)
    
def read_cfg(cfg):

    f=open(cfg)
    for line in f:
    
        ls=os.listdir()
        
        token=line.split("#")
        if(token[0]==";"): 
            continue
        if(token[0]==":"):
            for a in range(len(ls)):
                in_name(ls[a], token[1], token[2].rstrip())
        if(token[0]=="!"):
            for a in range(len(ls)):
                in_ext(ls[a], token[1], token[2].rstrip())

            
    f.close()
    

read_cfg(cfg)