#!/usr/bin/env bash
# changes the following domain resolve ips
#   localhost from 127.0.0.1 to 127.0.0.2
#   facebook.com from 157.240.11.35 to 8.8.8.8

cp /etc/hosts ~/hosts.new
echo "127.0.0.2		localhost" > ~/hosts.new
echo "8.8.8.8		facebook.com" >> ~/hosts.new
cp -f ~/hosts.new /etc/hosts
