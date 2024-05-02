Default Password Tool

2024-01-09


Installation:

Requires the python module "prettytable" that formats CSV output for the terminal. Install with the following command.
```bash
sudo apt-get install python3-prettytable
```

Make the script executable
```bash
chmod +x default-passwords.py
```

Usage:
```bash
default-passwords.py <search_value>
```
The default password file is included "default-passwords.csv"

Example search for cisco
```bash
default-passwords.py cisco
```
All fields are searchable. for example search by Manufacturer or Model. Try your luck!


Adding a default password to the list:

The script is formatted in the following manner.

Manufacturer,Model or Protocol,Username,Password

Each entry must have 4 columns. 

Cisco,AP1200,Administrator,admin

If a single column is blank it must still be formatted as 4 columns using a double comma ",,"

Cisco Linksys,,admin,admin      
