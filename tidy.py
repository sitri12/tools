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
import random

base=os.path.dirname(os.path.realpath(__file__))
pwd=os.getcwd()
#print(pwd)

cfg=base+"\\tidy.cfg"
#print(cfg)

def in_name(file, str, dest):
    
    rnd="copy_"
    
    file=file.lower()
    str=str.lower()
    
    if(file.find(str) != -1):        
        
        source=pwd+"\\"+file
        dst=dest+file
        
        if(os.path.isfile(dst)):
            dst=dest+rnd+file
        
        try:
            if(wordy==1):
                print("Moing "+file+" to "+dest)
            shutil.move(source, dst)
        except:
            pass

def in_ext(file, str, dest):

    rnd="Copy_"


    sp_name=file.split(".")

    if(sp_name[-1].lower()==str.lower()):

        dst=dest+file
        
        if(os.path.isfile(file)):
            dst=dest+rnd+file

        if(wordy==1):
            print("Moing "+file+" to "+dest) 
        source=pwd+"\\"+file
        shutil.move(source, dst)
    
def read_cfg(cfg):

    print("Tidying up "+pwd+":This may take some time.  \n\n\tPlease wait...")

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
    
def help():
    print(" Tidy.py     (Ver 1.02a)     (c) Paul Mann 2021                       Man Page")
    print(" =================================================================================")
    print(" ")
    print(" Synopsis")
    print(" ========")
    print(" ")
    print("     Script to sort any folder's contents into their required directories.")
    print(" ")
    print(" Usage")
    print(" =====")
    print(" ")
    print("     tidy.py")
    print("     tidy.py [-h][-f <filename>] (To Be Implemented)")
    print(" ")
    print(" Arguments")
    print(" =========")
    print(" ")
    print("     Switch          :   Meaning")
    print("     ----------------:----------------------------------------------------------")
    print("     -h              :   Show Help (This Page)")
    print("     -f <filename>   :   Use <filename> instead of the default (tidy.cfg)")
    print("     -v              :   Verbose mode - will list each file as it is moved")
    print(" ")
    print(" ")
    print(" Notes")
    print(" =====")
    print(" ")
    print(" 1. HOW IT WORKS")
    print(" ")
    print("     Tidy.py reads first tidy.cfg (or whatever file is specified by the -f argument)")
    print("     into memory before testing each file and folder name looking for a match either")
    print("     in the name or extention and if matching sends it to the desired directory.")
    print(" ")
    print(" 2. CREATING TIDY.CFG")
    print(" ")
    print("     The general format is:")
    print(" ")
    print("         [;|:|!]#<string>#<destination>")
    print(" ")
    print("     flag        Meaning")
    print("     -----------------------------------")
    print(" ")
    print("         ;   -   Comment")
    print("         :   -   <string> is in filename")
    print("         !   -   <string> is the same as the file extention.")
    print(" ")
    print(" 3. CONSERING THE ORDER of TIDY.CFG")
    print(" ")
    print("     The order of entries within tidy.cfg (or whatever file you choose) may be")
    print("     important to be able to sort efficiently.  I have ordered the default")
    print("     tidy.cfg as:")
    print(" ")
    print("         Audio")
    print("         TV")
    print("         Movies (Other Video files)")
    print("         Apps and Programs (inc Source code)")
    print("         Zips & Archives")
    print("         Images")
    print("         Books and Documents")
    print(" ")
    print("     Doing this helps with readability as well as the apps functionality (from")
    print("     my perspective).")
    print(" ")

def use_file(file):
    if(os.path.isfile(file)):
        read_cfg(file)
    else:
        print("\n\t"+file+" does not exist")
        
    
ts=time.perf_counter()
wordy=0
if(len(sys.argv)==1):
    read_cfg(cfg)
if(len(sys.argv)>1):
    if(sys.argv[1]=="-h"):
        help()
    elif(sys.argv[1]=="-v"):
        wordy=1
        read_cfg(cfg)
    elif(sys.argv[1]=="-f"):
        use_file(sys.argv[2])
    
    
    
te=time.perf_counter()
tt=int(te-ts+0.5)
sec=tt%60
min=(tt-sec)/60
print(f"\n\n\tJob completed in {min:0.0f} min and {sec:0.2f} secs\n\n")
