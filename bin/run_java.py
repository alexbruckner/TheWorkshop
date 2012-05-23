import subprocess

def run_java():
    process = subprocess.Popen("/apache-maven-3.0.3/bin/mvn.bat compile exec:java -Dexec.mainClass=com.bru.workshop.Application", cwd="/Users/alexb/django/workshop/java", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line = process.stdout.readline()
        if line != '':
            print line,
        else:
            break

if __name__ == "__main__":
    run_java()