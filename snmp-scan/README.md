Scans a CIDR address for SNMP community strings

Good for finding defaults and creating quick screenshots for reports

Required packages
```bash
sudo apt-get install snmp-mibs-downloader 
sudo apt-get install snmp
```

Example usage
```
snmp-scan.sh <subnet-to-scan> <community-string>
```
```bash
snmp-scan.sh 192.168.1.0/24 public
```
