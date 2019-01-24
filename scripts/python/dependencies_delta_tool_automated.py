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

import code

#locate dependencies directory

print '\n'
os.chdir("/home/jonest/power-up/logs/dependencies/")
cwd = os.getcwd()
print("Current working directory is:", cwd)

class engr_delta_collect:

      def __init__(self,pre_list_file,post_list_file):

          self.pre_list_file = pre_list_file
          self.post_list_file = post_list_file
          self.final_file = final_file = pre_list_file.split('_',3)[0] + "_" + pre_list_file.split('_',3)[1] +'_pkglist_final.txt'
          self.post_list_file = post_list_file
          self.pre_pkg_list = pre_pkg_list = []
          self.post_pkg_list = final_pkg_list = []
          self.delta_pkg_list = delta_pkg_list = []
   
      def pre_package_lister(self):  #parses pre-file data from the tuple of the text file in the given instance (complete)

        pre_dbfile  = open("{}".format(self.pre_list_file),'r')
        for line_a in pre_dbfile.readlines():
           value_a = line_a.split()
           final_value_a = value_a[0]
           self.pre_pkg_list.append(final_value_a)

        print "pre_package_lister completed"
        return self.pre_pkg_list
         
        code.interact(banner='DEBUG!!!!!', local=dict(globals(), **locals()))

      def post_package_lister(self):  #parses post-file data from the tuple of the text file in the given instance (complete)

        pre_dbfile  = open("{}".format(self.post_list_file),'r')
        for line_a in pre_dbfile.readlines():
           value_a = line_a.split()
           final_value_a = value_a[0]
           self.post_pkg_list.append(final_value_a)

        print "post_package_lister completed"
        return self.post_pkg_list

      def delta_logic(self): #find delta from pre and post package list and add to delta delta_pkg_list.

         for i in self.pre_pkg_list:
            for x in self.post_pkg_list:
               if x == i:
                  self.delta_pkg_list.append(x)
                  self.post_pkg_list.remove(x)
                  os.system('touch {}; chmod 777 {}'.format(self.final_file, self.final_file))

         with open('{}'.format(self.post_list_file)) as oldfile, open('{}'.format(self.final_file), 'wt+') as newfile:
            for line in oldfile:
               if any(pkg in line for pkg in self.post_pkg_list):
                  newfile.write(line)

         print "Results:\n"
         print self.post_pkg_list
         print '\n'

         return self.post_pkg_list

      def yum_formatter(self):

         dep_search = [
                       'anaconda',
                       'cuda-powerup',
                       'powerai-powerup',
                       'dependencies-powerup',
                       'epel-ppc64le-powerup',
                       'installed',
                      ]
         dep_files = [
                      'anaconda_{}'.format(self.final_file),
                      'cuda-powerup_{}'.format(self.final_file),
                      'powerai-powerup_{}'.format(self.final_file),
                      'dependencies-powerup_{}'.format(self.final_file),
                      'epel-ppc64le-powerup_{}'.format(self.final_file),
                      'installed_{}'.format(self.final_file),
                      ]

         tmp_dep_files = [
                          'tmp_anaconda_{}'.format(self.final_file),
                          'tmp_cuda-powerup_{}'.format(self.final_file),
                          'tmp_powerai-powerup_{}'.format(self.final_file),
                          'tmp_dependencies-powerup_{}'.format(self.final_file),
                          'tmp_epel-ppc64le-powerup_{}'.format(self.final_file),
                          'tmp_installed_{}'.format(self.final_file),
                         ]

         yum_conda_dbfile = open('anaconda_{}'
                                .format(self.final_file),'w+')
         yum_cuda_dbfile = open('cuda-powerup_{}'
                               .format(self.final_file),'w+')
         yum_powerai_dbfile = open('powerai-powerup_{}'
                                  .format(self.final_file),'w+')
         yum_dependencies_dbfile = open('dependencies-powerup_{}'
                                       .format(self.final_file),'w+')
         yum_epel_dbfile = open('epel-ppc64le-powerup_{}'
                               .format(self.final_file),'w+')
         yum_installed_dbfile = open('installed_{}'
                                    .format(self.final_file),'w+')

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
                               .format(self.final_file,search,self.final_file))

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

         os.system("sudo rm -rf tmp* {} ".format(self.final_file)) #creates temperary files, sorts between repositories, formats in proper form and adds to text file.

         print ("Yum Format Completed") 

      def pip_formatter(self):#executes pip_formatter based from pip output file and formats in proper form and adds to text file.

         pip_dbfile = open('{}'.format(self.final_file),'rb+')
         for line_c in pip_dbfile.readlines():
            value_c = line_c.split()
            prefix = value_c[0]
            suffix = value_c[1]
            new_value = "{}=={}".format(prefix,suffix)
            pip_dbfile.write('{}\n'.format(new_value))

      def conda_formatter(self):

         conda_dbfile = open('{}'.format(self.final_file),'rb+')
         for line_d in conda_dbfile.readlines():
            value_d = line_d.split()
            prefix = value_d[0]
            suffix = value_d[2]
            version = value_d[1]
            new_value = ("{}-{}-{}.tar.bz2"
                        .format(prefix,version,suffix))

