#!/usr/bin/python

import os
import sys

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
#        pre_pkg_version.append(value_a[1])

def post_package_lister():
    for line_a in post_dbfile.readlines():
        value_a = line_a.split()
        post_pkg_list.append(value_a[0])
 #       post_pkg_version.append(value_a[1])

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

#def dependencies():

#    for item in rpm_list:
#        print 'Package Name: {}'.format(item)
#        os.system("yum deplist {} | grep dependency".format(item))

#dependencies()
