#::toolz::
#::WiP::
import sys
import os

def mann():
    print("USAGE:\n\n\t MANN.PY <application>")
def help():
    print(" MANN.PY (ver 1.01a: (c) Paul Mann 2021)                             MANN Page")
    print(" ==============================================================================")
    print(" ")
    print(" Synopsis")
    print(" ========")
    print(" ")
    print("     Displays help for apps and scripts.")
    print(" ")
    print(" Usage")
    print(" =====")
    print(" ")
    print("     mann.py [-h][<topic>]")
    print(" ")
    print(" Arguments")
    print(" =========")
    print(" ")
    print("     -h      :   Displays Help (This page)")
    print("     <topic> :   Displays the help of the applicagion")
    print(" ")
    print(" Notes")
    print(" =====")
    print(" ")
    print("     Work in Progress")
    print(" ")
    print("     To Do")
    print("     -----")
    print(" ")
    print("     Add the following args to the script:")
    print(" ")
    print("         -import <applicagion>")
    print(" ")
    print("             Imports the help of <application> into the man.dat database.")
    print(" ")
    print("         -add <file>")
    print(" ")
    print("             Adds <file> to the database.")
    print(" ")

def list():

    m=int(max_rows())

    f=open("mann.dat", "r")
    a=[]
    for l in f:
        if l.startswith("#"):
            a.append(l[1:])
    
    a.sort()
    cnt=0    
    print("\n\nAvaailable topics: \n")
    cnt+=2

    for i in a:
        i=i.upper()
        print("\t"+i.rstrip())
        if(cnt==m-2):
            os.system("pause")
            cnt=0
        cnt+=1
    
    f.close()

def max_rows():

    a=[]
    a=os.get_terminal_size()
    a=str(a)
    b=a.split(",")
    c=b[1].split("=")
    a=c[1].split(")")
    return(a[0])

def main(page):
    p=page.strip()
    disp=0
    dispd=0
    c=0
    #open man.dat
    f=open("mann.dat","r")
    m=int(max_rows())
    cnt=0
    print("================================================================================")

    for l in f:                 #loop through each line of file
        if(l.startswith("#")):
            
            key=l[1:].strip()
            
            if(key.upper()==page.upper()):      #key match 
                disp=1          #Allow display
                dispd+=1
                
        if(l.startswith("!!")):    
            disp=0              #unallow display
                 

        if(disp==1):
            if(l.startswith("#")):
                cnt+=1
                continue
            print(l.rstrip())    #print the line
            if(cnt==m-2):
                os.system("pause")
                cnt=0
        cnt+=1
    
            
           
        c+=1
        
    if(dispd < 1):
        print("\n\t"+page+" could not be found in MANN")
    print("================================================================================")

if(len(sys.argv)<2):
    list()
elif(sys.argv[1]!="-h"):
    main(sys.argv[1].upper())
if(sys.argv[1]=="-h"):
    help()
elif(sys.argv[1]=="-list"):
    list()

