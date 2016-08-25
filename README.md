# pySQLdump 
Python 2.7
<h3>Set vi conf/settings.ini</h3>

[mysql]<br/>
user = user_name<br/>
password = pass_word<br/>
dbname = db_name<br/>
destination = /root/pySQLBackup/<br/>



# Dowload
```
# wget https://github.com/Guutong/pySQLdump/releases/download/v.0.0.1/pySQLdumpSetup.sh

# chmod +x pySQLdumpSetup.sh

# mkdir /root/pySQLBackup/

# ./pySQLdumpSetup.sh
```
# How to setting Auto backup with crontab
```
sudo apt-get install crontab
```

```
crontab -e
00 00 * * 0 cd /opt/pySQLdump/ && sh run.sh
ESC
:wq!
```
/etc/init.d/cron restart



