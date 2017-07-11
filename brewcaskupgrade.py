#!/usr/bin/env python

import subprocess

def run_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.stdout.readlines()

def get_app():
    p = run_command('brew cask list')
    return [x.strip() for x in p]

def check_version(app):
    p = run_command('brew cask info {}'.format(app))
    remote_ver = p[0].split()[1]
    local_ver  = p[2].split()[0].split('/')[-1]
    n = 0 if remote_ver == local_ver else 1
    return (n, remote_ver, local_ver)

def upgrade_apps_list():
    apps = dict()
    installed_apps = get_app()
    print('Check apps version:')
    for app in installed_apps:
        appinfo = check_version(app)
        if appinfo[0]:
            print('{}:{} ===> {}'.format(app, appinfo[2], appinfo[1]))
            apps[app] = appinfo
    return apps

def upgrade_app(apps):
    for app in apps:
        print('Begin update {}'.format(app))
        p = subprocess.Popen('brew cask reinstall {}'.format(app), shell=True)
        p.wait()

if __name__ == '__main__':
    print('Update brew cache...')
    run_command('brew update')
    print('###')
    apps = upgrade_apps_list()
    print('###')
    if apps:
        c = raw_input('Do you want upgrade? [Y/N]: ')
        if c.upper() == 'Y':
            upgrade_app(apps)
            print('Upgrade finish !')
        else:
            print('User cancel ...')
    else:
        print('All applications are new.')
