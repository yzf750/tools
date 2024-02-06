Scans a CIDR address using specified SNMP community string

Good for finding defaults and creating quick screenshots for reports

Required packages
```bash
sudo apt-get install nmap
sudo apt-get install snmp-mibs-downloader 
sudo apt-get install snmp
```

Example usage
```
snmp-scan.sh <subnet-to-scan> <community-string>
```
Single Host
```bash
snmp-scan.sh 192.168.1.222 public
```
Single Subnet
```bash
snmp-scan.sh 192.168.1.0/24 public
```
Multiple Subnets
```bash
snmp-scan.sh 192.168.1.0/24,10.10.10.0/24 public
```
