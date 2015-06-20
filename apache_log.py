#!/usr/bin/python3.4
import sys
#print(sys.argv[0])
#print(len(sys.argv))


if(len(sys.argv)<2):
      print("please give two arguments first for log file second for report file name")
      sys.exit(0) 
      
file1=sys.argv[1]
file2=sys.argv[2]

f=open(file1,'r')
f1=open(file2,'w')

ax="<html><head><title>Apache Log Analysys</title></head><body><table border=1><tr><td><b>Remote IP</b></td><td><b>Date And Time</b></td><td><b>Request Type & URL</b></td><td><b>Status</b></td><td><b>Byte Transfered</b></td><td><b>Browser</b></td></tr>"
f1.write(ax)
for line in f:
       a=line.split()
       ip1=a[0]
       date1=a[3]+" timezone="+a[4]
       request="RequestType= "+a[5]+"\""+" Url= \" "+a[6]+"\""+" "+"protocol=\""+a[7]+"\""     
       status=a[8]   
       size=a[9]
       browser=a[11]+a[12]
       #print(date1)  
       f1.write("<tr><td>"+ip1+"</td><td>"+date1+"</td><td>"+request+"</td><td>"+status+"</td><td>"+size+"</td><td>"+browser+"</td></tr>")

f1.write("</table></body></html>")

              
 
