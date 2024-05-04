#!/usr/bin/python3
'''A fabric script to pach folder to .tgz archive
'''
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    '''A function to archive a directory
    '''
    if not os.path.exists('versions'):
        local('mkdir versions')
    date_time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{date_time}'
    local(f'tar -czvf versions/{archive_name}.tgz web_static')
