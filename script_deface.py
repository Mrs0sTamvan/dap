#!/system/bin/python
"""
Author: Mr.s0s
Date  : 19-05-2017 (12:30)
Name  : Scripts0s

Copyright (c) 2017, Mr.s0s All rights reserved.
"""
import os
import sys
import time

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
print "+-----------------------------------------+"
print "|--------------Scripts0s v1.0--------------|"
print "+-----------------------------------------+"
print "| [+] Author: Mr.s0s                      |"
print "| [+] Date  : 19-05-2017 (12:30)          |"
print "| [+] Team  : G4L4XY CYB3R T34M           |"
print "| [+] Deface Simple Script Maker          |"
print "| [+] Its free and easy to use            |"
print "+-----------------------------------------+"
print
print "[1] Mulai Bro"
print "[2] About"
print "[0] Keluar tod"
print
aa = '"'
menu = raw_input("{Scritps0s}:> ")

try:
   file = open("Kontol.html", 'w')
except(IOError):
   print ("ERROR")
   sys.exit()
  
if menu == '1':
  print "Simple Script"
  print
  defstyletitle_simple = raw_input("Title nya: ")
  defstyleimage_src = raw_input("Link/Image: ")
  defstyleimage_width = raw_input("Lebar/Width: ")
  defstyleimage_height = raw_input("Tinggi/Height: ")
  defstylehacked_simple = raw_input("Hacked by: ")
  defstylemessage_simple = raw_input("Message: ")
  defstyleteam_simple = raw_input("Nama Team: ")
  time.sleep(1)
  print "[+] Berhasil coeg"
  print "[!] Script is save as index.html"
  a = '"center"'
  aaa = '"#111111"'
  b = '"100%"'
  bb = '""'
  c = '"0"'
  d = '"align"'
  e = '"#000000"'
  f = '"10"'
  gg = '"1"'
  h = '"#ffffff"'
  hh = '"#b21f25"'
  hhh = '"#333333"'
  
  file.write(" <body bgcolor=black>\n")
  file.write("\n")
  file.write("<br><title>"+defstyletitle_simple+"</title></br>\n")
  file.write("<td><div align="+a+">\n")
  file.write("</div>        <table width="+b+" border="+c+" cellpadding="+c+" cellspacing="+c+">\n")
  file.write("          <tbody><tr>\n")
  file.write("     <center><img src="+aa+""+defstyleimage_src+""+aa+" alt="+bb+" width="+aa+""+defstyleimage_width+""+aa+" height="+aa+""+defstyleimage_height+""+aa+" align="+d+"></a></center>\n")
  file.write("          </tr>\n")
  file.write("        </tbody></table>\n")
  file.write("<table width="+b+" bgcolor="+e+" border="+c+" cellpadding="+f+" cellspacing="+gg+">\n")
  file.write("\n")
  file.write("  <tbody><tr bgcolor="+h+">\n")
  file.write("    <td bgcolor="+h+"><center><b><font color="+hh+">Hacked By "+defstylehacked_simple+"</font></b></center></td>\n")
  file.write("\n")
  file.write("  </tr>\n")
  file.write("\n")
  file.write("  <tr bgcolor="+hhh+">\n")
  file.write("    <td bgcolor="+aaa+"><center><center><font color="+hh+"><b><br>"+defstylemessage_simple+"</center>\n")
  file.write("      <br><center>"+defstyleteam_simple+"</b></center>\n")
  file.write("\n")
  file.write("\n")
  file.write("   </td></tr><tr bgco")
  sys.exit()
  
if menu == '2':
  print "Scriptux v1.0 19-05-2017 (12:30)"
  print "Author: Mr.s0s"
  print "Team  : G4L4XY CYB3R T34M"
  print "Disclaimer: This tool is for educational purpose only."
  print "My Friends:"
  print "[+] Mr.Server"
  print "[+] InYourHead"
  print "[+] Mr.C"
  print "[+] Mr.Dork"
  print "[+] NoobBisaApah"
  print "[+] Tn.AlifCcr7"
  print "[+] Mr.Apoy"
  print "For the support..."
  
if menu == '0':
  print "Exiting..."
  sys.exit()
