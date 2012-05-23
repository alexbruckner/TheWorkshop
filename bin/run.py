from threading import Thread
from run_django import run_django
from run_java import run_java

if __name__ == "__main__":
    django_thread = Thread(target = run_django)
    django_thread.start()
    java_thread = Thread(target = run_java)
    java_thread .start()
