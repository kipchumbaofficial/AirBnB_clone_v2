#!/usr/bin/python3
'''Deploy archive
'''
from fabric.api import env, run, put
import os

env.user = 'ubuntu'
env.key_file = '~/.ssh/id_rsa'
env.hosts = ['107.22.144.84', '52.86.231.250']


def do_deploy(archive_path):
    '''A function to deploy archive
    '''
    if os.path.exists(archive_path):
        file_name = archive_path.split('/')[1]
        dir_name = file_name.split('.')[0]
        target_dir = f'/data/web_static/releases/{dir_name}'
        put(archive_path, '/tmp/')
        run(f'mkdir -p {target_dir}')
        run(f'tar -xzf /tmp/{file_name} -C {target_dir}')
        run(f'rm /tmp/{file_name}')
        run(f'mv {target_dir}/web_static/* {target_dir}')
        run('rm /data/web_static/current')
        run(f'ln -s {target_dir}/ /data/web_static/current')

        print("New version deployed!")

        return True
    return False
