#!/usr/bin/python3
''' a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
'''
from fabric.api import local
from datetime import datetime


def do_pack():
    ''' Packs all webstatic files into .tgz archive
    '''
    try:
        local("mkdir -p versions")
        path = local("tar -cvzf versions/web_static_{}.tgz web_static".format(
            datetime.now().strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz"
    except:
        return None