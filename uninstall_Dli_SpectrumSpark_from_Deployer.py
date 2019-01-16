#!/usr/bin/python

import os
import sys

#To uninstall the PAIE components plus Anaconda (but not Nvidia components and other pre-req packages);
#Do the clients first, then masters.


def CMD(input):
  output = os.system("ansible all -i ~/power-up/playbooks/software_hosts -m shell -a '{}'".format(input))
  return output

def print_menu(): 
 print("1. Stop snd shutdown all-services")
 print("2. Uninstall Deep Learning Impact")
 print("3. Uninstall Conductor Spark")
 print("4. Erase and Remove PowerAI License")
 print("5. Remove Directories")
 print("6. Extra - Teardown Containers")
 print("7. Extra - Teardown Networks")
 print("8. Exit")

loop=True

while loop:
   print_menu()
   choice = input("Enter your choice [1-6]: ")

   if choice==1:
       CMD("source /opt/ibm/spectrumcomputing/profile.platform")
       CMD("egosh user logon -u Admin -x Admin, egosh service stop all")
       print("all-services stopped")
       CMD("egosh ego shutdown")
       print("all-services shutdown")
   elif choice==2:
       CMD("./opt/ibm/spectrumcomputing/uninstall/deeplearningimpactuninstall-1.2.1.0.sh")
       print("Uninstalled Deep Learning Impact")
   elif choice==3:
       CMD("./opt/ibm/spectrumcomputing/uninstall/conductorsparkuninstall-2.3.0.sh")
       print("Uninstalled Conductor Spark")
   elif choice==4:
       CMD("yum erase powerai-license, yum remove powerai-enterprise-license")
       print("Erased and Removed PowerAI License")
   elif choice==5:
       CMD("rm -rf /opt/anaconda3,rm -rf /opt/DL, rm -rf /opt/ibm")
       print("Removed Directories")
   elif choice==6:
       os.system("ls /home/jonest/power-up | grep config")
       config_file_name = str(raw_input("Config File name: "))
       os.system("teardown deployer --container {}".format(config_file_name))
       print("Container Removed")
   elif choice==7:
       os.system("ls /home/jonest/power-up | grep config")
       config_file_name = str(raw_input("Config File name: "))
       os.system("teardown deployer --networks {}".format(config_file_name))
       print("Networks Removed")
   elif choice==8:
       print("Exit")
       loop=False
   else:
          raw_input("Enter any key to try again..")

