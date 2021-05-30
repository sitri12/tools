#toolz
#WiP
'''

Backup script takes items from cfg file - basic functionality works, but would be nice to have following

    *  create fresh cfg file
    *  Add current directory to cfg file
    *  Add named directory to cfg file
    *  Help option 


'''

import os
import sys
import subprocess
import string
import win32api
import time

base=os.path.dirname(os.path.realpath(__file__))

cfg=base+"\\backup.cfg"
#print(cfg)
    
def get_defaults(file):
    
    f=open(file, "r")
    default=[]
    dest={}
    ltr={"letter": 0}
    for line in f:  
        #print(line)
        line=line.rstrip()
        if(line.startswith(";")):
            continue
        if(line.startswith("DL")):
            dest["letter"]=line[3:].rstrip()
        if(line.startswith("DN")):
            dest["drive"]=line[3:].rstrip()
        if(line.startswith("DD")):
            dest["dest"]=line[3:].rstrip()
    f.close()
    
    return dest

def get_dirs(file):

    f=open(file, "r")
    backup_list=[]
    
    for l in f:
        l=l.lstrip()
        if(l.startswith(";")):
            continue
        if(l.startswith("+:")):
            backup_list.append(l[2:])
    f.close()
    return backup_list

def backup(ltr, dest, source):
    print("Backing Up now to drive "+ltr) 
    for a in range(len(source)):
        
        
        ls_path=source[a].split("\\")
        into=str(ls_path[-2:-1])
        into=into[2:-2]
        print(into)
        subprocess.run("xcopy "+source[a].rstrip()+" "+ltr+dest+into+"\ /e /q /h /r /y " )

def getDriveName(driveletter):
    try:
        return subprocess.check_output(["cmd","/c vol "+driveletter]).decode().split("\r\n")[0].split(" ").pop()
    except:
        pass

def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives

def add():
    here=os.path.dirname(os.path.realpath(__file__))
    file=open(cfg, "a")
    file.write("\n+:"+here)
    file.close()
    print(here+" has been added of config file")
    


def main():
    
    defaults=get_defaults(cfg)
    source=get_dirs(cfg)
    drv=defaults.get("drive")
    ltr=defaults.get("letter")
    dest=defaults.get("dest")
    if(ltr is None):                                    # drv ltr not specified
        print("No drive letter assigned: lookiing for "+drv)
    else:
        if(drv is None):                                # drv name not specified
            print("No Drive name assigned in config file")
        else:                                           # Drv specified`
            
            try:
                if(getDriveName(ltr)==drv):             #Drv & ltr are congruent
                    backup(ltr, dest, source)
                else:                                   # drv & ltr not congruent
                    avail=get_drives()
                    for d in range(len(avail)):
                        driv=getDriveName(avail[d][:2])
                        if(driv==drv):
                            backup(avail[d][:2], dest, source) 
                            break
                        else:
                            pass
                            #print("Backup drive not found")
            except:
                pass


ts=time.perf_counter()
if(len(sys.argv)==1):
    main()
elif(sys.argv[1]=="add"):
    add()


te=time.perf_counter()
tt=int(te-ts+0.5)
sec=tt%60
min=(tt-sec)/60
print(f"Backup completed in {min:0.0f} min and {sec:0.2f} secs")
