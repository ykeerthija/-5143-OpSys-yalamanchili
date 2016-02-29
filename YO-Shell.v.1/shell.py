#Program Name: Yo-Shell.v.1

import os
import sys
import shutil
import time
import stat

from os.path import expanduser

class historyManager(object):
    def __init__(self):
        self.command_history = []

   
    def push_command(self,cmd):
        self.command_history.append(cmd)
        
  
    def get_commands(self):
        return self.command_history
        
    
    def number_commands(self):
        return len(self.command_history)


class parserManager(object):
    def __init__(self):
        self.parts = []
    
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
        

class commandManager(parserManager):
    def __init__(self):
        self.command = None

    
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command

    def ls(self):
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
    
        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))

    def lsf(self,flag):
        files_info=[]
        for file_name in os.listdir('.'):
            file_stats=os.stat(file_name)
            file_info = [
            file_name,
            file_stats [stat.ST_SIZE],
            oct(stat.S_IMODE(file_stats.st_mode))[2:],
            time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
            time.strftime("%m/%d/%Y %I:%M:%S %P",time.localtime(file_stats[stat.ST_ATIME])),
            time.strftime("%m/%d/%Y &I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))
            ]
            files_info.append(file_info)
        #files_info.sort()        
        #for i in range(len(files_info)): 
        if(flag=='-m'):        
            files_info.sort(key=lambda x:time.strftime((x[3])))
        elif(flag=='-s'):
            files_info.sort(key=lambda x:time.strftime((x[2])))
        elif(flag=='-a'):
            files_info.sort(key=lambda x:time.strftime((x[4])))
        elif(flag=='-c'):
            files_info.sort(key=lambda x:time.strftime((x[5])))
            
        for file in files_info:
            #file.sort(key=lambda x: file_stats[stat.ST_MTIME])
            print(file)               
        
    def cat(self,file):
        if(os.path.isfile(file)):
            f = open(file,'r')
            print(f.read())
        else:
            print("file does not exist")
            
    def mv(self,file):
        shutil.move('a.txt','b.kml')	

    def cp(self,src1,dest1):
        filename1 = tempfile.mktemp (".txt")
        open (filename1, "w").close ()
        filename2 = filename1 + ".copy"
        print (filename1, "=>", filename2)
        shutil.copy (filename1, filename2)
        if os.path.isfile (filename2): print ("Success")
        dirname1 = tempfile.mktemp (".dir")
        os.mkdir (dirname1)
        dirname2 = dirname1 + ".copy"
        print (dirname1, "=>", dirname2)
        shutil.copytree (dirname1, dirname2)
        if os.path.isdir (dirname2): print ("Success")


            
    def wordcount(self,filename):
        try:
            f=open(filename,'r')
            wordcount=0 
            for lines in f:
                count=lines.split()
                wordcount=wordcount+len(count)
            f.close()
            print("word count:",str(wordcount))
        except IOError as e:
            print("no such file")
			
			
    def wc1(self,filename):
        for f in files:
        subprocess.call(['wc', '-l', f])             
               
            
    def cd(self,dir):
        s=os.path.join(os.getcwd(),dir)
        if(os.path.isdir(s)):
            os.chdir(s)       
        else:
            print("directory doesn't exist")
            

    def chmod(self,file):
        os.chmod("foo.txt", stat.S_IXGRP)
        os.chmod("foo.txt", stat.S_IWOTH)
        print ("Changed mode successfully!!")

    def rm(self,file):
        os.remove('filename')
    
    def history(self):
        his=historyManager.get_commands(self)
        return his
    
class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
        
    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("parser-$ ")         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            print(parts)
            print(parts[0])
            if parts[0]=='cat':
                self.commands.cat(parts[1])
            elif parts[0]=='ls':
                if(len(parts)==1):
                    self.commands.ls()
                elif(len(parts)==2):
                    self.commands.lsf(parts[1])
            elif parts[0]=='mv':
                if(len(parts)==3):
                    self.commands.mv(parts[1],parts[2])
                else:
                    print("given more or les files")
            elif parts[0]=='cp':
                self.commands.cp(parts[1],parts[2])
            elif parts[0]=='wc':
                if(len(parts)==2):
                    self.commands.wc(parts[1])
                elif(len(parts)==3):
                    self.commands.wcf(parts[1],parts[2]) 
                else:
                    print(" given more or less files")
            elif parts[0]=='cd':
                self.commands.cd(parts[1])
            elif parts[0]=='chmod':
                self.commands.chmod(parts[1])
            elif parts[0]=='rm':
                if(len(parts)==2):
                    self.commands.rm(parts[1]) 
                else:
                    print("given more or less files")
            elif parts[0]=='history':
                his=self.history.get_commands()
                if(len(parts)==1):
                    for item in his:
                        print(item)
                else:
                    print("more arguments in history command")
            else:
                print("command dismatched")
                
if __name__=="__main__":
    d = driver()    
    d.runShell()
