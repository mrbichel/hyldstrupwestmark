from fabric.api import env, run, prefix, cd, local

env.user = 'hyldstrupwestmark'
env.hosts = ['tango.johan.cc']
env.directory = '/home/hyldstrupwestmark/srv/hyldstrupwestmark'
env.activate = 'source /home/hyldstrupwestmark/.virtualenvs/hyldstrupwestmark/bin/activate'

def deploy():
    local('git push')
    with cd(env.directory):
        with prefix(env.activate):
            run('git pull')
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('python manage.py cleanup')
            run('touch hyldstrupwestmark/wsgi.py') # this triggers a gracefull reload
