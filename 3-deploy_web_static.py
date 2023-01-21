#!/usr/bin/python3
"""Write a Fabric script (based on the file
2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers,
using the function deploy"""
from fabric.api import *
import tarfile
import os.path
import re
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ["54.146.92.136", "54.88.19.28"]
env.key_filename = "~/id_rsa"


def do_pack():
    """function do_pack"""
    target = local("mkdir -p versions")
    hour = str(datetime.now()).replace(" ", '')
    name = re.sub(r'[^\w\s]', '', hour)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(name))
    if os.path.exists("./versions/web_static_{}.tgz".format(name)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(name))
    else:
        return None


def do_deploy(archive_path):
    """archive_path : filename path
    distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arch = archive_path.split("/")
        base = arch[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(base))
        main = "/data/web_static/releases/{}".format(base)
        sudo('tar -xzf /tmp/{} -C {}/'.format(arch[1], main))
        sudo('rm /tmp/{}'.format(arch[1]))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True
    except:
        return False


def deploy():
    """distributes an archive to your web servers"""
    path = do_pack()
    if path is None:
        return False
    f = do_deploy(path)
    return f