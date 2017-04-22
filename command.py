# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:05:10 2017

@author: Niket
"""
 
import win32com.client
import os
x=raw_input('Enter your command:')
y=raw_input('Enter your command:')
z=raw_input('Enter your command:')
a=[x,y,z]
for i in a:
    print i
    b= os.system(i + '    >NUL' and 'start' + ' /B '+i)
    if b!=0:
        print 'command not found:',i
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("^c", 1)