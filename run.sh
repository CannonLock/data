#!/bin/bash

cd /home/clock/data

git pull
git add .
git commit -m "CRON: Push New Data"
git push
