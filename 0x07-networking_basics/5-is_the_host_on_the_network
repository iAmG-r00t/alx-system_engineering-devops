#!/usr/bin/env bash
# script that pings an IP address passed as an argument

# ip variable
IP="${1}"

# filename variable
fn=$(basename "${BASH_SOURCE[@]}")

if ! [ "$IP" ]; then
	echo "Usage: ${fn} {IP_ADDRESS}"
else
	ping -c 5 "${IP}"
fi
