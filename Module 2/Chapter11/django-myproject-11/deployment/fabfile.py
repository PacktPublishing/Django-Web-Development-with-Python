# -*- coding: UTF-8 -*-
from fabric.api import env, run, prompt, local, get, sudo
from fabric.colors import red, green
from fabric.state import output

env.environment = ""
env.full = False

output['running'] = False

PRODUCTION_HOST = "myproject.com"
PRODUCTION_USER = "myproject"


def dev():
    """ chooses development environment """
    env.environment = "dev"
    env.hosts = [PRODUCTION_HOST]
    env.user = PRODUCTION_USER
    print("LOCAL DEVELOPMENT ENVIRONMENT\n")


def staging():
    """ chooses testing environment """
    env.environment = "staging"
    env.hosts = ["staging.myproject.com"]
    env.user = "myproject"
    print("STAGING WEBSITE\n")


def production():
    """ chooses production environment """
    env.environment = "production"
    env.hosts = [PRODUCTION_HOST]
    env.user = PRODUCTION_USER
    print("PRODUCTION WEBSITE\n")


def full():
    """ all commands should be executed without questioning """
    env.full = True


def deploy():
    """ updates the chosen environment """
    if not env.environment:
        while env.environment not in ("dev", "staging", "production"):
            env.environment = prompt(red('Please specify target environment ("dev", "staging", or "production"): '))
            print

    globals()["_update_%s" % env.environment]()


def _update_dev():
    """ updates development environment """
    run("")  # password request
    print

    if env.full or "y" == prompt(red('Get latest production database (y/n)?'), default="y"):
        print(green(" * creating production-database dump..."))
        run('cd ~/db_backups/ && ./backup_db.bsh --latest')
        print(green(" * downloading dump..."))
        get("~/db_backups/db_latest.sql", "tmp/db_latest.sql")
        print(green(" * importing the dump locally..."))
        local('python manage.py dbshell < tmp/db_latest.sql && rm tmp/db_latest.sql')
        print
        if env.full or "y" == prompt('Call prepare_dev command (y/n)?', default="y"):
            print(green(" * preparing data for development..."))
            local('python manage.py prepare_dev')
    print

    if env.full or "y" == prompt(red('Download media (y/n)?'), default="y"):
        print(green(" * creating an archive of media..."))
        run('cd ~/project/myproject/media/ '
            '&& tar -cz -f ~/project/myproject/tmp/media.tar.gz *')
        print(green(" * downloading archive..."))
        get("~/project/myproject/tmp/media.tar.gz",
            "tmp/media.tar.gz")
        print(green(" * extracting and removing archive locally..."))
        for host in env.hosts:
            local('cd media/ '
                '&& tar -xzf ../tmp/media.tar.gz '
                '&& rm tmp/media.tar.gz')
        print(green(" * removing archive from the server..."))
        run("rm ~/project/myproject/tmp/media.tar.gz")
    print

    if env.full or "y" == prompt(red('Update code (y/n)?'), default="y"):
        print(green(" * updating code..."))
        local('git pull')
    print

    if env.full or "y" == prompt(red('Migrate database schema (y/n)?'), default="y"):
        print(green(" * migrating database schema..."))
        local("python manage.py migrate --no-initial-data")
        local("python manage.py syncdb")
    print


