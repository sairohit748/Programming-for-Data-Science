# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 00:27:56 2018

@author: Sandy
"""

import io
import os
import re
import fileinput
import sys

## The code will traverse through the folder listing out all files and subfolders within root directory
## It will find for all files that starts with Hi so please place files starting with Hi...in any location
## within that file it will look for lines that has comma and replace tat line with "I am very fine".

folder='D:\\FinanceTrackerAdvisor'
#pattern=','
subst='I am very fine\n'   
#file='^Hi'   
#print(file)

folder='D:\\FinanceTrackerAdvisor'
subst='I am very fine\n'
for root, dirs, files in os.walk(folder, topdown=False):
   for name in files:
      x = os.path.join(root, name)
      #print(x)
      if re.search('^Hi',name):
          print(os.path.join(root, name))
          print(name)
          os.chdir(os.path.join(root))
          file_handle = open(name, 'r')
          file_string = file_handle.readlines()
          file_handle.close()
          count=0
          for line in file_string:
             print(line)
             if re.search(',',line):
                file_string[count]=subst
             count+=1
          print(file_string)
          new_line=''.join(file_string)
          file_handle = open(name, 'w')
          file_handle.write(new_line)
          file_handle.close()          
       
      