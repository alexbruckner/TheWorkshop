#!/bin/sh

cd webapp
nohup python manage.py runserver 0.0.0.0:8000 > django.out 2>&1&

cd ../java
nohup mvn compile exec:java -Dexec.mainClass=com.bru.workshop.Application > java.out 2>&1&
