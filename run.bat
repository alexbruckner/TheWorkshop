cd webapp
start env\webapp\Scripts\python.exe manage.py runserver 0.0.0.0:8000 

cd ..\java
start mvn compile exec:java -Dexec.mainClass=com.bru.workshop.Application
