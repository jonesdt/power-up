#!/usr/bin/python

import os
import sys

user             = "jonest"
deployer_node    = "simondeployernode"
deployer_ip      = "9.3.89.63"
Client_node      = "server-3"
Client_ip        = "192.168.47.21"
ansible_user     = "rhel75"
ansible_password = "passw0rd"

PATH = "/home/{}/power-up".format(user)

def CMD(host_input):
    output = os.system(host_input)
    return output

#Choose repo to search package dependinces for#

search = ""

def print_menu(): 
    print "1. ANACONDA PKGS [@anaconda/7.5]"
    print "2. dependencies-powerup"
    print "3. @powerai-powerup"
    print "4. CUDA PKGS [@cuda-powerup]"
    print "5. EPEL PKGS [@epel-ppc64le-powerup]"
    print "6. Start"
  
loop=True      
  
while loop:         
    print_menu() 
    choice = input("Enter your choice [1-6]: ")
     
    if choice==1:     
        print "@anaconda/7.5 has been selected"
        search = "@anaconda/7.5"
    elif choice==2:
        print "@dependencies-powerup has been selected"
        search = "@dependencies-powerup"
    elif choice==3:
        print "@powerai-powerup has been selected"
        search = "@powerai-powerup"
    elif choice==4:
        print "@cuda-powerup has been selected"
        search = "@cuda-powerup"
    elif choice==5:
        print "@epel-ppc64le-powerup has been selected"
        search = "@epel-ppc64le-powerup"
    elif choice==6:
        print "Exit"
        loop=False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")

#SSH to server-3 (Client Node) and create pre_install.txt list#
CMD("ansible all -i ~/power-up/playbooks/software_hosts -m shell -a 'yum list installed | grep {} > pre_install.txt'".format(search))

#Copy pre_install.txt to deployer_node#
CMD('scp pre_install.txt {}@{}:/{}'.format(user,deployer_ip,PATH))

#edit install_procedure.yml file on deployer node#
CMD('vi ~/power-up/software/paie112_install_procedure.yml')

#Run pup software#
CMD('pup software --install paie112.py')

#Generate post-list on server-3#
CMD("ansible all -i ~/power-up/playbooks/software_hosts -m shell -a 'yum list installed | grep {} > post_install.txt'".format(search))

#Copy post_install.txt to deployer_node#
CMD('scp post_install.txt {}@{}:/{}'.format(user,deployer_ip,PATH))

#Parse package data from pre and post text files#

txt_files  = ['pre_install.txt', 'post_install.txt']

pre_dbfile  = open('{}'.format(txt_files[0]),'r')
post_dbfile = open('{}'.format(txt_files[1]),'r')

pre_pkg_list    = []
pre_pkg_version = []

post_pkg_list = final_pkg_list = []
post_pkg_version = final_pkg_version = []

def pre_package_lister():
    for line_a in pre_dbfile.readlines():
        value_a = line_a.split()
        pre_pkg_list.append(value_a[0])
#       pre_pkg_version.append(value_a[1])

def post_package_lister():
    for line_a in post_dbfile.readlines():
        value_a = line_a.split()
        post_pkg_list.append(value_a[0])
 #      post_pkg_version.append(value_a[1])

pre_package_lister()
post_package_lister()

delta_pkg_list    = []
delta_pkg_version = []

for i in pre_pkg_list:
    for x in post_pkg_list:
        if x == i:
           delta_pkg_list.append(x)
           final_pkg_list.remove(x)

print "Results: "
print final_pkg_list
 
