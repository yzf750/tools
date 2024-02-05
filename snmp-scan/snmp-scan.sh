#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <CIDR> <COMMUNITY_STRING>"
    echo "Example: $0 192.168.1.0/24 public"
    exit 1
fi

CIDR=$1
COMMUNITY_STRING=$2

# ANSI escape codes for text formatting
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to check if an IP has SNMP enabled
echo ""
check_snmp() {
    IP=$1
    SYS_DESCR=$(snmpwalk -v2c -c $COMMUNITY_STRING $IP 1.3.6.1.2.1.1.1.0 2>/dev/null | awk -F ': ' '{print $2}')
    if [ $? -eq 0 ] && [ -n "$SYS_DESCR" ]; then

	# Use color output
	echo -e "SNMP community string ${GREEN}'$COMMUNITY_STRING${NC}' is enabled on ${RED}$IP${NC}"
	echo -e "System Description: $SYS_DESCR"
	echo ""
		
	# No color output
	#echo -e "SNMP community string '$COMMUNITY_STRING' is enabled on $IP"
	#echo -e "System Description: $SYS_DESCR"

        echo "$IP" > $COMMUNITY_STRING-affected-ips.txt
    fi
}

# Loop through the IP addresses in the CIDR range
for IP in $(nmap -sn $CIDR | grep 'Nmap scan report' | awk '{print $5}'); do
    check_snmp $IP &
done

# Wait for all background processes to finish
wait

# Display the list of affected IP addresses
echo -e "\nList of affected IP addresses:"
cat $COMMUNITY_STRING-affected-ips.txt
echo ""
# rm -f $COMMUNITY_STRING-affected_ips.txt
