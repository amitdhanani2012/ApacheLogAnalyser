if [[ `id -u` -eq 0 ]] 
then
   apt-get install python-pip && easy_install tornado
else
   echo "Login as Root"
fi 

if [ $? -eq 0 ]
then
   mkdir /ApacheLogAnalyser
   cp webapp.py /ApacheLogAnalyser
   cp -r templates /ApacheLogAnalyser
   cp run.sh shutdown.sh /ApacheLogAnalyser/.
   chmod  u+x /ApacheLogAnalyser/webappy.sh
   chmod  u+x /ApacheLogAnalyser/run.sh
   chmod  u+x /ApacheLogAnalyser/shutdown.sh
      
fi    