def _update_staging():
    """ updates testing environment """
    run("")  # password request
    print

    if env.full or "y" == prompt(red('Set maintenance screen (y/n)?'), default="y"):
        print(green(" * Setting maintenance screen"))
        run('cd ~/public_html/ '
            '&& cp .htaccess_maintenance .htaccess')
    print

    if env.full or "y" == prompt(red('Stop cron jobs (y/n)?'), default="y"):
        print(green(" * Stopping cron jobs"))
        sudo('/etc/init.d/cron stop')
    print

    if env.full or "y" == prompt(red('Get latest production database (y/n)?'), default="y"):
        print(green(" * creating production-database dump..."))
        run('cd ~/db_backups/ && ./backup_db.bsh --latest')
        print(green(" * downloading dump..."))
        run("scp %(user)s@%(host)s:~/db_backups/db_latest.sql ~/db_backups/db_latest.sql" % {
            'user': PRODUCTION_USER,
            'host': PRODUCTION_HOST,
        })
        print(green(" * importing the dump locally..."))
        run('cd ~/project/myproject/ && python manage.py dbshell < ~/db_backups/db_latest.sql')
        print
        if env.full or "y" == prompt(red('Call prepare_staging command (y/n)?'), default="y"):
            print(green(" * preparing data for testing..."))
            run('cd ~/project/myproject/ '
                '&& python manage.py prepare_staging')
    print

    if env.full or "y" == prompt(red('Get latest media (y/n)?'), default="y"):
        print(green(" * updating media..."))
        run("scp -r %(user)s@%(host)s:~/project/myproject/media/* ~/project/myproject/media/" % {
            'user': PRODUCTION_USER,
            'host': PRODUCTION_HOST,
        })
    print

    if env.full or "y" == prompt(red('Update code (y/n)?'), default="y"):
        print(green(" * updating code..."))
        run('cd ~/project/myproject '
            '&& git pull')
    print

    if env.full or "y" == prompt(red('Collect static files (y/n)?'), default="y"):
        print(green(" * collecting static files..."))
        run('cd ~/project/myproject '
            '&& python manage.py collectstatic --noinput')
    print

    if env.full or "y" == prompt(red('Migrate database schema (y/n)?'), default="y"):
        print(green(" * migrating database schema..."))
        run('cd ~/project/myproject '
            '&& python manage.py migrate --no-initial-data')
        run('cd ~/project/myproject '
            '&& python manage.py syncdb')
    print

    if env.full or "y" == prompt(red('Restart webserver (y/n)?'), default="y"):
        print(green(" * Restarting Apache"))
        sudo('/etc/init.d/apache2 graceful')
    print

    if env.full or "y" == prompt(red('Start cron jobs (y/n)?'), default="y"):
        print(green(" * Starting cron jobs"))
        sudo('/etc/init.d/cron start')
    print

    if env.full or "y" == prompt(red('Unset maintenance screen (y/n)?'), default="y"):
        print(green(" * Unsetting maintenance screen"))
        run('cd ~/public_html/ '
            '&& cp .htaccess_live .htaccess')
    print


def _update_production():
    """ updates production environment """
    if "y" != prompt(red('Are you sure you want to update ' + red('production', bold=True) + ' website (y/n)?'), default="n"):
        return

    run("")  # password request
    print

    if env.full or "y" == prompt(red('Set maintenance screen (y/n)?'), default="y"):
        print(green(" * Setting maintenance screen"))
        run('cd ~/public_html/ '
            '&& cp .htaccess_maintenance .htaccess')
    print

    if env.full or "y" == prompt(red('Stop cron jobs (y/n)?'), default="y"):
        print(green(" * Stopping cron jobs"))
        sudo('/etc/init.d/cron stop')
    print

    if env.full or "y" == prompt(red('Backup database (y/n)?'), default="y"):
        print(green(" * creating a database dump..."))
        run('cd ~/db_backups/ '
            '&& ./backup_db.bsh')
    print

    if env.full or "y" == prompt(red('Update code (y/n)?'), default="y"):
        print(green(" * updating code..."))
        run('cd ~/project/myproject/ '
            '&& git pull')
    print

    if env.full or "y" == prompt(red('Collect static files (y/n)?'), default="y"):
        print(green(" * collecting static files..."))
        run('cd ~/project/myproject '
            '&& python manage.py collectstatic --noinput')
    print

    if env.full or "y" == prompt(red('Migrate database schema (y/n)?'), default="y"):
        print(green(" * migrating database schema..."))
        run('cd ~/project/myproject '
            '&& python manage.py migrate --no-initial-data')
        run('cd ~/project/myproject '
            '&& python manage.py syncdb')
    print

    if env.full or "y" == prompt(red('Restart webserver (y/n)?'), default="y"):
        print(green(" * Restarting Apache"))
        sudo('/etc/init.d/apache2 graceful')
    print

    if env.full or "y" == prompt(red('Start cron jobs (y/n)?'), default="y"):
        print(green(" * Starting cron jobs"))
        sudo('/etc/init.d/cron start')
    print

    if env.full or "y" == prompt(red('Unset maintenance screen (y/n)?'), default="y"):
        print(green(" * Unsetting maintenance screen"))
        run('cd ~/public_html/ '
            '&& cp .htaccess_live .htaccess')
    print
