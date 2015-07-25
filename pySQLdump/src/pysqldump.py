#!/usr/bin/python
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
__author__ = "GuutonG"
__date__ = "$Jul 25, 2015 3:10:50 PM$"
######################################################
#____________________________________________________#
#_______________Mr.Pornmongkon Pongsai_______________#
#____________________pySQLdump v.0.1_________________#
#______________Create Date : 25-07-2015______________#
#____________________________________________________#
######################################################
from ConfigParser import SafeConfigParser
from os import path
from subprocess import Popen, PIPE
import shlex
import datetime
import logging

def main():
    config_file = 'conf/settings.ini'
    logs_path = 'logs/pySQLdump.log'
    logging.basicConfig(filename=logs_path,format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
    # Read in all the settings
    config = SafeConfigParser()
    config.read(config_file)
    user = config.get('mysql', 'user')
    password = config.get('mysql', 'password')
    database = config.get('mysql', 'dbname')
    destination = config.get('mysql', 'destination')
    date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    file_name = 'pySQLdump-' + database + '-' + date

    logging.info('==[RUN]== Running mysqldump')
    cmd = 'mysqldump -u' + user + ' ' + database + ' -p"' + password + '" --result-file="' + file_name + '.sql"'
    logging.debug(cmd)	
    run_cmd(cmd)

    logging.info('Creating Zip file')
    run_cmd('zip ' + file_name + '.zip ' + file_name + '.sql')

    logging.info('Removing dump file')
    run_cmd('rm ' + file_name + '.sql')

    logging.info('Moving zipped tarball to destination')
    run_cmd('mv ' + file_name + '.zip ' + destination)
    logging.info('==[PASS]== Mysqldump success!')
    
def run_cmd(cmd):
    process = Popen(shlex.split(cmd), stdout=PIPE)
    dump_output = process.communicate()[0]
    exit_code = process.wait()
    if exit_code != 0:
        print(dump_output)
        raise Exception(str(exit_code) + ' - Error executing command.  Please review output.')

if __name__ == '__main__':
    main()
