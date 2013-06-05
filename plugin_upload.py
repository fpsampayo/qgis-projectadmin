#!/usr/bin/env python
# This script uploads a plugin package on the server
#
# Author: fpsampayo

import os, sys
import getpass
from optparse import OptionParser


# Configuration
USER='root'
SERVER='10.0.0.90'
ENDPOINT='/var/www/qgis/'



def main(options, args):
    
    print "Ejecutando SCP"
    os.system('scp "%s" "%s@%s:%s"' % (args[0], USER, SERVER, ENDPOINT))
    
if __name__ == "__main__":
    parser = OptionParser(usage="%prog [options] plugin.zip")
    parser.add_option("-w", "--password", dest="password",
            help="Password for plugin site", metavar="******")
    parser.add_option("-u", "--username", dest="username",
            help="Username of plugin site", metavar="user")
    parser.add_option("-p", "--port", dest="port",
            help="Server port to connect to", metavar="80")
    parser.add_option("-s", "--server", dest="server",
            help="Specify server name", metavar="plugins.qgis.org")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        print "Please specify zip file.\n"
        parser.print_help()
        sys.exit(1)
    if not options.server:
        options.server = SERVER
    if not options.username:
        # interactive mode
        username = getpass.getuser()
        print "Please enter user name [%s] :"%username,
        res = raw_input()
        if res != "":
            options.username = res
        else:
            options.username = username
    if not options.password:
        # interactive mode
        options.password = getpass.getpass()
    main(options, args)
