from threading import Thread
from run_django import run_django
from run_java import run_java

if __name__ == "__main__":
    Thread(target = run_django).start()
    Thread(target = run_java).start()