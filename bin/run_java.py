import os, subprocess

def run_java():
    command = "%s compile exec:java -Dexec.mainClass=com.bru.workshop.Application" % os.environ.get('MAVEN')
    working_dir = os.path.join(os.path.abspath(os.path.dirname('../..')), 'java')
    print "command: %s, cwd: %s" % (command, working_dir)
    process = subprocess.Popen(command, cwd=working_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line = process.stdout.readline()
        if line != '':
            print line,
        else:
            break

if __name__ == "__main__":
    run_java()

