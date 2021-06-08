import logging
import os
import shutil
import subprocess

import pytest

from client import Client

log = logging.getLogger('Test')
REPORTS_DIR = 'allure-results'


@pytest.fixture()
def client():
    return Client()


def pytest_configure(config):
    # Prepare reports dir

    log.info("delete report dir")

    try:
        shutil.rmtree(REPORTS_DIR)
        log.info('  ... already deletes')
    except FileNotFoundError:
        pass
    finally:
        os.makedirs(REPORTS_DIR)
        log.info('  ... create report dir')

    log.info('Start executing:')


# noinspection PyUnusedLocal
def pytest_unconfigure(config):
    log.info('### Create allure report ')
    try:
        subprocess.check_call(f'allure generate -c {REPORTS_DIR}', shell=True)  # noqa

    except subprocess.CalledProcessError:
        logging.warning('!!! allure: cannot create report - report dir is empty')