def automator(self):

   pre_file = "{}".format(pre_list_file)
   post_file = "{}".format(post_list_file)

   function = j.split('_',3)[1]

   pre_package_lister()
   post_package_lister()
   delta_logic()

   #code.interact(banner='automator', local=dict(globals(), **locals()))

   if (function == 'yum'):
      print('yum') #call yum gathering tool
      yum_formatter()
   elif (function == 'pip'):
      print('pip') #call pip gathering tool
      pip_formatter()
   elif (function == 'conda'):
      print ('conda') #call conda gathering tool
      conda_formatter()


pre_list_file = [
                 'client_yum_pre_list.txt',
                 'client_pip_pre_install.txt',
                 'dlipy3_pip_pre_install.txt',
                 'dlipy2_pip_pre_install.txt',
                 'client_conda_pre_install.txt',
                 'dlipy3_conda_pre_install.txt',
                 'dlipy2_conda_pre_install.txt',
                ]

post_list_file = [
                  'client_yum_post_list.txt',
                  'client_pip_post_install.txt',
                  'dlipy3_pip_post_install.txt',
                  'dlipy2_pip_post_install.txt',
                  'client_conda_post_install.txt',
                  'dlipy3_conda_post_install.txt',
                  'dlipy2_conda_post_install.txt',
                 ]

client_yum = engr_delta_collect(pre_list_file[0],post_list_file[0])
engr_delta_collect.pre_package_lister(client_yum)
engr_delta_collect.post_package_lister(client_yum)
engr_delta_collect.delta_logic(client_yum)
engr_delta_collect.yum_formatter(client_yum)

client_pip = engr_delta_collect(pre_list_file[1],post_list_file[1])
engr_delta_collect.pre_package_lister(client_pip)
engr_delta_collect.post_package_lister(client_pip)
engr_delta_collect.delta_logic(client_pip)
engr_delta_collect.pip_formatter(client_pip)

dlipy3_pip = engr_delta_collect(pre_list_file[2],post_list_file[2])
engr_delta_collect.pre_package_lister(dlipy3_pip)
engr_delta_collect.post_package_lister(dlipy3_pip)
engr_delta_collect.delta_logic(dlipy3_pip)
engr_delta_collect.pip_formatter(dlipy3_pip)

dlipy2_pip = engr_delta_collect(pre_list_file[3],post_list_file[3])
engr_delta_collect.pre_package_lister(dlipy2_pip)
engr_delta_collect.post_package_lister(dlipy2_pip)
engr_delta_collect.delta_logic(dlipy2_pip)
engr_delta_collect.pip_formatter(dlipy2_pip)

client_conda = engr_delta_collect(pre_list_file[4],post_list_file[4])
engr_delta_collect.pre_package_lister(client_conda)
engr_delta_collect.post_package_lister(client_conda)
engr_delta_collect.delta_logic(client_conda)
engr_delta_collect.conda_formatter(client_conda)

dlipy3_conda = engr_delta_collect(pre_list_file[5],post_list_file[5])
engr_delta_collect.pre_package_lister(dlipy3_conda)
engr_delta_collect.post_package_lister(dlipy3_conda)
engr_delta_collect.delta_logic(dlipy3_conda)
engr_delta_collect.conda_formatter(dlipy3_conda)

dlipy2_conda = engr_delta_collect(pre_list_file[6],post_list_file[6])
engr_delta_collect.pre_package_lister(dlipy2_conda)
engr_delta_collect.post_package_lister(dlipy2_conda)
engr_delta_collect.delta_logic(dlipy2_conda)
engr_delta_collect.conda_formatter(dlipy2_conda)

