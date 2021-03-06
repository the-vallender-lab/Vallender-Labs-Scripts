#!/usr/bin/env python
"""Invoke tasks."""
import os
import json
import shutil
import webbrowser

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'cookiecutter.json'), 'r') as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
# Match default value of website_name from cookiecutter.json
COOKIE = os.path.join(HERE, COOKIECUTTER_SETTINGS['website_name'])
AUTOAPP = os.path.join(COOKIE, 'autoapp.py')
REQUIREMENTS = os.path.join(COOKIE, 'requirements', 'dev.txt')


@task
def build(ctx):
    """Build the cookiecutter.

    :param ctx: 

    """
    ctx.run('cookiecutter {0} --no-input'.format(HERE))


@task
def clean(ctx):
    """Clean out generated cookiecutter.

    :param ctx: 

    """
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print('Removed {0}'.format(COOKIE))
    else:
        print('App directory does not exist. Skipping.')


def _run_flask_command(ctx, command):
    """

    :param ctx: 
    :param command: 

    """
    ctx.run('FLASK_APP={0} flask {1}'.format(AUTOAPP, command), echo=True)


@task(pre=[clean, build])
def test(ctx):
    """Run lint commands and tests.

    :param ctx: 

    """
    ctx.run('pip install -r {0} --ignore-installed'.format(REQUIREMENTS),
            echo=True)
    os.chdir(COOKIE)
    _run_flask_command(ctx, 'lint')
    _run_flask_command(ctx, 'test')

@task
def readme(ctx, browse=False):
    """

    :param ctx: 
    :param browse:  (Default value = False)

    """
    ctx.run("rst2html.py README.rst > README.html")
    if browse:
        webbrowser.open_new_tab('README.html')

