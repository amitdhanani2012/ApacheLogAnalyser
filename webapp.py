#!/usr/bin/python2.7
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
      def get(self):
          self.render('index.html')

class SearchQuery(tornado.web.RequestHandler):
   def post(self):
       ip=self.get_argument('ip')
       date=self.get_argument('date')
       time=self.get_argument('time')
       url=self.get_argument('url')  
       request=self.get_argument('request')
       status=self.get_argument('status')
       size=self.get_argument('size')
       browser=self.get_argument('browser')
       fpath=self.get_argument('fpath')
       if fpath!="" and fpath!=" ":   
          f=open(fpath,"r")
          lines=f.readlines()
          b=[]
          for i in lines:
              a=i.split()
              ipx=a[0]
              datex=a[3].lstrip()
              datex1=datex.split(':') 
              dayx=datex1[0].lstrip('[')
              timex=datex1[1]+":"+datex1[2] #":"+datex1[3]
              requestx=a[5].lstrip('"')
              urlx=a[6].lstrip('/')  
              statusx=a[8]
              sizex=a[9]
              browserx1=a[11:]
              browserx=' '.join(browserx1)
             # browserx=' '.join(browserx2)
              p=""
              t="""if """
              if ip!="" and ip!=" ":
                 t=t+""" ipx==ip """
                 p="and" 
              if time!="" and time!=" ":
                 if p=="and":
                    t=t+""" and """ 
                 p="and" 
                 t=t+"""timex==time.strip()""" 
              if date!="" and date!=" ":
                 if p=="and":
                    t=t+""" and """
                 p="and" 
                 t=t+"""dayx==date.strip()"""  
              if url!="" and url!=" ":
                 if p=="and":
                    t=t+""" and """ 
                 p="and"
                 t=t+"""url==urlx"""
              if request!=" " and request!="":
                 if p=="and":
                    t=t+""" and """ 
                 p="and"
                 t=t+"""request==requestx"""
              if size!="" and size!=" ":
                 if p=="and":
                    t=t+""" and """ 
                 p="and"
                 t=t+"""int(sizex)>=int(size)"""
              if status!=" " and status!="":
                 if p=="and":
                    t=t+""" and """ 
                 p="and"
                 t=t+"""status==statusx"""
              if browser!=" " and browser!="":
                 if p=="and":
                    t=t+""" and """  
                 t=t+"""browser.lower() in browserx.lower()""" 

              if len(t)>3:
                 a[3]=dayx+" "+timex+datex1[3]
                 a[5]=requestx
                 a[6]=urlx
                 browserx=browserx.lstrip('["')
                 browserx=browserx.rstrip('"]')
                 a[11]=browserx  
                 if a[10]!="'-":
                    a[12]="location="+a[10].lstrip('"').rstrip('"')
                 t=t+""" :"""
                 t=t+"""\n\tb.append(a) """
                 #print sizex
                 #print size
                 exec t   
             
              #print t
              #print ipx
              #print ip
              #print date.strip()
              #print time.strip()
              #print url
              #print urlx.lstrip()
             
              
          if len(b)==0:
              b.append("no result")                     

          self.render('search.html',fpath1=b)

if __name__=='__main__':
     tornado.options.parse_command_line()
     app=tornado.web.Application(handlers=[(r'/',IndexHandler),(r'/search',SearchQuery)],template_path=os.path.join(os.path.dirname(__file__),"templates"))
     http_server=tornado.httpserver.HTTPServer(app)
     http_server.listen(options.port)
     tornado.ioloop.IOLoop.instance().start()   
            













