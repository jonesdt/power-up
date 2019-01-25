#!/usr/bin/python

# Copyright 2018 IBM Corp.
#
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import fileinput
import re

print '\n'
os.chdir("/home/jonest/power-up/logs/dependencies/")

<<<<<<< HEAD
class MyClass:
   def __init__(self):
      self.pre_file  = str(raw_input('Enter pre_install.txt File: '))
      self.post_file  = str(raw_input('Enter post_install.txt File: '))
      self.pre_dbfile  = open("{}".format(pre_file),'r') 
      self.post_dbfile  = open("{}".format(post_file),'r')
      
      self.pre_pkg_list = []
      self.post_pkg_list = []
      self.delta_pkg_list = []     
 
      self.pre_lists = [
                       'client_yum_pre_list.txt',
                       'client_pip_pre_install.txt',
                       'dlipy3_pip_pre_install.txt',
                       'dlipy2_pip_pre_install.txt',
                       'client_conda_pre_install.txt',
                       'dlipy3_conda_pre_install.txt',
                       'dlipy2_conda_pre_install.txt',
                       ]
          
      self.post_list = [
                       'client_yum_post_list.txt',
                       'client_pip_post_install.txt',
                       'dlipy3_pip_post_install.txt',
                       'dlipy2_pip_post_install.txt',
                       'client_conda_post_install.txt',
                       'dlipy3_conda_post_install.txt',
                       'dlipy2_conda_post_install.txt',
=======
pre_file  = str(raw_input('Enter pre_install.txt File: ')) #used only in manual_menu_process
post_file = str(raw_input('Enter post_install.txt File: '))#used only in manual_menu_process

#pre_dbfile  = open("{}".format(pre_file),'r')                  
#post_dbfile = open("{}".format(post_file),'r')

pre_pkg_list = []                                              
post_pkg_list = final_pkg_list = []

def pre_package_lister():                                      #instance
   pre_dbfile  = open("{}".format(pre_file),'r')
   for line_a in pre_dbfile.readlines():
      value_a = line_a.split()
      final_value_a = value_a[0]
      pre_pkg_list.append(final_value_a)
 
def post_package_lister():                                      #instance
   post_dbfile = open("{}".format(post_file),'r')
   for line_b in post_dbfile.readlines():
      value_b = line_b.split()
      final_value_b = value_b[0]
      post_pkg_list.append(final_value_b)

pre_package_lister()
post_package_lister()  

delta_pkg_list = []                                             #global variable

#Delta Logic
for i in pre_pkg_list:
   for x in post_pkg_list:
      if x == i:
         delta_pkg_list.append(x)
         final_pkg_list.remove(x)

#Delta File Created         
final_file  = str(raw_input('Enter final File name: '))          #global variable 
os.system('touch {}; chmod 777 {}'.format(final_file, final_file))

with open('{}'.format(post_file)) as oldfile, open('{}'.format(final_file), 'wt+') as newfile:
   for line in oldfile:
      if any(pkg in line for pkg in final_pkg_list):
         newfile.write(line)

print "Results:\n"
print final_pkg_list 
print '\n'

format_menu = True
while format_menu == True: 
   yml_file = str(raw_input("Would you like to format for pkglist.yml file? "
                           "\n(1)Yes \n(2)No \n"))
   if yml_file == '2':
      format_menu = False

   elif yml_file == '1':
      pkg_type_select = str(raw_input("Select Format Type: "
                                     "\n(3)Yum \n(4)PIP \n(5)Conda \n"))
      if pkg_type_select == '3':

         dep_search = [
                       'anaconda',
                       'cuda-powerup',
                       'powerai-powerup',
                       'dependencies-powerup',
                       'epel-ppc64le-powerup',
                       'installed',
>>>>>>> e4a385e6deecbc201821ee14d362946878ab94fe
                      ]
      
      self.final_file  = str(raw_input('Enter final File name: '))

   def pre_package_lister():
      
      for line_a in pre_dbfile.readlines():
         value_a = line_a.split()
         final_value_a = value_a[0]
         pre_pkg_list.append(final_value_a)
     
   def post_package_lister():
      
      for line_b in post_dbfile.readlines():
         value_b = line_b.split()
         final_value_b = value_b[0]
         post_pkg_list.append(final_value_b)
   
   def gather_delta():
   
      os.system('touch {}; chmod 777 {}'.format(final_file, final_file))
   
      for i in pre_pkg_list:
         for x in post_pkg_list:
            if x == i:
               delta_pkg_list.append(x)
               final_pkg_list.remove(x)
   
      with open('{}'.format(post_file)) as oldfile, open('{}'.format(final_file), 'wt+') as newfile:
         for line in oldfile:
            if any(pkg in line for pkg in final_pkg_list):
               newfile.write(line)
   
   def yum_formatter():
   
      dep_search = [
                    'anaconda',
                    'cuda-powerup',
                    'powerai-powerup',
                    'dependencies-powerup',
                    'epel-ppc64le-powerup',
                    'installed',
                   ]
   
      dep_files = [
                   'anaconda_{}'.format(final_file),
                   'cuda-powerup_{}'.format(final_file),
                   'powerai-powerup_{}'.format(final_file),
                   'dependencies-powerup_{}'.format(final_file),
                   'epel-ppc64le-powerup_{}'.format(final_file),
                   'installed_{}'.format(final_file),
                  ]
   
      tmp_dep_files = [
                       'tmp_anaconda_{}'.format(final_file),
                       'tmp_cuda-powerup_{}'.format(final_file),
                       'tmp_powerai-powerup_{}'.format(final_file),
                       'tmp_dependencies-powerup_{}'.format(final_file),
                       'tmp_epel-ppc64le-powerup_{}'.format(final_file),
                       'tmp_installed_{}'.format(final_file),
                      ]
   
      yum_conda_dbfile = open('anaconda_{}'
                             .format(final_file),'w+')
      yum_cuda_dbfile = open('cuda-powerup_{}'
                            .format(final_file),'w+')
      yum_powerai_dbfile = open('powerai-powerup_{}'
                               .format(final_file),'w+')
      yum_dependencies_dbfile = open('dependencies-powerup_{}'
                                    .format(final_file),'w+')
      yum_epel_dbfile = open('epel-ppc64le-powerup_{}'
                            .format(final_file),'w+')
      yum_installed_dbfile = open('installed_{}'
                                 .format(final_file),'w+')
   
      anaconda_list = []
      cuda_powerup_list = []
      powerai_powerup_list = []
      dependencies_powerup_list = []
      epel_ppc64le_powerup_list = []
      installed_list = []
   
      for dep in dep_files:
         os.system("touch {}; chmod 777 {}".format(dep,dep))
   
      for search in dep_search:
         dep_grep = os.popen("cat {} | xargs -n3 | column -t > tmp_{}_{}"
                            .format(final_file,search,final_file))
   
      for line_a in open("{}".format(tmp_dep_files[0]),'r').readlines():
         value_a = line_a.split()
         value_b = value_a[0]
         prefix = value_b.split('.',1)[0]
         suffix = value_b.split('.',1)[1]
         version = value_a[1]
         new_value = "{}-{}.{}".format(prefix,version,suffix)
         yum_conda_dbfile.write('{}\n'.format(new_value))
   
      for line_a in open("{}".format(tmp_dep_files[1]),'r').readlines():
         value_a = line_a.split()
         value_b = value_a[0]
         prefix = value_b.split('.',1)[0]
         suffix = value_b.split('.',1)[1]
         version = value_a[1]
         new_value = "{}-{}.{}".format(prefix,version,suffix)
         yum_cuda_dbfile.write('{}\n'.format(value_a[0]))
   
      for line_a in open("{}".format(tmp_dep_files[2]),'r').readlines():
         value_a = line_a.split()
         value_b = value_a[0]
         prefix = value_b.split('.',1)[0]
         suffix = value_b.split('.',1)[1]
         version = value_a[1]
         new_value = "{}-{}.{}".format(prefix,version,suffix)
         yum_powerai_dbfile.write('{}\n'.format(new_value))
   
      for line_a in open("{}".format(tmp_dep_files[3]),'r').readlines():
         value_a = line_a.split()
         value_b = value_a[0]
         prefix = value_b.split('.',1)[0]
         suffix = value_b.split('.',1)[1]
         version = value_a[1]
         new_value = "{}-{}.{}".format(prefix,version,suffix)
         yum_dependencies_dbfile.write('{}\n'.format(new_value))
   
      for line_a in open("{}".format(tmp_dep_files[4]),'r').readlines():
         value_a = line_a.split()
         value_b = value_a[0]
         prefix = value_b.split('.',1)[0]
         suffix = value_b.split('.',1)[1]
         version = value_a[1]
         new_value = "{}-{}.{}".format(prefix,version,suffix)
         yum_epel_dbfile.write('{}\n'.format(new_value))
   
      for line_b in open("{}".format(tmp_dep_files[5]),'r').readlines():
         value_a = line_a.split()
         value_b = value_a[0]
         prefix = value_b.split('.',1)[0]
         suffix = value_b.split('.',1)[1]
         version = value_a[1]
         new_value = "{}-{}.{}".format(prefix,version,suffix)
         yum_installed_dbfile.write('{}\n'.format(new_value))
   
      os.system("sudo rm -rf tmp* ")
   
   def pip_formatter():
   
      pip_dbfile = open('{}'.format(final_file),'rb+')
      for line_c in pip_dbfile.readlines():
         value_c = line_c.split()
         prefix = value_c[0]
         suffix = value_c[1]
         new_value = "{}=={}".format(prefix,suffix)
         pip_dbfile.write('{}\n'.format(new_value))
   
   def conda_formatter():
   
      conda_dbfile = open('{}'.format(final_file),'rb+')
      for line_d in conda_dbfile.readlines():
         value_d = line_d.split()
         prefix = value_d[0]
         suffix = value_d[2]
         version = value_d[1]
         new_value = ("{}-{}-{}.tar.bz2"
                     .format(prefix,version,suffix))
         conda_dbfile.write('{}\n'.format(new_value))
   
   def manual_menu():
   
      format_menu == True
   
      while format_menu == True: 
         yml_file = str(raw_input("Would you like to format for pkglist.yml file? "
                                 "\n(1)Yes \n(2)No \n"))
         if yml_file == '2':
            format_menu == False
   
         elif yml_file == '1':
            pkg_type_select = str(raw_input("Select Format Type: "
                                           "\n(3)Yum \n(4)PIP \n(5)Conda \n"))
            if pkg_type_select == '3':
               yum_formatter()
               format_menu == False
   
            elif pkg_type_select == '4':
               pip_formatter()
               format_menu == False
   
            elif pkg_type_select == '5':
               conda_formatter() 
               format_menu == False
            
            else:
               print ("Plese make valid selection")
   
         else:
            print ("Please select valid option")
   
      print ("Process Completed.")
   
   def manual_menu_process():
   
      print '\n'
      cwd = os.getcwd()
      print("Current working directory is:", cwd)
      os.system("ls -l /home/jonest/power-up/logs/dependencies")
   
      pre_package_lister()
      post_package_lister()
   
      post_pkg_list = final_pkg_list = []
   
      gather_delta()
   
      print "Results:\n"
      print final_pkg_list
      print '\n'
   
      manual_menu()
   
   def automator():
      for i, j in zip(pre_lists, post_list):
         
         pre_file = "{}".format(i)
         post_file = "{}".format(j)
         
         pre = i.split('_',3)[1]
         post = j.split('_',3)[1]
         print ('pre: {} post: {}'.format(pre,post))
   
         if (pre == 'yum'):
            print('yum') #call yum gathering tool
            yum_formatter() 
         elif (pre == 'pip'):
            print('pip') #call pip gathering tool
            pip_formatter()
         elif (pre == 'conda'):
            print ('conda') #call conda gathering tool
            conda_formatter()
   
         else:
            print ("pass")
            pass
   
   def options():
      opt = str(raw_input("Would you like to automate process? \n(1) yes - automate \n(2) no - manual\n"))
      if (opt == '1'):
         automator()
      elif (opt =='2'):
         manual_menu_process() 
      else:
         pass
   
   options()
