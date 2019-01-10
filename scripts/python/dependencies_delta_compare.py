#!/usr/bin/python

import os
import sys
import fileinput

print '\n'
os.chdir("/home/jonest/power-up/logs/dependencies/")
cwd = os.getcwd() 
print("Current working directory is:", cwd) 
os.system("ls -l /home/jonest/power-up/logs/dependencies")


pre_file  = str(raw_input('Enter pre_install.txt File: '))
post_file = str(raw_input('Enter post_install.txt File: '))

os.system("cat {} | wc -l".format(pre_file))
os.system("cat {} | wc -l".format(post_file))

pre_dbfile  = open("{}".format(pre_file),'r')
post_dbfile = open("{}".format(post_file),'r')

pre_pkg_list    = []
post_pkg_list = final_pkg_list = []

def pre_package_lister():
    for line_a in pre_dbfile.readlines():
        value_a = line_a.split()
        pre_pkg_list.append(value_a[0])

def post_package_lister():
    for line_a in post_dbfile.readlines():
        value_a = line_a.split()
        post_pkg_list.append(value_a[0])

pre_package_lister()
post_package_lister()

delta_pkg_list    = []

for i in pre_pkg_list:
    for x in post_pkg_list:
        if x == i:
           delta_pkg_list.append(x)
           final_pkg_list.remove(x)

final_file  = str(raw_input('Enter final File name: '))
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
         os.system('touch formatted_{}; chmod 777 formatted_{}'
                  .format(final_file,final_file))
         yum_dbfile = open('yml_formatted_{}'.format(final_file),'w')
         for j in final_pkg_list:
            pkg_strip = j.split('.',1)[0]
            new_value = os.popen("cat {} rpm_post_list.txt | grep {} "
                                .format(post_file,pkg_strip)).read()
            yum_dbfile.write('{}\n'.format(new_value))
         os.system("sudo rm -rf formatted_{}".format(final_file))
         format_menu = False

      elif pkg_type_select == '4':
         pip_dbfile = open('{}'.format(final_file),'wt+')
         for line_c in pip_dbfile.readlines():
            value_c = line_c.split()
            new_value = "{}=={}".format(value_c[0],value_c[1])
            pip_dbfile.write('{}\n'.format(new_value))
            print new_value
         format_menu = False
         print ("Done.")

      elif pkg_type_select == '5':
         conda_dbfile = open('{}'.format(final_file),'wt+')
         for line_d in conda_dbfile.readlines():
            value_d = line_d.split()
            new_value = ("{}-{}-{}.tar.bz2"
                        .format(value_d[0],value_d[1],value_d[2]))
            conda_dbfile.write('{}\n'.format(new_value))
            print new_value
         format_menu = False
      else:
         print ("Plese make valid selection")
   else:
      print ("Please select valid option")

print ("Process Completed.")


