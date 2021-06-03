#::Toolz::
#::Wip::
import sys

def get_base_name(file):

    a=file.split(".")
    out=a[1]+a[0]
    return(out)

def get_lang(flag):

    if(flag=="-b"):
        out="bat"
    if(flag=="-p"):
        out="py"
   
    return(out)

def create_head(lang):

    if(lang=="bat"):
        head="@echo off \n\n\n:_help\n"
    if(lang=="py"):
        head="def help():\n"
    
    return(head)

def create_tail(lang):
    
    if(lang=="bat"):
        pass
    if(lang=="py"):
        out="\n\nhelp()"
    return(out)

def create_line(line, lang):

    if(lang=="bat"):
        line=line.replace("<", "^<" )
        line=line.replace(">", "^>")
        if(line==""):
            out="echo.\n"
        else:
            out="echo    "+line+"\n"
    if(lang=="py"):
        out="    print(\" "+line+"\")\n"
    
    return(out)

def help():
    print(" TXT2HLP.PY   (ver 1.01a)               (c) Paul Mann 2021              MAN PAGE")
    print(" ===================================================================================")
    print(" ")
    print(" Synopsis")
    print(" =========")
    print(" ")
    print("     Another Lazy script.  Turns any named text file into a help() function.")
    print(" ")
    print(" Usage")
    print(" =====")
    print(" ")
    print("     txt2hlp.py [-h][-b][-p][<infile>]")
    print(" ")
    print(" Arguments")
    print(" =========")
    print(" ")
    print("     -h          :       Show Help (This page)")
    print("     -b          :       Outputs a BATCH compliant file")
    print("     -p          :       Outputs a PYTHON function")
    print("     <infile>    :       The source file")
    print(" ")
    print(" Notes")
    print(" =====")
    print(" ")
    print("     If creating a BATCH function you may need to edit any escaped characters by hand")
    print(" ")
    print(" ChangeLog")
    print(" =========")
    print(" ")
    print("     20210603")
    print("     --------")
    print(" ")
    print("     Couple of Minor tweeks.")
    print(" ")
    print("         1.  Adds a function call at the end of the file if python is selected.")
    print(" ")
    print("         2.  Output file is now named .bat or .py depending upon selection.")
    print(" ")
    print(" ")


help()
def main():

    lang=get_lang(sys.argv[1])

    inf=open(sys.argv[2], "r")
    out=[]
    out.append(create_head(lang))
    
    for i in inf:
        i=i.rstrip()
        line=create_line(i, lang)
        out.append(line)
        
    inf.close()

    
    
    ofile=get_base_name(sys.argv[2])
    
    f=open(ofile+"."+lang, "a")

    for i in range(len(out)):
        f.write(out[i])
    
    
    f.write(create_tail(lang))
    f.close()
    

if(len(sys.argv) >3):
    help()
    print(len(sys.argv))
elif(sys.argv[1].lower()=="-h"):    
    help()
else:
    main()  
