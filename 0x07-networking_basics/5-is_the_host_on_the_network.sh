#!/usr/bin/bash

# ip variable
IP="${1}"

# filename variable
fn=$(basename "$BASH_SOURCE" .sh)

if ! [ "$IP" ]; then
	echo "Usage: ${fn} {IP_ADDRESS}"
else
	ping -c 5 "${IP}"
fi
