#!/usr/bin/env bash
# install load balancer

# colors
blue='\e[1;34m'
brown='\e[0;33m'
green='\e[1;32m'
reset='\033[0m'

echo -e "${blue}Updating and doing some minor checks...${reset}\n"

function install() {
	command -v "$1" &> /dev/null

	#shellcheck disable=SC2181
	if [ $? -ne 0 ]; then
		echo -e "	Installing: ${brown}$1${reset}\n"
		sudo apt-get update -y -qq && \
			sudo apt-get install -y "$1" -qq
		echo -e "\n"
	else
		echo -e "	${green}${1} is already installed.${reset}\n"
	fi
}

install haproxy #install haproxy

echo -e "\n${blue}Setting up some minor stuff.${reset}\n"

# backup default server config file
sudo cp /etc/haproxy/haproxy.cfg haproxy_default.backup

server_config=\
"
defaults
  mode http
  timeout client 15s
  timeout connect 10s
  timeout server 15s
  timeout http-request 10s

frontend th3gr00t-tech-frontend
    bind *:80
    default_backend th3gr00t-tech-backend

backend th3gr00t-tech-backend
    balance roundrobin
    server 453-web-01 35.243.128.200:80 check
    server 453-web-02 3.239.120.96:80 check
"

# shellcheck disable=SC2154
echo "$server_config" | sudo dd status=none of=/etc/haproxy/haproxy.cfg

# enable haproxy to be started by init script
echo "ENABLED=1" | sudo dd status=none of=/etc/default/haproxy

if [ "$(pgrep -c haproxy)" -le 0 ]; then
	sudo service haproxy start
else
	sudo service haproxy restart
fi
