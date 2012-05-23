#!/bin/sh
ps aux | grep com.bru.workshop.Application | awk {'print $2'} | head -1 | xargs kill
ps aux | grep manage.py | awk {'print $2'} | head -1 | xargs kill

