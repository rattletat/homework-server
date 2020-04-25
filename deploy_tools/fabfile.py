import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run
env.use_ssh_config = True

REPO_URL = 'https://github.com/rattletat/homework-server.git'


def deploy(domain):
    site_folder = f'/home/{env.user}/sites/{domain}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv(domain)
        _create_or_update_dotenv(domain)
        _update_static_files()
        _update_database()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtualenv(domain):
    poetry_failed = run("poetry about").failed
    if poetry_failed:
        run("curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python")
        run('source $HOME/.poetry/env')
    if not exists('pyproject.toml'):
        run(f'poetry new . -n --src --name {domain}')
    run('poetry install')


def _create_or_update_dotenv(domain):
    append('.env', 'DJANGO_DEPLOY=y')
    append('.env', f'SITENAME={domain}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        choices = 'abcdefghijklmnopqrstuvwxyz123456789'
        new_secret = ''.join(random.SystemRandom().choices(choices, k=50))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files():
    run('poetry run python3.8 manage.py collectstatic --noinput')


def _update_database():
    run('poetry run python3.8 manage.py migrate --noinput')
