#!/usr/bin/python3
''' a Fabric script that distributes an archive to your web servers
'''
from fabric.api import *


def do_deploy(archive_path):
    ''' takes the archive path and distributes the given archive to webservers
    '''

    env.hosts = ["35.229.110.107", "35.196.24.51"]

    filename = archive_path.split('/')[-1]
    name = filename.split('.')[0]
    path = "/data/web_static/releases/{}/".format(name)
    currentpath = "/data/web_static/current"

    if not (archive_path):
        return false
    try:
        put(archive_path, "/tmp/")
        run("rm -rf /data/web_static/releases/{}/".format(
            (archive_path.split('/')[-1]).split(".")[0]))
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(
            (archive_path.split('/')[-1]), path))
        run("rm /tmp/{}".format(archive_path.split('/')[-1]))
        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf {}web_static".format(path))
        run("rm -rf {}".format(currentpath))
        run("ln -s /data/web_static/releases/{}/ {}".format(
            ((archive_path.split('/')[-1]).split(".")[0]), currentpath))
        return True

    except:
        return False