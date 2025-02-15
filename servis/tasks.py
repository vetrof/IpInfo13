import subprocess

from celery import shared_task


# Backup error [Errno 2] No such file or directory: 'docker' - найти решение ошибки
# Сделать другой проект и запихнуть его в докер и создать расписание что-либо, пусть он скачивает картинку и сохраняет ее локально
# Сохранять в модель (картинку)

@shared_task
def database_backup():
    try:
        # command = ["docker", "exec", "-t", "ipinfo13-db-1", "pg_dumpall", "-c", "-U", "postgr_user"]
        command = ["docker", "exec", "ipinfo13-web-1", "python", "manage.py", "postgres_backup"]
        with open("backup_dump.sql", "w") as file:
            subprocess.run(command, stdout=file, check=True)
        print("Backup save succesfully")
    except Exception as e:
        print("Backup error", e)
