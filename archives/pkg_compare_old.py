#!/usr/bin/python

import os
import sys

user          = "jonest"
deployer_node = "simondeployernode"
deployer_ip   = "9.3.89.63"
Client_node   = "server-3"
Client_ip     = "192.168.47.21"
ansible_user     = "rhel75" 
ansible_password = "passw0rd" 

PATH = "~/{}/power-up".format(user)

def CMD(input):
  output = os.system(input)
  return output

def client_CMD(client_input):
  client_login   = "egosh user logon -u {} -x {}".format(ansible_user, ansible_password)
  ansible        = "ansible all -i ~/power-up/playbooks/software_hosts -m shell -a {} ; {} ".format(client_login, client_input)
  ansible_output =  os.system(ansible)
  return ansible_output

#SSH to server-3 (Client Node) and create installed list#
client_CMD("yum list installed | grep @anaconda/7.5 > base_installed.txt ")

#Copy base_installed.txt to deployer_node#
client_CMD("scp base_installed.txt {}@{}:/{}".format(user,deployer_ip,PATH))

#edit install_procedure.yml file on deployer node#
CMD("vi ~/power-up/software/paie112_install_procedure.yml")

#Run pup software#
CMD("pup software --install paie112.py")

#Generate new list on server-3
client_CMD("yum list installed | grep @anaconda/7.5 > base_installed.txt1 ")

#Copy base_installed1.txt to deployer_node#
CMD("scp base_installed1.txt {}@{}:/{}".format(user,deployer_ip,PATH))




