#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <CIDR> <COMMUNITY_STRING>"
    echo "Example: $0 192.168.1.0/24 public"
	echo "Example: $0 192.168.1.0/24 private"
    exit 1
fi

CIDR=$1
COMMUNITY_STRING=$2

# Function to check if an IP has SNMP enabled
check_snmp() {
    IP=$1
    SYS_DESCR=$(snmpwalk -v2c -c $COMMUNITY_STRING $IP 1.3.6.1.2.1.1.1.0 2>/dev/null | awk -F ': ' '{print $2}')
    if [ $? -eq 0 ] && [ -n "$SYS_DESCR" ]; then
        echo "Default SNMP community string $COMMUNITY_STRING is enabled on IP address $IP - System Description: $SYS_DESCR"
    fi
}

# Loop through the IP addresses in the CIDR range
echo ""
for IP in $(nmap -sn $CIDR | grep 'Nmap scan report' | awk '{print $5}'); do
    check_snmp $IP &
done

# Wait for all background processes to finish
wait
