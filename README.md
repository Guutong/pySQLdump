# pySQLdump 
Python 2.7
<h3>Set vi conf/settings.ini</h3>

[mysql]<br/>
user = user_name<br/>
password = pass_word<br/>
dbname = db_name<br/>
destination = /root/pySQLBackup/<br/>



<h3>Dowload</h3><br/>
wget https://github.com/Guutong/pySQLdump/releases/download/v.0.0.1/pySQLdumpSetup.sh<br/>

<h3>How to setting Auto backup with crontab</h3><br/>
<p>sudo apt-get install crontab <br/>
crontab -e <br/>
00 00 * * 0 cd /opt/pySQLdump/ && sh run.sh <br/>
ESC<br/>
:wq!<br/>
/etc/init.d/cron restart <br/>
</p><br/>


