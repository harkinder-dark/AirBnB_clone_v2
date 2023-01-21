#!/usr/bin/python3
"""Write a Fabric script that generates a
.tgz archive from the contents of the web_static
folder of your AirBnB Clone repo,
using the function do_pack"""
from fabric.api import local
import tarfile
import os.path
import re
from datetime import datetime


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