"""Crontab practice
"""
import subprocess
import sys
from crontab import CronTab


def get_service_cmd_executable():
    try:
        complete_process = subprocess.run(
            'which service', shell=True, check=True, capture_output=True, text=True)
        return complete_process.stdout.strip()
    except subprocess.CalledProcessError as exc:
        print(f'Get service executable encounter error: {exc}')
        raise


def start_cron_service():
    try:
        service_cmd = get_service_cmd_executable()
        subprocess.run(f'{service_cmd} cron start', shell=True,
                       check=True, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as exc:
        print(f'Start cron service encounter error: {exc}')
        raise


def setup_cron_job(script_path: str):
    # instanciate crontab
    cron = CronTab(user='root')

    # execute script path
    if script_path is None:
        raise FileNotFoundError(f'Target script not found, please confirm script path exists: {script_path}')

    # create job
    job = cron.new(command=f'{sys.executable} {script_path}')

    # setup execution time for job
    job.minute.every(1)

    # add job into cron
    cron.write()


def main():
    script_path = ''
    start_cron_service()
    setup_cron_job(script_path)


if __name__ == '__main__':
    main()
