import subprocess

def run_django():
    process = subprocess.Popen("python manage.py runserver 0.0.0.0:8000", cwd="/Users/alexb/django/workshop/webapp", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line = process.stdout.readline()
        if line != '':
            print line,
        else:
            break

if __name__ == "__main__":
    run_django()