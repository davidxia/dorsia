# -*- coding: utf-8 -*-


from fabric.api import *
import os


# --------------------------------------------------------------------------------------------------
# Environment and constants
# --------------------------------------------------------------------------------------------------

if env.ssh_config_path and os.path.isfile(os.path.expanduser(env.ssh_config_path)):
    env.use_ssh_config = True

# Hosts onto which we deploy
env.hosts = ['dx']

# Codebase's installation path in hosts
env.code_dir = '/home/david/dorsia'
env.project_root = '/home/david/dorsia'


# --------------------------------------------------------------------------------------------------
# Utility functions
# --------------------------------------------------------------------------------------------------

# Context manager to disable fabric's 'die on non-zero exit status' behaviour
def nonzeroStatusOK():
    return settings(hide('warnings'), warn_only=True)


# Run a command inside the virtualenv
def run_env(cmd):
    return run('source %s/env/bin/activate && %s' % (env.project_root, cmd))


# --------------------------------------------------------------------------------------------------
# System tasks
# --------------------------------------------------------------------------------------------------

@task(default=True)
def setup_env(clean=None):
    '''
    Set up the virtualenv required to run the server.
    '''

    with cd(env.project_root):

        # Clean it out if required
        if clean:
            run('rm -rf env')

        # Make sure the env basedir exists
        with nonzeroStatusOK():
            if not run('test -d env').succeeded:
                run('mkdir -p env && virtualenv env')

        # Do the virtualenv setup
        run_env('./pip/install.py')


def deploy_static():
    '''
    Deploy static files by running collectstatic command.
    '''

    with cd(env.project_root):
        run_env('./manage.py collectstatic -v0 --noinput')


def deploy():
    '''
    Updates codebase from Github

    '''

    with settings(warn_only=True):
        if run('test -d %s' % env.code_dir).failed:
            run('git clone git@github.com:davidxia/dorsia.git %s' % env.code_dir)
        else:
            with cd(env.code_dir):
                run('git pull')
                with cd(env.project_root):
                    run('touch dorsia/wsgi.py')


@task(default=True)
def push():
    '''
    Pull latest changes from Github and collect static files.
    '''

    deploy()
    deploy_static()


@task(default=True)
def push_all():
    '''Pull latest changes from Github, setup virtualenv, collect static files.'''

    # Drop server build into place and set up virtualenv
    deploy()
    setup_env()
    deploy_static()
