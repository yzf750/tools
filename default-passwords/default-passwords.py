#!/usr/bin/env python3

# sudo apt-get install python3-prettytable

import csv
import sys
from prettytable import PrettyTable

def parse_csv_from_string(csv_data):
    data = []
    csv_reader = csv.reader(csv_data.splitlines())
    headers = next(csv_reader)  # Assuming the first row contains headers
    for row in csv_reader:
        data.append(dict(zip(headers, row)))
    return headers, data

def search_csv(headers, data, partial_value):
    results = []
    for row in data:
        for column in headers:
            cell_value = row.get(column)
            if cell_value and partial_value.lower() in cell_value.lower():
                results.append(row)
                break  # Stop searching other columns for the same row once a match is found
    return results

def display_results(results):
    if results:
        table = PrettyTable()
        table.field_names = results[0].keys()
        for result in results:
            table.add_row(result.values())
        print(table)
    else:
        print("No results found.")

if __name__ == "__main__":
    # CSV data included inside the script
    csv_data = """Manufacturer,Model or Protocol,Username,Password
MySQL,,root,mysql
MySQL,,root,root
MySQL,,root,chippc
MySQL,,admin,admin
MySQL,,root,nagiosxi
MySQL,,root,usbw
MySQL,,cloudera,cloudera
MySQL,,root,cloudera
MySQL,,root,moves
MySQL,,moves,moves
MySQL,,root,testpw
MySQL,,root,p@ck3tf3nc3
MySQL,,mcUser,medocheck123
MySQL,,root,mktt
MySQL,,root,123
MySQL,,dbuser,123
MySQL,,asteriskuser,amp109
MySQL,,asteriskuser,eLaStIx.asteriskuser.2oo7
MySQL,,root,raspberry
MySQL,,root,openauditrootuserpassword
MySQL,,root,vagrant
MySQL,,root,123qweASD#
Avaya,,superuser,pumpkin1
Avaya,,wsuperuser,pumpkin1
Avaya,,wlsadmin,pumpkin1
Avaya,,root,root
Avaya,,diag,danger
Avaya,,manuf,xxyyzz
Avaya,,root,cms500
Avaya,,dadmin,dadmin01
Avaya,,craft,crftpw
Avaya,,root,ROOT500
Avaya,,admin,admin123
Avaya,,admin,password
Avaya,,admin,admin
Alteon ACEDirector3,console,admin,(none)
Alteon ACEswitch 180e,HTTP,admin,admin
Alteon ACEswitch 180e,HTTP,admin,linga
Alteon ACEswitch 180e,Telnet,admin,(none)
Alteon Web Systems 5.2,Telnet,(none),14admin
Alteon ACEDirector3,console,admin,(none)
Alteon ACEswitch 180e,HTTP,admin,admin
Alteon ACEswitch 180e,HTTP,admin,linga
Alteon ACEswitch 180e,Telnet,admin,(none)
Alteon Web Systems 5.2,Telnet,(none),14admin
Konica Minolta,,<blank>,sysadm
Konica Minolta,,<blank>,sysAdmin
Konica Minolta,(web),admin,administrator
Konica Minolta,(web),<blank>,0
Konica Minolta,(web),<blank>,0000
Konica Minolta,(web),<blank>,1234
Konica Minolta,(web),<blank>,1234567812345678
Konica Minolta,(web),<blank>,<blank>
Konica Minolta,(web),<blank>,MagiMFP
Konica Minolta,(web),<blank>,sysadm
Konica Minolta,(web),<blank>,sysAdmin
Canon,MG7500,ADMIN,canon
Canon,MG6600,ADMIN,canon
Canon,MG5600,ADMIN,canon
Canon,MG2900,ADMIN,canon
Canon,MX490,ADMIN,canon
Canon,MB5300,ADMIN,canon
Canon,MB5000,ADMIN,canon
Canon,MB2300,ADMIN,canon
Canon,MB2000,ADMIN,canon
Canon,iB4000,ADMIN,canon
Canon,PRO-100,ADMIN,canon
Canon,PRO-10,ADMIN,canon
100Fio Networks,Station M5,admin,admin
1net1,R-90,admin,1
2wire,1000hg,,
2wire,1000s,NOLOGIN,NOLOGIN
2wire,1000sw,NOLOGIN,NOLOGIN
2wire,1070-B,,NOLOGIN
2wire,1700hw,NOLOGIN,NOLOGIN
2wire,1701HG,,NOLOGIN
2wire,1800hg,NOLOGIN,NOLOGIN
2wire,1800hw,NOLOGIN,NOLOGIN
2wire,2071,,NOLOGIN
2wire,2071-A,,NOLOGIN
2wire,2700HBV-2,,NOLOGIN
2wire,2700hg,,NOLOGIN
2wire,2700HG,,NOLOGIN
2wire,2700HG-B,,
2wire,2700HG-D,Blank,NOLOGIN
2wire,2700HG-D,blank,blank
2wire,2700HG-E,,NOLOGIN
2wire,2700HG-S,,NOLOGIN
2wire,2701HG,,NOLOGIN
2wire,2701HG-B,,NOLOGIN
2wire,2701HG-D,,NOLOGIN
2wire,2701HG-D,blank,blank
2wire,2701HG-G,,NOLOGIN
2wire,2701HG-G,,
2wire,2701HG-S,,NOLOGIN
2wire,2701HG-T,,NOLOGIN
2wire,2701HGV-B,,NOLOGIN
2wire,2701HGV-E,,NOLOGIN
2wire,2701HGV-W,,NOLOGIN
2wire,3600HGV,,NOLOGIN
2wire,3800HGV-B,,NOLOGIN
2wire,3801HGV,,NOLOGIN
2wire,5012NV-002,,NOLOGIN
2wire,BT2700HG-V,,NOLOGIN
2wire,i3812V,,NOLOGIN
3BB,NT3BB-1PWN,admin,3bb
3BB,NT3BB-4PWN,admin,3bb
3com,3c510,NONE,admin
3com,3c855,NONE,admin
3com,3C857,NONE,admin
3com,3CP4130,admin,1234
3com,3cr856-95,NONE,admin
3com,3CR858-91,none,admin
3com,3cr860-95,NONE,1234
3com,3CRWDR100A-72,NONE,admin
3com,3CRWDR101A-75,none,admin
3com,3CRWDR101E-75,none,admin
3com,3CRWDR300A-73,,admin
3com,3crwe51196,NONE,admin
3com,3crwe52196,NONE,admin
3com,3crwe53172,,admin
3com,3crwe554G72,NONE,admin
3com,3CRWE554G72T,admin,admin
3com,3CRWE754G72,NONE,admin
3com,3CRWER100-75,none,admin
3com,3CRWER200-75,blank,admin
3com,3CRWER300-73,blank,admin
3com,WL522,,admin
3com,WL540,NONE,admin
8level,WRT-150,admin,admin
A-Link,BR4,admin,1234
A-Link,RoadRunner 24,admin,password
A-Link,RoadRunner 24AP,admin,password
A-Link,RoadRunner 24API,admin,password
A-Link,RoadRunner 44b,admin,epicrouter
A-Link,RoadRunner 64,admin,password
A-Link,RoadRunner 84AP,admin,password
A-Link,RoadRunner 84AP,admin,password
A-Link,WL54AP2,UNKNOWN,UNKNOWN
A-Link,WNAP4G,,admin
ACorp,HU5D,blank,blank
ACorp,Sprinter LAN420M,admin,admin
ADB,P RG A4202N,3play,3play
ADDON,ARM8100,Admin,Admin
ADDON,ARM8200,addon,addon
ADDON,BR4000,admin,1234
ADDON,GWAR3000,Admin,Admin
ADDON,WBR9200,blank,blank
ADDON,WTC229T,unknown,unknown
AGK Nordic,WA-4054,blank,admin
AOpen,AOR-411,,1234
AP Router,NG-5.2,root,root
ATEL,ALR-U270,admin,admin
ATnT,6800G,UNKNOWN,UNKNOWN
ATnT,Home Base,none,attadmin
AWB Networks,RG231,operator,oper1234
AZiO,AER114A,unknown,unknown
Above Cable,AirCon 1100,NONE,admin
Accton,Cheetah Access,NONE,blank
Acer,Wlan GRU2,admin,password
Actiontec,1020,NOLOGIN,NOLOGIN
Actiontec,2700HG-D,,NOLOGIN
Actiontec,C1000A,admin,unknown
Actiontec,F2250,admin,admin
Actiontec,GT701-WG,admin,password
Actiontec,GT701-WRU,NOLOGIN,NOLOGIN
Actiontec,GT701R,,NOLOGIN
Actiontec,GT701WG,NOLOGIN,NOLOGIN
Actiontec,GT701WG,admin,admin
Actiontec,GT704-WG,NOLOGIN,NOLOGIN
Actiontec,GT704-WG,admin,password
Actiontec,GT704-WG,admin,password
Actiontec,GT704WG,NOLOGIN,NOLOGIN
Actiontec,GT724R,admin,password
Actiontec,GT724WG,admin,password
Actiontec,GT784WN,admin,none
Actiontec,GT784WN,admin,on router sticker
Actiontec,GT784WN TDS,admin,password
Actiontec,GT784WNV,admin,found on router label
Actiontec,M1000,admin,password
Actiontec,M1000,blank,blank
Actiontec,M1000,admin,password
Actiontec,MI424WR,admin,password
Actiontec,MI424WR,admin,password
Actiontec,MI424WR,admin,password
Actiontec,MI424WR,admin,password
Actiontec,MI424WR,admin,password
Actiontec,MI424WR,admin,password
Actiontec,MI424WR GEN2,admin,password
Actiontec,MI424WR GEN2,admin,password
Actiontec,MI424WR GEN2,admin,password
Actiontec,MI424WR GEN2,admin,password
Actiontec,MI424WR GEN3I,admin,password
Actiontec,PK5000,blank,blank
Actiontec,PK5000,blank,blank
Actiontec,PK5000,blank,blank
Actiontec,Q1000,blank,blank
Actiontec,Q1000,blank,blank
Actiontec,Q1000,blank,blank
Actiontec,R1000H,admin,admin
Actiontec,R1000H,created in initial setup,created in initial setup
Actiontec,R1520SU,NOLOGIN,NOLOGIN
Actiontec,R1524SU,NOLOGIN,NOLOGIN
Actiontec,R1524SU-1,NOLOGIN,NOLOGIN
Actiontec,T1200H,admin,printed on router
Actiontec,T2200H,admin,printed on bottom of router
Actiontec,T3200,admin,printed on side of router
Actiontec,TDSGT784WN,admin,password
Actiontec,V1000H,admin,none
Actiontec,V1000H,admin,telus
Actiontec,V1000H,admin,telus
Adaptec,AWM-8084,admin,blank
Advantek,abr241,admin,1234
Advantek,ABR241,admin,1234
Advantek,ABR241,admin,1234
Advantek,AWR-954GR,unknown,unknown
Aethra,FS4104-AW,UNKNOWN,UNKNOWN
Aethra Starvoice,IADSV1042,anything,blank
AirLAN,WR150,root,admin
AirLive,WL-1500R,airlive,airlive
AirLive,WL-1500R,airlive,airlive
AirLive,WT-2000ARM,admin,1234
AirRouter,AirOS,blank,blank
AirTies,RT-110,unknown,unknown
AirTies,RT-205,,blank
AirTies,RT-211,none,unknown
Airlink 101,AR315W,NOLOGIN,NOLOGIN
Airlink 101,AR325W,NONE,admin
Airlink 101,AR410W,admin,admin
Airlink 101,AR420W,unknown,unknown
Airlink 101,AR430W,admin,admin
Airlink 101,AR504,blank,admin
Airlink 101,AR525W,admin,admin
Airlink 101,AR570W,admin,blank
Airlink 101,AR625W,admin,admin
Airlink 101,AR670W,admin,admin
Airlink 101,AR680W,admin,admin
Airlink 101,AR695W,none,admin
Airlink 101,ASOHO4P,blank,blank
Airlink 101,AWLH6080,unknown,unknown
Airlink 101,RT210W,none,unknown
Airnet,AER014,admin,1234
Airnet,AER114,admin,1234
Airnet,AWR014G,admin,admin
Alcatel Lucent,Cellpipe 7130,admin,admin
Alcatel Lucent,I-240G-D,admin,conf
Alcatel Lucent,I-240W-Q,admin,admin
Alice,AH4021,,AliceMod
Alice,IAD-5130,unknown,unknown
Alice Box,AH4021,UNKNOWN,UNKNOWN
AllNet,ALL0276,blank,blank
Allied Data,CopperJet 1616-2P,admin,admin
Allied Data,CopperJet 810,admin,admin
Allied Data,CopperJet 816-2P,admin,admin
Allied Data,HLF-1616-2PEU76-01,admin,admin
Allied Telesyn,AR240E,manager,friend
Allied Telesyn,AT-APR16,admin,admin
Allied Telesyn,AT-AR220E,root,blank
Allied Telesyn,AT-AR221E,,blank
Allied Telesyn,AT-AR236E,manager,friend
Alpha,ASL-26555,1234,1234
Alvarion,BMAX-6000,operator,wimax
Alvarion,WIXFBR-103X187,admin,admin
Ambit,AB Orion 3000,root,root
Ambit,U10C022,admin,cableroot
Ambit,U10C022,user,user
Ambit,U10C037,user,user
Amped Wireless,R10000,admin,admin
Amped Wireless,RTA15,admin,admin
Amped Wireless,RTA2600,blank,blank
Amped Wireless,TAP-R2,none,none
Ansel,9010,,admin
Aolynk,DR814,admin,admin
Aolynk,DR814Q,admin,admin
Aolynk,DR814Q,admin,admin
Apple,AirPort Extreme,NONE,NONE
Arris,DG860A,admin,password
Arris,DG950,admin,password
Arris,NVG589,unknown,unknown
Arris,NVG595,Admin,printed on router label
Arris,SBG6580,admin,motorola
Arris,SBG6700-AC,admin,password
Arris,SBG6782-AC,admin,motorola
Arris,SBG6900-AC,admin,password
Arris,SBR-AC1750,admin,password
Arris,SBR-AC3200P,admin,motorola
Arris,SBR-AC3200P,admin,password
Arris,TG1682G,admin,password
Arris,TG2472G,admin,password
Arris,TG852,admin,password
Arris,TG852G,admin,password
Arris,TG852G,admin,password
Arris,TG862,admin,password
Arris,TG862G,admin,password
Arris,TG862G,admin,password
Arris,TG862G-CT,admin,password
Arris,TG862G-NA,admin,password
Arris,TM501b,admin,1234
Arris,TM502b,admin,1234
Arris,WTM552,,blank
Arris,WTM552G,,blank
Arris,WTM652,,blank
Arris,WTM652G,none,blank
Articonet,ACN-411RE,admin,admin
Artnet,AR800C2-A04G,admin,epicrouter
Artnet,rta-230,admin,admin
Artnet,TW263R4,admin,admin
Asante,FriendlyNet FR1004,NONE,admin
Asante,FriendlyNet FR1004AL,NONE,admin
Asante,FriendlyNet FR1104-G,NONE,admin
Asante,FriendlyNet FR3002AL,NONE,admin
Asante,FriendlyNet FR3004,NONE,admin
Asante,FriendlyNet FR3004C,NONE,admin
Asante,FriendlyNet FR3004FLC,NONE,admin
Asante,FriendlyNet FR3004LC,NONE,blank
Asmax,AR-904G,unknown,unknown
Asmax,AR-904U,admin,epicrouter
Asmax,AR804u,admin,epicrouter
Asus,4G-AC55U,admin,admin
Asus,4G-N12,admin,admin
Asus,AAM6000EV,admin,admin
Asus,AAM6010EV,admin,admin
Asus,AAM6010EV-T4,Admin,Admin
Asus,AAM6310,root,root
Asus,AM602,admin,admin
Asus,AM604,admin,admin
Asus,AM604G,admin,admin
Asus,DSL-AC68U,admin,admin
Asus,DSL-N10E,admin,admin
Asus,DSL-N11,admin,admin
Asus,DSL-N13,admin,admin
Asus,DSL-N17U,admin,admin
Asus,DSL-N55U,admin,admin
Asus,G-136,admin,epicrouter
Asus,RT-AC1200,admin,admin
Asus,RT-AC1200G,admin,admin
Asus,RT-AC1200HP,admin,admin
Asus,RT-AC1900,admin,admin
Asus,RT-AC1900P,admin,admin
Asus,RT-AC3100,admin,admin
Asus,RT-AC3200,admin,admin
Asus,RT-AC51U,admin,admin
Asus,RT-AC52U,admin,admin
Asus,RT-AC53,admin,admin
Asus,RT-AC5300,admin,admin
Asus,RT-AC55U,admin,admin
Asus,RT-AC56R,admin,admin
Asus,RT-AC56S,admin,admin
Asus,RT-AC56U,admin,admin
Asus,RT-AC66R,admin,admin
Asus,RT-AC66U,admin,admin
Asus,RT-AC68P,admin,admin
Asus,RT-AC68R,admin,admin
Asus,RT-AC68U,admin,admin
Asus,RT-AC68W,admin,admin
Asus,RT-AC87R,admin,admin
Asus,RT-AC87U,admin,admin
Asus,RT-AC88U,admin,admin
Asus,RT-ACRH13,admin,admin
Asus,RT-ARCH13,admin,admin
Asus,RT-G32,unknown,unknown
Asus,RT-N10,admin,admin
Asus,RT-N10E,admin,password
Asus,RT-N10U,admin,admin
Asus,RT-N11,admin,admin
Asus,RT-N12,admin,admin
Asus,RT-N12 D1,admin,admin
Asus,RT-N12B1,admin,admin
Asus,RT-N14UHP,admin,admin
Asus,RT-N15,admin,admin
Asus,RT-N15U,admin,admin
Asus,RT-N16,admin,admin
Asus,RT-N53,admin,admin
Asus,RT-N56U,admin,admin
Asus,RT-N56UB1,admin,admin
Asus,RT-N600,admin,admin
Asus,RT-N65R,admin,admin
Asus,RT-N65U,admin,admin
Asus,RT-N66R,admin,admin
Asus,RT-N66U,admin,admin
Asus,RT-N66U,admin,admin
Asus,RT-N66W,admin,admin
Asus,RX3041,admin,admin
Asus,RX3041-G,admin,admin
Asus,RX3041H,admin,admin
Asus,TM-AC1900,admin,admin
Asus,WL-500G,admin,admin
Asus,WL-500GP,admin,admin
Asus,WL-500W,admin,admin
Asus,WL-520G,admin,admin
Asus,WL-520GC,admin,admin
Asus,WL-520GU,admin,admin
Asus,WL-520GU,Admin,Admin
Asus,WL-530G,admin,admin
Asus,WL-530g,admin,admin
Asus,WL-566GM,admin,admin
Asus,WL-700GE,admin,admin
Asus,WL500g Deluxe,admin,admin
Asus,WL500GP,admin,admin
Asus,WL520GC,admin,admin
Asus,WL520GU,admin,admin
Asus,WL550gE,admin,admin
Asus,WL600g,admin,admin
Asus,WL700gE,admin,admin
Ativa,AWGR54,,blank
Ativa,RTL8139,,blank
Atlantis Land,A01-AE1 GX01,admin,admin
Atlantis Land,WebShare 111,admin,admin
AusLinx,AL-2108P,root,root
Axesstel,AXV-D450,admin,admin
Axesstel,AXW-D800,admin,admin
Axesstel,CDMA 1XEV-DO,admin,admin
Axesstel,D8190AF,admin,admin
Axesstel,MV400,admin,admin
Axesstel,MV410R,admin,admin
Axesstel,MV430i,admin,admin
Axesstel,MV600,admin,1
Aztech,600EW,admin,admin
Aztech,DSL1000EW-L,admin,admin
Aztech,DSL1015EN-L,blank,blank
Aztech,DSL1015EN-L,blank,blank
Aztech,DSL1100R,admin,admin
Aztech,DSL305EU,admin,blank
Aztech,DSL308EW,admin,admin
Aztech,DSL3100R,admin,admin
Aztech,DSL5001EN,user,user
Aztech,DSL5005EN,admin,admin
Aztech,DSL5018EN,user,user
Aztech,DSL5068EN-1T1R,user,user
Aztech,DSL600E,admin,admin
Aztech,DSL600ER,admin,admin
Aztech,DSL600EU,admin,admin
Aztech,DSL600EW,admin,admin
Aztech,DSL605EU,admin,admin
Aztech,DSL605EW,admin,admin
Aztech,DSL7000GR,,Aztechadmin
Aztech,DSL7000GRV,,Aztechadmin
Aztech,DSL7000GRV-S,none,Aztechadmin
Aztech,DSL906EU,admin,admin
Aztech,HW550-3G,admin,admin
Aztech,HW5503G,admin,admin
Aztech,NA83002,admin,password
Aztech,WL230USB,admin,admin
Aztech,WL830RT4,admin,admin
BEC Technologies,5102 ADSL,admin,admin
BEC Technologies,5200W,admin,admin
BEC Technologies,7402GTMR4-SCED,admin,admin
BEC Technologies,BEC 7402GTM-MI,,admin
BEC Technologies,BEC 7402T,,admin
BEC Technologies,BEC 7800TN,admin,admin
BEC Technologies,BEC 7800TN,admin,admin
BT,2700HGV,blank,blank
BT,2700HGV,,password
BT,Home Hub,admin,admin
BT,Home Hub,admin,password
BT,Home Hub 2,admin,password
BT,Home Hub 3,,
BT,Home Hub 4,,
BT,Home Hub 5,,
BT,Home Hub 6,none,printed on router
BT,Hub,admin,admin
BT,Smart Hub,none,printed on router
BT,Voyager 1500,admin,admin
BT,Voyager 200,admin,admin
BT,Voyager 2000,admin,admin
BT,Voyager 205,admin,admin
BT,Voyager 2091,admin,admin
BT,Voyager 210,admin,admin
BT,Voyager 2100,admin,admin
BT,Voyager 2110,admin,admin
BT,Voyager 220V,admin,admin
BT,Voyager 240,,admin
BT,Voyager 2500V,admin,admin
BT,Wireless Network 1250,blank,blank
Bandluxe,R100,admin,hsparouter
Bandluxe,R300,admin,hsparouter
Bandluxe,R529,admin,admin
Bandridge,CWN7004G,none,none
Baudtec,40068194,admin,1234
Baudtec,T263R14,admin,1234
Baudtec,T263R1U,admin,1234
Baudtec,TW263R4-A0,admin,1234
Baudtec,TW263R4-A2,admin,1234
Bausch,Proxima PRI,admin,epicrouter
Baytec,RTA04N,admin,gvt12345
BeWAN,700 ADSL2+,unknown,unknown
BeWAN,ADSL 600G,unknown,unknown
Beam,GW410,unknown,unknown
Beeline,Smart Box,admin,admin
Beetel,110BX1,admin,password
Beetel,110TC1,admin,password
Beetel,110TC2,admin,password
Beetel,220BX,admin,password
Beetel,220BX1,admin,password
Beetel,440TXI,admin,password
Beetel,450BX1,admin,password
Beetel,450TC1,admin,password
Beetel,450TC3,admin,password
Belgacom,B-Box 2,admin,BGCVDSL2
Belgacom,b-box 3,User,password
Belgacom,BBOX 6726,none,admin
Belgacom,CIA6726N BG,unknown,unknown
Belgacom,Fast 3464,unknown,unknown
Belkin,F1P1242EGau,admin,admin
Belkin,F1P1243EGau,,admin
Belkin,F1P1243EGau iiNet,none,blank
Belkin,F1PI241EGau,NONE,admin
Belkin,F1PI241ENau,NONE,admin
Belkin,F1PI242EGau,blank,admin
Belkin,F1PI242ENau,blank,admin
Belkin,F1PI243EGau,admin,admin
Belkin,F1PI24EGau,admin,admin
Belkin,F1Pl242ENau,admin,admin
Belkin,F5D5230-4,Admin,blank
Belkin,F5D5230-4,,blank
Belkin,F5D5231-4,,blank
Belkin,F5D5231-4,NONE,blank
Belkin,F5D5630au4,none,admin
Belkin,F5D5730au,admin,password
Belkin,F5D6230-3,NONE,blank
Belkin,F5D6231-4,NONE,blank
Belkin,F5D6231-4,NONE,blank
Belkin,F5D7010,,blank
Belkin,F5D7130UK,blank,blank
Belkin,F5D7230-4,NONE,blank
Belkin,F5D7230-4,,blank
Belkin,F5D7230-4,,blank
Belkin,F5D7230-4,,blank
Belkin,F5D7231-4,NONE,blank
Belkin,F5D7231-4,NONE,blank
Belkin,F5D7231-4,NONE,blank
Belkin,F5D7231-4,NONE,blank
Belkin,F5D7231-4P,NONE,blank
Belkin,F5D7234-4,none,blank
Belkin,F5D7234-4,blank,blank
Belkin,F5D7234-4,,blank
Belkin,F5D7234-4,,blank
Belkin,F5D7234-4,,blank
Belkin,F5D7630,NONE,blank
Belkin,F5D7630-4,NONE,blank
Belkin,F5D7632-4,blank,blank
Belkin,F5D7632-4,none,admin
Belkin,F5D7632-4,,blank
Belkin,F5D7632ef4a,NONE,blank
Belkin,F5D7633-4,blank,blank
Belkin,F5D7633-4,,blank
Belkin,F5D7633-4A,blank,blank
Belkin,F5D7633au4A,,blank
Belkin,F5D7634-4,none,blank
Belkin,F5D8230-4,blank,blank
Belkin,F5D8231-4,blank,blank
Belkin,F5D8231-4,,blank
Belkin,F5D8231-4,,blank
Belkin,F5D8232-4,,blank
Belkin,F5D8232-4,,blank
Belkin,F5D8233-4,blank,blank
Belkin,F5D8233-4,blank,blank
Belkin,F5D8233-4,blank,blank
Belkin,F5D8235-4,,blank
Belkin,F5D8235-4,,blank
Belkin,F5D8235-4,,blank
Belkin,F5D8235-4,,blank
Belkin,F5D8236-4,blank,blank
Belkin,F5D8236-4,,blank
Belkin,F5D8236-4,blank,blank
Belkin,F5D8630-4,,blank
Belkin,F5D8630-4A,,blank
Belkin,F5D8631-4,,blank
Belkin,F5D8631-4,,blank
Belkin,F5D8632-4,,blank
Belkin,F5D8632-4,,blank
Belkin,F5D8633-4,blank,blank
Belkin,F5D8633-4,blank,blank
Belkin,F5D8635-4,,blank
Belkin,F5D8635au4A,none,blank
Belkin,F5D8636-4,none,none
Belkin,F5D8636-4,none,none
Belkin,F5D8636uk4A,none,none
Belkin,F5D9230-4,admin,admin
Belkin,F5D9230-4,,blank
Belkin,F5D9230-4,,blank
Belkin,F5D9230-4,,blank
Belkin,F5D9231-4,blank,blank
Belkin,F5D9231-4,blank,blank
Belkin,F5D9231-4,blank,blank
Belkin,F5D9630-4,,blank
Belkin,F5D9630-4,blank,blank
Belkin,F5D9630-4,blank,blank
Belkin,F5D9630-4A,,blank
Belkin,F6D3230-4,,blank
Belkin,F6D4230-4,none,blank
Belkin,F6D4230-4,,blank
Belkin,F6D4230-4,,blank
Belkin,F6D4230-4,none,blank
Belkin,F6D4260-4,,blank
Belkin,F7D1301,none,blank
Belkin,F7D1401,,blank
Belkin,F7D2301,,blank
Belkin,F7D2401,,blank
Belkin,F7D3301,,blank
Belkin,F7D3302,,blank
Belkin,F7D3402,,blank
Belkin,F7D4301,,blank
Belkin,F7D4302,,blank
Belkin,F7D4401,,blank
Belkin,F7D4402,,
Belkin,F7D5301,blank,blank
Belkin,F7D6301,none,blank
Belkin,F7D7301,,blank
Belkin,F7D8301,,blank
Belkin,F7D8302,,blank
Belkin,F9J1002,,blank
Belkin,F9J1004,admin,admin
Belkin,F9J1102,,blank
Belkin,F9J1107,,blank
Belkin,F9K1001,,blank
Belkin,F9K1001,,blank
Belkin,F9K1002,,blank
Belkin,F9K1002,,blank
Belkin,F9K1002,,blank
Belkin,F9K1002,none,blank
Belkin,F9K1003,,blank
Belkin,F9K1009v2,NONE,NONE
Belkin,F9K1102,,blank
Belkin,F9K1102,,blank
Belkin,F9K1102,none,none
Belkin,F9K1102 v4,NO LOGIN ,NO LOGIN
Belkin,F9K1103,none,blank
Belkin,F9K1105,,blank
Belkin,F9K1110,none,blank
Belkin,F9K1112,none,blank
Belkin,F9K1113,admin,admin
Belkin,F9K1116,admin,admin
Belkin,F9K1117,admin,admin
Belkin,FD730-4,blank,blank
Belkin,FSD7230-4,,blank
Belkin,ME1004-R,blank,blank
Belkin,MyEssentials ME1004-R,blank,blank
Belkin,WRTR-159G,none,blank
Belkin,WRTR-159G,none,blank
Bell,CellPipe 7130,admin,admin
Bell,Connection Hub,admin,admin
Bell,Home Hub 1000,unknown,admin
Bell,Speedstream 6300,admin,admin
Bell,Speedstream 6520,admin,admin
Benq,AWL 700,admin,admin
Benq,BW 3700,,unknown
Benq,ESG 103,admin,admin
Best Data,DSL800EU,admin,blank
Billion,400G,admin,admin
Billion,5102G,admim,password
Billion,5200G,admim,admin
Billion,5200S,admin,admin
Billion,5210S,admim,password
Billion,7204W,admin,admin
Billion,800VGT,admin,admin
Billion,810VGTX,admin,admin
Billion,Biguard 2,admin,admin
Billion,Biguard 30,admin,admin
Billion,Bipac 5100,admin,admin
Billion,Bipac 5100S,admin,admin
Billion,Bipac 5100W,admin,admin
Billion,Bipac 5102,admin,admin
Billion,Bipac 5102,admim,admin
Billion,Bipac 51025,admin,admin
Billion,Bipac 5102G,admim,admin
Billion,Bipac 5102s,,admin
Billion,Bipac 5102S,admim,admin
Billion,Bipac 5102S,admin,admin
Billion,Bipac 5112S,admin,password
Billion,Bipac 5112S,admin,admin
Billion,Bipac 5200,admim,admin
Billion,Bipac 5210S,admim,password
Billion,Bipac 6404VGP,admin,admin
Billion,Bipac 640AE,blank,blank
Billion,Bipac 640SE,blank,blank
Billion,Bipac 643,blank,blank
Billion,Bipac 7025,blank,blank
Billion,Bipac 7100S,admin,admin
Billion,Bipac 711CE,admin,password
Billion,Bipac 7202A,admin,admin
Billion,Bipac 7202GR2A,admin,admin
Billion,Bipac 7300A,admin,admin
Billion,Bipac 7300G RA,admin,admin
Billion,Bipac 7300GA,admin,admin
Billion,Bipac 7300GX,admin,admin
Billion,Bipac 7300RA,admin,admin
Billion,Bipac 7300W,admin,admin
Billion,Bipac 740,blank,blank
Billion,Bipac 7401VGP,admin,admin
Billion,Bipac 7401VGPR3,admin,admin
Billion,Bipac 7401VP,admin,admin
Billion,Bipac 7402g,admin,admin
Billion,Bipac 7402GL,admin,admin
Billion,Bipac 7402NX,admin,admin
Billion,Bipac 7402VGO,,admin
Billion,Bipac 7404VGO,admin,admin
Billion,Bipac 7404VGOX,admin,admin
Billion,Bipac 7404VGP,admin,admin
Billion,Bipac 7404VNOX,admin,admin
Billion,Bipac 7404VNPX,admin,admin
Billion,Bipac 7404VPNX,admin,admin
Billion,Bipac 741,blank,blank
Billion,Bipac 743,admin,admin
Billion,Bipac 7500g,,admin
Billion,Bipac 7560,admin,admin
Billion,Bipac 7700N R2,admin,admin
Billion,Bipac 7800N,admin,admin
Billion,Bipac 7800NL,admin,admin
Billion,myGuard 7202GA,admin,admin
Binatone,ADSL 2000,Admin,blank
Binatone,ADSL 2001,Admin,blank
Binatone,DT 850W,admin,password
BlackBox,BB54G,Admin,Admin
Blanc,BW-54R11,blank,blank
Blitzz,BWA 611,blank,blank
Blitzz,BWA 611B,admin,blank
Blitzz,BWA 711,admin,admin
Blitzz,BWA 721,admin,admin
Blue Thunder,9307-1,Admin,Admin
Bountiful WiFi,BWRG1000,admin,admin
Broadnext,BritePort 8120,admin,admin
Bticino,F444,admin,bticinoadsl
Buffalo,BBR4MG,root,blank
Buffalo,DD-WRT,admin,password
Buffalo,WBMR-125G,root,blank
Buffalo,WBMR-G54,admin,admin
Buffalo,WBMR-HP-G300H,root,blank
Buffalo,WBMR-HP-GN,root,none
Buffalo,WBMR-HP-GNV2,admin,admin
Buffalo,WBR-G54,root,blank
Buffalo,WBR-G54,admin,admin
Buffalo,WCR-GN,root,blank
Buffalo,WHR-G125,root,blank
Buffalo,WHR-G300N,root,blank
Buffalo,WHR-G54S,root,blank
Buffalo,WHR-HP-G54,root,blank
Buffalo,WHR-HP-G54,admin,admin
Buffalo,WLAR-L11-L,root,blank
Buffalo,WYR-G54,root,blank
Buffalo,WZR-1750DHP,admin,password
Buffalo,WZR-600DHP DD-WRT,admin,password
Buffalo,WZR-D1800H,admin,password
Buffalo,WZR-G300N,root,blank
Buffalo,WZR-HP-AG300H DD-WRT,admin,password
Buffalo,WZR-HP-G300NH,root,blank
Buffalo,WZR2-G300N,root,blank
CBN,CH7486E,admin,password
CD-R King,3G Router,admin,admin
CD-R King,3G-52,admin,admin
CD-R King,CW-5356U,admin,admin
CD-R King,IP04177,admin,admin
CD-R King,WR-NET-018-CC,admin,admin
CNET,CAR-854,admin,admin
CNET,CAR2-804,admin,admin
CNET,CBR-980,admin,admin
CNET,CNAD804-NF,admin,epicrouter
CNET,CNAD804-NF,admin,epicrouter
CNET,CNAD810-NF,admin,admin
CNET,CNBR-914W,Admin,Admin
CNET,CNIG-914,admin,admin
CNET,CWR-854,admin,1234
CNET,CWR-903,root,1234
CT Systems,VRG-21412-WF-G-RF Triple Play Gateway,admin,blank
CTC Union,ATU-R130,root,root
Cabac,LWADSLR4P,admin,admin
Cable N Wireless,ADSLR10CW3,admin,1234
Cable N Wireless,HSADSLR15CW3,,admin
Calix,813G-2,admin,blank
Cambridge Industries Group,GPON G-93RG1,unknown,unknown
Cameo,WLG-2206,admin,admin
Canyon,CN-AMR,admin,epicrouter
Canyon,CN-BR1,,admin
Canyon,CN-WF505,admin,1234
Canyon,CN-WF506,admin,1234
Canyon,CN-WF514,admin,1234
Canyon,CN-WF514M,admin,1234
Canyon,CNR-BR2,admin,1234
Caremo,x8268r,admin,admin
CastleNet,AS800,,Unknown
CastleNet,CBW511,NONE,cable
Cayman,3200,admin,admin
Cerberus Adsl,PC-0404000457,admin,password
Cisco,870 Series,admin,admin
Cisco,CVR100W,cisco,cisco
Cisco,DPC2320,blank,blank
Cisco,DPC2325,admin,password
Cisco,DPC3825,cusadmin,password
Cisco,DPC3828D,blank,blank
Cisco,DPC3848,blank,blank
Cisco,DPC3914B,cusadmin,highspeed
Cisco,DPC3925,blank,blank
Cisco,DPC3939 XFINITY,admin,password
Cisco,DPC3941B,cusadmin,highspeed
Cisco,DPC3941T XFINITY,admin,password
Cisco,DPQ3925,admin,admin
Cisco,ECP3940ADL,unknown,unknown
Cisco,EPC2425,blank,blank
Cisco,EPC3825,none, none
Cisco,EPC3828D,unknown,unknown
Cisco,EPC3925,none,none
Cisco,EPC3928AD,none,none
Cisco,EPC3940AD,blank,blank
Cisco,M10,admin,admin
Cisco,M20,admin,blank
Cisco,RV120W,admin,admin
Cisco,RV180,admin,admin
Cisco,RVS4000,admin,admin
Cisco,WRVS4400N,admin,admin
Cisco,X3000,admin,blank
Cisco Linksys,E1000,admin,admin
Cisco Linksys,E1200,admin,admin
Cisco Linksys,E1500,admin,admin
Cisco Linksys,E1550,admin,admin
Cisco Linksys,E2000,admin,admin
Cisco Linksys,E2100L,admin,admin
Cisco Linksys,E2500,admin,admin
Cisco Linksys,E3000,admin,admin
Cisco Linksys,E3200,admin,admin
Cisco Linksys,E4200,admin,admin
Cisco Linksys,E900,admin,blank
Cisco Linksys,EA2700,admin,blank
Cisco Linksys,EA3500,admin,blank
Cisco Linksys,EA4500,admin,admin
Cisco Linksys,X2000,admin,blank
Cisco Linksys,X3000,admin,blank
Comcast,CG814WG,,1234
Comcast,WCG200-CC,comcast,1234
CompUSA,BR-6104KL,blank,blank
CompUSA,Generic,,admin
CompUSA,Soho,admin,blank
Compaq,iPaq Connection Point CP-2W,admin,blank
Compex,NetPassage 16A,unknown,unknown
Comstar,WA-6202,none,none
Comtrend,AR-5302,admin,admin
Comtrend,AR-5381u,,admin
Comtrend,CT-5071,,admin
Comtrend,CT-535,1234,1234
Comtrend,CT-536,,admin
Comtrend,CT-5361,,admin
Comtrend,CT-5367,,admin
Comtrend,CT-5372,,admin
Comtrend,CT-560,admin,admin
Comtrend,CT-561,root,12345
Comtrend,CT-562,root,12345
Comtrend,CT-562+,root,12345
Comtrend,CT-5621,,admin
Comtrend,CT-600,root,root
Comtrend,NexusLink 5631,,admin
Comtrend,VR-2035UN,,admin
Comtrend,WAP5813n,,admin
Conceptronic,C100BRS4H,admin,1234
Conceptronic,C100BRS4H,NONE,blank
Conceptronic,C300BRS4,admin,admin
Conceptronic,C54APRA,admin,admin
Conceptronic,C54APRA2,admin,admin
Conceptronic,C54BRS4,admin,1234
Conceptronic,C54BRS4A,admin,1234
Conexant,2-2-8-1,,conexant
Conexant,4.1.0.21-f,user,password
Conexant,4.1.0.21-S,user,password
Conexant,4.1.0.34,,conexant
Conexant,n791,,conexant
Conexant,PT-3830,admin,epicrouter
Conexant,Vulcan 810100,root,root
Corecess,3115,admin,corecess
Coredy,RT1200,admin,admin
Corega,BarSD,root,blank
Corega,CG-WLBARGO,root,blank
Cosy,C6104K,,1234
Cradlepoint,CTR350,none,last 6 digits of MAC address found on bottom of device
Cradlepoint,CTR350,none,last 6 digits of MAC address found on bottom of device
Cradlepoint,CTR500,none,last 6 digits of MAC address found on bottom of device
Cradlepoint,MBR1000,none,found on the bottom of the router.
Cradlepoint,MBR1200,none,last 6 digits of MAC address found on bottom of device
Cradlepoint,MBR900,none,found on the bottom of the router.
Creative,Blaster 8015U,admin,admin
Creative,Briteport 2103,,UNKNOWN
Creative,Network Blaster CW2202,admin,admin
Creative,Network Blaster CW2202-5,admin,admin
Crypto,F300,admin,conexant
Crypto,F320,admin,conexant
Crypto,F330,,conexant
Crypto,F360,admin,admin
Crypto,WF200,admin,admin
Cyberoam,NetGenie,admin,admin
D-Link,AirPlus DI-524,admin,blank
D-Link,AirPlus DI-524,admin,blank
D-Link,AirPlus DI-524,admin,blank
D-Link,AirPlus DI-524,admin,blank
D-Link,AirPlus DI-524UP,admin,blank
D-Link,AirPlus DI-614+,admin,blank
D-Link,AirPlus DI-614+,admin,blank
D-Link,AirPlus DI-624,admin,blank
D-Link,AirPlus DI-624,admin,blank
D-Link,AirPlus DI-624,admin,blank
D-Link,AirPlus DI-624,admin,blank
D-Link,AirPlus DI-624+,admin,blank
D-Link,AirPlus DI-624S,admin,blank
D-Link,AirPlus DI-724P+,admin,blank
D-Link,AirPlus DI-824VUP,admin,admin
D-Link,AirPremier DI-784,admin,blank
D-Link,AirPro DI-754,admin,blank
D-Link,Airspot DSA-3100,admin,admin
D-Link,Airspot DSA-3200,admin,admin
D-Link,Airspot DSA-5100,admin,admin
D-Link,Amplifi DIR-645,admin,blank
D-Link,Amplifi DIR-657,admin,blank
D-Link,DAP-1350,admin,blank
D-Link,DCM-604,admin,password
D-Link,DFL-1100 Firewall,admin,admin
D-Link,DFL-200 Firewall,admin,admin
D-Link,DFL-700 Firewall,admin,admin
D-Link,DFL-80 Firewall,admin,admin
D-Link,DHP-1565,Admin,blank
D-Link,DI-514,admin,blank(no password)
D-Link,DI-514,admin,blank(no password)
D-Link,DI-604,admin,blank
D-Link,DI-604,admin,blank
D-Link,DI-604,admin,blank
D-Link,DI-604,admin,blank
D-Link,DI-624M,admin,blank
D-Link,DI-634M,admin,leave blank
D-Link,DI-634M,admin,blank
D-Link,DI-704,NONE,admin
D-Link,DI-704P,admin,blank
D-Link,DI-704P,admin,blank
D-Link,DI-704P,NONE,admin
D-Link,DI-704p,admin,blank
D-Link,DI-704P,admin,blank
D-Link,DI-704P,admin,blank
D-Link,DI-704P,admin,blank
D-Link,DI-704UP,admin,blank
D-Link,DI-707,NONE,admin
D-Link,DI-707P,admin,blank
D-Link,DI-711,admin,blank
D-Link,DI-713,NONE,admin
D-Link,DI-713P,NONE,admin
D-Link,DI-714,admin,none
D-Link,DI-714+,admin,blank
D-Link,DI-714P+,admin,blank
D-Link,di-714P+,,blank
D-Link,DI-724,admin,blank
D-Link,DI-724GU,admin,blank
D-Link,DI-724U,admin,blank
D-Link,DI-764,admin,blank
D-Link,DI-774,admin,blank
D-Link,DI-804,admin,none
D-Link,DI-804HV,admin,blank
D-Link,DI-804HV,admin,blank
D-Link,DI-804V,admin,blank
D-Link,DI-808HV,admin,blank
D-Link,DI-904,,blank
D-Link,DI-LB604,admin,blank
D-Link,DIR-100,admin,blank
D-Link,DIR-100,create in initial setup,create in initial setup
D-Link,DIR-120,admin,blank
D-Link,DIR-130,admin,blank
D-Link,DIR-300,admin,blank
D-Link,DIR-301,admin,blank
D-Link,DIR-320,admin,blank
D-Link,DIR-330,admin,blank
D-Link,DIR-400,admin,blank
D-Link,DIR-412,admin,blank
D-Link,DIR-450,admin,
D-Link,DIR-451,admin,
D-Link,DIR-515,admin,blank
D-Link,DIR-600,admin,blank
D-Link,DIR-600L,admin,blank
D-Link,DIR-600M,admin,blank
D-Link,DIR-601,admin,blank
D-Link,DIR-605L,admin,admin
D-Link,DIR-615,admin,blank
D-Link,DIR-615,admin,blank
D-Link,DIR-615,admin,blank
D-Link,DIR-615,admin,blank
D-Link,DIR-615,Admin,blank
D-Link,DIR-620 Etisalat,admin,admin
D-Link,DIR-625,admin,blank
D-Link,DIR-625,admin,blank
D-Link,DIR-632,admin,blank
D-Link,DIR-635,admin,blank
D-Link,DIR-636L,Admin,leave blank
D-Link,DIR-655,admin,blank
D-Link,DIR-655,Admin,
D-Link,DIR-660,admin,blank
D-Link,DIR-685,admin,blank
D-Link,DIR-803,admin,admin
D-Link,DIR-810L,admin,blank
D-Link,DIR-815,Admin,none
D-Link,DIR-817LW,Admin,blank
D-Link,DIR-818LW,,
D-Link,DIR-826L,admin,blank
D-Link,DIR-835,Admin,blank
D-Link,DIR-850,unknown,unknown
D-Link,DIR-850L,none,blank
D-Link,DIR-855,admin,blank
D-Link,DIR-860L,Admin,blank
D-Link,DIR-862L,Admin,blank
D-Link,DIR-866L,admin,blank
D-Link,DIR-868L,admin,blank
D-Link,DIR-868L,admin,leave blank
D-Link,DIR-880L,admin,blank
D-Link,DIR-890L,admin,blank
D-Link,DIR-895L,none,blank
D-Link,DMG-6661,admin,blank
D-Link,DPN-5402,admin,admin
D-Link,DSL DSL-2730R,admin,password
D-Link,DSL-225,admin,admin
D-Link,DSL-2500E,admin,blank
D-Link,DSL-2500U,admin,admin
D-Link,DSL-2500U,admin,admin
D-Link,DSL-2520U,admin,blank
D-Link,DSL-2524B,admin,admin
D-Link,DSL-2540T,admin,admin
D-Link,DSL-2540U,admin,admin
D-Link,DSL-2542B,admin,admin
D-Link,DSL-254OU,admin,admin
D-Link,DSL-2600U,admin,admin
D-Link,DSL-2640B,admin,admin
D-Link,DSL-2640B,admin,admin
D-Link,DSL-2640B,admin,admin
D-Link,DSL-2640B,admin,admin
D-Link,DSL-2640R,admin,admin
D-Link,DSL-2640S,admin,sky
D-Link,DSL-2640T,admin,admin
D-Link,DSL-2640U,admin,admin
D-Link,DSL-2642B,admin,admin
D-Link,DSL-2680,admin,admin
D-Link,DSL-2730B,admin,admin
D-Link,DSL-2730U,admin,admin
D-Link,DSL-2740B,admin,admin
D-Link,DSL-2740B,admin,admin
D-Link,DSL-2740B-F1,admin,admin
D-Link,DSL-2740R,admin,admin
D-Link,DSL-2740U,admin,admin
D-Link,DSL-2750B,admin,admin
D-Link,DSL-2750U,admin,admin
D-Link,DSL-2750U,admin,admin
D-Link,DSL-2760U,admin,admin
D-Link,DSL-2760U-BN,admin,admin
D-Link,DSL-2780,admin,admin
D-Link,DSL-2870B,admin,admin
D-Link,DSL-2877AL,admin,admin
D-Link,DSL-2888A,none,admin
D-Link,DSL-2890AL,Admin,blank
D-Link,DSL-302,admin,admin
D-Link,DSL-302G,admin,admin
D-Link,DSL-302G,admin,admin
D-Link,DSL-320G,admin,admin
D-Link,DSL-3680,admin,admin
D-Link,DSL-3780,admin,admin
D-Link,DSL-500,admin,admin
D-Link,DSL-500B,admin,admin
D-Link,DSL-500G,admin,admin
D-Link,DSL-500Gv4,admin,admin
D-Link,DSL-500T,admin,admin
D-Link,DSL-500T,admin,admin
D-Link,DSL-502G,admin,admin
D-Link,DSL-502T,admin,admin
D-Link,DSL-502T,,admin
D-Link,DSL-504,admin,admin
D-Link,DSL-504,admin,admin
D-Link,DSL-504G,admin,admin
D-Link,DSL-504G,admin,admin
D-Link,DSL-504G,admin,admin
D-Link,DSL-504T,admin,admin
D-Link,DSL-504T,admin,admin
D-Link,DSL-504T,admin,admin
D-Link,DSL-520B,admin,admin
D-Link,DSL-520T,admin,admin
D-Link,DSL-524T,admin,admin
D-Link,DSL-526B,admin,admin
D-Link,DSL-584T,admin,admin
D-Link,DSL-604+,admin,admin
D-Link,DSL-604+,admin,blank
D-Link,DSL-6740U,admin,admin
D-Link,DSL-G604T,admin,admin
D-Link,DSL-G604T,admin,admin
D-Link,DSL-G604T,admin,admin
D-Link,DSL-G624M,admin,admin
D-Link,DSL-G624T,admin,admin
D-Link,DSL-G624T,admin,admin
D-Link,DSL-G684T,admin,admin
D-Link,DSL-G804V,admin,admin
D-Link,DVA-G3170i,admin,admin
D-Link,DVA-G3340S,admin,admin
D-Link,DVA-G3810BN-TL,admin,telus
D-Link,DVG-1102M,admin,password
D-Link,DVG-1120M,none,none
D-Link,DVG-1120M,root,none
D-Link,DVG-1402S,admin,admin
D-Link,DVG-5102S,none,admin
D-Link,DVG-G1402S,admin,admin
D-Link,DVG-N5402SP,admin,password
D-Link,DWL-1700AP,admin,blank
D-Link,DWL-1750,admin,blank
D-Link,DWL-3150,admin,blank
D-Link,DWL-G730AP,admin,blank
D-Link,DWR-113,admin,blank
D-Link,DWR-116,admin,blank
D-Link,DWR-512,admin,blank
D-Link,DWR-921,admin,blank
D-Link,EBR-2310,admin,blank
D-Link,EBR-2310,admin,admin
D-Link,GamerLounge DGL-3420,NONE,blank
D-Link,GamerLounge DGL-4100,NONE,blank
D-Link,GamerLounge DGL-4300,admin,admin
D-Link,GamerLounge DGL-4500,admin,admin
D-Link,GamerLounge DGL-5500,none,blank
D-Link,GLB-502C,admin,admin
D-Link,GLB-502T,admin,admin
D-Link,GLB-802C,admin,admin
D-Link,GO-RT-N150,admin,blank
D-Link,RangeBooster DIR-628,admin,blank
D-Link,SharePort DIR-506L,admin,blank
D-Link,TM-G5240,admin,admin
D-Link,VWR,user,user
D-Link,VWR-VR,user,user
D-Link,WBR-1310,admin,admin
D-Link,WBR-1310,admin,admin
D-Link,WBR-2310,admin,blank
D-Link,WBR-2310,admin,blank
D-Link,Xtreme DIR-825,admin,blank
D-Link,Xtreme DIR-825,admin,blank
D-Link,Xtreme DIR-825,admin,blank
DABS,Value,admin,epicrouter
DSLink,200e,root,root
DSLink,220u-e,root,root
DSLink,260E,root,root
DSLink,485,unknown,unknown
Dana,NW514OSR,blank,blank
Dasan,H640DW Viettel,user,user
Davolink,DV-201 AMR,user,user
Davolink,DV-2020,user,user
Dell,TrueMobile 1184,admin,admin
Dell,TrueMobile 1184,admin,admin
Dell,TrueMobile 2300,admin,admin
Dell,TrueMobile 2350,admin,admin
Dick Smith Elec,DSE XH 1149,admin,password
Dick Smith Elec,DSE XH 1149,admin,password
Dick Smith Elec,DSE XH 1169,admin,password
Dick Smith Elec,DSE XH 1169,admin,password
Dick Smith Elec,DSE XH 1173,admin,password
Dick Smith Elec,DSE XH 1175,admin,password
Dick Smith Elec,DSE XH 7916,admin,password
Dick Smith Elec,DSE XH 7916,admin,password
Dick Smith Elec,DSE XH 9950,admin,password
Digicom,DG-5314T,admin,admin
Digicom,Michelangelo Home 54,admin,password
Digicom,Michelangelo LAN CX,root,root
Digicom,Michelangelo WAVE,admin,admin
Digicom,Michelangelo Wave,admin,admin
Digicom,Michelangelo Wave,admin,admin
Digicom,Wavegate 150R 3g,admin,1234
Digiconnect,WIC328,admin,1234
Digisol,DG-BG4011N,admin,admin
Digisol,DG-BG4300N,admin,1234
Digisol,DG-BR4000N,admin,1234
Digisol,DG-BR4015N,unknown,unknown
Digitus,DN-11004,Admin,Admin
Digitus,DN-11004-N,Admin,Admin
Digitus,DN-11004-O,admin,admin
Digitus,DN7039-A,admin,admin
Digitus,HP-400S,none,admin
DirecWay,DW600E,admin,admin
Dovado,3GN,admin,password
Dovado,UMR mobile Broadband,admin,password
Draytek,Vigor 2130,admin,admin
Draytek,Vigor 2130n,admin,admin
Draytek,Vigor 2132F,admin,admin
Draytek,Vigor 2132FVn,admin,admin
Draytek,Vigor 2200E,blank,blank
Draytek,Vigor 2500,blank,blank
Draytek,Vigor 2500V,admin,blank
Draytek,Vigor 2600WE,blank,blank
Draytek,Vigor 2700V,admin,admin
Draytek,Vigor 2800G,admin,admin
Draytek,Vigor 2900V,blank,blank
Draytek,Vigor 2910,admin,admin
Draytek,Vigor 2930,blank,blank
Draytek,Vigor 2930n,admin,admin
Draytek,VigorPro 5300,blank,blank
Dynalink,RTA 100+,admin,admin
Dynalink,RTA1025W,,admin
Dynalink,RTA1046VW,admin,admin
Dynalink,RTA1320,,admin
Dynalink,RTA1335,admin,admin
Dynalink,RTA220,admin,admin
Dynalink,RTA230,admin,admin
Dynalink,RTA300,admin,admin
Dynalink,RTA770,admin,admin
Dynamode,BR6004,,1234
Dynamode,BR6004W-G1,guest,guest
Dynamode,BR6004W-G2M,admin,admin
Dynamode,R-ADSL-C4,admin,conexant
Dynamode,R-ADSL-C4-2,,root
Dynamode,R-ADSL-C4-2,admin,password
Dynamode,R-ADSL-C4S,,conexant
Dynamode,R-ADSL-C4W-G1,admin,password
Dynamode,RADSL-C4W-G,,Admin
Dynex,DX-E401,admin,blank
Dynex,DX-E402,admin,admin
Dynex,DX-NRUTER,none,blank
Dynex,DX-WEGRTR,blank,blank
Dynex,DX-WGRTR,none,blank
Dynex,WRTB-239GN,none,blank
E Tec,PTI-845G,,Admin
E-Tech,ADRT02,admin,epicrouter
E-Tech,ADRT03,unknown,unknown
E-Tech,ADWG03,,Admin
E-Tech,ATBR03,admin,admin
E-Tech,RTBR03,blank,admin
E-Tech,RTBR05,blank,blank
E-Tech,RTVP03,,admin
E-Tech,WGRT04,admin,admin
E-Tech,WLRT03,blank,admin
ECI,B-Focus 270 PR,admin,admin
ECI,B-Focus 312 TR,admin,password
EE,Bright Box,admin,sticker on bottom of router
EE,Bright Box 2,printed on bottom of router,printed on bottom of router
Easy Touch,ET-1220,unknown,unknown
Ecom,ED-802EC,admin,epicrouter
Econ,MC8000UE-S4,admin,epicrouter
Edimax,AR-6024 WGA,Admin,blank
Edimax,AR-6024A,admin,conexant
Edimax,AR-7000,root,root
Edimax,AR-7024,admin,epicrouter
Edimax,AR-7024WG,admin,epicrouter
Edimax,AR-7024WG,admin,epicrouter
Edimax,AR-7064G+A,admin,admin
Edimax,AR-7064MG+,,admin
Edimax,AR-7084A,admin,admin
Edimax,AR-7084gA,admin,admin
Edimax,AR-7084gB,admin,admin
Edimax,AR-7265WnA,admin,admin
Edimax,AR-7266WnA,admin,1234
Edimax,BR-6004 Plus,NONE,password
Edimax,BR-6104 WG,,1234
Edimax,BR-6104K,admin,1234
Edimax,BR-6104K,admin,1234
Edimax,BR-6104P,blank,blank
Edimax,BR-6104W,blank,blank
Edimax,BR-6104WB,admin,1234
Edimax,BR-6204WG,,1234
Edimax,BR-6204WLg,admin,1234
Edimax,BR-6208AC,admin,1234
Edimax,BR-6214K,admin,1234
Edimax,BR-6215SRG,admin,1234
Edimax,BR-6216Mg,admin,1234
Edimax,BR-6304K,admin,1234
Edimax,BR-6478AC,admin,1234
Edimax,BR-6504N,admin,1234
Edimax,BR-6624,admin,blank
Edimax,BR6228nC,admin,1234
Edimax,BR6228nS,admin,1234
Edimax,BR6428n,admin,1234
Edimax,ER-1088,admin,blank
Edimax,EW-7209APG,blank,blank
Edimax,Wi-Fi ADSL2+,admin,epicrouter
Efficient Siemens,Speedstream 2510,blank,SpeedStream
Efficient Siemens,Speedstream 2524,blank,SpeedStream
Efficient Siemens,Speedstream 2602,none,admin
Efficient Siemens,Speedstream 2604,blank,SpeedStream
Efficient Siemens,Speedstream 2614,blank,admin
Efficient Siemens,Speedstream 2623,blank,admin
Efficient Siemens,Speedstream 2624,blank,SpeedStream
Efficient Siemens,Speedstream 5100,NOLOGIN,NOLOGIN
Efficient Siemens,Speedstream 5100,admin,admin
Efficient Siemens,Speedstream 5200,admin,admin
Efficient Siemens,Speedstream 5400,NOLOGIN,NOLOGIN
Efficient Siemens,Speedstream 5500,NOLOGIN,NOLOGIN
Efficient Siemens,Speedstream 6300,admin,admin
Eicon Networks,Diva 2440,blank,blank
Elcon,ADSL 2253EU,blank,blank
Eltex,NTP-RG-1402G-W,user,user
Eminent,EM2012,,blank
Eminent,EM4012,,blank
Eminent,EM4013,guest,guest
Eminent,EM4100,admin,admin
Eminent,EM4202,admin,epicrouter
Eminent,EM4206,Admin,Admin
Eminent,EM4207,Admin,Admin
Eminent,EM4218,admin,admin
Eminent,EM4412,admin,admin
Eminent,EM4420,admin,admin
Eminent,EM4422,blank,admin
Eminent,EM4450,admin,admin
Eminent,EM4544,admin,admin
Eminent,EM4551,admin,admin
EnGenius,ESR 1220,admin,password
EnGenius,ESR 9750G,admin,admin
EnGenius,ESR 9752,admin,admin
EnGenius,ESR 9753,admin,admin
EnGenius,ESR600H,admin,admin
EnGenius,ESR900,admin,admin
EnGenius,ESR9350,admin,admin
EnGenius,ESR9850,admin,admin
Encore,ENDSL-AR4,,conexant
Encore,ENHWI-2AN3,admin,admin
Encore,ENHWI-G,,admin
Encore,ENHWI-G2,admin,admin
Encore,ENHWI-G3,admin,admin
Encore,ENHWI-N,Administrator,admin
Encore,ENHWI-N2,admin,admin
Encore,ENHWI-N3,admin,admin
Encore,ENRTR-104,,blank
Encore,SOHO,admin,1234
Encore,WTC215,unknown,unknown
Energy Imports,VB204W,admin,admin
Ericsson,HM210DI,root,root
Ericsson,HM210DP,root,root
Ericsson,hn290dp,admin,admin
Ericsson,W20e,user,user
Ericsson,W35,,admin
Etec,PT-645,UNKNOWN,UNKNOWN
Etec,PT-811G,admin,admin
Etec,PT-8411G,admin,admin
Etec,PT-8505G,Admin,Admin
Etec,PT3808,admin,epicrouter
Etec,PT3810,admin,epicrouter
Etec,PT3812,admin,epicrouter
Etec,PT3812,admin,epicrouter
Etec,PT3816,admin,epicrouter
Etec,PT3818,admin,epicrouter
Etec,PT3830,admin,epicrouter
Etec,PTI-815,Admin,Admin
Etec,PTI-845G,admin,admin
Eusso,UGL2454 RTK,user,123456
Eusso,UIS1400-C7,admin,admin
Eusso,UIS1400-C8,admin,admin
Everest,EWR-301,admin,admin
FPT,FP804W,admin,admin
FRITZ BOX,Fon 5010,admin,admin
FRITZ BOX,Fon 5050,UNKNOWN,UNKNOWN
FRITZ BOX,Fon 5140,admin,admin
FRITZ BOX,Fon Annex A,UNKNOWN,UNKNOWN
FRITZ BOX,Fon Annex A,admin,admin
FRITZ BOX,Fon Annex A,admin,admin
FRITZ BOX,Fon WLAN 7570,admin,fritzfonbox
FRITZ BOX,SL,UNKNOWN,UNKNOWN
FRITZ BOX,SL WLAN,admin,admin
FRITZ BOX,SL WLAN 3030,admin,admin
FRITZ BOX,WLAN 3030,none,unknown
FRITZ BOX,WLAN 3050,admin,admin
FRITZ BOX,WLAN 7050,none,unknown
FRITZ BOX,WLAN 7113,admin,admin
FRITZ BOX,WLAN 7141,admin,admin
FRITZ BOX,WLAN 7170,admin,admin
FRITZ BOX,WLAN 7170-EN,none,unknown
FRITZ BOX,WLAN 7330,none,unknown
FRITZ BOX,WLAN 7340,none,none
FRITZ BOX,WLAN 7390,unknown,unknown
FRITZ BOX,WLAN 7490,none,unknown
Fiber Home,AN1020-25,admin,admin
Fiber Home,AN5506 04 F2,admin,admin
Fiberline,IR 3440,admin,admin
Flextronics,DNA A211 I,admin,admin
Franklin Wireless,R720,admin,admin
FreeWiFiLink,NHP-628,admin,admin
Frys,FR-300RTR,Admin,
Fujitsu Siemens,Connect2Air Wlan AP-600RP-USB,blank,connect
GVC,E800-RB1S,admin,epicrouter
Gateway,RCA DCW615R,blank,admin
Gateway,WBR-100,admin,admin
Gateway,WGC-220,admin,admin
Gateway,WGR-200AP,admin,admin
Gateway,WGR-200G,admin,admin
Gateway,Wireless Cable,blank,admin
Geek ADSL,Promax Q31,admin,geekadsl
Geek ADSL,Promax Q51,admin,geekadsl
Geewan,GF3,none,admin
Gembird,IS-BR4,admin,1234
Gemtek,CPE7000,unknown,unknown
Gemtek,WLTCS-106,,
Generic,54m,admin,admin
Generic,HPR4C0,blank,admin
Genexis,DRG700,admin,admin
Genexis,DRG716,admin,admin
Gennet OxyGEN,RFA1400.W,admin,admin
Gennet OxyGEN,RFA1400.W,admin,admin
GetNet,GR-534W,admin,admin
Gezz,AS900UR-SP4,admin,epicrouter
Gigabyte,GN-AR01G,admin,admin
Gigabyte,GN-B40,blank,admin
Gigabyte,GN-B41G,admin,admin
Gigabyte,GN-B46B,admin,admin
Gigabyte,GN-B49G,admin,admin
Gigabyte,GN-BR01G,admin,admin
Gigabyte,GN-BR01G,admin,admin
Gigabyte,GN-BR401,admin,admin
Gigafast,EE 400-R,blank,admin
Gigafast,WF719-CAPR,UNKNOWN,UNKNOWN
Gnet,BB0060B,DSL,DSL
Gnet,GBB2083,admin,admin
Gnet,IP0006,,admin
Gnet,IP0061,,admin
Gnet,IP104,blank,admin
Grandstream,HandyTone 486,none,123
Gravis Plus,e3000xdsl,blank,blank
Great Speed,GS 525G,root,root
Great Speed,GS-R250S,admin,broadband
Green Packet,DT-235,admin,admin
Green Packet,WN-600,admin,admin
GreyFox,F7562,,blank
Hama,62726,unknown,unknown
Hama,62726,unknown,unknown
Hama,62727,unknown,unknown
Hama,62731,admin,admin
Hama,DM-20,admin,admin
Hama,DR-20,admin,admin
Hama,DR-50,admin,epicrouter
Hame,MPR-A1,unknown,unknown
Hamlet,HRDSL512W,admin,admin
Hamlet,HRDSL640,admin,password
Hamlet,HRDSL742W,admin,password
Hatari,HW-AA101,admin,1234
Hawking,H2BR4,admin,1234
Hawking,HAWNR1,admin,1234
Hawking,HW2R1,admin,1234
Hawking,HWR54G,admin,blank
Hawking,HWRN1A,admin,1234
Hawking,HWRN2,admin,1234
Hawking,WR254,blank,blank
Hewlett Packard,hn200e,admin,admin
Hiro,H50188,admin,admin
Hitron Technologies,CGN,cusadmin,password
Hitron Technologies,CGN2 ROG,admin,password
Hitron Technologies,CGN3,cusadmin,password
Hitron Technologies,CGN3 ROG,cusadmin,password
Hitron Technologies,CVE-30360,admin,password
Hitron Technologies,CVW-30360,admin,password
Homeline,HLA-BR1000,user,blank or none
Homeline,HLA-WR3000,user,blank or none
HooToo,HT-ND003,none,admin
HooToo,HT-ND003,none,admin
HooToo,HT-ND006,none,admin
HooToo,N300,none,admin
Hot,Hotbox,admin,admin
Hot,Hotbox,admin,admin
HotBrick,LB-2 VPN,admin,
Hotline,DX-R204A,root,root
Huawei,B3000,admin,admin
Huawei,B593,admin,admin
Huawei,B660,admin,admin
Huawei,B660,admin,admin
Huawei,B681,admin,admin
Huawei,B683,admin,admin
Huawei,B683V,admin,admin
Huawei,B970,admin,blank
Huawei,BM625,admin,admin
Huawei,BM632,admin,admin
Huawei,BM635,admin,admin
Huawei,D100,admin,blank
Huawei,D105,admin,admin
Huawei,DR814,admin,admin
Huawei,E355,admin,admin
Huawei,E5172,admin,admin
Huawei,E5172s-920,admin,admin
Huawei,E5186s-22a,admin,admin
Huawei,E5573s,admin,admin
Huawei,E5577s,admin,admin
Huawei,E5776,admin,admin
Huawei,E586,admin,admin
Huawei,E960,admin,blank
Huawei,EchoLife BM625,admin,admin
Huawei,EchoLife BM626,admin,admin
Huawei,EchoLife HG520b,admin,admin
Huawei,EchoLife HG520b Telmex,user,user
Huawei,EchoLife HG520c,admin,admin
Huawei,EchoLife HG520i,admin,admin
Huawei,EchoLife HG520s,admin,admin
Huawei,EchoLife HG520u,admin,admin
Huawei,EchoLife HG520v,admin,admin
Huawei,EchoLife HG521,admin,admin
Huawei,EchoLife HG523,admin,admin
Huawei,EchoLife HG532,admin,admin
Huawei,EchoLife HG532b,admin,admin
Huawei,EchoLife HG556a,admin,admin
Huawei,EchoLife HG556a,vodafone,vodafone
Huawei,EchoLife HG866,root,admin
Huawei,F2000,admin,same as WiFi key on back of router
Huawei,Flybox B970,Admin,admin
Huawei,HG232f,admin,admin
Huawei,HG253s,admin,superonline
Huawei,HG256s,admin,admin
Huawei,HG510,admin,admin
Huawei,HG521c,admin,3bb
Huawei,HG530,admin,admin
Huawei,HG531,admin,admin
Huawei,HG532b,admin,admin
Huawei,HG532b,admin,admin
Huawei,HG532b,admin,admin
Huawei,HG532d,admin,admin
Huawei,HG532e,user,user
Huawei,HG532f,admin,admin
Huawei,HG532s,admin,admin
Huawei,HG533,admin,admin
Huawei,HG552e,admin,admin
Huawei,HG553,admin,admin
Huawei,HG556a,vodafone,vodafone
Huawei,HG556a,vodafone,vodafone
Huawei,HG556a,vodafone,vodafone
Huawei,HG55a,vodafone,vodafone
Huawei,HG622,admin,admin
Huawei,HG622u,admin,admin
Huawei,HG630,admin,3bb
Huawei,HG630,user,HuaweiUser
Huawei,HG630,user,user
Huawei,HG630b,admin,admin
Huawei,HG655b,admin,admin
Huawei,HG655d,admin,admin
Huawei,HG658,user,HuaweiUser 
Huawei,HG658b,user,HuaweiUser
Huawei,HG658c,vodafone,vodafone
Huawei,HG658G,vodafone,vodafone
Huawei,HG659,admin,admin
Huawei,HG685c,vodafone,vodafone
Huawei,HG8245,telecomadmin,admintelecom
Huawei,HG8245A,telecomadmin,admintelecom
Huawei,HG8245H,root,admin
Huawei,HG8245H,telecomadmin,admintelecom
Huawei,HG8245Q,digicel,digicel
Huawei,HG8245T,telecomadmin,admintelecom
Huawei,HG8247,telecomadmin,admintelecom
Huawei,HG8247H,root,admin
Huawei,R205,none,admin
Huawei,SMARTAX MT800,admin,admin
Huawei,SmartAX MT800,admin,admin
Huawei,Smartax MT841,admin,admin
Huawei,SmartAX MT880,admin,admin
Huawei,SmartAX MT880,admin,admin
Huawei,SmartAX MT880,admin,admin
Huawei,SmartAX MT880,admin,admin
Huawei,SmartAX MT880a,user,user
Huawei,SmartAX MT880a,admin,admin
Huawei,SmartAX MT882,admin,admin
Huawei,SmartAX MT882,admin,admin
Huawei,SmartAX MT882,admin,admin
Huawei,WA1003A,admin,admin
Hyundai,AS-502,root,root
ICIDU,NI-707502,admin,password
IDream,ADSL2 2+,Admin,Admin
IOGear,GNS1000200,unknown,unknown
IPSTAR,Satellite Modem,ADMIN,operator
ITI,DNA-A211-1,admin,admin
Icotera,i5800,admin,admin
Icotera,i6800,unknown,unknown
Inca,AMX-CA81R,admin,epicrouter
Inca,AR7WRD,admin,admin
Inexq,BR400,blank,blank
Inexq,ISO50s,blank,blank
Inexq,ISO50t,admin,1234
Inexq,ISW050u,admin,1234
Infomark,IMW-C600W,unknown,unknown
Infosmart,NFR3100P,admin,admin
Innomedia,MTA 3328-2R,admin,admin
Innotech,W7100N,tmadmin,tmadmin
Intel,Wireless Gateway,Admin,Intel
Intelbras,GKM 1000E,admin,admin
Intellinet,3G 375G,admin,1234
Intellinet,520454,,blank
Intellinet,Active Networking,admin,1234
Inteno,DG150B,user,user
Inteno,DG301 iopsys,user,user
Inteno,DG301AL,admin,SerialNumber
Inteno,EG101R1,user,user
Inteno,x5668,user,user
Inteno,X5668B,user,user
Inteno,X5669A,admin,admin
Inteno,X5671,user,user
Inteno,X5671B,user,user
Intercross,5633NE,admin,admin
Intertex,IX67,UNKNOWN,UNKNOWN
Intracom,JetSpeed 500,admin,admin
Intracom,JetSpeed 500i,admin,admin
Intracom,jetSpeed 520,admin,admin
Intracom,jetSpeed 520i,admin,admin
Intracom,NetFasteR IAD,admin,admin
Intracom,NetFasteR WLAN,admin,admin
Inventel,D5213,blank,blank
Inventel,Livebox,UNKNOWN,UNKNOWN
Inventel,Livebox,admin,admin
Inventel,Livebox 3c0e,admin,admin
Inventel,Livebox 7DD8,admin,admin
Inventel,Livebox 9270,admin,admin
Inventel,Livebox DV4210-WA,UNKNOWN,UNKNOWN
Inventel,Livebox DV4210-WU,admin,admin
Iskratel,SI2000 Callisto 821+,admin,admin
Jaht,EA-2104G,admin,admin
Jaht,WA-4054X,admin,1234
Jensen Scandinavia,AirLink 10006,admin,1234
Jensen Scandinavia,AirLink 29150,admin,1234
Jensen Scandinavia,AirLink 29150,admin,1234
Jensen Scandinavia,AirLink 2954,admin,admin
Jensen Scandinavia,AirLink 5000AC,admin,1234
Jensen Scandinavia,Airlink 59300,admin,1234
Jensen Scandinavia,AirLink 59300,admin,1234
Jensen Scandinavia,AirLink 89300,admin,1234
Jensen Scandinavia,Airlink WBR-6911,blank,blank
Jensen Scandinavia,Airlink WBR-6954,,blank
Jensen Scandinavia,AirLink WBR-7954,admin,admin
Jensen Scandinavia,AL29150,admin,1234
Jensen Scandinavia,NL610,admin,admin
Jensen Scandinavia,WebLink 39300,admin,1234
Justec,JBR454W,NONE,admin001
Justec,JDR810,,Justec
Justec,JDR840,user,password
KEEBOX,W150NR,admin,blank
KONIG,CMP ROUTER10,admin,admin
Kaiomy,500G 4PU,admin,epicrouter
Kaiomy,APR-4P,guest,guest
Kasda,KD318MUI,admin,0
Kasda,KE318D,admin,password or telekomst
Kasda,RTL867x,user,password
Kcorp,KLG-575,admin,admin
Kcorp,KLS-6615,,blank
Keyteck,NET-25GSU,admin,password
Kingnet,KN-S1060,admin,admin
Kobian,Mercury KOB BR100,blank,blank
Kozumi,K-5400GR,guest,guest
Kozumi,KM-400P,admin,admin
Kraun,KR-1W,admin,admin
Kraun,KR-1W,admin,admin
Kraun,KR.1N,admin,admin
Kyocera,KR-2,none,admin
Kyocera,KR1002,admin,none
L7 Networks,L7-NR-2000,admin,admin
LB-Link,BL-WR3000,admin,admin
LG,LAM400,admin,epicrouter
LG,LRG1004,,blank
LG,LWG5400R,admin,admin
La Fonera,FON2100,admin,admin
LanTech,HR-114-II,blank,blank
LanTech,HR-117,blank,root
Lectron,AR800C2,admin,epicrouter
Lectron,AR800C2-A04,admin,epicrouter
Legrand,On-Q 364772-02-V1,admin,admin
Legrand,On-Q DA1004,admin,admin
Level One,FBR 1100TX,NOLOGIN,NOLOGIN
Level One,FBR 1161,admim,admin
Level One,FBR 1400TX,NOLOGIN,NOLOGIN
Level One,FBR 1401TX,NOLOGIN,NOLOGIN
Level One,FBR 1402TX,NOLOGIN,NOLOGIN
Level One,FBR 1403TX,NOLOGIN,NOLOGIN
Level One,FBR 1405TX,NONE,blank
Level One,FBR 1405TX,admin,1234
Level One,FBR 1406TX,NONE,blank
Level One,FBR 1407A,NONE,admin
Level One,FBR 1407B,NONE,admin
Level One,FBR 1409TX,NONE,admin
Level One,FBR 1411TX,NONE,admin
Level One,FBR 1413TX,NONE,admin
Level One,FBR 1416A,admin,password
Level One,FBR 1418TX,,admin
Level One,FBR 1461A,admin,admin
Level One,WBR 1100TX,NOLOGIN,NOLOGIN
Level One,WBR 1400TX,NOLOGIN,NOLOGIN
Level One,WBR 2400TX,NOLOGIN,NOLOGIN
Level One,WBR 2401A,NONE,admin
Level One,WBR 2401B,NONE,admin
Level One,WBR 3400TX,NOLOGIN,NOLOGIN
Level One,WBR 3400TX,NOLOGIN,NOLOGIN
Level One,WBR 3402,NONE,admin
Level One,WBR 3403TX,NONE,admin
Level One,WBR 3404TX,NONE,admin
Level One,WBR 3405TX,admin,admin
Level One,WBR 3406TX,admin,admin
Level One,WBR 3407a,blank,blank
Level One,WBR 3408,blank,blank
Level One,WBR 3460,unknown,unknown
Level One,WBR 5400,admin,admin
Level One,WBR 6001,,password
Leviton,10-100,admin,
Leviton,47611-GT4,,leviton
Libya,Libyamax,admin,admin
Linetec,LT150MR,unknown,unknown
Link-Max,LM341,blank,12345
LinkPro,WL-G54AAR,admin,admin
LinksKey,LKR-604,admin,admin
Linksys,AG241,admin,admin
Linksys,AG300,admin,admin
Linksys,AM200,admin,admin
Linksys,AM300,admin,admin
Linksys,BEFCMUH4,none,admin
Linksys,BEFDSR41W,blank,admin
Linksys,BEFN2PS4,blank,admin
Linksys,BEFSR11,blank,admin
Linksys,BEFSR11,admin,admin
Linksys,BEFSR41,blank,admin
Linksys,BEFSR41,blank,admin
Linksys,BEFSR41,blank,admin
Linksys,BEFSR41,admin,admin
Linksys,BEFSR81,blank,admin
Linksys,BEFSR81,blank,admin
Linksys,BEFSR81,blank,admin
Linksys,BEFSRU31,blank,admin
Linksys,BEFSX41,blank,admin
Linksys,BEFSX41,blank,admin
Linksys,BEFSX41,blank,admin
Linksys,BEFSX41,blank,admin
Linksys,BEFVP41,blank,admin
Linksys,BEFVP41,admin,admin
Linksys,BEFW11P1,blank,admin
Linksys,BEFW11S4,blank,admin
Linksys,BEFW11S4,blank,admin
Linksys,BEFW11S4,blank,admin
Linksys,BEFW11S4,blank,admin
Linksys,BEFW11S4,blank,admin
Linksys,befw11s4,blank,admin
Linksys,BEFW11S4,blank,admin
Linksys,BEFW11S4,blank,admin
Linksys,BEFW11S4,blank,admin
Linksys,befws1s4,blank,admin
Linksys,DD-WRT,root,admin
Linksys,E1000,admin,admin
Linksys,E1200,admin,admin
Linksys,E1500,admin,admin
Linksys,E1550,admin,admin
Linksys,E1700,admin,admin
Linksys,E2000,admin,admin
Linksys,E2100L,admin,admin
Linksys,E2500,admin,admin
Linksys,E3000,admin,admin
Linksys,E3200,admin,admin
Linksys,E4200,admin,admin
Linksys,E4200,admin,admin
Linksys,E8350,admin,blank
Linksys,E900,blank,admin
Linksys,EA2700,admin,blank
Linksys,EA3500,admin,blank
Linksys,EA4500,admin,admin
Linksys,EA4500 Smart Wi-Fi,admin,admin
Linksys,EA6100,admin,admin
Linksys,EA6350,admin,admin
Linksys,EA6500,none,admin
Linksys,EA6900,admin,admin
Linksys,EA7300,admin,admin
Linksys,EA8500,created in initial setup,created in initial setup
Linksys,EA9200,admin,admin
Linksys,EA9500,admin,admin
Linksys,HG200,blank,admin
Linksys,HR200,blank,admin
Linksys,Network Everywhere NR041,blank,admin
Linksys,RT31P2,blank,admin
Linksys,RT41-BU,,admin
Linksys,RT41P2 AT,blank,admin
Linksys,RTP300,admin,admin
Linksys,RV016,admin,admin
Linksys,RV042,admin,admin
Linksys,RV082,admin,admin
Linksys,RV082,admin,admin
Linksys,RVS4000,admin,admin
Linksys,SPA-2100,user,primus
Linksys,SPA-2102,admin,password
Linksys,SPA-3102,admin,password
Linksys,SPA-9000,admin,password
Linksys,UTA200-TM,blank,admin
Linksys,WAG120N,admin,admin
Linksys,WAG160N,admin,admin
Linksys,WAG160N,admin,admin
Linksys,WAG200G,admin,admin
Linksys,WAG300N,admin,admin
Linksys,WAG320N,admin,admin
Linksys,WAG325N,admin,admin
Linksys,WAG354G,admin,admin
Linksys,WAG354G,admin,admin
Linksys,WAG54G,blank,admin
Linksys,WAG54G,blank,admin
Linksys,WAG54G,linksys,blank
Linksys,WAG54G,blank,admin
Linksys,WAG54G,admin,admin
Linksys,WAG54G,admin,admin
Linksys,WAG54G-XW,blank,admin
Linksys,WAG54G2,admin,admin
Linksys,WAG54G2-NL,admin,admin
Linksys,WAG54GP2,blank,admin
Linksys,WAG54GS,,admin
Linksys,WAG54GX2,linksys,blank
Linksys,WCG200,blank,admin
Linksys,WCG200,blank,admin
Linksys,WRH54G,blank,admin
Linksys,WRK54G,blank,admin
Linksys,WRP200,,admin
Linksys,WRP400,admin,admin
Linksys,WRT100,blank,admin
Linksys,WRT110,blank,admin
Linksys,WRT110,blank,admin
Linksys,WRT120N,admin,admin
Linksys,WRT150,blank,admin
Linksys,WRT150N,blank,admin
Linksys,WRT150N-PT,blank,admin
Linksys,WRT160N,blank,admin
Linksys,WRT160N,blank,admin
Linksys,WRT160N,admin,admin
Linksys,WRT160N,admin,admin
Linksys,WRT160NL,admin,admin
Linksys,WRT1900AC,admin,admin
Linksys,WRT1900ACS,admin,admin
Linksys,WRT300N,blank,admin
Linksys,WRT310N,blank,admin
Linksys,WRT310N,admin,admin
Linksys,WRT310N-ES,blank,admin
Linksys,WRT3200ACM,admin,admin
Linksys,WRT320N,admin,admin
Linksys,WRT330N,admin,admin
Linksys,WRT350N,blank,admin
Linksys,WRT350N,blank,admin
Linksys,WRT400N,admin,admin
Linksys,WRT51AB,blank,admin
Linksys,WRT54AG,blank,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G,root,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G,root,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G,blank,admin
Linksys,WRT54G-TM,blank,admin
Linksys,WRT54G2,admin,admin
Linksys,WRT54G2,admin,admin
Linksys,WRT54G3G,blank,admin
Linksys,WRT54G3G,admin,admin
Linksys,WRT54G3G,admin,admin
Linksys,WRT54G3G,admin,admin
Linksys,WRT54G3G,admin,admin
Linksys,WRT54GC,admin,admin
Linksys,WRT54GH,admin,admin
Linksys,WRT54GL,blank,admin
Linksys,WRT54GL,blank,admin
Linksys,WRT54GL FON,none,admin
Linksys,WRT54GP2,admin,admin
Linksys,WRT54GP2A-AT,admin,admin
Linksys,WRT54GR,blank,admin
Linksys,WRT54GS,blank,admin
Linksys,WRT54GS,admin,admin
Linksys,WRT54GS,admin,admin
Linksys,WRT54GS,blank,admin
Linksys,WRT54GS,blank,admin
Linksys,WRT54GS,blank,admin
Linksys,WRT54GS2,admin,admin
Linksys,WRT54GX,blank,admin
Linksys,WRT54GX,blank,admin
Linksys,WRT54GX2,blank,admin
Linksys,WRT54GX4,blank,admin
Linksys,WRT55AG,blank,admin
Linksys,WRT55AG,blank,admin
Linksys,WRT600N,none,admin
Linksys,WRT610N,blank,admin
Linksys,WRT610N,admin,admin
Linksys,WRTP54G,admin,admin
Linksys,WRTP54G-ER,admin,admin
Linksys,WRTSL54GS,admin,admin
Linksys,WRTU54G-TM,admin,admin
Linksys,WRV200,admin,admin
Linksys,WRV54G,blank,admin
Linksys,WRV54G,blank,admin
Linksys,WRV54G,blank,admin
Linksys,WRVS4400N,admin,admin
Linksys,WTR54GS,admin,admin
Linksys,WUSB54GS,admin,admin
Linksys,X1000,admin,admin
Linksys,X2000,admin,blank
Linksys,X2000,admin,blank
Linksys,X6200,admin,admin
LogN,HN-DR4PG,admin,password
Longshine,LCS-883-DSL-4F,unknown,unknown
Loopcomm,LP-8186,admin,1234
Loopcomm,LP-AL2011,admin,epicrouter
Loopcomm,LP-AL2014P,user,password
Loopcomm,LP-AL5011P,root,root
Lucent Technologies,CELL-22A-FX-CZ,root,root
Luxul,XWR-1750,admin,admin
MS-Tech,LR-510,admin,blank
MSI,RG300N,admin,admin
MSI,RG54G2,admin,admin
MSI,RG54G3,admin,admin
MSI,RG54GS,admin,admin
MSI,RG54GS2,admin,admin
MSI,RG54SE,admin,admin
MSI,RG54SE II,admin,admin
MSI,RG60G,admin,admin
MSI,RG60SE,unknown,unknown
MTN,ShareLink,admin,admin
MacSense,MIH-130A,blank,admin
Maplin,AR25TU2,unknown,unknown
Marconi,Model 2,admin,epicrouter
Marconi,Telkom Adsl,,password
Marconi,Telkom Premium Combo,admin,administrator
Marconi,X7721r,unknown,unknown
MaxGate,UGate 3000,blank,blank
MaxGate,UGate 3200,blank,blank
MaxGate,UGate 3200P,blank,blank
MaxGate,UGate 3300,blank,blank
MaxGate,UGate Plus,blank,blank
Maxim Networking,WRS-G54MR,admin,admin
Mecer,E5104N2,admin,password
MediaLink,MWN-APR150N,admin,admin
MediaLink,MWN-WAPR150N,admin,admin
MediaLink,MWN-WAPR300N,admin,admin
Medion,MD 40900,medion,admin
Mentor,Annex A,admin,epicrouter
Mentor,FR411,blank,blank
Mentor,FR411UK,,blank
Mentor,Wireless G,,UNKNOWN
Mentor,wl r4rii uk,,UNKNOWN
Microcom,2632,admin,epicrouter
Microcom,2636,admin,epicrouter
Microcom,AD 2651,,epicrouter
Microcom,AD 2654,,epicrouter
Microcom,AD 2656,,epicrouter
Microcom,AD 2706,admin,admin
Microcom,deskporte 400,admin,epicrouter
Microlink,Dsl Router,Admin,password
Micronet,SP3351,admin,epicrouter
Micronet,SP3364,admin,admin
Micronet,SP880B,admin,blank
Micronet,SP888B,admin,admin
Micronet,SP888C,,blank
Micronet,SP916GK,admin,1234
Micronet,SP916GK,admin,admin
Microsoft,MN-100,NONE,admin
Microsoft,MN-500,NONE,admin
Microsoft,MN-700,NONE,admin
Microsoft,MN-820,NONE,admin
Minitar,MN54G4R,blank,admin
MoFi,3500-3GN,root,admin
Mobily,Connect 4G,admin,
Modecom,MC-WR22,admin,admin
Motorola,2210,admin,password
Motorola,2210,admin,password
Motorola,3347,admin,blank
Motorola,3347,admin,password
Motorola,3347-02,admin,password
Motorola,3347-02,admin,admin
Motorola,BR700,admin,motorola
Motorola,CPEi 25150,none,motorola
Motorola,CPEi 35775,none,motorola
Motorola,CPEo 400,none,motorola
Motorola,i600,admin,motorola
Motorola,MT123,admin,motorola
Motorola,NVG510,none,none
Motorola,NVG595,none,Printed on Routers Label
Motorola,SBG1000,admin,motorola
Motorola,SBG6580,admin,motorola
Motorola,SBG6580,admin,motorola
Motorola,SBG6782-AC,admin,motorola
Motorola,SBG900,admin,motorola
Motorola,SBG901,admin,Motorola
Motorola,SBG941,admin,motorola
Motorola,SVG1501,admin,motorola
Motorola,SVG2501,admin,Motorola
Motorola,VT1000,NONE,blank
Motorola,VT1005V,unknown,unknown
Motorola,VT2142,router,router
Motorola,VT2442,,admin
Motorola,WR850G,admin,motorola
Motorola,WR850G,admin,motorola
Mototech,AXR1100,unknown,unknown
Multilaser,RE024,admin,admin
Multitech,RouteFinder RF560VPN,admin,blank
MyMax,MWR AP 54M,admin,admin
MyMax,WR923-BK,admin,admin
MyTech,Facile,admin,admin
NTech Wireless Tech,ADSL-AR41A,admin,admin
Net-Lynx,Vulcan,root,root
Net-Lynx,WAR25TC,admin,trendchip
Net-Lynx,WR514R,admin,1234
NetBox Blue,Corporate,unknown,unknown
NetMaster,CBW-560,none,cable
Netcomm,3G10WVT,admin,admin
Netcomm,3G21WB,admin,admin
Netcomm,3G36W-V,admin,blank
Netcomm,3G42W-MB,admin,admin
Netcomm,3G9WB,admin,admin
Netcomm,4G100W,admin,blank
Netcomm,MyZone 3G24W,admin,blank
Netcomm,nb1,admin,admin
Netcomm,NB1300 ADSL,admin,password
Netcomm,NB1300 PLUS 4,admin,password
Netcomm,NB14WN,admin,admin
Netcomm,NB2800,blank,admin
Netcomm,NB3,root,root
Netcomm,NB3000,blank,admin
Netcomm,NB304N,admin,admin
Netcomm,NB3100,blank,admin
Netcomm,NB3100C,blank,admin
Netcomm,NB3200,blank,admin
Netcomm,NB3300,blank,admin
Netcomm,NB4,admin,password
Netcomm,NB5,admin,admin
Netcomm,NB5 Plus 4,admin,admin
Netcomm,NB5 Plus 4W,admin,admin
Netcomm,NB5540,blank,admin
Netcomm,NB5580W,admin,admin
Netcomm,NB6 Plus 4,admin,admin
Netcomm,NB6 PLUS 4W,admin,admin
Netcomm,NB600W,admin,admin
Netcomm,NB604N,admin,admin
Netcomm,NB6W,admin,admin
Netcomm,NB7,admin,admin
Netcomm,NB9W,admin,admin
Netcomm,NB9WMAXX,admin,admin
Netcomm,NF15ACV,admin,trustpower
Netcomm,NF15ACV,admin,admin
Netcomm,NF2,admin,admin
Netcomm,NF2 N900,admin,admin
Netcomm,NF3ADV,admin,admin
Netcomm,NF4V Orcon,admin,password
Netcomm,NP803n,admin,admin
Netcomm,NP805N,admin,admin
Netcomm,NP805N 11n,admin,admin
Netcomm,NW5580W,,admin
Netcomm,SM4300,blank,default
Netcoretek,2105NR,guest,guest
Netcoretek,2505NR,Guest,Guest
Netgear,7550,admin,password
Netgear,AC1600 C6250EMR,admin,password
Netgear,AC1750 C6300,admin,password
Netgear,AC790S,none,admin
Netgear,AirCard 782S,none,admin
Netgear,C3000 N300,admin,password
Netgear,C6300,admin,password
Netgear,CBVG834G,admin,password
Netgear,CBVG834G,admin,password
Netgear,CG3000,admin,password
Netgear,CG3000D,admin,password
Netgear,CG3000D,admin,password
Netgear,CG3000D,admin,password
Netgear,CG3100,admin,password
Netgear,CG3100D-2,admin,password
Netgear,CG3101D,admin,password
Netgear,CG3101D,unknown,unknown
Netgear,CG4500BD,admin,password
Netgear,CG814GCMR,admin,password
Netgear,CG814W,admim,password
Netgear,CG814WG,comcast,1234
Netgear,CG814WG,admin,password
Netgear,CG814WG,superuser,password
Netgear,CGD24G,admin,password
Netgear,CGD24N,admin,password
Netgear,CGD24N,admin,password
Netgear,CGW814WG,comcast,1234
Netgear,CVG824G,admin,password
Netgear,CVG834G,admin,password
Netgear,D6300,admin,password
Netgear,D7000 Nighthawk AC1900,admin,password
Netgear,DG480,admin,changeme
Netgear,DG632,admin,password
Netgear,DG632,admin,password
Netgear,DG814,admin,password
Netgear,DG814,admin,password
Netgear,DG824M,admin,password
Netgear,DG834,admin,password
Netgear,DG834G,admin,password
Netgear,DG834GSP,admin,password
Netgear,DG834GT,,password
Netgear,DG834GU,admin,password
Netgear,DG834N,admin,admin
Netgear,DG834PN,,password
Netgear,DG934G,admin,password
Netgear,DGFV338,admin,password
Netgear,DGN1000,admin,password
Netgear,DGN1000SP,admin,password
Netgear,DGN2000,admin,password
Netgear,DGN2200,admin,password
Netgear,DGN2200,admin,password
Netgear,DGN2200,admin,password
Netgear,DGN2200,admin,password
Netgear,DGN2200B,admin,password
Netgear,DGN3500,admin,password
Netgear,DGND3300,admin,password
Netgear,DGND3700,admin,password
Netgear,DGND3700,admin,password
Netgear,DM111PSP,admin,password
Netgear,DM602,admin,password
Netgear,EVG2000,admin,password
Netgear,FM114P,admin,password
Netgear,FR114P,admin,password
Netgear,FR114W,admin,password
Netgear,FR314,admin,password
Netgear,FR318,admin,password
Netgear,FR328S,admin,password
Netgear,FV318,admin,password
Netgear,FVG318,admin,password
Netgear,FVL328,admin,password
Netgear,FVS114,admin,password
Netgear,FVS124G,admin,password
Netgear,FVS318,admin,password
Netgear,FVS318,admin,password
Netgear,FVS318,admin,password
Netgear,FVS318G,admin,password
Netgear,FVS328,admin,password
Netgear,FVS336G,admin,password
Netgear,FVS336G,admin,password
Netgear,FVS338,admin,password
Netgear,FVX538,,password
Netgear,FWAG114,admin,password
Netgear,FWG114,admin,password
Netgear,FWG114P,admin,password
Netgear,FWG114P,admin,password
Netgear,HR314,admin,password
Netgear,KWGR614,admin,password
Netgear,MBR1210,admin,password
Netgear,MBR624GU,admin,password
Netgear,MBR814X,admin,password
Netgear,ME102,admin,epicrouter
Netgear,MR314,admin,password
Netgear,MR314,admin,1234
Netgear,MR814,admin,password
Netgear,MR814,admin,password
Netgear,MR814,admin,password
Netgear,Nighthawk R7000,admin,password
Netgear,Nighthawk R8300,admin,password
Netgear,Nighthawk R8500,admin,password
Netgear,Nighthawk X6 R8000,admin,password
Netgear,Orbi RBK50,admin,password
Netgear,Orbi RBR50,admin,password
Netgear,R6100,admin,password
Netgear,R6300,admin,password
Netgear,R6300,admin,password
Netgear,R6400,admin,password
Netgear,R7000,admin,password
Netgear,R8300,admin,password
Netgear,R8500,admin,password
Netgear,R9000 Nighthawk X10,admin,password
Netgear,RH340,NONE,1234
Netgear,RM356,NONE,1234
Netgear,RO318,admin,1234
Netgear,RP114,admin,1234
Netgear,RP614,admin,password
Netgear,RP614,admin,password
Netgear,RP614,admin,password
Netgear,RP614,admin,password
Netgear,RT311,NONE,1234
Netgear,RT314,NONE,1234
Netgear,RT314,admin,1234
Netgear,RT314,admin,1234
Netgear,RT388,NONE,1234
Netgear,Super Hub 2,admin,admin
Netgear,TA612V,admin,password
Netgear,UTM5,admin,password
Netgear,VMDG280,admin,password
Netgear,VMDG480,admin,changeme
Netgear,VMDG480,admin,changeme
Netgear,VMDG485,admin,admin
Netgear,VMDG485,admin,admin
Netgear,VMDG490,NONE,on router label
Netgear,VVG2000,admin,password
Netgear,WGR613VAL,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGT624,admin,password
Netgear,WGT624,admin,password
Netgear,WGT624,admin,password
Netgear,WGT624,admin,password
Netgear,wgt634u,admin,password
Netgear,WGU624,admin,password
Netgear,WGXB102,admin,password
Netgear,WNDR3300,admin,password
Netgear,WNDR3400,admin,password
Netgear,WNDR3400,admin,password
Netgear,WNDR3700,admin,password
Netgear,WNDR3800,admin,password
Netgear,WNDR4000,admin,password
Netgear,WNDR4300,admin,password
Netgear,WNDR4500,admin,password
Netgear,WNDR4500,admin,password
Netgear,WNDR4700,admin,password
Netgear,WNDRMAC,admin,password
Netgear,WNR1000,admin,password
Netgear,WNR1000,admin,password
Netgear,WNR1000,admin,password
Netgear,WNR1000,admin,password
Netgear,WNR2000,admin,password
Netgear,WNR2000,admin,password
Netgear,WNR2000,admin,password
Netgear,WNR2000,admin,password
Netgear,WNR2000,admin,password
Netgear,WNR2500,admin,password
Netgear,WNR3500,admin,password
Netgear,WNR3500,admin,admin
Netgear,WNR3500L,admin,admin
Netgear,WNR3500L,admin,password
Netgear,WNR612,admin,password
Netgear,WNR834B,admin,password
Netgear,WNR834B,admin,password
Netgear,WNR834M,admin,password
Netgear,WNR854T,admin,password
Netgear,WPN824,admin,password
Netgear,WPN824,admin,password
Netgear,WPN824,admin,password
Netgear,WPN824N,admin,password
Netgear,WPNT834,admin,password
Netis,WF-2404,guest,guest
Netis,WF-2409,guest,guest
Netis,WF2411,admin,admin
Netis,WF2411,NONE,NONE
Netis,WF2419,netis,password
Netis,WF2419E,,
Netopia,2240N-VGx,admin,1234
Netopia,2241N-ITel,admin,admin
Netopia,2241N-VGx,admin,1234
Netopia,2246N-VGx,admin,1234
Netopia,2247-02,admin,admin1
Netopia,2247-62,admin,admin
Netopia,2247NWG-VGx,admin,1234
Netopia,3000,admin,password
Netopia,3341,admin,1234
Netopia,3341,blank,blank
Netopia,3341-006,admin,1234
Netopia,3342,admin,1234
Netopia,3346-006,admin,1234
Netopia,3346N-002,admin,1234
Netopia,3346N-VGx,admin,1234
Netopia,3346N-VGx,blank,blank
Netopia,3347-02,admin,admin
Netopia,3347-02,admin,password
Netopia,3347-02-1006l,admin,password
Netopia,3347-02-1022,admin,password
Netopia,3347NWG,admin,1234
Netopia,3347NWG-006,admin,1234
Netopia,3347NWG-006,admin,admin
Netopia,3347NWG-VGx,admin,1234
Netopia,3347NWGv2,admin,1234
Netopia,3347W,admin,1234
Netopia,3347W-006,admin,1234
Netopia,3347W-T,admin,1234
Netopia,3347WG-VGx,admin,1234
Netopia,3387WG-VGx,admin,1234
Netopia,3546,admin,1234
Netopia,3546-002,admin,1234
Netopia,3547W,admin,1234
Netopia,Cayman3300,admin,admin
Netopia,Cayman3341,admin,1234
Netopia,Cayman3346,admin,1234
Netvigator,30M,user,user
Network Everywhere,NR041,blank,admin
Network Everywhere,NWM11B,blank,admin
Network Everywhere,NWR04B,blank,admin
Network Everywhere,NWR11B,blank,admin
Network Everywhere,NWU11B,blank,admin
New Link,93071G,Admin,Admin
New Link,NLWL-ROU01,unknown,
Nexian,RE-251,unknown,unknown
Nexland,ISB-Pro400,UNKNOWN,UNKNOWN
Nexxt Solutions,NW230NXT15,guest,guest
Noganet,NG-150N,admin,admin
Noganet,NG-R2504P,admin,admin
Noganet,TEI-6608,unknown,unknown
Nokia,BR41,blank,blank
Nokia,IP55,UNKNOWN,UNKNOWN
Nokia,MW1122,UNKNOWN,UNKNOWN
Nokia Siemens,C2110,admin,admin
Nokia Siemens,H640V-25E,root,admin
NovaTech,NV-945W,unknown,unknown
Novatel Wireless,MiFi 2372,none,admin
Novatel Wireless,MiFi 4082,none,admin
Novatel Wireless,MiFi 6620L,NONE,admin
Nucom,R5000UN,unknown,unknown
O2,TG582n,unknown,unknown
O2,TG585,unknown,unknown
OTE,Speedport W 724V,none,on the rear panel of the device
Octtel,SP4220,blank,blank
Olitec,SX200,admin,adslolite
On Networks,N150R,admin,admin
On Networks,N300R,admin,admin
Open Networks,iConnect 625W,root,0P3N
Open Networks,iConnect Access 611,root,OP3N
Open Networks,iConnect Access 612,root,OP3N
Open Networks,iConnect Access 621,root,OP3N
Open Networks,iConnect Access 624,root,0P3N
Opticom,DSLink 485,admin,gvt12345
Orcon,Genius,none,admin
Origo,ASR-8100,unknown,unknown
Origo,ASR-8400,admin,epicrouter
Origo,ASR-8400,admin,epicrouter
Origo,AWR-8210,unknown,unknown
Origo,BRP-1400,,admin
Ovislink,AirLive IP-1000R,admin,airlive
Ovislink,Airlive WL-5424AR,admin,blank
Ovislink,Airlive WL-8064ARM,admin,airlive
Ovislink,AirLive WL-8064ARM,admin,airlive
Ovislink,AirLive WMM-3000R,admin,airlive
Ovislink,Airlive WT-2000ARM,admin,1234
Ovislink,AirLive WT-2000R,admin,airlive
Ovislink,ARM-104,admin,airlive
Ovislink,DV711C,user,password
Ovislink,ELive ARM104,admin,epicrouter
Ovislink,EVO-WR54ADSL,admin,admin
Ovislink,OV IPAC7 11,user,password
Ovislink,SR-600,blank,blank
Ozenda,11g Wireless,NONE,blank
Ozenda,AR4505GW,none,blank
PCI,BLW-54MF,admin,admin
PCI,BLW-HPMM,admin,0
PLDT,SpeedSurf 504AN,adminpldt,1234567890
PLDT,SpeedSurf 504AN,adminpldt,1234567890
PTI,PAE-CE81,admin,epicrouter
PTI,PAE-CE84,admin,epicrouter
PTI,PTI-840,admin,epicrouter
PTI,PTI-840G,admin,blank
Pace Plc,3801HGV,none,printed on router
Pace Plc,4111N-030,admin,admin
Pace Plc,4111N-031,admin,admin
Pace Plc,5268AC,unknown,unknown
Paradigm,PTI-8411,admin,admin
Paradigm,PTI-8411,admin,admin
Paradigm,PTI-8611GU,admin,admin
Paradyne,6211-I1,admin,admin
Paradyne,6211-I2,admin,admin
Paradyne,6211-I3,admin,admin
Paradyne,6212-I3,admin,admin
Paradyne,6218-I2,admin,admin
Paradyne,6381,admin,admin
Paradyne,6381-A3,admin,admin
Paradyne,6381-A4,Admin,Admin
ParkerVision,WR1500,NONE,1234
Pass and Seymour,CNR-7562V,blank,blank
Peak,M73-APO07-480,blank,blank
Pegasus,ART25GSU,root,root
Pentagram,Cerberus,admin,admin
Pentagram,Cerberus P 6351,admin,pentagram
Pentagram,P6311-07A,unknown,unknown
Pheenet,WBIG-614AGC,admin,epicrouter
Philips,CGA3600N-TE,admin,admin
Philips,CGA5720N-TE,UNKNOWN,UNKNOWN
Philips,CGA5720S-TE,UNKNOWN,UNKNOWN
Philips,CPWBS054,blank,blank
Philips,CPWBS154-18,blank,blank
Philips,SNA6500,UNKNOWN,UNKNOWN
Philips,SNA6500-18,UNKNOWN,UNKNOWN
Philips,SNA6600-18,UNKNOWN,UNKNOWN
Philips,SNA6640-00,UNKNOWN,UNKNOWN
Philips,SNB5600,blank,blank
Philips,SNB6500,blank,blank
Philips,SNV6520-18,UNKNOWN,UNKNOWN
Phoebe,oct11g-ir,,admin
Pikatel,Airmax 101,admin,password
Pikatel,Combo,,DSL
Pikatel,Quartet,DSL,DSL
Ping Communication,RGW208EN,Admin,unknown
Pirelli,AGEmB,admin,microbusiness
Pirelli,Alice AH4021,,AliceMod
Pirelli,DRG-A112,3play,3play
Pirelli,DRG-A124G,admin,admin
Pirelli,DRG-A125G,admin,admin
Pirelli,DRG-A225G,3play,3play
Pirelli,DRG-A225G,admin,admin
Pirelli,DRG-A226G,telekom,telekom
Pirelli,NetGate VoIP,user,user
Pirelli,PRG AV4202N,admin,admin
Pirelli,VoIP AG,on,on
Pirelli,Wireless VoIP AG,user,user
Planet,ADE-3000,admin,conexant
Planet,ADE-3100,admin,epicrouter
Planet,ADE-3400,admin,admin
Planet,ADE-4000,admin,epicrouter
Planet,ADE-4100,admin,admin
Planet,ADE-4100A,admin,epicrouter
Planet,ADE-4120,admin,admin
Planet,ADE-4200,admin,admin
Planet,ADE-4400,admin,admin
Planet,ADN-4100,admin,admin
Planet,ADW-4100,admin,epicrouter
Planet,ADW-4200,admin,admin
Planet,ADW-4300,admin,blank
Planet,ADW-4401,admin,admin
Planet,ADW-4401A,admin,admin
Planet,WMRT-414,unknown,unknown
Planet,WRT-416,admin,admin
Planet,WRT410,admin,admin
Planet,XRT-401B,,Admin
Planet,XRT-401C,,blank
Planet,XRT-401D,admin,1234
Planet,XRT-401E,admin,admin
Planet,XRT-402D,admin,1234
Planex,BLW-54SAG,admin,password
Planex,BRL-04UR,admin,0
Pluscom,AWR-7200,admin,admin
Pluscom,BR7-WP3221,admin,admin
Pluscom,WR2-RTL8186,unknown,unknown
Portal,AC2400,none,password
PowerNet,PAR-720G,Admin,Admin
Primatel,P101,admin,admin
Primus Lingo,iAN-02ex,user,user
Pro-Nets,RT514S,admin,1234
Prolink,9200S,admin,password
Prolink,H5001N,admin,password
Prolink,H5004N,admin,password
Prolink,H5004NK Tattoo,admin,password
Prolink,H5200,user,user
Prolink,H5201,unknown,unknown
Prolink,H5201,user,user
Prolink,H6300G,admin,admin
Prolink,H9000,admin,password
Prolink,H9200,admin,password
Prolink,H9200AR,admin,password
Prolink,H9200P,admin,password
Prolink,H9300G,admin,admin
Prolink,Hurricane 5200,admin,password
Prolink,Hurricane 5305G,admin,password
Prolink,Hurricane 6300GL,admin,password
Prolink,Hurricane 9000,admin,password
Prolink,Hurricane 9000G,admin,admin
Prolink,Hurricane 9000P,admin,password
Prolink,Hurricane 9000W,admin,password
Prolink,WER-401,admin,blank
Prolink,WGR1004,admin,1234
Prolink,WNR1006,admin,password
Pronet,PN-54WADSL2,unknown,unknown
Pronet,PN-54WRT,admin,admin
Pronets,ART-25-GSU,,root
Pronets,RT514WH2,admin,1234
Pronets,RTS14WH2,admin,1234
Q-Tec,584AA,admin,epicrouter
Q-Tec,585AB,admin,epicrouter
Q-Tec,773WR,admin,1234
Q-Tec,778WR,blank,blank
Q-Tec,790RH,blank,blank
Quanta,Mobily 4G,none,blank
Qubs,QAR40X04E,admin,1234
Quick Eagle Networks,DL710,admin,admin
Quicktel,QAR367E4W,admin,admin
Quicktel,QAR367EW,unknown,unknown
RadioLabs,O2 Storm,none,none
Ramp Networks,Webramp 600i,,trancell
ReadyNet,WRT300N,admin,pz938qd6
RealTek,RT-3500,admin,admin
Repotec,RP-IP2014,admin,admin
Repotec,RP-IP2105,guest,guest
Repotec,RP-IP2401A,admin,admin
Repotec,RP-IP2404,admin,admin
Repotec,RP-IP2404A,admin,admin
Repotec,RP-IP3014,admin,admin
Repotec,RP-IP509,admin,admin
Repotec,RP-WR1440A,admin,admin
Retail Plus,Router Plus,blank,blank
Retail Plus,Router Plus,unknown,unknown
Riger,DB108-WL,tmadmin,tmadmin
Riger,DB120WL,tmadmin,password
Riger Corporation,DB102,tmadmin,tmadmin
Rogers,AC763S,none,swiadmin
Rosewill,RNX-EasyN4,admin,password
Rosewill,RNX-GX4,admin,guest
Rosewill,RNX-N300RT,admin,admin
Rosewill,T600N,admin,admin
Ruckus,2211-EXT,admin,password
SBS,BW5150,admin,admin
SMC,SMC1244TX,NONE,blank
SMC,SMC2404WBR,NONE,blank
SMC,SMC2804WBR,NONE,smcadmin
SMC,SMC2804WBR,NONE,smcadmin
SMC,SMC2804WBR,blank,smcadmin
SMC,SMC2804WBRP-G,NONE,smcadmin
SMC,SMC2804WBRP-G,none,smcadmin
SMC,SMC7004ABR,NONE,blank
SMC,SMC7004ABR,,blank
SMC,SMC7004ABR,none,blank
SMC,SMC7004AWBR,NONE,blank
SMC,SMC7004BR,NONE,admin
SMC,SMC7004BR,NONE,admin
SMC,SMC7004FW,NONE,blank
SMC,SMC7004VBR,NONE,smcadmin
SMC,SMC7004VBR,,blank
SMC,SMC7004VBR,blank,smcadmin
SMC,SMC7004VWBR,,admin
SMC,SMC7004WBR,NONE,admin
SMC,SMC7004WFW,NONE,blank
SMC,SMC7008ABR,NONE,blank
SMC,SMC7008ABR,,blank
SMC,SMC7008BR,NONE,admin
SMC,SMC7204BRA,smc,smcadmin
SMC,SMC7401BRA,root,root
SMC,SMC7401BRA,admin,barricade
SMC,SMC7401BRA,admin,barricade
SMC,SMC7804WBRB,NONE,smcadmin
SMC,SMC7901BRA-A2,blank,smcadmin
SMC,SMC7904BRA,,smcadmin
SMC,SMC7904WBRA-N,smcadmin,blank
SMC,SMC7904WBRA2,smcadmin,blank
SMC,SMC7904WBRAS-N2,admin,admin
SMC,SMC7908VoWBRB,,admin
SMC,SMC8014,none,smcadmin
SMC,SMC8014-CCR,admin,admin
SMC,SMC8014WG,cusadmin,password
SMC,SMC8014WG-SI,unknown,unknown
SMC,SMC8014WG-TWC,cusadmin,password
SMC,SMC8014WN,cusadmin,password
SMC,SMCBR14UP,,smcadmin
SMC,SMCD3G-CCR,cusadmin,highspeed
SMC,SMCD3GN,cusadmin,password
SMC,SMCD3GN2-RES,cusadmin,password
SMC,SMCD3GNV,admin,password
SMC,SMCG3G-CCR,cusadmin,highspeed
SMC,SMCWBR14-G,NONE,blank
SMC,SMCWBR14-G2,unknown,unknown
SMC,SMCWBR14-G2,unknown,unknown
SMC,SMCWBR14-G2,UNKNOWN,UNKNOWN
SMC,SMCWBR14-G2,UNKNOWN,UNKNOWN
SMC,SMCWBR14-GM,none,smcadmin
SMC,SMCWBR14-N,Admin,smcadmin
SMC,SMCWBR14S-N,,smcadmin
SMC,SMCWBR14S-N2,blank,smcadmin
SMC,SMCWBR14S-N3,admin,smcadmin
SMC,SMCWBR14S-N4,admin,smcadmin
SMC,SMCWBR14T-G,UNKNOWN,UNKNOWN
SMC,SMCWGBR14-N,Admin,smcadmin
SMC,SMCWHSG44G,admin,smcadmin
ST Labs,IRP-4P-1,blank,blank
Sabrent,NT-WRLRT,admin,admin
Safecom,SAMR-4110,admin,epicrouter
Safecom,SAMR-4114,admin,epicrouter
Safecom,SART2-4112,admin,admin
Safecom,SART2-4115,Admin,Admin
Safecom,SBRU-10100,admin,admin
Safecom,SWAMRU-54108,,admin
Safecom,SWART2-54125,admin,admin
Sagem,2804STC,unknown,unknown
Sagem,Fast 1500WG,NONE,blank
Sagem,Fast 1704,admin,admin
Sagem,Fast 2000,admin,admin
Sagem,Fast 2404,admin,admin
Sagem,Fast 2444,admin,admin
Sagem,Fast 2504,admin,sky
Sagem,Fast 2504 Sky,admin,sky
Sagem,Fast 2504n Sky,admin,sky
Sagem,FAST 2864,admin,admin
Sagem,FAST 3001,blank,blank
Sagem,Fast 3302,admin,admin
Sagem,Fast 3464,admin,admin
Sagem,Livebox 7359,admin,admin
Sagem,Livebox Fast 3202,admin,admin
Sagem,Livebox Fast 3202,admin,admin
Sagem,Livebox TP Fast 3202,admin,admin
Sagemcom,3764,admin,admin
Sagemcom,Fast 3284,admin,admin
Sagemcom,Fast 3304,menara,menara
Sagemcom,Fast 3686,admin,admin
Sagemcom,Fast 5350GV,admin,gvt12345
Sagemcom,Fast 5355,unknown,unknown
Sagemcom,Orange Livebox 3,unknown,unknown
Samsung,SCH-LC11,admin,admin
Samsung,SMT-67400-XEN,admin,admin
Samsung,SMT-G7400,admin,admin
Schmid,ZI.620.V400,root,root
Scientific Atlanta,WebSTAR DPR2320,admin,admin
Scientific Atlanta,WebSTAR EPC2434,unknown,unknown
Securifi,Almond,admin,admin
Seowonintech,SLC-120S07OG,admin,password
ShenZhen ICC Tech,ICR-4004A,,Admin
Shiro Corp,DSL805E,admin,admin
Shock,741A,admin,password
Siemens,4100,admin,admin
Siemens,4200,,admin
Siemens,c-010-i,unknown,unknown
Siemens,C2110,admin,admin
Siemens,CL-110,admin,admin
Siemens,E-010-I,admin,admin
Siemens,e-110,,admin
Siemens,Giga762SX,,admin
Siemens,Gigaset,blank,blank
Siemens,Gigaset 204A,admin,admin
Siemens,Gigaset SE105,blank,blank
Siemens,Gigaset SE361,UNKNOWN,UNKNOWN
Siemens,Gigaset SE505,blank,blank
Siemens,gigaset se515,blank,blank
Siemens,Gigaset SE551,blank,blank
Siemens,Gigaset SE555,blank,admin
Siemens,Gigaset SE560,admin,admin
Siemens,Gigaset SE565,admin,admin
Siemens,Gigaset SE567,unknown,unknown
Siemens,Gigaset SE567,admin,admin
Siemens,Gigaset SE572,none,admin
Siemens,Gigaset SE587,admin,admin
Siemens,Gigaset SX541,blank,blank
Siemens,Gigaset SX551,blank,blank
Siemens,Gigaset SX552,unknown,unknown
Siemens,Gigaset SX763,blank,blank
Siemens,SE260,user,user
Siemens,SL2-141,admin,admin
Siemens,SpeedStream 4200,,admin
Siemens,SpeedStream 4300,admin,admin
Siemens,SpeedStream 5200,,admin
Siemens,Speedstream 5450,admin,admin
Siemens,SpeedStream 6300,admin,admin
Siemens,Speedstream 6520,admin,admin
Siemens,SpeedStream SS2602,none,admin
Sierra Wireless,AC763S Rogers,none,swiadmin
Sierra Wireless,AirCard 802S,none,admin
Sierra Wireless,MC7710,admin,blank
Sierra Wireless,Overdrive Pro,none,admin
Sierra Wireless,SWAC802,none,admin
Simple Mobility,SM-36WR,unknown,unknown
Sitecom,300N X4,admin,admin
Sitecom,300N-XR,admin,admin
Sitecom,DC-200,blank,blank
Sitecom,DC-201,blank,blank
Sitecom,DC-202,admin,admin
Sitecom,DC-202,blank,blank
Sitecom,DC-202,blank,blank
Sitecom,DC-202,blank,blank
Sitecom,DC-202,admin,admin
Sitecom,DC-203,blank,blank
Sitecom,DC-207,admin,admin
Sitecom,DC-213,admin,password
Sitecom,DC-213,admin,admin
Sitecom,DC-214,admin,password
Sitecom,DC-214,admin,admin
Sitecom,DC-215,admin,password
Sitecom,DC-216,admin,password
Sitecom,DC-224,admin,admin
Sitecom,DC-227,admin,admin
Sitecom,Greyhound,none,printed on bottom of router
Sitecom,WL-017,blank,blank
Sitecom,WL-018,admin,admin
Sitecom,WL-025,blank,blank
Sitecom,WL-026,blank,admin
Sitecom,WL-106,blank,blank
Sitecom,WL-108,admin,password
Sitecom,WL-109,admin,password
Sitecom,WL-114,admin,admin
Sitecom,WL-114,admin,admin
Sitecom,WL-118,admim,admin
Sitecom,WL-122,blank,sitecom
Sitecom,WL-127,admin,admin
Sitecom,WL-127,admin,admin
Sitecom,WL-143,admin,admin
Sitecom,WL-153,admin,admin
Sitecom,WL-153-NL,admin,admin
Sitecom,WL-160,admin,admin
Sitecom,WL-173,admin,admin
Sitecom,WL-174,admin,admin
Sitecom,WL-176,admin,admin
Sitecom,WL-183,admin,admin
Sitecom,WL-303,admin,admin
Sitecom,WL-304,admin,admin
Sitecom,WL-306,admin,admin
Sitecom,WL-308,admin,admin
Sitecom,WL-309,admin,admin
Sitecom,WL-312,admin,admin
Sitecom,WL-312,admin,admin
Sitecom,WL-322,unknown,unknown
Sitecom,WL-342,admin,admin
Sitecom,WL-342,admin,admin
Sitecom,WL-347,admin,admin
Sitecom,WL-348,admin,admin
Sitecom,WL-350,admin,admin
Sitecom,WL-521,,blank
Sitecom,WL-607,admin,admin
Sitecom,WL527,admin,admin
Sitecom,WLR-4001,admin,admin
Sitecom,WLR-4100,admin,admin
Sitecom,WLR-5000,admin,printed on bottom of router
Sitecom,X4 N300,admin,admin
Sitel,DB120WL,admin,1234
SmartRG,SR350N Clear Access,admin,admin
SmoothWall,Express 3.0,admin,unknown
Soho,18-OB-WR85-FHEU,admin,1234
Soho,1A400+,admin,0
Soho,TEI402M,admin,admin
Soho,TEI402M,unknown,unknown
Soho,TEI6608,admin,admin
SohoSpeed,ATU-R140,Admin,Admin
Solwise,AR110,DSL,DSL
Solwise,SAR-600EW,admin,admin
Solwise,SAR130,DSL,DSL
Solwise,SAR715,admin,admin
Sonicwall,Pro 230,unknown,unknown
Sonicwall,SOHO 3,admin,password
Sonicwall,TZ-170,admin,password
Soniq,CWR150NS,admin,admin
Sorenson VRS,SR-200,admin,blank
SparkLAN,WX-6615M,blank,blank
Sparkcom,BR41,blank,blank
Sparkcom,R04AC,admin,epicrouter
SpeedUp,SU-8800MBR,none,admin
Speedcom,ART18CX,admin,epicrouter
Speedcom,ART514CX,admin,conexant
Sphairon,Turbolink AR860C1 A,Admin,Admin
Sphirewall,Open Edgewize,admin,admin
StarTech,BR4100DC,none,none
StarTech,BR4100DC,admin,1234
Starbridge,L-220,unknown,unknown
Starbridge,L-326,admin,admin
Starbridge,L-525,unknown,unknown
Starbridge,LYNX 320,admin,admin
Starbridge,Pyxis 210,admin,blank
Steren,COM 815,admin,admin
Sterlite,SAM300AX,admin,admin
SunRocket,AC-211,,admin
Surecom,AWR51A,admin,epicrouter
Surecom,EP-4704SX,surecom,surecom
Surecom,EP-4704SX-A,admin,epicrouter
Surecom,EP-4904SX,,admin
Surecom,EP-9410SX-g,Admin,Admin
Surecom,EP-9510AX,blank,admin
Surecom,EP-9610SX-g,admin,blank
Surecom,EP-9610SX-GP,admin,admin
Surecom,NE-4904SX,admin,admin
Sweex,Annex A,admin,epicrouter
Sweex,Annex B,admin,epicrouter
Sweex,CC300011,admin,epicrouter
Sweex,CC400020,admin,epicrouter
Sweex,LB000010,admin,1234
Sweex,LB000020,,blank
Sweex,LB000021,admin,1234
Sweex,LB000021,,1234
Sweex,LC000070,admin,admin
Sweex,LW050,sweex,mysweex
Sweex,LW050,sweex,mysweex
Sweex,LW055,sweex,mysweex
Sweex,LW150,sweex,mysweex
Sweex,MO200UK,sweex,mysweex
Sweex,MO251,sweex,mysweex
Sweex,RO001,admin,admin
Sweex,RO002,sweex,mysweex
Sweex,RO003,sweex,mysweex
Sweex,Wireless Annex A,admin,epicrouter
Sweex,Wireless Annex B,admin,epicrouter
Symantec,200R,admin,password
Symbol,WS-2000,admin,symbol
Synology,RT1900ac,created during initial setup,created during initial setup
Synology,RT2600ac,admin,blank
T-Com,Speedport W303V,unknown,unknown
T-Com,Speedport W502V,unknown,unknown
TDS,GT784WN,unknown,unknown
TOT,DB120,admin,tot
TOT,X8824M,admin,tot
TP-Link,AC1750,admin,admin
TP-Link,Archer C1200,admin,admin
TP-Link,Archer C1900,admin,admin
TP-Link,Archer C2,admin,admin
TP-Link,Archer C2600,admin,admin
TP-Link,Archer C3150,admin,admin
TP-Link,Archer C50,admin,admin
TP-Link,Archer C5400,admin,admin
TP-Link,Archer C59,admin,admin
TP-Link,Archer C7,admin,admin
TP-Link,Archer C7 v2,admin,admin
TP-Link,Archer C8,admin,admin
TP-Link,Archer C9,admin,admin
TP-Link,Archer D5,admin,admin
TP-Link,Talon AD7200,admin,admin
TP-Link,TD-854W,admin,ttnet
TP-Link,TD-8616,admin,admin
TP-Link,TD-8800,,admin
TP-Link,TD-8810,admin,admin
TP-Link,TD-8816,admin,admin
TP-Link,TD-8817,admin,admin
TP-Link,TD-8840,admin,admin
TP-Link,TD-8961ND,admin,admin
TP-Link,TD-W8151N,admin,admin
TP-Link,TD-W8901G,admin,admin
TP-Link,TD-W8901N,admin,admin
TP-Link,TD-W890iG,admin,admin
TP-Link,TD-W8910G,admin,admin
TP-Link,TD-W8920G,admin,admin
TP-Link,TD-W8950ND,admin,admin
TP-Link,TD-W8951ND,admin,admin
TP-Link,TD-W8960N,admin,admin
TP-Link,TD-W8960N,admin,admin
TP-Link,TD-W8960NB,admin,admin
TP-Link,TD-W8961N,admin,admin
TP-Link,TD-W8961NT,admin,admin
TP-Link,TD-W8970,admin,admin
TP-Link,TD-W8980,admin,admin
TP-Link,TD-W8980,admin,admin
TP-Link,TD-W9810G,admin,admin
TP-Link,TL-ER5120,admin,admin
TP-Link,TL-MR3220,admin,admin
TP-Link,TL-MR3240,admin,admin
TP-Link,TL-MR3420,admin,admin
TP-Link,TL-R402M,admin,admin
TP-Link,TL-R402M,admin,admin
TP-Link,TL-R460,admin,admin
TP-Link,TL-R460,admin,admin
TP-Link,TL-R470T Plus,admin,admin
TP-Link,TL-R600VPN,admin,admin
TP-Link,TL-WA7210N,admin,admin
TP-Link,TL-WDR4300,admin,admin
TP-Link,TL-WR1043N,admin,admin
TP-Link,TL-WR1043N,admin,admin
TP-Link,TL-WR1043ND,root,admin
TP-Link,TL-WR1043ND,admin,admin
TP-Link,TL-WR1043ND,admin,admin
TP-Link,TL-WR2543ND,admin,admin
TP-Link,TL-WR340G,admin,admin
TP-Link,TL-WR340G,admin,admin
TP-Link,TL-WR340GD,admin,admin
TP-Link,TL-WR541G,admin,admin
TP-Link,TL-WR541G,admin,admin
TP-Link,TL-WR541G,admin,admin
TP-Link,TL-WR542G,admin,admin
TP-Link,TL-WR542G,admin,admin
TP-Link,TL-WR542G,admin,admin
TP-Link,TL-WR641G,admin,admin
TP-Link,TL-WR642G,admin,admin
TP-Link,TL-WR642G,admin,admin
TP-Link,TL-WR720N,admin,admin
TP-Link,TL-WR740N,admin,admin
TP-Link,TL-WR740ND,admin,admin
TP-Link,TL-WR741N,admin,admin
TP-Link,TL-WR741ND,admin,admin
TP-Link,TL-WR743ND,admin,admin
TP-Link,TL-WR802N,admin,admin
TP-Link,TL-WR810N,admin,admin
TP-Link,TL-WR841N,admin,admin
TP-Link,TL-WR841ND,admin,admin
TP-Link,TL-WR842N,admin,admin
TP-Link,TL-WR842ND,admin,admin
TP-Link,TL-WR940N,admin,admin
TP-Link,TL-WR941ND,admin,admin
TP-Link,Touch P5,admin,admin
Tactio,ALTERA-04,admin,epicrouter
Tactio,Altera-04G,admin,admin
Techmade,TM-ART25GSU,admin,admin
Technicolor,7300b,unknown,unknown
Technicolor,DPC3939,admin,password
Technicolor,TC7200,admin,admin
Technicolor,TC7200-U,admin,admin
Technicolor,TC7210.dNZ,blank,admin
Technicolor,TC7230,admin,admin
Technicolor,TC8305C,admin,password
Technicolor,TD5130,admin,admin
Technicolor,TD5136v2,admin,admin
Technicolor,TG582n,admin,SerialNumber
Technicolor,TG582n-O2,Administrator,blank
Technicolor,TG587n,admin,admin
Technicolor,TG587n,admin,admin
Technicolor,TG589vn,admin,admin
Technicolor,TG784n,Administrator,blank or the access key printed on label
Technicolor,TG788vn,unknown,unknown
Technicolor,TG788vn,Administrator,none
Technicolor,TG789vn,admin,blank
Technicolor,TG799vn,admin,password
Technicolor,TG852n,admin,1234
Tecom,AH2322W,unknown,unknown
Tecom,AH4021,user,user
Tecom,AH4222,admin,admin
Tecom,AR1021,root,root
Tecom,AR1031,admin,admin
Tecom,AW4062,1234,1234
Tecom,WL5041,unknown,unknown
TekComm,ADSL2 2,,Admin
Telekom,TSinus 130,,admin
Telenet,TNDSL 2120,unknown,unknown
Telewell,TW-EA1000,admin,admin
Telewell,TW-EA310,admin,admin
Telewell,TW-EA310,admin,admin
Telewell,TW-EA500,admin,password
Telewell,TW-EA501,admin,admin
Telewell,TW-EA510,admin,admin
Telewell,TW-EA510,admin,admin
Telewell,TW-EA510v3-b,admin,admin
Telewell,TW-EA511,admin,admin
Telewell,TW-EQ501,admin,admin
Telindus,1124,admin,admin
Telindus,1131,admin,admin
Telio,SPA2100,blank,blank
Telkom,5100DSL,,admin
Telkom,ADSL 5102G,admin,admin
Telkom,Mega 100WR,admin,admin
Telkom,Mega 105WR,admin,password
Telkom,Mega 200VWR,admin,admin
Telkom,MPC850,root,root
Telmex,Infinitum EchoLife HG520b,unknown,unknown
Telrad,CPE7000,unknown,unknown
Telrad,WLTCS-106,unknown,unknown
Telsec,TS-9000,admin,admin
Telsey,CPVA202+,admin,admin
Telsey,WAU11n,admin,admin
Telstra,AC753S,none,admin_Ultimate
Telstra,Ultimate AC753S,none,admin_Ultimate
Teltonika,RUT500,admin,admin01
Teltonika,RUT950,admin,admin
Telus,V1000H,admin,telus
Tenda,11N,,NULL
Tenda,D301,admin,admin
Tenda,D840R,admin,admin
Tenda,FH303,admin,admin
Tenda,R360,none,admin
Tenda,W150D,admin,admin
Tenda,W300D,admin,admin
Tenda,W302R,admin,admin
Tenda,W303R,admin,admin
Tenda,W306R,admin,admin
Tenda,W308R,unknown,unknown
Tenda,W311R+,admin,admin
Tenda,W541R,admin,admin
Tenda,WBR-T3,admin,admin
Tendia,TWL54C,admin,admin
Teracom,T1-B-DSL699E9.4U6 5,admin,admin
Teracom,TAD 100,admin,admin
Thomson,DCW725,blank,admin
Thomson,DWG855,blank,admin
Thomson,DWG855TLG,blank,admin
Thomson,DWG875,none,admin
Thomson,TCW770,none,password
Thomson,TCW7704,none,admin
Thomson Alcatel,3881,blank,blank
Thomson Alcatel,ACG905,blank,admin
Thomson Alcatel,DCW725,blank,admin
Thomson Alcatel,DWG855T,none,admin
Thomson Alcatel,SpeedTouch 510,blank,blank
Thomson Alcatel,SpeedTouch 510,blank,blank
Thomson Alcatel,SpeedTouch 510,blank,blank
Thomson Alcatel,Speedtouch 510,admin,admin
Thomson Alcatel,Speedtouch 510,admin,admin
Thomson Alcatel,Speedtouch 510,admin,admin
Thomson Alcatel,SpeedTouch 510i,unknown,unknown
Thomson Alcatel,SpeedTouch 511,,blank
Thomson Alcatel,SpeedTouch 516,,blank
Thomson Alcatel,SpeedTouch 516,admin,admin
Thomson Alcatel,SpeedTouch 516i,admin,admin
Thomson Alcatel,SpeedTouch 530,blank,blank
Thomson Alcatel,Speedtouch 530,admin,admin
Thomson Alcatel,SpeedTouch 536,blank,blank
Thomson Alcatel,SpeedTouch 536,admin,admin
Thomson Alcatel,SpeedTouch 536,blank,blank
Thomson Alcatel,SpeedTouch 540,blank,blank
Thomson Alcatel,SpeedTouch 545,blank,blank
Thomson Alcatel,SpeedTouch 546,blank,blank
Thomson Alcatel,Speedtouch 546,admin,admin
Thomson Alcatel,SpeedTouch 546,blank,blank
Thomson Alcatel,SpeedTouch 570,blank,blank
Thomson Alcatel,SpeedTouch 570,blank,blank
Thomson Alcatel,SpeedTouch 570,blank,blank
Thomson Alcatel,SpeedTouch 576,blank,blank
Thomson Alcatel,SpeedTouch 580,,blank
Thomson Alcatel,SpeedTouch 585,Administrator,blank
Thomson Alcatel,SpeedTouch 585i,Administrator,blank
Thomson Alcatel,Speedtouch 608,blank,blank
Thomson Alcatel,SpeedTouch 625,Administrator,blank
Thomson Alcatel,SpeedTouch 716WL,blank,blank
Thomson Alcatel,Speedtouch 780,admin,admin
Thomson Alcatel,SpeedTouch Firewall,blank,blank
Thomson Alcatel,ST536,blank,blank
Thomson Alcatel,ST546,blank,blank
Thomson Alcatel,ST585,blank,blank
Thomson Alcatel,ST585,blank,blank
Thomson Alcatel,ST5x6,blank,blank
Thomson Alcatel,ST780,blank,blank
Thomson Alcatel,TCW690,blank,admin
Thomson Alcatel,TCW710,blank,admin
Thomson Alcatel,TCW750-4,none,admin
Thomson Alcatel,TG508,none,none
Thomson Alcatel,TG580,none,none
Thomson Alcatel,TG582n-O2,Administrator,blank
Thomson Alcatel,TG585,Administrator,blank
Thomson Alcatel,TG585,Administrator,Administrator
Thomson Alcatel,TG585,Administrator,blank
Thomson Alcatel,TG585n,Administrator,blank
Thomson Alcatel,TG585n,Administrator,blank
Thomson Alcatel,TG587n,Administrator,blank
Thomson Alcatel,TG712,Administrator,blank
Thomson Alcatel,TG782,unknown,unknown
Thomson Alcatel,TG782T,unknown,unknown
Thomson Alcatel,TG784,unknown,unknown
Thomson Alcatel,TG784,none,none
Thomson Alcatel,TG787,unknown,unknown
Thomson Alcatel,TG789vn,unknown,unknown
Thomson Alcatel,TG797,Administrator,blank
Thomson Alcatel,TWG-870,none,admin
Thomson Alcatel,TWG-870U,none,admin
Thomson Alcatel,TWG850,blank,admin
Tilgin,Vood 322,unknown,unknown
Tilgin,Vood 422,unknown,unknown
Tilgin,Vood 452w,Conf,admin
Tilgin,Vood 452W,Conf,admin
Top Global,MB6000,public,public
Topcom,BR 104,admin,
Topcom,BR 204,admin,blank
Topcom,BR 604,admin,admin
Topcom,WBR 244,admin,admin
Topcom,WBR 254,admin,admin
Topcom,WBR 254G,admin,admin
Topcom,WBR 354G,admin,admin
Topcom,WBR 611,admin,admin
Topcom,WBR 654,admin,admin
Topcom,WBR 7001g,admin,admin
Topcom,webracer 1104,,blank
Topcom,Webracer 880,admin,admin
Topcom,WL-108,admin,admin
Topcom,Xplorer 870+,admin,12345678
Topcom,Xplorer 871 BT,unknown,unknown
Tornado,242,NONE,admin
Tornado,2441,admin,admin
Tornado,840,NONE,admin
Toshiba,WRC-1000,admin,password
Totolink,N100RE,admin,admin
Totolink,N151RA,admin,admin
Trellis,BSMART,admin,admin
TrendChip,HG520,admin,admin
TrendChip,TC3085,admin,admin
TrendChip,TW263R4-A1,admin,1234
Trendnet,GS8100,admin,admin
Trendnet,TDM-C400,admin,admin
Trendnet,TEW-211BRP,admin,1234
Trendnet,TEW-231BRP,blank,blank
Trendnet,TEW-311BRP,admin,admin
Trendnet,TEW-411BRP+,blank,admin
Trendnet,TEW-431BRP,blank,blank
Trendnet,TEW-432BRP,admin,admin
Trendnet,TEW-432BRP,admin,admin
Trendnet,TEW-432BRP,admin,admin
Trendnet,TEW-432BRP,admin,admin
Trendnet,TEW-435BRM,admin,password
Trendnet,TEW-435BRM,blank,blank
Trendnet,TEW-435BRM,blank,blank
Trendnet,TEW-435BRM,admin,password
Trendnet,TEW-436BRM,admin,admin
Trendnet,TEW-452BRP,admin,admin
Trendnet,TEW-452BRP,admin,admin
Trendnet,TEW-452BRP,admin,admin
Trendnet,TEW-511BRP,blank,admin
Trendnet,TEW-611BRP,admin,unknown
Trendnet,TEW-631BRP,Admin,none
Trendnet,TEW-631BRP,Admin,none
Trendnet,TEW-631BRP,Admin,none
Trendnet,TEW-632BRP,admin,admin
Trendnet,TEW-632BRP,admin,admin
Trendnet,TEW-633GR,Admin,unknown
Trendnet,TEW-634GRU,admin,admin
Trendnet,TEW-635BRM,admin,password
Trendnet,TEW-635BRM,admin,password
Trendnet,TEW-639GR,admin,password
Trendnet,TEW-651BR,admin,admin
Trendnet,TEW-651BR,admin,admin
Trendnet,TEW-652BRP,admin,admin
Trendnet,TEW-652BRP,admin,admin
Trendnet,TEW-654TR,admin,admin
Trendnet,TEW-657BRM,admin,password
Trendnet,TEW-658BRM,admin,admin
Trendnet,TEW-671BR,admin,admin
Trendnet,TEW-672GR,admin,none
Trendnet,TEW-673GRU,admin,admin
Trendnet,TEW-691GR,admin,none
Trendnet,TEW-692GR,admin,admin
Trendnet,TEW-731BR,admin,admin
Trendnet,TEW-811DRU,,
Trendnet,TEW-812DRU,admin,admin
Trendnet,TEW-812DRU,admin,admin
Trendnet,TEW-818DRU,printed on bottom of router,printed on bottom of router
Trendnet,TEW-823DRU,admin,printed on bottom of router
Trendnet,TEW-827DRU,admin,printed on bottom of router
Trendnet,TEW-828DRU,printed on router,printed on router
Trendnet,TPL-111BR,admin,admin
Trendnet,TVP-224HR,admin,123
Trendnet,TW100-BRF1141,blank,blank
Trendnet,TW100-BRF114U,blank,blank
Trendnet,TW100-BRM504,blank,blank
Trendnet,TW100-BRV204,blank,blank
Trendnet,TW100-BRV204,blank,blank
Trendnet,TW100-BRV304,blank,blank
Trendnet,TW100-S4W1CA,blank,blank
Trendnet,TW100-S4W1CA,admin,blank
Trendnet,TW100-S4W1CA,admin,blank
Trendnet,TW100-S4W1CA,blank,blank
Trendnet,TWG-BRF114,blank,blank
Trust,340 SpeedShare,unknown,unknown
Trust,GB-445A,admin,epicrouter
Trust,MD-4050,unknown,unknown
Trust,Speedshare Turbo Pro,admin,admin
Twister,RT-710,blank,admin
US Robotics,SureConnect 9003,root,12345
US Robotics,SureConnect 9106,admin,admin
US Robotics,SureConnect 9107,admin,admin
US Robotics,SureConnect 9108,admin,admin
US Robotics,USR5461,blank,blank
US Robotics,USR5462,admin,admin
US Robotics,USR5463,blank,blank
US Robotics,USR5464,blank,blank
US Robotics,USR5465,none,admin
US Robotics,USR8000,NONE,admin
US Robotics,USR8000A,NONE,blank
US Robotics,USR8000A,NONE,blank
US Robotics,USR8000A,NONE,blank
US Robotics,USR8001,NONE,blank
US Robotics,USR8003,NONE,blank
US Robotics,USR8004,NONE,blank
US Robotics,USR8011,NONE,blank
US Robotics,USR8022,NONE,blank
US Robotics,USR8054,NONE,blank
US Robotics,USR819112,admin,none
US Robotics,USR8550,blank,12345
US Robotics,USR9107,admin,admin
US Robotics,USR9110,admin,1234
US Robotics,USR9112,admin,1234
US Robotics,USR9114,admin,admin
US Robotics,xx5462,admin,admin
UStec,TP-IPR8,blank,blank
UTStarcom,AR7RD,,utstar
UTStarcom,UT-300R,root,root
UTStarcom,UT-300R2,admin,utstar
UTStarcom,UT-300R2,admin,admin
UTStarcom,UT-300R2U,admin,admin
UTStarcom,UT4110A,admin,admin
UTStarcom,WA3002-g1,admin,admin
UTStarcom,WA3002-G4,admin,admin
UTStarcom,WA3002-G4,admin,admin
Ubee,Ambit U10C022,user,user
Ubee,Ambit U10C037,user,user
Ubee,DDW 336,user,user
Ubee,DDW 3610,user,user
Ubee,DDW 3611,user,user
Ubee,DDW 365,user,user
Ubee,DDW 366,user,user
Ubee,DDW 36C,admin,on router label
Ubee,DVW 3102B,user,user
Ubee,DVW 3201B,user,user
Ubee,DVW 326,user,admin
Ubee,DVW 326B,user,user
Ubee,DVW 32C,unknown,unknown
Ubee,DVW 32C1,admin,printed on router
Ubee,DVW 32CB,admin,on label under heading of GUI password
Ubee,EVW 3226 upc,admin,admin
Ubee,EWV 3200,unknown,unknown
Ubiquiti,AirOS,blank,blank
Ubiquiti,AirOS AirGrid M5HP,blank,blank
Ubiquiti,NanoStation M5,blank,blank
Umax,SWC-9200,user,user
Unex,IS050E,none,administrator
Unex,IS050S,blank,blank
Uniden,ENR1504,UNIDEN,blank
Uniden,WNR2004,UNIDEN,blank
Unihero,VT-AD02,unknown,unknown
V-Link,VLR-1505n,admin,gvt12345
Verizon,Fivespot,admin,admin
Verizon,Jetpack MiFi 6620L,NONE,admin
Viking II,AR520,root,root
Virata,DSL906EU WebCom,UNKNOWN,UNKNOWN
Virgin Media,Hub 3.0,NONE,found on router sticker
Virgin Media,Super Hub 2,found on label,found on label
Virgin Media,Super Hub 2ac,NONE,on router label
VisionNet,200ES-RADSL,admin,visionnet
VisionNet,M404,enduser,password
VisionNet,M504,unknown,unknown
VisionNet,M505N,enduser,password
Vizio,XWR100,unknown,unknown
Vodafone,ARV4519PW,vodafone,vodafone
Vodafone,Box,vodafone,vodafone
Vodafone,R216,none,admin
Vonage,VDV21-VD,router,router
Vonage,VDV23,admin,admin
Vonage,VWR,user,user
Vood,322,,Admin
Vood,453W,unknown,unknown
Vtech,ip8100,VTech,VTech
W-linx,MB-400XP,blank,admin
W-linx,MB400-X2,blank,blank
Wayjet,WT-3525,,conexant
Web Excel,adsl2-2,admin,admin
Web Excel,PT3812,admin,epicrouter
Westell,6100,admin,password
Westell,A90-220015-04,UNKNOWN,UNKNOWN
Westell,A90-327W15-06,admin,admin
Westell,A90-750014-07,admin,unknown
Westell,A90-750015-07,admin,password
Westell,A90-750018-07,admin,password
Westell,A90-750020-07,admin ,password
Westell,A90-750022-07,admin,password
Westell,A90-750045-07,admin,password
Westell,A90-9100EM15-10,admin,password
Westell,B90-220030-04,NOLOGIN,NOLOGIN
Westell,B90-327W15-06,admin,admin
Westell,b90-740010-07,admin,password
Westell,C90-327W30-06,admin,admin
Westell,C90-610015-06,admin,admin
Westell,C90-610030-06,admin,admin
Westell,D90-327W14-06,admin,admin
Westell,D90-327W15-06,admin,admin
Westell,D90-740010-06,admin,password
Westell,E90-610014-06,admin,admin
Westell,E90-610015-06,admin,admin
Westell,E90-610030-06,admin,admin
Westell,G90-610060-20,unknown,unknown
Westell,Versalink 327W,admin,admin
Westell,Versalink 327W,admin,admin
Westell,Wirespeed 2100,NOLOGIN,NOLOGIN
Westell,Wirespeed 2200,UNKNOWN,UNKNOWN
Westell,Wirespeed 2400,NOLOGIN,NOLOGIN
Westell,Wirespeed 2410,NOLOGIN,NOLOGIN
Westell,Wirespeed 36R570,NOLOGIN,NOLOGIN
Western Digital,MyNet N750,admin,password
Western Digital,N900,admin,password
WiFiRanger,Elite,unknown,unknown
WiFiRanger,Go2v6,unknown,unknown
WiFiRanger,Marine 2,unknown,unknown
WiFiRanger,Sky,unknown,unknown
Wise,WR-5004,admin,admin
Wisenet,WR-6004+,none,none
Witpack,4P,witpack,witpack
X-Micro,wlan 11g,admin,admin
X-Micro,Wlan 802.11,UNKNOWN,UNKNOWN
X-Micro,XWL-11GUZX,admin,1234
X-linx,MB-100S,blank,blank
Xavi,7868r,1234,1234
Xavi,7968,admin,Xavi
Xavi,8021R,admin,admin
Xavi,8124r,admin,admin
Xavi,X5258-P2,Admin,Admin
Xavi,X7721r+,admin,admin
Xavi,X7822r,unknown,unknown
Xavi,x7868r+,root,root
Xavi,x8121,admin,admin
Xavi,x8122R,admin,admin
Xavi,X8222r,unknown,unknown
Xavi,x825,Admin,Admin
Xavi,X8821r+,admin,admin
Xavi,x9368n,user,user
Xincom,502,admin,blank
Xperio Labs,XL-8121W12,unknown,unknown
Xterasys,XR-1105+,blank,blank
Xtremeit,10242,guest,guest
ZIO,WLB5254AIP,unknown,unknown
ZTE,AC30,admin,admin
ZTE,AR550,admin,admin
ZTE,Bavo ZXV10-W300,admin,admin
ZTE,F620,admin,admin
ZTE,F660,admin,admin
ZTE,H220N,HPN,blank
ZTE,MF286,admin,admin
ZTE,MF28B,none,none
ZTE,MF29A,none,admin
ZTE,MF612,admin,admin
ZTE,MF65,none,smartbro
ZTE,MF65M,none,admin
ZTE,MF910V,admin,admin
ZTE,MF923,none,attadmin
ZTE,MF93D,admin,admin
ZTE,NetFasteR WLAN,admin,admin
ZTE,Unite US,unknown,unknown
ZTE,Z-917,none,admin
ZTE,Z288L,admin,printed on router
ZTE,Z700A,none,attadmin
ZTE,ZHXN-H108NS,admin,admin
ZTE,ZXDSL 531B,admin,admin
ZTE,ZXDSL 831,ZXDSL,ZXDSL
ZTE,ZXDSL 831,ZXDSL,ZXDSL
ZTE,ZXDSL 831,ZXDSL,ZXDSL
ZTE,ZXDSL 831,admin,admin
ZTE,ZXDSL 831,admin,admin
ZTE,ZXDSL 831CII,admin,admin
ZTE,ZXDSL 831D,ZXDSL,ZXDSL
ZTE,ZXDSL 931VII,admin,admin
ZTE,ZXHN F620,admin,admin
ZTE,ZXHN H108N,admin,admin
ZTE,ZXHN H208N,admin,admin
ZTE,ZXHN H208N,cytauser,cytauser
ZTE,ZXHN H267N,admin,admin
ZTE,ZXHN H298N,user,user
ZTE,ZXV10 H201L,admin,admin
ZTE,ZXV10 H208L,admin,admin
ZTE,ZXV10 W300,admin,admin
ZTE,ZXV10 W300,on,on
ZTE,ZXV10 W300,on,on
ZTE,ZXV10 W300,admin,admin
ZTE,ZXV10 W300,admin,admin
Zero One Tech,AF420B,UNKNOWN,UNKNOWN
Zhone,1511-A1,admin,admin
Zhone,1518-A1,admin,admin
Zhone,1518-A1,admin,admin
Zhone,1518-A1,admin,admin
Zhone,6211-I3,admin,admin
Zhone,6218-12-200-0TT,admin,admin
Zhone,6219-x1,admin,admin
Zhone,6219-X1-NA-0CC,admin,cciadmin
Zhone,6381-A4-200-1PR,Admin,Admin
Zhone,6518-A1,admin,admin
Zhone,6519-A2,admin,admin
Zhone,6519-A2,admin,admin
Zhone,6519-A2,admin,admin
Zhone,6718-W1,admin,admin
Zhone,6718-W1-EUB,admin,admin
Zhone,6748-W1,admin,admin
Zhone,ZNID-GPON-2426-UK,admin,zhone
Zioncom,IP0143,unknown,unknown
Zioncom,iP0143-B,admin,admin
Zioncom,IP0803,admin,admin
Zmodo, H9104V, admin,111111
Zmodo, H9104V, admin,888888
Zmodo, H9108V, admin,111111
Zmodo, H9108V, admin,888888
Zmodo, ZMD-DD-SBN4, admin,111111
Zmodo, ZMD-DD-SBN4, admin,888888
Zmodo, ZMD-DD-SBN6, admin,111111
Zmodo, ZMD-DD-SBN6, admin,888888
Zmodo, ZMD-DD-SBN8, admin,111111
Zmodo, ZMD-DD-SBN8, admin,888888
Zmodo, H8104UV, admin,666666
Zmodo, H8106UV, admin,666666
Zmodo, H8108UV, admin,666666
Zmodo, H8114UV, admin,666666
Zmodo, H8116UV, admin,666666
Zmodo, H8118UV, admin,666666
Zmodo, ZMD-DT-SFN6, admin,
Zmodo, ZMD-DT-SFN6, admin,111111
Zmodo, ZMD-DT-SFN6, admin,
Zmodo, ZMD-DT-SCN4, admin,111111
Zmodo, ZMD-DT-SCN4, admin,
Zmodo, ZMD-DT-SCN8, admin,111111
Zmodo, ZMD-DT-SCN8, admin,
Zmodo, ZMD-DH-SEN6, admin,111111
Zmodo, ZMD-DH-SEN6, admin,
Zmodo, ZMD-NV-SBN4, admin,111111
Zmodo, ZH-NA04-W, admin,111111
Zmodo, ZP-NC14-P, admin,111111
Zonet,ZSR0104B,admin,0
Zonet,ZSR0104CP,admin,admin
Zonet,ZSR0104CP,admin,admin
Zonet,ZSR1124WE,guest,guest
Zonet,ZSR4154WE,admin,admin
Zoom,4402,admin,admin
Zoom,4501,,admin
Zoom,5350,admin,admin
Zoom,5352,admin,admin
Zoom,5354,admin,admin
Zoom,5363,admin,admin
Zoom,5551 ADSL,admin,zoomadsl
Zoom,5554 ADSL,admin,zoomadsl
Zoom,5560,admin,zoomadsl
Zoom,5560 ADSL,admin,zoomadsl
Zoom,5654,admin,zoomadsl
Zoom,5660,admin,zoomadsl
Zoom,Adsl X6 5590,admin,zoomadsl
Zoom,X4 5551,admin,zoomadsl
Zoom,X5,admin,zoomadsl
Zoom,X5,admin,zoomadsl
Zoom,X5 5654A,admin,zoomadsl
Zoom,X5 5654B,admin,zoomadsl
Zoom,X6,admin,zoomadsl
Zoom,X6 5990,admin,zoomadsl
ZyXEL,660H-61,,1234
ZyXEL,AMG1202-T10A,none,1234
ZyXEL,C1000Z,admin,on router sticker
ZyXEL,C1100Z,printed on bottom of router,printed on bottom of router
ZyXEL,EQ-660R,admin,1234
ZyXEL,HS-100W,admin,admin
ZyXEL,IAD-P2602,blank,admin
ZyXEL,NBG-334W,none,1234
ZyXEL,NBG-415N,admin,1234
ZyXEL,NBG-416N,admin,1234
ZyXEL,NBG-418N,admin,1234
ZyXEL,NBG-419N,none,1234
ZyXEL,NBG-4604,admin,1234
ZyXEL,P 2601HN,blank,1234
ZyXEL,P 2602H,blank,1234
ZyXEL,P 2602HW,blank,1234
ZyXEL,P 2602HW,blank,1234
ZyXEL,P 2602HWT,admin,blank
ZyXEL,P 2602R,blank,1234
ZyXEL,P 2812HNU,admin,1234
ZyXEL,P 320W,none,1234
ZyXEL,P 324,NONE,1234
ZyXEL,P 330w,admin,1234
ZyXEL,P 330W EE,admin,1234
ZyXEL,P 334WT,none,1234
ZyXEL,P 335WT,,blank
ZyXEL,P 336M,admin,1234
ZyXEL,P 660 D1 RoHS,1234,1234
ZyXEL,P 660 RT 1 v3s,admin,1234
ZyXEL,P 660H T1,admin,admin
ZyXEL,P 660H T3,1234,1234
ZyXEL,P 660HN F1Z,,1234
ZyXEL,P 660HN T1A,,1234
ZyXEL,P 660HW D1,none,1234
ZyXEL,P 660HW D1,none,1234
ZyXEL,P 660HW T1,none,admin
ZyXEL,P 660HW T1,none,admin
ZyXEL,P 660HW T1,none,admin
ZyXEL,P 660HW T3,1234,1234
ZyXEL,P 660R D1,1234,1234
ZyXEL,P 660R D1,,1234
ZyXEL,P 660R ELNK,admin,1234
ZyXEL,P 660R F1,,1234
ZyXEL,P 660R T1,none,admin
ZyXEL,P 660R T1,admin,1234
ZyXEL,P 660RT2,none,1234
ZyXEL,P 660RU T1,admin,1234
ZyXEL,P 661H D1,admin,admin
ZyXEL,P 661HNU F1,admin,1234
ZyXEL,P 661HW D1,user,1234
ZyXEL,P 662H D1,,1234
ZyXEL,P 870HN 51b,admin,1234
ZyXEL,PK5000Z,none,none
ZyXEL,PK5000Z,blank,blank
ZyXEL,PK5001Z,admin,unknown
ZyXEL,Prestige 2302R,,unknown
ZyXEL,Prestige 2602H 61,NONE,admin
ZyXEL,Prestige 2602H 61C,NONE,admin
ZyXEL,Prestige 2602H 61C,NONE,1234
ZyXEL,Prestige 2602HW 61,blank,admin
ZyXEL,Prestige 2602HWL 61,blank,admin
ZyXEL,Prestige 334,NONE,1234
ZyXEL,Prestige 600,admin,1234
ZyXEL,Prestige 600HW T1,admin,1234
ZyXEL,Prestige 623,admin,1234
ZyXEL,Prestige 623 41,admin,1234
ZyXEL,Prestige 623ME,admin,1234
ZyXEL,Prestige 623R A1,admin,1234
ZyXEL,Prestige 623R T1,admin,1234
ZyXEL,Prestige 645,Admin,1234
ZyXEL,Prestige 645R A1,admin,1234
ZyXEL,Prestige 645R A2,admin,1234
ZyXEL,Prestige 650,admin,1234
ZyXEL,Prestige 650H,admin,1234
ZyXEL,Prestige 650R,admin,1234
ZyXEL,Prestige 650R 31,admin,1234
ZyXEL,Prestige 650R 33,admin,1234
ZyXEL,Prestige 650R E1,admin,1234
ZyXEL,Prestige 652,admin,1234
ZyXEL,Prestige 652H 33,,1234
ZyXEL,Prestige 653HWI,admin,1234
ZyXEL,Prestige 660HW 61,unknown,unknown
ZyXEL,Prestige 660HW T1,admin,admin
ZyXEL,Prestige 660HW T3,admin,1234
ZyXEL,Prestige 660HW T3,admin,1234
ZyXEL,Prestige 660HW61,admin,1234
ZyXEL,Prestige 660HW67,admin,1234
ZyXEL,Prestige 660ME61,admin,1234
ZyXEL,Prestige 660R 61,,1234
ZyXEL,Prestige 660R 61C,,1234
ZyXEL,Prestige 660R 63 67C,,1234
ZyXEL,Prestige 660R T1,,1234
ZyXEL,Prestige 660RU T1,,1234
ZyXEL,Prestige 660RU T3,admin,admin
ZyXEL,Prestige 792H,admin,1234
ZyXEL,Prestige 960,webadmin,1234
ZyXEL,Prestige 964,webadmin,1234
ZyXEL,Q1000Z,blank,blank
ZyXEL,RP314,admin,1234
ZyXEL,SP 660,none,1234
ZyXEL,VFG6005N,admin,1234
ZyXEL,VMG3926 B10A,admin,1234
ZyXEL,VMG8324 B10A,admin,password
ZyXEL,VMG8324 B10A,admin,1234
ZyXEL,VMG8924 B10A,admin,password
ZyXEL,X 550,admin,1234
ZyXEL,X550N,,1234
ZyXEL,X650,admin,1234
ZyXEL,ZyAIR B 2000,NONE,1234
ZyXEL,ZyAIR B 2000,NONE,1234
ZyXEL,ZyAIR G 2000,NONE,1234
ZyXEL,ZyAIR G 2000 Plus,NONE,1234
ZyXEL,ZyWall 1,NONE,1234
ZyXEL,ZyWall 10,NONE,1234
ZyXEL,ZyWall 100,NONE,1234
ZyXEL,ZyWALL 2,,1234
ZyXEL,ZyWall 2WE,NONE,1234
ZyXEL,ZyWALL 35,admin,1234
ZyXEL,Zywall 70,NONE,1234
ZyXEL,ZyWALL Z 70 UTM,NONE,1234
bRoad Lanner,BRL-04FXP,blank,0
bebo,700,admin,epicrouter
eHome,EH100,admin,blank
iBall,iB-LR6111A,admin,admin
iBall,iB-WRB150N,admin,admin
ice.net,D-35,admin,admin
ice.net,R-90,admin,admin
iiNet,BoB,,admin
iiNet,BoB Lite,,admin
iiNet,BoB2,,admin
neufbox,NB4-SER-r0,unknown,unknown
pcWRT,TORONTO-N,none,pcwrt
vividwireless,DX-230,unknown,unknown
vividwireless,WIXFMR-107,admin,admin123
2Wire Inc.,Wireless Routers,http,<blank>
2Wire,WiFi routers,<blank>,Wireless
360 Systems,Image Server 2000,factory,factory
3COM,,adm,<blank>
3COM,,admin,synnet
3COM,,manager,manager
3COM,,monitor,monitor
3COM,,read,synnet
3COM,,security,security
3COM,,write,synnet
3COM,,root,letmein
3COM,11g Cable/DSL Gateway,<blank>,<blank>
3COM,3C16405,admin,<blank>
3COM,3C16406,admin,<blank>
3COM,3C16450,admin,<blank>
3COM,3CRADSL72,<blank>,1234admin
3COM,3CRWE52196,<blank>,admin
3COM,3Com SuperStack 3 Switch 3300XM,security,security
3COM,3Com SuperStack 3,security,security
3COM,3c16405,Administrator,<blank>
3COM,AccessBuilder,SNMPWrite,private
3COM,AirConnect AP,<blank>,comcomcom
3COM,AirConnect Access,<blank>,<blank>
3COM,CB9000/4007,FORCE,<blank>
3COM,CellPlex,admin,synnet
3COM,CellPlex,<blank>,<blank>
3COM,CellPlex,admin,<blank>
3COM,CellPlex,admin,admin
3COM,CellPlex,root,<blank>
3COM,CellPlex,tech,<blank>
3COM,CellPlex,tech,tech
3COM,CoreBuilder,operator,admin
3COM,CoreBuilder,SNMPWrite,private
3COM,CoreBuilder,<blank>,<blank>
3COM,CoreBuilder,<blank>,admin
3COM,CoreBuilder,debug,synnet
3COM,CoreBuilder,tech,tech
3COM,HiPerACT,admin,<blank>
3COM,HiPerARC,adm,<blank>
3COM,HiPerARC,adm,<blank>
3COM,Internet Firewall,admin,password
3COM,LANplex,debug,synnet
3COM,LANplex,tech,<blank>
3COM,LANplex,tech,tech
3COM,LinkBuilder,tech,tech
3COM,LinkSwitch,tech,tech
3COM,NetBuilder,<blank>,admin
3COM,NetBuilder,admin,<blank>
3COM,NetBuilder,<blank>,ANYCOM
3COM,NetBuilder,<blank>,ANYCOM
3COM,NetBuilder,<blank>,ILMI
3COM,NetBuilder,<blank>,ILMI
3COM,Netbuilder,Root,<blank>
3COM,Netbuilder,admin,<blank>
3COM,OCR-812,root,!root
3COM,OfficeConnect 812 ADSL,Administrator,admin
3COM,OfficeConnect 812 ADSL,adminttd,adminttd
3COM,OfficeConnect 812 ADSL,admin,<blank>
3COM,OfficeConnect ADSL Wireless 11g Firewall Router,<blank>,admin
3COM,OfficeConnect ADSL,<blank>,admin
3COM,OfficeConnect ISDN Routers,<blank>,PASSWORD
3COM,OfficeConnect Remote Router,root,!root
3COM,OfficeConnect Wireless AP,<blank>,admin
3COM,OfficeConnect Wireless,<blank>,admin
3COM,OfficeConnect,root,!root
3COM,Router,<blank>,<blank>
3COM,SS III Switch,recovery,recovery
3COM,SuperStack 3 Switch,recover,recover
3COM,SuperStack 3,manager,manager
3COM,SuperStack 3,admin,<blank>
3COM,SuperStack 3,monitor,monitor
3COM,SuperStack II Switch,3comcso,RIP000
3COM,SuperStack II Switch,admin,<blank>
3COM,SuperStack II Switch,manager,manager
3COM,SuperStack II Switch,monitor,monitor
3COM,SuperStack II Switch,security,security
3COM,SuperStack II Switch,security,security
3COM,SuperStack II Switch,debug,synnet
3COM,SuperStack II Switch,tech,tech
3COM,SuperStack II Switch,tech,tech
3COM,SuperStack III Switch,manager,manager
3COM,SuperStack III Switch,recovery,recovery
3COM,Switch,admin,admin
3COM,US Robotics ADSL Router,<blank>,12345
3COM,Wireless AP,admin,comcomcom
3COM,Wireless AP,admin,comcomcom
3COM,cellplex,<blank>,<blank>
3COM,cellplex,admin,admin
3COM,cellplex,operator,<blank>
3COM,cellplex,admin,admin
3COM,officeconnect,<blank>,<blank>
3COM,superstack II Netbuilder,<blank>,<blank>
3COM,superstack II,3comcso,RIP000
3Com,,root,letmein
3Com,3CRWDR100A-72,admin,1234admin
3Com,AirConnect Access Point,<blank>,comcomcom
3Com,CoreBuilder,debug,tech
3Com,Internet Firewall,admin,password
3Com,LinkSwitch and CellPlex,tech,tech
3Com,OfficeConnect 5×1,<blank>,PASSWORD
3Com,Shark Fin,User,Password
3Com,SuperStack II Switch 1100,manager,manager
3Com,SuperStack II Switch 2200,debug,synnet
3Com,SuperStack II Switch 3300,manager,manager
3Com,SuperStack/CoreBuilder,admin,<blank>
3Com,SuperStack/CoreBuilder,write,<blank>
3Com,Switch 3000/3300,monitor,monitor
3Com,e960,Admin,Admin
3M,VOL-0215 etc.,volition,volition
3M,Volition Fibre Switches,volition,volition
3M,Volition,volition,<blank>
3M,Volition,VOL-0215,<blank>
3com,3C16405,admin,<blank>
3com,3CRADSL72,<blank>,1234admin
3com,3c16405,Administrator,<blank>
3com,3c16405,<blank>,<blank>
3com,3comCellPlex7000,tech,tech
3com,812,Administrator,admin
3com,CB9000/4007,FORCE,<blank>
3com,Cable Managment System SQL Database (DOSCIC DHCP),DOCSIS_APP,3com
3com,CellPlex,root,<blank>
3com,CellPlex,tech,<blank>
3com,CellPlex,tech,tech
3com,HiPerACT,admin,<blank>
3com,Home Connect,User,Password
3com,LANplex,<blank>,admin
3com,NBX100,administrator,0
3com,Netbuilder,admin,<blank>
3com,OfficeConnect 812 ADSL,adminttd,adminttd
3com,OfficeConnect 812 ADSL,admin,<blank>
3com,OfficeConnect Wireless 11g Cable/DSL Gateway,<blank>,admin
3com,OfficeConnect Wireless 11g,<blank>,admin
3com,SS III Switch,recovery,recovery
3com,Superstack II 3300FX,admin,<blank>
3com,Switch 3000/3300,Admin,3com
3com,Switch,admin,admin
3com,cellplex,<blank>,<blank>
3com,cellplex,admin,admin
3com,cellplex,admin,admin
3com,cellplex,operator,<blank>
3com,corebuilder,defug,synnet
3com,office connect,admin,<blank>
3com,officeconnect,<blank>,<blank>
3com,officeconnect,admin,<blank>
3com,super,admin,<blank>
3com,superstack II Netbuilder,<blank>,<blank>
3ware,3DM,Administrator,3ware
3xLogic,IP Camera system,admin,12345
5200-Serie,,<blank>,<blank>
8level,,admin,admin
ABB,Controller,service,ABB800xA
ABB,Ethernet Adapter Module,admin,admin
ACC,Congo/Amazon/Tigris,netman,netman
ACCTON,CheetahChassis Workgroup Switch,admin,<blank>
ACCTON,CheetahChassis Workgroup Switch,manager,manager
ACCTON,CheetahChassis Workgroup Switch,monitor,monitor
ACCTON,Wirelessrouter,<blank>,0
ACCTON,Wirelessrouter,<blank>,0
ACIE SECURITE,ADIP,adip,admin
ACIE SECURITE,ADIP,adip,consul
ACIE SECURITE,ADIP,adip,insta
ACTi,IP Camera,admin,123456
ADC Kentrox,Pacesetter Router,<blank>,secret
ADIC,Scalar 100/1000,admin,secure
ADIC,Scalar i2000,admin,password
ADP,ADP Payroll HR Database,sysadmin,master
ADT,Safewatch Pro3000,<blank>,2580
AIRAYA Corp,AIRAYA WirelessGRID,Airaya,Airaya
ALCATEL,4400,mtcl,<blank>
ALLNET,ALL 130DSL,admin,password
ALLNET,ALL129DSL,admin,admin
ALLNET,T-DSL Modem,admin,admin
ALLNET,T-DSL Modem,admin,admin
AMBIT,ADSL,root,<blank>
AMI,AT 49,<blank>,<blank>
AMI,PC BIOS,<blank>,A.M.I
AMI,PC BIOS,<blank>,AM
AMI,PC BIOS,<blank>,AMI
AMI,PC BIOS,<blank>,AMI.KEY
AMI,PC BIOS,<blank>,AMIDECOD
AMI,PC BIOS,<blank>,AMI~
AMI,PC BIOS,<blank>,BIOSPASS
AMI,PC BIOS,<blank>,CMOSPWD
AMI,PC BIOS,<blank>,aammii
AMI,PC BIOS,<blank>,amipswd
AMX,CSG,admin,1988
AMX,Endeleo UDM-0102,<blank>,admin
AMX,Endeleo UDM-0404,<blank>,admin
AMX,Endeleo UDM-0808-SIG,administrator,password
AMX,Environmental Controls ENV-VST-C,<blank>,1988
AMX,IS-SPX-1000,<blank>,<blank>
AMX,MAX Server,root,mozart
AMX,MAX-CSD10,administrator,password
AMX,MAX-CSE,administrator,password
AMX,MET-ECOM/-D,admin,1988
AMX,NI Series,NetLinx,password
AMX,NI Series,administrator,password
AMX,NXA-ENET24,Admin,1988
AMX,NXA-ENET24,guest,guest
AMX,NXA-ENET8POE,admin,1988
AMX,NXA-WAP1000,admin,1988
AMX,NXA-WAP250G,admin,1988
AMX,NXA-WAPZD1000 (Zone Director),admin,admin
AMX,NXR-ZGW-PRO/-ZRP-PRO,Admin,1988
AMX,NXR-ZGW/-ZRP,Admin,1988
AMX,TVM-1600,<blank>,admin
AMX,V2 Server,Administrator,vision2
AOC,zenworks 4.0,<blank>,admin
APC,9606 Smart Slot,<blank>,backdoor
APC,AP9606 SmartSlot Web/SNMP Management Card,(any),TENmanUFactOryPOWER
APC,Any,apcuser,apc
APC,Call-UPS,<blank>,serial number of the Call-UPS
APC,MasterSwitch,apc,apc
APC,Powerchute Plus,POWERCHUTE,APC
APC,SNMP Adapter,apc,apc
APC,Share-UPS,<blank>,serial number of the Share-UPS
APC,Smart UPS,apc,apc
APC,UPS Network Management Card 2,readonly,apc
APC,UPS Network Management Card 2,device,apc
APC,UPSes (Web/SNMP Mgmt Card),device,device
APC,USV Network Management Card,<blank>,TENmanUFactOryPOWER
APC,Web/SNMP Management Card,apc,apc
APC,Web/SNMP Management Card,apc,apc
ARtem,ComPoint - CPD-XT-b,<blank>,admin
ASMAX,AR701u/ASMAX AR6024,admin,epicrouter
ASMAX,AR800C2,admin,epicrouter
AST,PC BIOS,<blank>,SnuFG5
AST,PC BIOS,<blank>,SnuFG5
ATL,P1000,Service,5678
ATL,P1000,operator,1234
AVAYA,Cajun P33x,<blank>,admin
AVAYA,P333,Administrator,ggdaseuaimhrke
AVAYA,P333,root,ggdaseuaimhrke
AVAYA,g3R,root,ROOT500
AVM,Fritz!Box Fon,<blank>,<blank>
AVM,Fritz!Box,<blank>,0
AWARD,PC BIOS,<blank>,1322222
AWARD,PC BIOS,<blank>,256256
AWARD,PC BIOS,<blank>,256256
AWARD,PC BIOS,<blank>,589589
AWARD,PC BIOS,<blank>,589721
AWARD,PC BIOS,<blank>,<blank>
AWARD,PC BIOS,<blank>,?award
AWARD,PC BIOS,<blank>,AWARD SW
AWARD,PC BIOS,<blank>,AWARD?SW
AWARD,PC BIOS,<blank>,AWARD_PW
AWARD,PC BIOS,<blank>,AWARD_SW
AWARD,PC BIOS,<blank>,AWARD_SW
AWARD,PC BIOS,<blank>,Award
AWARD,PC BIOS,<blank>,Award
AWARD,PC BIOS,<blank>,BIOS
AWARD,PC BIOS,<blank>,BIOS
AWARD,PC BIOS,<blank>,CONCAT
AWARD,PC BIOS,<blank>,CONDO
AWARD,PC BIOS,<blank>,CONDO
AWARD,PC BIOS,<blank>,Condo
AWARD,PC BIOS,<blank>,HELGA-S
AWARD,PC BIOS,<blank>,HEWITT RAND
AWARD,PC BIOS,<blank>,HEWITT RAND
AWARD,PC BIOS,<blank>,HLT
AWARD,PC BIOS,<blank>,PASSWORD
AWARD,PC BIOS,<blank>,PASSWORD
AWARD,PC BIOS,<blank>,SER
AWARD,PC BIOS,<blank>,SKY_FOX
AWARD,PC BIOS,<blank>,SWITCHES_SW
AWARD,PC BIOS,<blank>,SW_AWARD
AWARD,PC BIOS,<blank>,SW_AWARD
AWARD,PC BIOS,<blank>,SZYX
AWARD,PC BIOS,<blank>,Sxyz
AWARD,PC BIOS,<blank>,Sxyz
AWARD,PC BIOS,<blank>,TTPTHA
AWARD,PC BIOS,<blank>,TTPTHA
AWARD,PC BIOS,<blank>,ZAAADA
AWARD,PC BIOS,<blank>,aLLy
AWARD,PC BIOS,<blank>,aPAf
AWARD,PC BIOS,<blank>,aPAf
AWARD,PC BIOS,<blank>,admin
AWARD,PC BIOS,<blank>,alfarome
AWARD,PC BIOS,<blank>,alfarome
AWARD,PC BIOS,<blank>,award.sw
AWARD,PC BIOS,<blank>,award_?
AWARD,PC BIOS,<blank>,award_ps
AWARD,PC BIOS,<blank>,awkward
AWARD,PC BIOS,<blank>,biosstar
AWARD,PC BIOS,<blank>,biostar
AWARD,PC BIOS,<blank>,biostar
AWARD,PC BIOS,<blank>,condo
AWARD,PC BIOS,<blank>,condo
AWARD,PC BIOS,<blank>,djonet
AWARD,PC BIOS,<blank>,efmukl
AWARD,PC BIOS,<blank>,g6PJ
AWARD,PC BIOS,<blank>,h6BB
AWARD,PC BIOS,<blank>,h6BB
AWARD,PC BIOS,<blank>,j09F
AWARD,PC BIOS,<blank>,j09F
AWARD,PC BIOS,<blank>,j256
AWARD,PC BIOS,<blank>,j262
AWARD,PC BIOS,<blank>,j262
AWARD,PC BIOS,<blank>,j322
AWARD,PC BIOS,<blank>,j64
AWARD,PC BIOS,<blank>,j64
AWARD,PC BIOS,<blank>,lkw peter
AWARD,PC BIOS,<blank>,lkwpeter
AWARD,PC BIOS,<blank>,lkwpeter
AWARD,PC BIOS,<blank>,setup
AWARD,PC BIOS,<blank>,setup
AWARD,PC BIOS,<blank>,t0ch20x
AWARD,PC BIOS,<blank>,t0ch20x
AWARD,PC BIOS,<blank>,t0ch88
AWARD,PC BIOS,<blank>,wodj
AWARD,PC BIOS,<blank>,wodj
AWARD,PC BIOS,<blank>,zbaaaca
AWARD,PC BIOS,<blank>,zjaaadc
AWARD,PC BIOS,Administrator,admin
AWARD,PC BIOS,<blank>,<blank>
AXIS,200 V1.32,admin,<blank>
AXUS,AXUS YOTTA,<blank>,0
Acc/Newbridge,Congo/Amazon/Tigris,netman,netman
Accelerated Networks,DSL CPE and DSLAM,sysadm,anicust
Accelerated,DSL CPE and DSLAM,sysadm,anicust
Accton,Gigabit Switches,__super,(caclulated)
Aceex,Modem ADSL Router,admin,<blank>
Acer,517te,<blank>,<blank>
Acer,Phoenix,<blank>,<blank>
Acer,Phoenix,<blank>,Admin
Acti,IP Camera system,admin,admin
Actiontec,GE344000-01,<blank>,<blank>
Actiontec,GT701-WG,admin,password
Actiontec,M1424WR,admin,password
Actiontec,Wireless Broadband Router,admin,password
AdComplete.com,Ban Man Pro,Admin1,Admin1
AdComplete.com,Banman Pro,Admin1,Admin1
Adaptec,RAID Controller,Administrator,adaptec
Adaptec,Storage Manager PRO,Administrator,adaptec
Adcon Telemetry,Telemetry Gateway,root,840sw
Adcon Telemetry,Wireless Modem,root,840sw
Adcon Telemetry,addVANTAGE,root,root
AddPac Technology,AP2120,root,router
Addon,GWAR3000/ARM8100,admin,admin
Adobe,CQ,admin,admin
Adobe,CQ,author,author
Adobe,Experience Manager,admin,admin
Adobe,Experience Manager/CQ,anonymous,anonymous
Adobe,Experience Manager/CQ,aparker@geometrixx.info,aparker
Adobe,Experience Manager/CQ,jdoe@geometrixx.info,jdoe
Adobe,Experience Manager/CQ,replication-receiver,replication-receiver
Adobe,Vignette Connector,vgnadmin,vgnadmin
Adtech,AX4000,root,ax400
Adtran,MX2800,<blank>,adtran
Adtran,NetVanta,admin,password
Adtran,TSU 600 Ethernet module,18364,<blank>
Advanced Integration,PC BIOS,<blank>,Advance
Advantek Networks,Wireless LAN 802.11 g/b,admin,<blank>
Aethra,Starbridge EU,admin,password
AirLink Plus,RTW026,<blank>,admin
AirTies RT-210,AirTies RT-210,admin,admin
Airlink,AnyGate,<blank>,admin
Aironet,All,<blank>,<blank>
Airtel,wifi router,admin,admin
Airties,Air4310,<blank>,<blank>
Airway,Transport,<blank>,0
Aladdin,eSafe Appliance,root,kn1TG7psLu
Alcatel,7300 ASAM,SUPERUSER,ANS#150
Alcatel,OXO,<blank>,admin
Alcatel,Office 4200,<blank>,1064
Alcatel,OmniPCX Office,ftp_admi,kilo1987
Alcatel,OmniPCX Office,ftp_inst,pbxk1064
Alcatel,OmniPCX Office,ftp_nmc,tuxalize
Alcatel,OmniPCX Office,ftp_oper,help1954
Alcatel,OmniStack 6024,admin,switch
Alcatel,OmniStack/OmniSwitch,diag,switch
Alcatel,Omnistack/Omniswitch,diag,switch
Alcatel,Omnistack/Omniswitch,diag,switch
Alcatel,Omnistack/omniswitch,diag,switch
Alcatel,PBX,at4400,at4400
Alcatel,PBX,dhs3mt,dhs3mt
Alcatel,PBX,halt,tlah
Alcatel,PBX,kermit,kermit
Alcatel,PBX,mtcl,mtcl
Alcatel,PBX,adfexc,adfexc
Alcatel,PBX,at4400,at4400
Alcatel,PBX,client,client
Alcatel,PBX,dhs3mt,dhs3mt
Alcatel,PBX,dhs3pms,dhs3pms
Alcatel,PBX,halt,tlah
Alcatel,PBX,install,llatsni
Alcatel,PBX,kermit,kermit
Alcatel,PBX,mtch,mtch
Alcatel,PBX,mtcl,mtcl
Alcatel,PBX,root,letacla
Alcatel,PBX,adfexc,adfexc
Alcatel,PBX,at4400,at4400
Alcatel,PBX,client,client
Alcatel,PBX,dhs3mt,dhs3mt
Alcatel,PBX,dhs3pms,dhs3pms
Alcatel,PBX,halt,tlah
Alcatel,PBX,install,llatsni
Alcatel,PBX,kermit,kermit
Alcatel,PBX,mtch,mtch
Alcatel,PBX,mtcl,mtcl
Alcatel,PBX,root,letacla
Alcatel,Speedtouch,<blank>,<blank>
Alcatel,Timestep VPN 1520,root,permit
Alcatel,VPN Gateway,root,permit
Alcatel/Newbridge/Timestep,VPN Gateway 15xx/45xx/7xxx,root,permit
Alien Technology,ALR-9900,alien,alien
Alien Technology,ALR-9900,root,alien
Allied Telesyn,ALAT8326GB,manager,manager
Allied Telesyn,AT Router,root,<blank>
Allied Telesyn,AT-8024(GB),<blank>,admin
Allied Telesyn,AT-8024(GB),manager,admin
Allied Telesyn,AT-AR130 (U) -10,Manager,friend
Allied Telesyn,AT8016F,manager,friend
Allied Telesyn,Rapier G6 Switch,<blank>,manager
Allied Telesyn,Various Switches,manager,manager
Allied,CJ8MO E-U,<blank>,<blank>
Allied,Telesyn,manager,friend
Allied,Telesyn,secoff,secoff
Allnet,ALL0275 802.11g AP,<blank>,admin
Allnet,ALL129DSL,admin,admin
Allot,Netenforcer,admin,allot
Allot,Netenforcer,root,bagabu
Alteon,ACEDirector3,admin,<blank>
Alteon,ACEDirector3,admin,<blank>
Alteon,ACEswitch,admin,admin
Alteon,ACEswitch,admin,admin
Alteon,ACEswitch,admin,linga
Alteon,ACEswitch,admin,linga
Alteon,ACEswitch,admin,<blank>
Alteon,AD4,admin,admin
Alteon,Web Systems,<blank>,14admin
Ambit,Cable Modem 60678eu,root,root
Ambit,Cable Modem,root,root
Ambit,Cable Modems,root,root
Ambit,Cable Modems,user,user
Ambit,ntl:home 200,root,root
American Dynmics,IP Camera system,admin,admin
Amino,AmiNET Set Top Box,<blank>,leaves
Amino,AmiNET Set Top Box,<blank>,snake
Amitech,wireless router and access point 802.11g 802.11b,admin,admin
AmpJuke,AmpJuke,admin,pass
Amptron,PC BIOS,<blank>,Polrty
Amptron,PC BIOS,<blank>,Polrty
Andover Controls,Infinity,acc,acc
Apache Project,,jj,<blank>
Apache,Tomcat Web Server Administration Tool,admin,<blank>
Apache,Tomcat Web Server,admin,<blank>
Apache,Tomcat,admin,j5Brn9
Apache,Tomcat,admin,admin
Apache,Tomcat,admin,tomcat
Apache,Tomcat,role,changethis
Apache,Tomcat,role1,role1
Apache,Tomcat,root,changethis
Apache,Tomcat,root,root
Apache,Tomcat,tomcat,changethis
Apache,Tomcat,tomcat,tomcat
Apache,Tomcat,both,tomcat
Apache,Tomcat,role1,tomcat
Apple Computer,Airport,<blank>,public
Apple Computer,Network Assistant,<blank>,xyzzy
Apple Computer,Remote Desktop,<blank>,xyzzy
Apple,AirPort Base Station (Graphite),<blank>,public
Apple,Airport Base Station (Dual Ethernet),<blank>,password
Apple,Airport Extreme Base Station,<blank>,admin
Apple,Airport,<blank>,public
Apple,Almost all iOS devices,root,alpine
Apple,Network Assistant,<blank>,xyzzy
Apple,airport5,root,admin
Apple,iPhone,mobile,dottie
Apple,iPhone,root,alpine
Applied Innovations,AIscout,scout,scout
Areca,RAID controllers,admin,0
Areca,RAID controllers,admin,0
Arecont Vision,IP Camera system,admin,<blank>
Arescom,modem/router,<blank>,atc123
Armenia,Forum,admin,admin
Arris,DG3450,admin,password
Arris,DG860P2,admin,password
Arris,DG950A,admin,password
Arris,SB8200,admin,password
Arris,SBG10,admin,password
Arris,SBG6700-AC,admin,password
Arris,SBG6900-AC,admin,password
Arris,SBG8300,admin,password
Arris,SBR-AC1750,admin,password
Arris,SBR-AC1900P,admin,password
Arris,SBR-AC3200P,admin,password
Arris,TG1672G,admin,password
Arris,TG1682G,admin,password
Arris,TG862,admin,password
Arris,Touchstone Gateway,admin,password
Arris,VAP4641,admin,<blank>
Arris,WR2100,admin,password
Arrowpoint,,<blank>,<blank>
Arrowpoint,,admin,system
Arrowpoint,any?,admin,system
Aruba Networks,RAP-155 (APINR155),admin,admin
Aruba Networks,RAP-3WNP,admin,admin
Aruba,Mobility Controller,admin,admin
Asante,FM2008,admin,asante
Asante,FM2008,superuser,<blank>
Asante,FM2008,superuser,asante
Asante,IntraStack,IntraStack,Asante
Asante,IntraSwitch,IntraSwitch,Asante
Asante,IntraSwitch,IntraSwitch,Asante
Ascend,All TAOS models,admin,Ascend
Ascend,Router,<blank>,ascend
Ascend,Router,<blank>,ascend
Ascend,Sahara,root,ascend
Ascend,Yurie,readonly,lucenttech2
Ascend,Yurie,readonly,lucenttech2
Ascom,Ascotel PBX,<blank>,3ascotel
Ascom,Ascotel PBX,<blank>,3ascotel
Ascom,Ascotel,<blank>,3ascotel
Askey,RTF8115VW,admin,admin
Asmax,Ar-804u,admin,epicrouter
Aspect,ACD,customer,<blank>
Aspect,ACD,customer,<blank>
Aspect,ACD,DTA,TJM
Aspect,ACD,DTA,TJM
Aspect,ACD,DTA,TJM
Asus,4G-AC55U,admin,admin
Asus,4G-AC68U,admin,admin
Asus,4G-N12,admin,admin
Asus,520g,admin,admin
Asus,AAM6020VI-FI,root,admin
Asus,BRT-AC828/M2,admin,admin
Asus,Blue Cave,admin,admin
Asus,CM-16,admin,admin
Asus,CM-32,admin,admin
Asus,DSL-AC52U,admin,admin
Asus,DSL-AC55U,admin,admin
Asus,DSL-AC56U,admin,admin
Asus,DSL-AC68U,admin,admin
Asus,DSL-G31,admin,admin
Asus,DSL-N10,admin,admin
Asus,DSL-N11,admin,admin
Asus,DSL-N12U rev B1,admin,admin
Asus,DSL-N12U,admin,admin
Asus,DSL-N13,admin,admin
Asus,DSL-N17U B1,admin,admin
Asus,DSL-N17U,admin,admin
Asus,DSL-N55U C1,admin,admin
Asus,DSL-N55U,admin,admin
Asus,DSL-N66U,admin,admin
Asus,EA-AC87,admin,admin
Asus,EA-N66,admin,admin
Asus,GT-AC2900,admin,admin
Asus,GT-AC5300,admin,admin
Asus,GT-AC9600,admin,admin
Asus,GT-AX11000,admin,admin
Asus,Internet Radio (AIR),admin,admin
Asus,Internet Radio 3 (AIR3),admin,admin
Asus,Lyra Mini,admin,admin
Asus,Lyra Trio,admin,admin
Asus,Lyra Voice,admin,admin
Asus,Lyra,admin,admin
Asus,P5P800,<blank>,admin
Asus,PL-AC56,admin,admin
Asus,PL-N12,admin,admin
Asus,RP-AC52,admin,admin
Asus,RP-AC53,admin,admin
Asus,RP-AC55,admin,admin
Asus,RP-AC56,admin,admin
Asus,RP-AC68U,admin,admin
Asus,RP-AC87,admin,admin
Asus,RP-N12,admin,admin
Asus,RP-N14,admin,admin
Asus,RP-N53,admin,admin
Asus,RT-AC1200 v2,admin,admin
Asus,RT-AC1200,admin,admin
Asus,RT-AC1200G,admin,admin
Asus,RT-AC1200GP,admin,admin
Asus,RT-AC1200GU,admin,admin
Asus,RT-AC1200HP,admin,admin
Asus,RT-AC1750,admin,admin
Asus,RT-AC1900,admin,admin
Asus,RT-AC1900P,admin,admin
Asus,RT-AC3100,admin,admin
Asus,RT-AC3200,admin,admin
Asus,RT-AC42U,admin,admin
Asus,RT-AC51U,admin,admin
Asus,RT-AC52U B1,admin,admin
Asus,RT-AC52U,admin,admin
Asus,RT-AC53,admin,admin
Asus,RT-AC5300,admin,admin
Asus,RT-AC53U,admin,admin
Asus,RT-AC54U,admin,admin
Asus,RT-AC55U,admin,admin
Asus,RT-AC55UHP,admin,admin
Asus,RT-AC56S,admin,admin
Asus,RT-AC56U,admin,admin
Asus,RT-AC57U,admin,admin
Asus,RT-AC58U,admin,admin
Asus,RT-AC59U,admin,admin
Asus,RT-AC65P,admin,admin
Asus,RT-AC65U,admin,admin
Asus,RT-AC66U B1,admin,admin
Asus,RT-AC66U,admin,admin
Asus,RT-AC68P,admin,admin
Asus,RT-AC68U Extreme,admin,admin
Asus,RT-AC68U,admin,admin
Asus,RT-AC68UF,admin,admin
Asus,RT-AC750,admin,admin
Asus,RT-AC750GF,admin,admin
Asus,RT-AC85U,admin,admin
Asus,RT-AC86U,admin,admin
Asus,RT-AC87U,admin,admin
Asus,RT-AC88U,admin,admin
Asus,RT-ACRH12,admin,admin
Asus,RT-ACRH13,admin,admin
Asus,RT-ACRH15,admin,admin
Asus,RT-ACRH17,admin,admin
Asus,RT-AX56U,admin,admin
Asus,RT-AX88U,admin,admin
Asus,RT-AX92U,admin,admin
Asus,RT-AX95U,admin,admin
Asus,RT-G32 rev A1,admin,admin
Asus,RT-G32 rev B1,admin,admin
Asus,RT-G32 rev C1,admin,admin
Asus,RT-N10 rev A1,admin,admin
Asus,RT-N10 rev C1,admin,admin
Asus,RT-N10 rev D1,admin,admin
Asus,RT-N10+ rev B1,admin,admin
Asus,RT-N10+ rev D1,admin,admin
Asus,RT-N10E B1,admin,admin
Asus,RT-N10E,admin,admin
Asus,RT-N10P V2,admin,admin
Asus,RT-N10P,admin,admin
Asus,RT-N10U B,admin,admin
Asus,RT-N10U,admin,admin
Asus,RT-N11,admin,admin
Asus,RT-N11P B1,admin,admin
Asus,RT-N11P,admin,admin
Asus,RT-N12 rev A1,admin,admin
Asus,RT-N12 rev B1,admin,admin
Asus,RT-N12 rev C1,admin,admin
Asus,RT-N12 rev D1,admin,admin
Asus,RT-N12+ B1,admin,admin
Asus,RT-N12+B1,admin,admin
Asus,RT-N12E B1,admin,admin
Asus,RT-N12E C1,admin,admin
Asus,RT-N12E,admin,admin
Asus,RT-N12HP B1,admin,admin
Asus,RT-N12HP,admin,admin
Asus,RT-N12K,admin,admin
Asus,RT-N12VP,admin,admin
Asus,RT-N13,admin,admin
Asus,RT-N13U B1,admin,admin
Asus,RT-N13U,admin,admin
Asus,RT-N14U,admin,admin
Asus,RT-N14UHP,admin,admin
Asus,RT-N15,admin,admin
Asus,RT-N15U,admin,admin
Asus,RT-N16,admin,admin
Asus,RT-N16,admin,admin
Asus,RT-N18U,admin,admin
Asus,RT-N300 B1,admin,admin
Asus,RT-N300,admin,admin
Asus,RT-N53,admin,admin
Asus,RT-N54U,admin,admin
Asus,RT-N56U B1,admin,admin
Asus,RT-N56U,admin,admin
Asus,RT-N56U,admin,HTTP
Asus,RT-N600,admin,admin
Asus,RT-N600RU,admin,admin
Asus,RT-N65U,admin,admin
Asus,RT-N66U C1,admin,admin
Asus,RT-N66U,admin,admin
Asus,RT-N66W,admin,admin
Asus,RT-N800HP,admin,admin
Asus,RX3041,admin,admin
Asus,SMTA Router,admin,admin
Asus,TM-AC1900,admin,password
Asus,TM-AC1900,admin,admin
Asus,WL-300,<blank>,asus
Asus,WL-300g,admin,admin
Asus,WL-320gP,admin,admin
Asus,WL-330,admin,admin
Asus,WL-330N3G,admin,admin
Asus,WL-330g,admin,admin
Asus,WL-330gE,admin,admin
Asus,WL-500,admin,admin
Asus,WL-500W,admin,admin
Asus,WL-500b,admin,admin
Asus,WL-500g Deluxe,admin,admin
Asus,WL-500g,admin,admin
Asus,WL-500gP v1,admin,admin
Asus,WL-500gP v2,admin,admin
Asus,WL-520g,admin,admin
Asus,WL-520gC,admin,admin
Asus,WL-520gU,admin,admin
Asus,WL-530g,admin,admin
Asus,WL-530gV2,admin,admin
Asus,WL-550gE,admin,admin
Asus,WL-566gM,admin,admin
Asus,WL-600g,admin,admin
Asus,WL-700gE,admin,admin
Asus,WL-HDD2.5,admin,admin
Asus,WL-HDD2.5,admin,admin
Asus,WL500g Deluxe,admin,admin
Asus,WMP-N12,admin,admin
Asus,WMVN25E2+,admin,admin
Asus,Zenbo,admin,admin
Asus,wl300,admin,admin
Asus,wl500,admin,admin
Asus,wl500,admin,admin
Asus,wl503g,admin,admin
Atlantis,A02-RA141,admin,atlantis
Atlantis,I-Storm Lan Router ADSL,admin,atlantis
Atlassian,Crowd,Crowd,password
Atlassian,Crowd,Demo,password
Atlassian,Crowd,Username,password
Atlassian,Crowd,crowd-openid-server,password
Attachmate,Attachmate Gateway,<blank>,PASSWORD
Attachmate,Attachmate Gateway,<blank>,PASSWORD
Audioactive,MPEG Realtime Encoders,<blank>,telos
Audioactive,MPEG Realtime Encoders,<blank>,telos
Autodesk,Autocad,autocad,autocad
Avaya,4602 SIP Telephone,admin,barney
Avaya,CMS Supervisor,root,cms500
Avaya,Cajun Pxxx,root,root
Avaya,Cajun,diag,danger
Avaya,Cajun,manuf,xxyyzz
Avaya,Cajun,diag,danger
Avaya,Cajun,manuf,xxyyzz
Avaya,Cajun,diag,danger
Avaya,Cajun,<blank>,<blank>
Avaya,Definity,dadmin,dadmin
Avaya,Definity,dadmin,dadmin01
Avaya,Definity,craft,<blank>
Avaya,Integrated Management Database (IMD),admin,admin123
Avaya,Intuity Audix,Craft,crftpw
Avaya,P330 Stackable Switch,root,root
Avaya,Pxxx,diag,danger
Avaya,Pxxx,manuf,xxyyzz
Avaya,Pxxx,manuf,xxyyzz
Avaya,Pxxx,diag,danger
Avaya,Pxxx,manuf,xxyyzz
Avaya,Scopia Gateway,admin,password
Avaya,Scopia,admin,admin
Avaya,Winspm,<blank>,Craftr4
Avaya,definity,craft,crftpw
Avaya,routers,root,root
Avenger News System (ANS),ANS,<blank>,Administrative
Avigilon,IP Camera system,admin,admin
Avocent,Cyclade,root,tslinux
Avocent,Cyclade,root,tslinux
Axent,NetProwler manager,administrator,admin
Axis Communications,Axis Network Camera,root,pass
Axis Communications,Axis Network Camera,root,pass
Axis Communications,Axis Network Camera,root,pass
Axis Communications,Printserver,root,pass
Axis,540/542 Print Server,root,pass
Axis,All Axis Printserver,root,pass
Axis,Camera Server,root,pass
Axis,IP Camera system,root,<blank>
Axis,NETCAM,root,pass
Axis,NETCAM,root,pass
Axis,Printserver,root,pass
Axis,StorPoint CD E100,root,pass
Axis,StorPoint NAS 100,root,pass
Axis,Webcams,root,pass
Axway,SecureTransport,setup,setup
Aztecj,DSL 600EU,isp,isp
Aztecj,DSL 600EU,root,admin
B-FOCuS,B-FOCuS 270/400,root,1234
BBR-4MG and BBR-4HG,Buffalo,root,<blank>
BBR-4MG and,BUFFALO,root,<blank>
BEA,WebLogic Process Integrator,joe,password
BEA,WebLogic Process Integrator,system,security
BEA,Weblogic,system,weblogic
BMC Software,Patrol,Administrator,the same all over
BMC,Patrol,patrol,patrol
BT,BT Mobile Hotspot,<blank>,admin
BUFFALO,WLAR-L11-L / WLAR-L11G-L,root,<blank>
Banana Pi,BPI-M64 Manjaro,root,bananapi
Basler,IP Camera system,admin,admin
Bausch Datacom,Proxima PRI ADSL PSTN Router4 Wireless,admin,epicrouter
Bausch Datacom,Proxima PRI ADSL PSTN,admin,epicrouter
Bay Networks,Router,User,<blank>
Bay Networks,Router,Manager,<blank>
Bay Networks,Router,User,<blank>
Bay Networks,SuperStack II,security,security
Bay Networks,SuperStack II,security,security
Bay Networks,Switch,<blank>,NetICs
Bay Networks,Switch,<blank>,NetICs
Beck,IPC@Chip,anonymous,<blank>
Beck,IPC@Chip,tel,<blank>
Beetel,ADSL Modem,admin,password
Belkin,BoB (F1PI243EGau / iinet),<blank>,admin
Belkin,F5D5230-4,Admin,<blank>
Belkin,F5D6130,<blank>,MiniAP
Belkin,F5D6130,<blank>,MiniAP
Belkin,F5D7150,<blank>,admin
Belkin,F9K1103 v1,admin,password
Belkin,F9K1103 v1xxx,admin,password
Benq,awl 700 wireless router,admin,admin
Billion,BIPAC-640 AC,<blank>,<blank>
Billion,Bipac 5100,admin,admin
BinTec,Bianca/Brick,<blank>,snmp
BinTec,Bianca/Brick,<blank>,snmp-Trap
BinTec,x1200,admin,bintec
BinTec,x1200,admin,bintec
BinTec,x2300i,admin,bintec
BinTec,x2300i,admin,bintec
BinTec,x3200,admin,bintec
BinTec,x3200,admin,bintec
Bintec,Bianka Routers,admin,bintec
Bintec,all Routers,admin,bintec
BioData,all Babylon Boxes,<blank>,Babylon
Biostar,PC BIOS,<blank>,Q54arwms
BizDesign,ImageFolio Pro,Admin,ImageFolio
Blue Coat Systems,ProxySG,admin,articon
Blue Coat Systems,ProxySG,admin,articon
Bluecoat,ProxySG (all model),admin,admin
Borland,Interbase,politcally,correct
Borland/Inprise,Interbase,SYSDBA,masterkey
Bosch Dinion,IP Camera system,admin,<blank>
Bosch,IP Camera system,service,service
Bosch,NWC-0455 Dinion IP Cameras,live,live
Bosch,NWC-0455 Dinion IP Cameras,service,service
Bosch,NWC-0455 Dinion IP Cameras,user,user
Boston,router simulator,admin,admin
Boston,router simulator,<blank>,admin
BreezeCOM,,<blank>,Master
BreezeCOM,Station Adapter and Access Point,<blank>,Super
Breezecom,Breezecom Adapters,<blank>,laflaf
Breezecom,Breezecom Adapters,<blank>,laflaf
Breezecom,Breezecom Adapters,<blank>,Master
Breezecom,Breezecom Adapters,<blank>,Master
Breezecom,Breezecom Adapters,<blank>,Helpdesk
Breezecom,Breezecom Adapters,<blank>,Super
Brickcom,IP Camera system,admin,admin
Broadlogic,XLT router,webadmin,webadmin
Broadlogic,XLT router,admin,admin
Broadlogic,XLT router,installer,installer
Brocade,Fabric OS,factory,Fact4EMC
Brocade,Fabric OS,root,Serv4EMC
Brocade,Fabric OS,admin,password
Brocade,Fabric OS,user,password
Brocade,Fabric OS,root,fivranne
Brocade,Fiberchannel Switches,admin,password
Brocade,Silkworm,admin,password
Brother,DCP-7065DN,admin,access
Brother,DCP-7065DN,user,access
Brother,HL-1270n,<blank>,access
Brother,HL-1270n,<blank>,access
Brother,HL-5250DN,admin,access
Brother,HL-5350DN,admin,access
Brother,HL5270DN,admin,access
Brother,MFC-420CN,<blank>,access
Brother,MFC-7225,admin,access
Brother,NC-2100p,<blank>,access
Brother,NC-3100h,<blank>,access
Brother,NC-3100h,<blank>,access
Brother,NC-4100h,<blank>,access
Brother,NC-4100h,<blank>,access
Buffalo Technology,TeraStation,admin,password
Buffalo,WHR-G300N,root,<blank>
Buffalo,Wireless Broadband Base Station-g,root,<blank>
Buffalo,Wireless Broadband Base,root,<blank>
Buffalo/MELCO,AirStation WLA-L11,root (cannot be changed),<blank>
CBC Ganz,IP Camera system,admin,admin
CNB,IP Camera system,root,admin
CNET,CNET 4PORT ADSL MODEM,admin,epicrouter
CNET,CNET 4PORT ADSL MODEM,admin,epicrouter
CNET,CSH-2400W,admin,1234
CNet,CWR- 500 Wireless-B Router,Admin,admin
COM3,OLe,admin,admin
CTC Union,ATU-R130,root,root
Cable And Wireless,ADSL Modem/Router,admin,1234
Cabletron,Netgear modem/router and SSR,netman,<blank>
Cabletron,Netgear modem/router,netman,<blank>
Cabletron,any,<blank>,<blank>
Cabletron/Enterasys,WebView for Matrix E1 (1G694-13 or 1G582-09 or 1H582-51) switch,<blank>,<blank>
Calix,Residential Gateway,admin,admin
Calix,Router,admin,<blank>
Canonical Ltd.,Ubuntu,ubuntu,ubuntu
Cassandra,CassandraDB,cassandra,cassandra
Cayman,3220-H DSL Router,Any,<blank>
Cayman,Cayman DSL,<blank>,<blank>
Celerity,Mediator,root,Mau'dib
Celerity,Mediator,root,Mau’dib
Celerity,Mediator,mediator,mediator
Cellit,CCPro,cellit,cellit
Centreon,Web UI,admin,centreon
Centreon,Web UI,admin,centreon
Centreon,Web UI,admin,centreon
Centreon,Web UI,admin,centreon
Checkpoint,SecurePlatform,admin,admin
CipherTrust,IronMail,admin,password
Cisco,,pixadmin,pixadmin
Cisco,1900,<blank>,<blank>
Cisco,2501,<blank>,<blank>
Cisco,2503,<blank>,<blank>
Cisco,2600,Administrator,admin
Cisco,3600,Administrator,admin
Cisco,3600,<blank>,<blank>
Cisco,881-W,Cisco,Cisco
Cisco,AIR-AP1220B-A-K9,Cisco,Cisco
Cisco,AIR-AP1231G-A-K9,Cisco,Cisco
Cisco,AIR-AP3802I-A-K9,Cisco,Cisco
Cisco,AIR-LAP1131AG-A-K9,Cisco,Cisco
Cisco,AP1200,Cisco,Cisco
Cisco,AP541N,cisco,cisco
Cisco,Aironet 1200,root,Cisco
Cisco,Aironet,<blank>,_Cisco
Cisco,Aironet,Cisco,Cisco
Cisco,Any Router and Switch,cisco,cisco
Cisco,BBSD MSDE Client,bbsd-client,NULL
Cisco,BBSM Administrator,Administrator,changeme
Cisco,BBSM MSDE Administrator,sa,<blank>
Cisco,BBSM,bbsd-client,changeme2
Cisco,CNR,admin,changeme
Cisco,CVA 122,admin,admin
Cisco,CVR100W,cisco,cisco
Cisco,Cache Engine,admin,diamond
Cisco,CallManager,admin,admin
Cisco,Catalyst 4000/5000/6000,<blank>,public/private/secret
Cisco,Cisco Wireless Location Appliance,root,password
Cisco,CiscoWorks 2000,admin,cisco
Cisco,CiscoWorks 2000,guest,<blank>
Cisco,Ciso Aironet 1100 series,<blank>,Cisco
Cisco,ConfigMaker,cmaker,cmaker
Cisco,Content Engine,admin,default
Cisco,DDR2200-CL,admin,1PTV-ADM1N
Cisco,DPC3939,admin,password
Cisco,DPC3941,admin,password
Cisco,ESW-520-24-K9,cisco,cisco
Cisco,HSE,hsa,hsadb
Cisco,HSE,root,blender
Cisco,Hot Standby Routing Protocol,<blank>,cisco
Cisco,IOS,<blank>,Cisco router
Cisco,IOS,<blank>,cc
Cisco,IOS,cisco,cisco
Cisco,IOS,ripeop,(no pw)
Cisco,IOS,private ReadWrite access,secret
Cisco,IOS,<blank>,cable-docsis
Cisco,IOS,<blank>,c
Cisco,MGX,superuser,superuser
Cisco,MeetingPlace,technician,2 + last 4 of Audio Server chasis Serial case-sensitive+ 561384
Cisco,Meraki MR12,admin,<blank>
Cisco,Netranger/secure IDS,netrangr,attack
Cisco,Netranger/secure IDS,root,attack
Cisco,Network Registar,ADMIN,changeme
Cisco,ONS,CISCO15,otbu+1
Cisco,PIX firewall,<blank>,<blank>
Cisco,PIX firewall,<blank>,cisco
Cisco,PIX,enable,<blank>
Cisco,RAN201,admin,admin
Cisco,RTP300 W/2 PHONE PORTS,admin,admin
Cisco,RTP300 W/2 PHONE PORTS,user,tivonpw
Cisco,RV0041 (Linksys),admin,admin
Cisco,RV042 (Linksys),admin,admin
Cisco,RV042 v3,admin,admin
Cisco,RV042,admin,admin
Cisco,RV042G,admin,admin
Cisco,RV082 (Linksys),admin,admin
Cisco,RV082 v3,admin,admin
Cisco,RV120W,cisco,cisco
Cisco,RV130,cisco,cisco
Cisco,RV180,cisco,cisco
Cisco,RV215W,cisco,cisco
Cisco,RV220W,cisco,cisco
Cisco,RV315W,cisco,cisco
Cisco,RV320,cisco,cisco
Cisco,RV340W,cisco,cisco
Cisco,Router,<blank>,<blank>
Cisco,SF300,cisco,cisco
Cisco,VEN401,ATTadmin,401!VEN
Cisco,VPN 3000 Concentrator,admin,admin
Cisco,VPN Concentrator 3000 series,admin,admin
Cisco,Valet Plus M20,admin,admin
Cisco,WAP131,cisco,cisco
Cisco,WAP200,admin,admin
Cisco,WAP2000,admin,admin
Cisco,WAP200E,admin,admin
Cisco,WAP371,cisco,cisco
Cisco,WAP4410N,admin,admin
Cisco,WAP551,cisco,cisco
Cisco,WAP561,cisco,cisco
Cisco,WAP581,cisco,cisco
Cisco,WLSE,root,blender
Cisco,WLSE,wlse,wlsedb
Cisco,WLSE,enable,<blank>
Cisco,WSLE,wlseuser,wlsepassword
Cisco,aironet,<blank>,<blank>
Cisco,pix,<blank>,<blank>
Cisco-Arrowpoint,Arrowpoint,admin,system
Citel,Handset Gateway,citel,password
Citel,Handset Gateway,<blank>,citel
Cobalt,RaQ * Qube*,admin,admin
Colubris,MSC,admin,admin
Com21,General Equipment(?),<blank>,<blank>
Comcast Home Networking,Comcast Home Networking,comcast,<blank>
Comersus,Shopping Cart,admin,dmr99
Compaq,Armada E500,Administrator,admin
Compaq,Armada M700,Administrator,admin
Compaq,Insight Manager,PFCUser,240653C9467E45
Compaq,Insight Manager,administrator,administrator
Compaq,Insight Manager,anonymous,<blank>
Compaq,Insight Manager,operator,operator
Compaq,Insight Manager,user,public
Compaq,Insight Manager,user,user
Compaq,Insight Manager,<blank>,<blank>
Compaq,Management Agents,administrator,<blank>
Compaq,PC BIOS,<blank>,Compaq
Compaq,dc770t,<blank>,<blank>
Compualynx,Cmail Server,administrator,asecret
Compualynx,SCM,administrator,asecret
Comtrend,ct-536+,admin,1234
Comtrend,ct-536+,admin,admin
Conceptronic,C54BRS4,admin,1234
Concord,PC BIOS,<blank>,last
Conexant,Router,<blank>,admin
Conexant,Router,<blank>,epicrouter
Corecess,6808 APC,corecess,corecess
Corecess,Corecess 3112,Administrator,admin
Costar,IP Camera system,root,root
Coyote-Point,Equaliser 4,eqadmin,equalizer
Coyote-Point,Equaliser 4,root,<blank>
Crestron,AM-100,admin,admin
Crestron,DM-NVX-3XX,admin,admin
Crestron,DM-XIO-DIR-XX,admin,admin
Crestron,Mercury,admin,admin
Crossbeam,COS/XOS,<blank>,x40rocks
Crystalview,OutsideView 32,<blank>,Crystal
CyberMax,PC BIOS,<blank>,Congress
CyberPower,Remote Management Card RMCARD302,cyber,cyber
CyberPower,Remote Management Card RMCARD302,device,cyber
Cyberguard,all firewalls,cgadmin,cgadmin
Cyclades,Cyclades-TS800,root,<blank>
Cyclades,MP/RT,super,surt
Cyclades,PR 1000,super,surt
Cyclades,TS800,root,tslinux
D-LINK,DSL-G664T,admin,admin
D-Link,AC1200,admin,admin
D-Link,AC1740,admin,admin
D-Link,AC1750,admin,1234
D-Link,Cable/DSL Routers/Switches,<blank>,admin
D-Link,D-704P,admin,admin
D-Link,D-704P,admin,<blank>
D-Link,DCM-604,admin,password
D-Link,DFE-538TX 10/100 Adapter,<blank>,<blank>
D-Link,DFL-300,admin,admin
D-Link,DGN2200M,admin,dareadsl
D-Link,DI-101,<blank>,meet
D-Link,DI-104,<blank>,admin
D-Link,DI-106 ISDN router,<blank>,1234
D-Link,DI-514,user,<blank>
D-Link,DI-524,Alphanetworks,wrgg15_di524
D-Link,DI-524,admin,<blank>
D-Link,DI-524,user,<blank>
D-Link,DI-604,admin,<blank>
D-Link,DI-604,admin,<blank>
D-Link,DI-604,admin,admin
D-Link,DI-604,admin,<blank>
D-Link,DI-614+,admin,admin
D-Link,DI-614+,user,<blank>
D-Link,DI-614+,admin,<blank>
D-Link,DI-624+,admin,admin
D-Link,DI-624,User,<blank>
D-Link,DI-624,admin,<blank>
D-Link,DI-634M,admin,<blank>
D-Link,DI-701,<blank>,year2000
D-Link,DI-704,<blank>,admin
D-Link,DI-704,<blank>,admin
D-Link,DI-704,<blank>,admin
D-Link,DI-804,admin,<blank>
D-Link,DIR-610,admin,<blank>
D-Link,DIR-615,admin,<blank>
D-Link,DIR-650IN,admin,admin
D-Link,DIR-835,admin,<blank>
D-Link,DSA-31003,admin,admin
D-Link,DSA-51003,admin,admin
D-Link,DSL-2750U,admin,admin
D-Link,DSL-300g+,admin,admin
D-Link,DSL-302G,admin,admin
D-Link,DSL-500,admin,admin
D-Link,DSR-1000,admin,admin
D-Link,DWL 1000,admin,<blank>
D-Link,DWL 2100AP,admin,<blank>
D-Link,DWL 900AP,<blank>,public
D-Link,DWL 900AP,admin,public
D-Link,DWL-2000AP+,admin,<blank>
D-Link,DWL-614+,admin,<blank>
D-Link,DWL-614+,admin,<blank>
D-Link,DWL-900+,admin,<blank>
D-Link,DWL-G730AP,admin,<blank>
D-Link,Dl 604,admin,<blank>
D-Link,Dsl-300g+,<blank>,private
D-Link,G624T,admin,admin
D-Link,WBR-1310,admin,<blank>
D-Link,firewall,admin,admin
D-Link,hubs/switches,D-Link,D-Link
D-link,504g adsl router,admin,admin
D-link,DSL-504T,admin,admin
D-link,DSL-G604T,admin,admin
D-link,DSL500G,admin,admin
D-link,DWL-900AP+,admin,<blank>
D-link,Di-707p router,admin,<blank>
D-link,ads500g,admin,admin
D9287ar,Pavilion6640c,Clarissa,<blank>
DELL,REMOTE ACCESS CARD,root,calvin
DI624,D-LINK,admin,password
DIGICOM,Michelangelo Wave108,root,admin
DLINK,604,<blank>,admin
DLink,DI-206 ISDN router,Admin,Admin
DVTel,IP Camera system,Admin,1234
DZS - DASAN Zhone,ZNID-GPON-2426A-EU,user,user
Daewoo,PC BIOS,<blank>,Daewuu
Dahua,IP Camera system,admin,admin
Dallas Semiconductors,TINI embedded JAVA Module,root,tini
Datacom,BSASX/101,<blank>,letmein
Datawizard.net,FTPXQ server,anonymous,any@
Davolink,DV2020,user,user
Davox,Unison,admin,admin
Davox,Unison,davox,davox
Davox,Unison,root,davox
Davox,Unison,sa,<blank>
Daytek,PC BIOS,<blank>,Daytec
Debian,Linux LILO Default,<blank>,tatercounter2000
Deerfield,MDaemon,MDaemon,MServer
Deerfield,MDaemon,MDaemon,MServer
Dell,2161DS Console Switch,Admin,<blank>
Dell,CSr500xt,<blank>,admin
Dell,LATITUDE,<blank>,<blank>
Dell,Laser Printer 3000cn / 3100cn,admin,password
Dell,Latitude,<blank>,1RRWTTOOI
Dell,PC BIOS,<blank>,Dell
Dell,PowerApp Web 100 Linux,root,powerapp
Dell,PowerConnect 2724,admin,<blank>
Dell,PowerVault 50F,root,calvin
Dell,Remote Access Card,root,calvin
Dell,TrueMobile 1184 Wireless Broadband Gateway Router,admin,admin
Dell,WRTA-108GD,admin,admin
Dell,bios,<blank>,<blank>
Dell,c600,<blank>,<blank>
Dell,cpx h500gt,<blank>,<blank>
Dell,dell latitude cpx,admin,admin
Dell,latitude c610,admin,admin
Dell,notebook,<blank>,<blank>
Demarc,Network Monitor,admin,my_DEMARC
Deutsch Telekomm,T-Sinus 130 DSL,<blank>,0
Deutsche Telekom,T-Sinus 1054 DSL,<blank>,0
Deutsche Telekom,T-Sinus 154 DSL,<blank>,0
Deutsche Telekom,T-Sinus DSL 130,admin,<blank>
Develcon,Orbitor Default Console,<blank>,BRIDGE
Develcon,Orbitor Default Console,<blank>,password
Dictaphone,ProLog,NETOP,<blank>
Dictaphone,ProLog,NETWORK,NETWORK
Dictaphone,ProLog,PBX,PBX
Digiboard,Portserver 8 & 16,root,dbps
Digicom,Michelangelo,admin,michelangelo
Digicom,Michelangelo,user,password
Digicorp,Router,<blank>,BRIDGE
Digicorp,Router,<blank>,password
Digicorp,Viper,<blank>,BRIDGE
Digicorp,Viper,<blank>,password
Digital,DEC-10,2,maintain
Dlink,DFE-538TX 10/100 Adapter,<blank>,<blank>
Dlink,DSL-500,admin,admin
Dlink,Dl-106 ISDN router,<blank>,1234
Draytek,Vigor 2600,admin,<blank>
Draytek,Vigor 2900+,admin,admin
Draytek,Vigor,admin,admin
Draytek,Vigor3300 series,draytek,1234
Drs,IP Camera system,admin,1234
Dupont,Digital Water Proofer,root,par0t
DynaColor,IP Camera system,admin,1234
Dynalink,RTA020,admin,admin
Dynalink,RTA230,admin,admin
E-Con,Econ DSL Router,admin,epicrouter
E-Tech,ADSL Ethernet Router,admin,epicrouter
E-Tech,ADSL Ethernet Router,admin,epicrouter
E-Tech,Router,<blank>,admin
E-Tech,Wireless 11Mbps Router Model:WLRT03,<blank>,admin
E-Tech,Wireless 11Mbps Router,<blank>,admin
ECI,,admin,password
ECI,Any,<blank>,<blank>
EMC,DS-4100B,admin,<blank>
ETISYS,Printer,admin,1111
Edimax,Broadband Router,admin,1234
Edimax,ES-5224RXM,admin,123
Edimax,EW-7205APL,guest,<blank>
Edimax,EW-7206APG,admin,1234
Edimax,Edimax Fast Ethernet Switch,admin,password
Edimax,PS-1203/PS-1205Um/PS-3103,admin,<blank> OR su@psir
Edimax,PS-1208MFG,edimax,software01
Efficient Networks,5851 SDSL Router,<blank>,hs7mwxkk
Efficient Networks,EN 5861,login,admin
Efficient Networks,Speedstream 5711,<blank>,4getme2
Efficient,,<blank>,<blank>
Efficient,5851,login,password
Efficient,5871 DSL Router,login,admin
Efficient,Speedstream DSL,<blank>,admin
Elron,Firewall,hostname/ ip address,sysadmin
Elsa,LANCom Office ISDN Router,<blank>,cisco
Enox,PC BIOS,<blank>,xo11nE
Enterasys,ANG-1105,admin,netadmin
Enterasys,ANG-1105,<blank>,netadmin
Enterasys,ANG-1105,<blank>,netadmin
Enterasys,Vertical Horizon,admin,<blank>
Enterasys,Vertical Horizon,tiger,tiger123
Entrust,getAccess,websecadm,changeme
Epox,PC BIOS,<blank>,central
Ericsson ACC,Tigris Platform,public,<blank>
Ericsson,ACC,netman,netman
Ericsson,BP250,admin,default
Ericsson,Ericsson Acc,netman,netman
Ericsson,MD110,MD110,help
Ericsson,SBG,expert,expert
Ericsson,md110 pabx,<blank>,help
Erpepe,ADSL Router,chochete,tiabuena
EverFocus,PowerPlex,admin,admin
EverFocus,PowerPlex,operator,operator
EverFocus,PowerPlex,supervisor,supervisor
Exabyte,Magnum20,anonymous,Exabyte
Excitel,Wireless AP,admin,exc@123
Extended Systems,Print Servers,admin,extendnet
Extreme Networks,All Switches,admin,<blank>
Extreme,All,Admin,<blank>
F5,Bigip 540,root,default
F5-Networks,BIGIP,<blank>,<blank>
Fast-wi,COOG001,admin,admin
Fastwire,Fastwire Bank Transfer,fastwire,fw
Fastwire,Fastwire Bank Transfer,fastwire,fw
FiberDriver,N-Base Switches,<blank>,forgot
Fiberhome,HG6243C,user,user1234
Flir,IP Camera system,admin,fliradmin
Flowpoint,100 IDSN,admin,admin
Flowpoint,144,<blank>,password
Flowpoint,2200 SDSL,admin,admin
Flowpoint,2200,<blank>,Serial Num
Flowpoint,40 IDSL,admin,admin
Flowpoint,DSL,<blank>,password
Flowpoint,DSL,admin,admin
Flowpoint,Flowpoint 2200,<blank>,Serial Number
Flowpoint,Flowpoint DSL,admin,admin
Fortinet,Fortigate,maintainer,admin
Fortinet,Fortigate,maintainer,bcpb+serial#
Fortinet,Fortigate,admin,<blank>
Foscam,IP Camera system,admin,<blank>
Foundry Networks,IronView Network Manager,admin,admin
Freetech,BIOS,<blank>,Posterie
Freetech,PC BIOS,<blank>,Posterie
FritzBox,Wireless,admin,admin
FritzBox,Wireless,admin,admin
FritzBox,Wireless,admin,admin
FritzBox,Wireless,admin,fritzfonbox
FritzBox,Wireless,admin,admin
FritzBox,Wireless,admin,admin
FritzBox,Wireless,admin,admin
FritzBox,Wireless,admin,admin
FritzBox,Wireless,admin,admin
FritzBox,Wireless,admin,admin
Fujitsu Siemens,Fibre Channel SAN storage FX 60,manage,!manage
Fujitsu Siemens,Fibre Channel SAN storage FX 60,manage,!manage
Fujitsu Siemens,Fibre Channel SAN storage,manage,!manage
Fujitsu Siemens,Fibre Channel SAN storage,manage,!manage
Fujitsu Siemens,Routers,<blank>,connect
Funk Software,Steel Belted Radius,admin,radius
GVC,e800/rb4,Administrator,admin
GVI,IP Camera system,Admin,1234
Galacticomm,Major BBS,Sysop,Sysop
GarrettCom,Magnum Switch,manager,manager
Gateway,Solo,<blank>,<blank>
GeoVision,IP Camera system,admin,admin
Gericom,Phoenix,Administrator,<blank>
Gigabyte,Gigabyte,<blank>,<blank>
GoNET,General Equipment(?),fast,adb234
Google,Urchin,admin,urchin
Grandstream,GXP-2000,admin,1234
Grandstream,IP Camera system,admin,admin
GuardOne,BizGuard,n.a,guardone
Guru,Wireless ADSL2,admin,admin
H2 Database,H2,sa,<blank>
HC-05 Bluetooth Module,HC-05 for Arduino,<blank>,1234
HIKVision,IP Camera system,admin,12345
HP,E1200,root,password
HP,HP 1820-24G-PoE+ J9983A,admin,<blank>
HP,HP 2000/3000 MPE/XX,HELLO,OP.OPERATOR
HP,HP 2000/3000 MPE/XX,MGR,ITF3000
HP,HP 2000/3000 MPE/XX,MGR,NETBASE
HP,ISEE,admin,isee
HP,MSL Series Libraries,Factory,56789
HP,t5000 Thin Client series,Administrator,admin
Hewlett Packard,Power Manager,admin,admin
Hewlett-Packard,HP 2000/3000 MPE/xx,ADVMAIL,HP
Hewlett-Packard,HP 2000/3000 MPE/xx,ADVMAIL,HPOFFICE DATA
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,HPONLY
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,HPP187 SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,HPWORD PUB
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,LOTUS
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,MANAGER
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,MGR
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,SERVICE
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,SUPPORT
Hewlett-Packard,HP 2000/3000 MPE/xx,HELLO,FIELD.SUPPORT
Hewlett-Packard,HP 2000/3000 MPE/xx,HELLO,MANAGER.SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,HELLO,MGR.SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,HELLO,OP.OPERATOR
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,MAIL
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,MPE
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,REMOTE
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,TELESUP
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,COGNOS
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,ITF3000
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,SECURITY
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,TCH
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,TELESUP
Hewlett-Packard,HP 2000/3000 MPE/xx,MGE,VESOFT
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,CAROLIAN
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,CCC
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,CNAS
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,COGNOS
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,CONV
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPDESK
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPONLY
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPP187
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPP189
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPP196
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,INTX3
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,ITF3000
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,NETBASE
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,REGO
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,RJE
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,ROBELLE
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,SECURITY
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,TELESUP
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,VESOFT
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,WORD
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,XLSERVER
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,COGNOS
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,DISC
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,SUPPORT
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,SYSTEM
Hewlett-Packard,HP 2000/3000 MPE/xx,PCUSER,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,RSBCMON,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,SPOOLMAN,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,WP,HPOFFICE
Hewlett-Packard,LaserJet Net Printers,<blank>,<blank>
Hewlett-Packard,LaserJet Net Printers,<blank>,<blank>
Hewlett-Packard,LaserJet Net Printers,<blank>,<blank>
Hewlett-Packard,LaserJet Net Printers,Anonymous,<blank>
Hewlett-Packard,LaserJet Net Printers,<blank>,<blank>
Hewlett-Packard,LaserJet Net Printers,<blank>,<blank>
Hewlett-Packard,Omnibook XE3,<blank>,<blank>
Hewlett-Packard,Vectra,<blank>,hewlpack
Hewlett-Packard,notebook,<blank>,<blank>
Hewlett-Packard,omnibook 4150b,<blank>,(nessun)
Hewlett-Packard,omnibook,<blank>,admin
Hewlett-Packard,omnibook6000,<blank>,<blank>
Hewlett-Packard,webmin,admin,hp.com
Hitron Technologies,CGN5-AP Router,admin,password
Hitron Technologies,CGN5-AP Router,msoadmin,kbro-TFM
Hitron Technologies,CGNV5-MAX Router,cusadmin,password
Hitron,CGNM-3550,cusadmin,password
Honeywell,IP Camera system,administrator,1234
Huawei,4G wingle,admin,admin
Huawei,All Router Models,admin,Admin@huawei
Huawei,All Router Models,admin,admin@huawei.com
Huawei,E960,admin,admin
Huawei,EchoLife,admin,1DF5E3ERFF6C
Huawei,HG531 v1,admin,@HuaweiHgw
Huawei,HG8245H,root,admin
Huawei,Home Gateway HG255s,admin,superonline
Huawei,MT880,admin,admin
Huawei,MT880r,TMAR#HWMT8007079,<blank>
Huawei,S2700,admin,admin@huawei.com
Huawei,S3700,admin,admin@huawei.com
Huawei,S5700,admin,admin@huawei.com
Huawei,S6700,admin,admin@huawei.com
Huawei,mt820,admin,admin
Hyland Software Inc.,Nuxeo,Administrator,Administrator
IBM,2210,def,trade
IBM,2628,<blank>,<blank>
IBM,3534 F08 Fibre Switch,admin,password
IBM,3583 Tape Library,admin,secure
IBM,390e,<blank>,admin
IBM,600x,<blank>,admin
IBM,8224 HUB,vt100,public
IBM,8225,I5rDv2b2JjA8Mm,A52896nG93096a
IBM,8239 Token Ring HUB,<blank>,R1QTPS
IBM,A21m,<blank>,<blank>
IBM,AIX,guest,<blank>
IBM,AIX,root,ibm
IBM,AS/400,qpgmr,qpgmr
IBM,AS/400,QUSER,QUSER
IBM,AS400,QSRV,QSRV
IBM,Ascend OEM Routers,<blank>,ascend
IBM,BladeCenter Mgmt Console,USERID,PASSW0RD
IBM,DB2,db2admin,db2admin
IBM,Directory - Web Administration Tool,superadmin,secret
IBM,Hardware Management Console,hscroot,abc123
IBM,Hardware Management,hscroot,abc123
IBM,IBM,<blank>,<blank>
IBM,Infoprint 6700,root,<blank>
IBM,LAN Server OS,username,password
IBM,Lotus Domino Go Web Server (net.commerce edition),webadmin,webibm
IBM,OS/400,11111111,11111111
IBM,OS/400,ibm,password
IBM,OS/400,ibm,service
IBM,OS/400,qsecofr,22222222
IBM,OS/400,qsecofr,qsecofr
IBM,OS/400,qsrv,qsrv
IBM,OS/400,qsvr,qsvr
IBM,OS/400,qsysopr,qsysopr
IBM,OS/400,secofr,secofr
IBM,OS/400,sysopr,sysopr
IBM,PC BIOS,<blank>,IBM
IBM,PC BIOS,<blank>,sertafu
IBM,POS CMOS,ESSEX,<blank>
IBM,RS/6000,root,ibm
IBM,Remote Supervisor Adapter (RSA),USERID,PASSW0RD
IBM,T20,<blank>,admin
IBM,T42,Administrator,admin
IBM,Tivoli,admin,admin
IBM,TotalStorage Enterprise Server,storwatch,specialist
IBM,VM/CMS,$ALOC$,<blank>
IBM,VM/CMS,AP2SVP,<blank>
IBM,VM/CMS,AUTOLOG1,<blank>
IBM,VM/CMS,BATCH1,<blank>
IBM,VM/CMS,CCC,<blank>
IBM,VM/CMS,CMSUSER,<blank>
IBM,VM/CMS,CPRM,<blank>
IBM,VM/CMS,CVIEW,<blank>
IBM,VM/CMS,DEMO1,<blank>
IBM,VM/CMS,DEMO3,<blank>
IBM,VM/CMS,DIRECT,<blank>
IBM,VM/CMS,DISKCNT,<blank>
IBM,VM/CMS,FSFADMIN,<blank>
IBM,VM/CMS,FSFTASK2,<blank>
IBM,VM/CMS,IDMS,<blank>
IBM,VM/CMS,IIPS,<blank>
IBM,VM/CMS,ISPVM,<blank>
IBM,VM/CMS,IVPM2,<blank>
IBM,VM/CMS,MOESERV,<blank>
IBM,VM/CMS,OLTSEP,<blank>
IBM,VM/CMS,OPERATNS,<blank>
IBM,VM/CMS,PENG,<blank>
IBM,VM/CMS,PRODBM,<blank>
IBM,VM/CMS,PSFMAINT,<blank>
IBM,VM/CMS,RDM470,<blank>
IBM,VM/CMS,RSCS,<blank>
IBM,VM/CMS,SAVSYS,<blank>
IBM,VM/CMS,SFCNTRL,<blank>
IBM,VM/CMS,SQLDBA,<blank>
IBM,VM/CMS,SYSADMIN,<blank>
IBM,VM/CMS,SYSDUMP1,<blank>
IBM,VM/CMS,SYSWRM,<blank>
IBM,VM/CMS,TEMP,<blank>
IBM,VM/CMS,VASTEST,<blank>
IBM,VM/CMS,VMARCH,<blank>
IBM,VM/CMS,VMASSYS,<blank>
IBM,VM/CMS,VMBSYSAD,<blank>
IBM,VM/CMS,VMTAPE,<blank>
IBM,VM/CMS,VMUTIL,<blank>
IBM,VM/CMS,VSEMAINT,<blank>
IBM,VM/CMS,VTAM,<blank>
IBM,a20m,<blank>,admin
IBM,ra6000,<blank>,<blank>
IBM,switch,admin,<blank>
IBM,thinkpad,<blank>,<blank>
IMAI,Traffic Shaper,<blank>,<blank>
INFOSMART,SOHO ROUTER,admin,0 or 0000
INOVA,ONT4BKP (IP clock),iclock,timely
IOImage,IP Camera system,admin,admin
IPX-DDK,IP Camera system,root,Admi<blank>dmin
IQInvision,IP Camera system,root,system
IRC,IRC Daemon,<blank>,FOOBAR
IRCXPro,IRCXPro Server,admin,password
IRIS,,PDP11,User
Iammeter,WEM3080,admin,admin
Iammeter,WEM3080T,admin,admin
Iiawmd,web page,<blank>,<blank>
Infoblox,INFOBLOX Appliance,admin,<blank>
Informix,Database,informix,informix
Infosmart,SOHO router,admin,0
Integral Technologies,RemoteView,Administrator,letmein
Integral,RemoteView,Administrator,letmein
Intel,460T Express Switch,<blank>,<blank>
Intel,510T,<blank>,admin
Intel,All Routers,<blank>,babbit
Intel,Express 520T Switch,setup,setup
Intel,Express 9520 Router,NICONEX,NICONEX
Intel,LanRover VPN Gateway,<blank>,shiva
Intel,Shiva,Guest,<blank>
Intel,Shiva,root,<blank>
Intel,Shiva,root,<blank>
Intel,Wireless AP 2011,<blank>,Intel
Intel,Wireless Gateway,intel,intel
Intel,lan rover,root,admin
Intel,netstructure,admin,<blank>
Intel,wireless lan access Point,<blank>,comcomcom
Intel/Shiva,Access Port,admin,hello
Intel/Shiva,Mezza ISDN Router,admin,hello
Intelbras,WRN300,admin,admin
Interbase,Interbase Database Server,SYSDBA,masterkey
Intermec,Mobile LAN,intermec,intermec
Intershop,Intershop,operator,$chwarzepumpe
Intersystems,Cache Post-RDMS,system,sys
Intex,organizer,<blank>,<blank>
Intracom,jetSpeed,admin,admin
Inventel,Livebox,admin,admin
Ipswitch,Whats up Gold,admin,admin
IronPort,Messaging Gateway Appliance,admin,ironport
Irongate,NetSurvibox 266,admin,NetSurvibox
Iwill,PC BIOS,<blank>,iwill
JAHT,adsl router,admin,epicrouter
JD Edwards,WorldVision/OneWorld,JDE,JDE
JDE,WorldVision/OneWorld,PRODDTA,PRODDTA
JDS Microprocessing,Hydra 3000,hydrasna,<blank>
JDS,Hydra 3000,hydrasna,<blank>
JVC,IP Camera system,admin,Model# of camera
JetWay,PC BIOS,<blank>,spooml
Jetform,Jetform Design,Jetform,<blank>
Jio,Jio Centrum,admin,Jiocentrum
Jio,JioFi M2,admin,admin
Jio,JioFi,admin,admin
Jio,JioFi,administrator,administrator
Jio,JioFi-JDR740,admin,admin
Jio,JioFi-JMR815,admin,admin
Jio,JioFiber-Un339,admin,Etha1Mi0chaibie
Jio,JioFibre Router,admin,Jiocentrum
JioFi,Web UI,administrator,administrator
Juniper,All,root,<blank>
Juniper,ISG2000,netscreen,netscreen
Juniper,Netscreen,serial#,serial#
KASDA,KD318-MUI,admin,adslroot
KASDA,KD318-MUI,admin,adslroot
KTI,KS-2260,superuser,123456
KTI,KS2260,admin,123
KTI,KS2600,admin,123456
Kalatel,Calibur DSR-2000e,<blank>,3477
Kalatel,Calibur DSR-2000e,<blank>,8111
Kawa,All,<blank>,<blank>
Knox,Arkeia Server,root,<blank>
Konica Minolta,magicolor 1690MF,(non),sysAdmin
Konica Minolta,magicolor 2300 DL,<blank>,1234
Konica Minolta,magicolor 2430DL,<blank>,<blank>
Konica Minolta,magicolor 5430 DL,admin,administrator
Konica/ Minolta,Di 2010f,<blank>,0
Kyocera Printers,2020D,<blank>,admin00
Kyocera,EcoLink,<blank>,PASSWORD
Kyocera,FS-2020D,<blank>,admin00
Kyocera,Intermate LAN FS Pro 10/100,admin,admin
Kyocera,Printer,<blank>,admin00
Kyocera,Telnet Server IB-20/21,root,root
LANCAST,All,<blank>,<blank>
LANCOM,IL11,<blank>,<blank>
LAXO,IS-194G,admin,admin
LG,Aria iPECS,<blank>,jannie
LG,LAM200E/LAM200R,admin,epicrouter
LG,LG TV,<blank>,0
LG,LG-N1T1DD1,admin,admin
LGIC,Goldstream,LR-ISDN,LR-ISDN
LOGITECH,LOGITECH MOBILE HEADSET,<blank>,0 or 0000
LTS Security,IP Camera system,admin,12345
LUCENT,M770,super,super
Lanier,Digital Imager,admin,<blank>
Lanier,LD335,supervisor,<blank>
Lantronics,Lantronics Terminal Server,<blank>,access
Lantronics,Lantronics Terminal Server,<blank>,system
Lantronix,ETS16P,<blank>,<blank>
Lantronix,ETS32PR,<blank>,<blank>
Lantronix,ETS422PR,<blank>,<blank>
Lantronix,ETS4P,<blank>,<blank>
Lantronix,LPS1-T Print Server,any,system
Lantronix,LSB4,<blank>,system
Lantronix,Lantronix Terminal,<blank>,lantronix
Lantronix,MSS110/MSSVIA/UDS10,<blank>,system
Lantronix,SCS100,<blank>,access
Lantronix,SCS1620,sysadmin,PASS
Lantronix,SCS200,<blank>,admin
Lantronix,SCS3200,login,access
Lantronix,SCS3200,login,access
Lantronix,SCS400,<blank>,admin
Lantronix,Terminal Server,<blank>,access
Lantronix,Terminal Server,<blank>,lantronix
Laradock,MySQL,default,secret
Laradock,MySQL,root,root
Lenel,OnGuard,admin,admin
Leviton,47611-GT5,admin,leviton
LinkSys,WAP11,<blank>,<blank>
Linksys,ADSLME3,root,orion99
Linksys,AG 241 - ADSL2 Gateway with 4-Port Switch,admin,admin
Linksys,BEFSR41,<blank>,admin
Linksys,BEFW11S4,admin,<blank>
Linksys,Comcast,comcast,1234
Linksys,DSL,<blank>,admin
Linksys,EtherFast Cable/DSL ROuter,Administrator,admin
Linksys,EtherFast Cable/DSL Router,Administrator,admin
Linksys,Linksys DSL,<blank>,admin
Linksys,Linksys Router DSL/Cable,<blank>,admin
Linksys,WAG354G,admin,admin
Linksys,WAG54G,admin,admin
Linksys,WAG54GS,admin,admin
Linksys,WAP11,<blank>,<blank>
Linksys,WAP54G,<blank>,admin
Linksys,WRT54G,admin,admin
Linksys,WRT54G,<blank>,admin
Linksys,WRT54GS,admin,admin
Linksys,model WRT54GC compact wireless-G broadband router,<blank>,admin
Linksys,model WRT54GC compact,<blank>,admin
Linksys,rv082,admin,<blank>
Linksys/Cisco,RTP300 w/2 phone ports,admin,admin
Linksys/Cisco,RTP300 w/2 phone ports,user,tivonpw
Linunx,Linux,Administrator,admin
Linux Mint,Linux Mint Live session,mint,<blank>
Linux,Bankmandiri.co.id,Administrator,<blank>
Linux,Slackware,satan,<blank>
Linux,Slackware,satan,<blank>
Linux,UCLinux for UCSIMM,root,uClinux
Livingston,IRX Router,!root,<blank>
Livingston,IRX Router,!root,<blank>
Livingston,Livingston Portmaster 3,!root,<blank>
Livingston,Livingston officerouter,!root,blank
Livingston,Officerouter,!root,<blank>
Livingston,Officerouter,!root,<blank>
Livingstone,Portmaster 2R,root,<blank>
Lockdown Networks,All Lockdown Products,setup,changeme (exclamation)
Lockdown,All Lockdown Products,setup,changeme (exclamation)
LogiLink,WL0026,admin,1234
Logitech,Logitech Mobile Headset,<blank>,0
Lucent,AP-1000,public,private
Lucent,AP-1000,public,public
Lucent,Anymedia,LUCENT01,UI-PSWD-01
Lucent,Anymedia,LUCENT01,UI-PSWD-01
Lucent,Anymedia,LUCENT02,UI-PSWD-02
Lucent,Anymedia,LUCENT02,UI-PSWD-02
Lucent,B-STDX9000,(any 3 characters),cascade
Lucent,B-STDX9000,<blank>,cascade
Lucent,B-STDX9000,<blank>,cascade
Lucent,CBX 500,(any 3 characters),cascade
Lucent,CBX 500,<blank>,cascade
Lucent,CBX 500,<blank>,cascade
Lucent,Cajun Family,root,root
Lucent,Cellpipe 22A-BX-AR USB D,admin,AitbISP4eCiG
Lucent,Cellpipe,<blank>,admin
Lucent,GX 550,(any 3 characters),cascade
Lucent,GX 550,<blank>,cascade
Lucent,GX 550,<blank>,cascade
Lucent,MAX,<blank>,<blank>
Lucent,MAX-TNT,admin,Ascend
Lucent,PSAX 1200 and below,root,ascend
Lucent,PSAX 1250 and above,readonly,lucenttech2
Lucent,PSAX 1250 and above,readonly,lucenttech2
Lucent,PSAX 1250 and above,readwrite,lucenttech1
Lucent,PSAX 1250 and above,readwrite,lucenttech1
Lucent,PacketStar,Administrator,<blank>
Lucent,Packetstar (PSAX),readwrite,lucenttech1
Lucent,Portmaster 2,!root,<blank>
Lucent,System 75,bciim,bciimpw
Lucent,System 75,bcim,bcimpw
Lucent,System 75,bcms,bcmspw
Lucent,System 75,bcnas,bcnaspw
Lucent,System 75,blue,bluepw
Lucent,System 75,browse,browsepw
Lucent,System 75,browse,looker
Lucent,System 75,craft,craft
Lucent,System 75,craft,craftpw
Lucent,System 75,cust,custpw
Lucent,System 75,enquiry,enquirypw
Lucent,System 75,field,support
Lucent,System 75,inads,inads
Lucent,System 75,inads,indspw
Lucent,System 75,init,initpw
Lucent,System 75,locate,locatepw
Lucent,System 75,maint,maintpw
Lucent,System 75,maint,rwmaint
Lucent,System 75,nms,nmspw
Lucent,System 75,rcust,rcustpw
Lucent,System 75,support,supportpw
Lucent,System 75,tech,field
M-M-O,Webrealm,Administrator,admin
MERCURY,234234,Administrator,admin
MERCURY,KT133A/686B,Administrator,admin
MICROSOFT,NT,free user,user
MX Linux,MX Linux Live Medium,demo,demo
MX Linux,MX Linux Live Medium,root,root
MX Linux,MX Linux,Free4Me,free4me
MacSense,X-Router Pro,admin,admin
MachSpeed,PC BIOS,<blank>,sp99dd
Macromedia,Dreamweaver,<blank>,admin
Magic-Pro,PC BIOS,<blank>,prost
Mambo,Site Server,admin,admin
Manjaro,Manjaro Live System,manjaro,user access
Manjaro,Manjaro Live System,manjaro,sudo access
March Networks,IP Camera system,admin,<blank>
Marconi,Fore ATM Switches,ami,<blank>
McAfee,SCM 3100,scmadmin,scmchangeme
McData,FC Switches/Directors,Administrator,password
McData,i10k Switch,McdataSE,redips
Mediatrix,MDD 2400/2600,administrator,<blank>
Megastar,BIOS,<blank>,star
Megastar,PC BIOS,<blank>,star
Mentec,Micro/RSX,MICRO,RSX
Mentec,Micro/RSX,MICRO,RSX
Meridian,PBX,service,smile
Meridian,PBX,service,smile
Merit Lilin,IP Camera system,Camera,admin pass
Merit Lilin,IP Camera system,Recorder,admin / 1111
Messoa,IP Camera system,admin,Model# of camera
Micron,,<blank>,<blank>
Micron,PC BIOS,<blank>,xyzall
Micronet,3351 / 3354,admin,epicrouter
Micronet,Access Point,root,default
Micronet,Micronet SP5002,mac,<blank>
Micronics,PC BIOS,<blank>,dn_04rjc
Microplex,Print Server,root,root
Microprocessing,,<blank>,<blank>
Microsoft,Base Station Access Point,<blank>,admin
Microsoft,MN-500 Wireless Base Station,admin,admin
Microsoft,SQL Server,sa,(blank)
Microsoft,Windows NT,(null),<blank>
Microsoft,Windows NT,Guest,<blank>
Microsoft,Windows NT,User,User
Microsoft,Windows NT,Administrator,<blank>
Microsoft,Windows NT,Guest,<blank>
Microsoft,Windows NT,Mail,<blank>
MikroTik,All Routers,admin,<blank>
Mikrotik,Mikrotik,admin,<blank>
Mikrotik,Router OS,admin,<blank>
Mikrotik,Router OS,admin,<blank>
Mikrotik,Router OS,admin,<blank>
Milan,mil-sm801p,root,root
Minolta PagrPro,QMS 4100GN PagePro,<blank>,sysadm
Minolta QMS,Magicolor 3100,admin,<blank>
Minolta QMS,Magicolor 3100,operator,<blank>
Mintel,Mintel PBX,<blank>,SYSTEM
Mitel,3300 ICP,system,password
Mitel,5320 IP Phone,<blank>,1111
Mitel,5330e IP Phone,<blank>,1111
Mitel,6900 Series IP Phones,<blank>,73738
Mitel,SX2000,<blank>,<blank>
MitraStar,GPT-2541GNAC,admin,1234
Mobotix,IP Camera system,admin,meinsm
Motorola,Cablerouter,cablecom,router
Motorola,Motorola Cablerouter,cablecom,router
Motorola,Motorola-Cablerouter,cablecom,router
Motorola,SBG900,admin,motorola
Motorola,SURFboard,admin,motorola
Motorola,WR850G,admin,motorola
Motorola,Wireless Router,admin,motorola
Multi-Tech,ProxyServer,supervisor,<blank>
Mutare Software,EVM Admin,<blank>,admin
Mutare,EVM Admin,<blank>,admin
MySQL,MySQL,root,<blank>
NAI,Entercept,GlobalAdmin,GlobalAdmin
NAI,Intrushield IPS,admin,admin123
NAI,Intrushield IPS,admin,admin123
NCR,NCR UNIX,ncrm,ncrm
NEC,WARPSTAR-BaseStation,<blank>,<blank>
NETGEAR,DG834G,admin,password
NETIO 4All,PowerPDU 4C,admin,admin
NGSec,NGSecureWeb,admin,<blank>
NGSec,NGSecureWeb,admin,asd
NOKIA,7360,<blank>,9999
NOMADIX,AG5000,admin,<blank>
NRG or RICOH,DSc338 Printer,<blank>,password
Nanoteq,NetSeq firewall,admin,NetSeq
NeXT,,me,<blank>
NeXT,NeXTStep,root,NeXT
NetApp,NetCache,admin,NetCache
NetApp,ONTAP,admin,netapp!123
NetGear,Comcast,comcast,1234
NetGear,RM356,<blank>,1234
NetGear,WGT624,admin,password
NetGear,WGT624,admin,password
NetGenesis,NetAnalysis Web Reporting,naadmin,naadmin
Netcomm,NB1300,admin,password
Netgaer,RH328,<blank>,1234
Netgea,FR314,admin,password
Netgear,ADSL Modem DG632,admin,password
Netgear,CG814CCR,cusadmin,highspeed
Netgear,D6200,admin,password
Netgear,DM602,admin,password
Netgear,FR114P,admin,password
Netgear,FSM7326P 24+2 L3 mANAGED PoE Switch,admin,<blank>
Netgear,FSM7326P 24+2 L3 mANAGED,admin,<blank>
Netgear,FVS114,admin,password
Netgear,FVS318,admin,password
Netgear,FWG114P,<blank>,admin
Netgear,GS724t,<blank>,password
Netgear,GSM7224,admin,<blank>
Netgear,ISDN-Router RH348,<blank>,1234
Netgear,ME102,<blank>,private
Netgear,MR-314,admin,1234
Netgear,MR314,admin,1234
Netgear,MR814,admin,password
Netgear,MR814,admin,password
Netgear,Nighthawk AX8,PixelPenguin42,Admin
Netgear,RH338,<blank>,1234
Netgear,RH338,<blank>,1234
Netgear,RH438,<blank>,1234
Netgear,RH438/ISDN-Router RH348,<blank>,1234
Netgear,RO318,admin,1234
Netgear,RP114,admin,1234
Netgear,RP114,<blank>,1234
Netgear,RP614,admin,password
Netgear,RT112,admin,1250
Netgear,RT311,admin,1234
Netgear,RT311,admin,1234
Netgear,RT314,admin,1234
Netgear,RT314,admin,admin
Netgear,RT314,Admin,1234
Netgear,RT338,<blank>,1234
Netgear,ReadyNas Duo,admin,infrant1
Netgear,ReadyNas Duo,admin,netgear1
Netgear,Router/Modem,admin,password
Netgear,WG602,admin,password
Netgear,WG602,super,5777364
Netgear,WG602,super,5777364
Netgear,WG602,superman,21241036
Netgear,WG602,super,5777364
Netgear,WG602,superman,21241036
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,password
Netgear,WGR614,admin,draadloos
Netgear,WGT624,Gearguy,Geardog
Netgear,WGT634U,admin,password
Netgear,WPN824 / WPN824v2,admin,password
Netgear,Wifi Router,admin,password
Netgear,dg834g,admin,password
Netopia,3351,<blank>,<blank>
Netopia,4542,admin,noway
Netopia,455,<blank>,<blank>
Netopia,Netopia 7100,<blank>,<blank>
Netopia,Netopia 9500,netopia,netopia
Netopia,Netopia 9500,netopia,netopia
Netopia,R910,admin,<blank>
Netport,Express 10/100,setup,setup
Netscape,Netscape Enterprise Server,admin,admin
Netscape,Netscape Enterprise Server,admin,admin
Netscreen,,netscreen,netscreen
Netscreen,Firewall,netscreen,netscreen
Netscreen,NS-5/NS10/NS-100,netscreen,netscreen
Netscreen,firewall,admin,<blank>
Netscreen,firewall,Administrator,<blank>
Netscreen,firewall,operator,<blank>
Netstar,Netpilot,admin,password
Network Appliance,NetCache,admin,NetCache
Network Associates,WebShield Security Appliance e250,e250,e250changeme
Network Associates,WebShield Security Appliance e500,e500,e500changeme
Network Associates,WebShield Security,e250,e250changeme
Network Associates,WebShield Security,e500,e500changeme
Network Everywhere,NWR11B,<blank>,admin
NetworkICE,ICECap Manager,iceman,<blank>
Niksun,NetDetector,vcr,NetVCR
Nimble,BIOS,<blank>,xdfk9874t3
Nimble,PC BIOS,<blank>,xdfk9874t3
Nokia,ADSL router M1921,<blank>,nokia
Nokia,All Router Models,admin,<blank>
Nokia,DSL Router M1122,m1122,m1122
Nokia,G-2425G-A,admin,admin
Nokia,M1122,<blank>,Telecom
Nokia,M1921,<blank>,nokai
Nokia,MW1122,telecom,telecom
Nokia,MW1122,telecom,telecom
Norman,5.3,<blank>,<blank>
Nortel,Accelar (Passport) 1000 series routing switches,l2,l2
Nortel,Accelar (Passport) 1000 series routing switches,l3,l3
Nortel,Accelar (Passport) 1000 series routing switches,ro,ro
Nortel,Accelar (Passport) 1000 series routing switches,rw,rw
Nortel,Accelar (Passport) 1000 series routing switches,rwa,rwa
Nortel,Bay,<blank>,<blank>
Nortel,Baystack 350-24T,<blank>,secure
Nortel,Baystack 450T sw V.4.1.0.6,<blank>,secure
Nortel,Business Communications Manager,supervisor,PlsChgMe
Nortel,Contivity Extranet Switches,admin,setup
Nortel,Contivity,admin,setup
Nortel,Extranet Switches,admin,setup
Nortel,Matra 6501 PBX,<blank>,0
Nortel,Meridian 1 PBX,0,0
Nortel,Meridian CCR,ccrusr,ccrusr
Nortel,Meridian CCR,disttech,4tas
Nortel,Meridian CCR,maint,maint
Nortel,Meridian CCR,service,smile
Nortel,Meridian Link,disttech,4tas
Nortel,Meridian Link,maint,maint
Nortel,Meridian Link,mlusr,mlusr
Nortel,Meridian Link,service,smile
Nortel,Meridian MAX,maint,ntacdmax
Nortel,Meridian MAX,root,3ep5w2u
Nortel,Meridian MAX,service,smile
Nortel,Meridian PBX,login,0
Nortel,Meridian PBX,login,1111
Nortel,Meridian PBX,login,8429
Nortel,Meridian PBX,spcl,0
Nortel,Meridian,<blank>,<blank>
Nortel,Norstar Modular ICS,**ADMIN (**23646),ADMIN (23646)
Nortel,Norstar,266344,266344
Nortel,Passport 2430,Manager,<blank>
Nortel,Phone System,<blank>,266344
Nortel,Remote Annex 2000,admin,(ip address)
Nortel,Remote Office 9150,admin,root
Nortel,Shasta,admin,admin
Nortel,VPN Gateway,admin,admin
Northern,IP Camera system,admin,12345
Novell,NetWare,GATEWAY,<blank>
Novell,NetWare,CHEY_ARCHSVR,WONDERLAND
Novell,Netware,ADMIN,ADMIN
Novell,Netware,ARCHIVIST,<blank>
Novell,Netware,BACKUP,<blank>
Novell,Netware,CHEY_ARCHSVR,<blank>
Novell,Netware,FAX,<blank>
Novell,Netware,FAXUSER,<blank>
Novell,Netware,FAXWORKS,FAXWORKS
Novell,Netware,GATEWAY,<blank>
Novell,Netware,GUEST,GUEST
Novell,Netware,GUEST,GUESTGUEST
Novell,Netware,HPLASER,<blank>
Novell,Netware,LASER,<blank>
Novell,Netware,LASERWRITER,LASERWRITER
Novell,Netware,MAIL,<blank>
Novell,Netware,POST,<blank>
Novell,Netware,PRINT,<blank>
Novell,Netware,PRINTER,<blank>
Novell,Netware,ROOT,<blank>
Novell,Netware,ROUTER,<blank>
Novell,Netware,SUPERVISOR,NETFRAME
Novell,Netware,SUPERVISOR,NF
Novell,Netware,SUPERVISOR,SUPERVISOR
Novell,Netware,SUPERVISOR,SYSTEM
Novell,Netware,TEST,<blank>
Novell,Netware,USER_TEMPLATE,USER_TEMPLATE
Novell,Netware,WANGTEK,WANGTEK
Novell,Netware,WINDOWS_PASSTHRU,WINDOWS_PASSTHRU
Novell,Netware,WINSABRE,SABRE
Novell,iChain,<blank>,san fran 8
Novell,iChain/ICS,<blank>,root
NuCom,NC-WR764TGV,1234,1234
Nullsoft,Shoutcast,admin,changeme
Nullsoft,Shoutcast,admin,changeme
Nurit,PC BIOS,$system,<blank>
OCE,Printers,<blank>,0 and the number of OCE printer
OCS Inventory NG,OCS Inventory,admin,admin
ODS,1094 IS Chassis,ods,ods
OKI,6120e and 421n,admin,OkiLAN
OKI,C5700,root,the 6 last digit of the MAC adress
OMRON,MR104FH,<blank>,<blank>
OPEN Networks,812L,root,0P3N
OPNsense,OPNsense,root,OPNsense
ORiNOCO,Access Server,<blank>,orinoco
Offensive Security,Kali Linux,root,toor
Offensive Security,Kali Linux,kali,kali
Omnitronix,Data-Link,<blank>,SMDR
Omnitronix,Data-Link,<blank>,SUPER
Omuron,MR104FH,<blank>,<blank>
OpenConnect,OC://WebConnect Pro,admin,OCS
OpenConnect,OC://WebConnect Pro,adminstat,OCS
OpenConnect,OC://WebConnect Pro,adminuser,OCS
OpenConnect,OC://WebConnect Pro,adminview,OCS
OpenConnect,OC://WebConnect Pro,helpdesk,OCS
OpenNetAdmin,OpenNetAdmin,admin,admin
Openwave,MSP,cac_admin,cacadmin
Openwave,WAP Gateway,sys,uplink
Optivision,Nac 3000 & 4000,root,mpegvideo
Optus,Counter-Strike,Administrator,admin
Oracle,7 or later,system,manager
Oracle,7 or later,Scott,Tiger
Oracle,8i,internal,oracle
Oracle,Finacial Package,SAPR3,SAP
Oracle,Glassfish,admin,admin
Oracle,Oracle RDBMS,ADAMS,WOOD
Oracle,Oracle RDBMS,APPS,APPS
Oracle,Oracle RDBMS,AURORA@ORB@UNAUTHENTICATED,INVALID
Oracle,Oracle RDBMS,CTXSYS,CTXSYS
Oracle,Oracle RDBMS,DBSNMP,DBSNMP
Oracle,Oracle RDBMS,MDSYS,MDSYS
Oracle,Oracle RDBMS,NAMES,NAMES
Oracle,Oracle RDBMS,ORDPLUGINS,ORDPLUGINS
Oracle,Oracle RDBMS,OUTLN,OUTLN
Oracle,Oracle RDBMS,SYSADM,SYSADM
Oracle,Oracle RDBMS,SYSTEM,MANAGER
Oracle,Oracle RDBMS,MODTEST,YES
Oracle,Oracle RDBMS,MTYSYS,MTYSYS
Oracle,Oracle RDBMS,RMAIL,RMAIL
Oracle,Oracle RDBMS,SAMPLE,SAMPLE
Oracle,Oracle RDBMS,<blank>,<blank>
Oracle,Oracle RDBMS,AQUSER,AQUSER
Oracle,Oracle RDBMS,CATALOG,CATALOG
Oracle,Oracle RDBMS,CDEMOCOR,CDEMOCOR
Oracle,Oracle RDBMS,CDEMOUCB,CDEMOUCB
Oracle,Oracle RDBMS,COMPANY,COMPANY
Oracle,Oracle RDBMS,DEMO8,DEMO8
Oracle,Oracle RDBMS,EVENT,EVENT
Oracle,Oracle RDBMS,FND,FND
Oracle,Oracle RDBMS,GPLD,GPLD
Oracle,Oracle RDBMS,MILLER,MILLER
Oracle,Oracle RDBMS,POWERCARTUSER,POWERCARTUSER
Oracle,Oracle RDBMS,PUBSUB,PUBSUB
Oracle,Oracle RDBMS,SECDEMO,SECDEMO
Oracle,Oracle RDBMS,TSDEV,TSDEV
Oracle,Oracle RDBMS,USER0,USER0
Oracle,Oracle RDBMS,USER2,USER2
Oracle,Oracle RDBMS,USER4,USER4
Oracle,Oracle RDBMS,USER6,USER6
Oracle,Oracle RDBMS,USER8,USER8
Oracle,Oracle RDBMS,VRR1,VRR1
Oracle,Oracle RDBMS,system/manager,sys/change_on_install
Oracle,OracleRDBMS,AQUSER,AQUSER
Oracle,OracleRDBMS,FND,FND
Oracle,Web DB,webdb,webdb
Oracle,Web DB,webgb,webdb
Oracle,every,sys,change_on_install
Osicom (Datacom),Osicom(Datacom),sysadm,sysadm
Osicom,JETXPrint,sysadm,sysadm
Osicom,JETXPrint,sysadm,sysadm
Osicom,JETXPrint,sysadm,sysadm
Osicom,JETXPrint,sysadm,sysadm
Osicom,NETCommuter Remote Access Server,debug,d.e.b.u.g
Osicom,NETCommuter Remote Access Server,guest,guest
Osicom,NETCommuter Remote Access Server,sysadm,sysadm
Osicom,NETCommuter Remote,sysadm,sysadm
Osicom,NETCommuter,Manager,Admin
Osicom,NETCommuter,d.e.b.u.g,User
Osicom,NETCommuter,echo,User
Osicom,NETCommuter,guest,User
Osicom,NETCommuter,sysadm,Admin
Osicom,NETPrint and JETX Print,sysadm,sysadm
Osicom,NETPrint and JETX Print,sysadm,sysadm
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,debug,d.e.b.u.g
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,Manager,Manager
Osicom,NETPrint,echo,echo
Osicom,NETPrint,guest,guest
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,echo,echo
Osicom,NETPrint,guest,guest
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,debug,d.e.b.u.g
Osicom,NETPrint,guest,guest
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,Manager,Manager
Osicom,NETPrint,echo,echo
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,Manager,Manager
Osicom,NETPrint,Manager,Manager
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,sysadm,sysadm
Osicom,NETPrint,1500,and 2000 Series
Osicom,Osicom Plus T1/PLUS 56k,write,private
Osicom,Osicom Plus T1/PLUS 56k,write,private
Otenet,otenet,<blank>,<blank>
Overland,NEO Series Libraries,Factory,56789
PFSense,,admin,pfsense
PHPReactor,PHPReactor,core,phpreactor
PTCL,Huawei HG510,admin,admin
PTCL,ZYXEL P-660R-T1,admin,1234
Pacific Micro Data,MAST 9500 Universal Disk Array,pmd,<blank>
Packeteer,Packetshaper,<blank>,touchpwd=
Palo Alto Networks,GlobalProtect Gateway,admin,admin
Panasonic,CF-28,<blank>,<blank>
Panasonic,CF-45,<blank>,<blank>
Panasonic,IP Camera system,admin,12345
Panasonic,IP Camera system,admin1,password
Panasonic,PBX TDA 100/200/400,<blank>,1234
Panasonic,kx-td816,<blank>,1234
Pandatel,EMUX,admin,admin
Pansonic,KXTD1232,admin,1234
Patton,RAS,monitor,monitor
Pelco,IP Camera system,admin,admin
PentaSafe,VigilEnt Security Manager,PSEAdmin,$secure$
Pentagram,Cerberus ADSL modem + router,admin,password
Pentaoffice,Sat Router,<blank>,pento
Perle,CS9000,admin,superuser
Philips,Praesideo PA System,admin,admin
Phoenix v1.14,Phoenix v1.14,Administrator,admin
Phoenix,4,<blank>,admin
Phoenix,bios,<blank>,<blank>
Phoenix,dell,<blank>,admin
PiXORD,IP Camera system,admin,admin
PiXORD,IP Camera system,root,pass
PingTel,Xpressa,admin,<blank>
Pirelli,AGE ADSL Router,admin,microbusiness
Pirelli,AGE ADSL Router,user,password
Pirelli,DRG A125G,admin,admin
Pirelli,Pirelli AGE-SB,admin,smallbusiness
Pirelli,Pirelli Router,admin,microbusiness
Pirelli,Pirelli Router,admin,mu
Pirelli,Pirelli Router,user,password
PlainTree,Waveswitch 100,<blank>,default.password
Planet,ADE-4000,admin,epicrouter
Planet,ADE-4110,admin,epicrouter
Planet,WAP 4000,admin,admin
Planet,WAP-1900/1950/2000,<blank>,default
Planet,WAP-1900/1950/2000,<blank>,default
Planet,WAP-1900/1950/2000,<blank>,default
Planet,XRT-401D,admin,1234
Planex,BRL-04UR,admin,0
Pollsafe,Pollsafe,SMDR,SECONDARY
Polycom,SoundPoint IP Phones,Polycom,456
Polycom,Soundpoint VoIP phones,Polycom,SpIp
Polycom,ViewStation 4000,<blank>,admin
Polycom,Viewstation,administrator,<blank>
Polycom,iPower 9000,<blank>,<blank>
PostgreSQL,PostgreSQL,postgres,<blank>
Prestigio,Nobile,<blank>,<blank>
Prime,PrimeOS,dos,dos
Prime,PrimeOS,guest,guest
Prime,PrimeOS,guest1,guest
Prime,PrimeOS,maint,maint
Prime,PrimeOS,netlink,netlink
Prime,PrimeOS,prime,primeos
Prime,PrimeOS,primenet,primeos
Prime,PrimeOS,primeos,primeos
Prime,PrimeOS,primos_cs,prime
Prime,PrimeOS,system,system
Prime,PrimeOS,test,test
Prolink,H9000 Series,admin,password
Promise,NS4300N NAS,engmode,hawk201
Proxim,Orinoco 600/2000,<blank>,<blank>
Psion Teklogix,9150,support,h179350
Psionteklogix,9160,admin,admin
Pyramid Computer,BenHur,admin,admin
QDI,PC BIOS,<blank>,QDI
QLogic,SANbox 5602 Fibre Channel Switch,admin,password
QLogic,SANbox 5602 Fibre Channel Switch,images,images
QVIS,IP Camera system,admin,1234
Quantex,PC BIOS,<blank>,teX1
Quantum,File Servers,<blank>,<blank>
Quintum Technologies Inc.,Tenor Series,admin,admin
RM,Broadlink RM,setup,changeme
RM,RM Connect,RMUser1,password
RM,RM Connect,admin,rmnetlm
RM,RM Connect,admin2,changeme
RM,RM Connect,adminstrator,changeme
RM,RM Connect,deskalt,password
RM,RM Connect,deskman,changeme
RM,RM Connect,desknorm,password
RM,RM Connect,deskres,password
RM,RM Connect,guest,<blank>
RM,RM Connect,replicator,replicator
RM,RM Connect,setup,changeme
RM,RM Connect,teacher,password
RM,RM Connect,temp1,password
RM,RM Connect,topicalt,password
RM,RM Connect,topicnorm,password
RM,RM Connect,topicres,password
RM,Server BIOS,<blank>,RM
ROLM,phones/phone mail,<blank>,111#
Radware,AppDirect,radware,radware
Radware,AppXcel,radware,radware
Radware,Linkproof,lp,lp
Radware,Linkproof,radware,radware
Raidzone,raid arrays,<blank>,raidzone
Ramp Networks,WebRamp,wradmin,trancell
Rapid7 Inc,Metasploitable,msfadmin,msfadmin
RapidStream,RapidStream Appliances,rsadmin,(null)
Raritan,KVM Switches,admin,raritan
Raspberry Pi Foundation,Raspberry Pi OS,pi,raspberry
RedHat,Piranha,<blank>,Q
RedHat,Redhat 6.2,piranha,piranha
RedHat,Redhat 6.2,piranha,q
Reda,,<blank>,<blank>
Redemo,da,admin,<blank>
Redhat,Redhat 6.2,piranha,piranha
Remedy,Any,Demo,<blank>
Remedy,Remedy,demos,<blank>
Replicom,ProxyView,Administrator,Pvremote
Research,BIOS,<blank>,Col2ogro2
Research,PC BIOS,<blank>,Col2ogro2
Resumix,Resumix,root,resumix
Ricoh,AP410N,admin,<blank>
Ricoh,Aficio 1013F,<blank>,sysadm
Ricoh,Aficio 1018d,<blank>,sysadm
Ricoh,Aficio 2020D,admin,password
Ricoh,Aficio 2228c,sysadmin,password
Ricoh,Aficio 2232C,<blank>,password
Ricoh,Aficio 551,<blank>,sysadm
Ricoh,Aficio AP3800C,<blank>,password
Ricoh,Aficio MP 161L,(<blank> - Not required),sysadm
Ricoh,Aficio MP 161L,<blank>,sysadm
Ricoh,Aficio,<blank>,password
Ricoh,Aficio,sysadmin,password
Ricoh,Ricoh,admin,<blank>
Rizen,WebGUI,Admin,123qwe
RoamAbout,RoamAbout R2 Wireless Access Platform,admin,password
RoamAbout,RoamAbout R2 Wireless,admin,password
Rodopi,Rodopi billing software (AbacBill) sql database,rodopi,rodopi
Roxio,Aesy cd,<blank>,<blank>
Ruckus Wireless,M510,super,sp-admin
Ruckus Wireless,MediaFlex 2111,admin,password
Ruckus Wireless,MediaFlex 2825,admin,password
Ruckus Wireless,MediaFlex 7111,admin,password
Ruckus Wireless,MediaFlex 7211,super,sp-admin
Ruckus Wireless,MediaFlex 7811,admin,password
Ruckus Wireless,R320,super,sp-admin
Ruckus Wireless,R500,super,sp-admin
Ruckus Wireless,R750,super,sp-admin
Ruckus Wireless,ZoneFlex 2942,admin,password
Ruckus Wireless,ZoneFlex 7055,admin or super,sp-admin
Ruckus Wireless,ZoneFlex 7321,super,sp-admin
Ruckus Wireless,ZoneFlex 7343,super,sp-admin
Ruckus Wireless,ZoneFlex 7351,super,sp-admin
Ruckus Wireless,ZoneFlex 7352,super,sp-admin
Ruckus Wireless,ZoneFlex 7363,super,sp-admin
Ruckus Wireless,ZoneFlex 7372,super,sp-admin
Ruckus Wireless,ZoneFlex 7441,super,sp-admin
Ruckus Wireless,ZoneFlex 7762,super,sp-admin
Ruckus Wireless,ZoneFlex 7962,super,sp-admin
Ruckus Wireless,ZoneFlex R310,super,sp-admin
Ruckus Wireless,ZoneFlex T300,super,sp-admin
S2400,Toshiba,Administrator,admin
SAF Tehnika,CFQ series modems,administrator,d1scovery
SAF Tehnika,CFQ series modems,integrator,p1nacate
SAF Tehnika,CFQ series modems,monitor,monitor
SAF Tehnika,CFQ series modems,operator,col1ma
SAGEM,FAST 1400,admin,epicrouter
SAMSUNG,Samsung AHT-E300 Multi,admin,sec00000
SANS Institute,SIFT Workstation,sansforensics,forensics
SAP,SAP,DDIC,19920706
SAP,SAP,SAP*,PASS
SAP,SAP,SAPCPIC,ADMIN
SGI,IRIX,EZsetup,<blank>
SGI,IRIX,demos,<blank>
SGI,all,root,<blank>
SIEMENS,SE515,admin,<blank>
SKY,FEBRUARY 2016 MODEL,admin,sky
SMC,2804wr,<blank>,smcadmin
SMC,7204BRA,smc,smcadmin
SMC,7401BRA,admin,barricade
SMC,7401BRA,smc,smcadmin
SMC,Barricade 7004 AWBR,admin,<blank>
SMC,Barricade,<blank>,admin
SMC,Barricade7204BRB,admin,smcadmin
SMC,Modem/Router,cusadmin,highspeed
SMC,Router,admin,admin
SMC,Router/Modem,admin,barricade
SMC,SMB2804WBR,Administrator,smcadmin
SMC,SMC broadband router,admin,admin
SMC,SMC2804WBR,<blank>,smcadmin
SMC,SMC7004VBR,<blank>,smcadmin
SMC,SMC8013WG-CCR,mso,w0rkplac3rul3s
SMC,SMCWBR14-G,<blank>,smcadmin
SMC,SMCWBR14-G,<blank>,smcadmin
SMC,SMCWBR14-G,<blank>,smcadmin
SMC,SMCWBR14-G,<blank>,smcadmin
SMC,WiFi Router,<blank>,smcadmin
SMC,smc7904wbrb,<blank>,smcadmin
SOHOWARE,NBG800,admin,1234
SOPHIA (Schweiz) AG,Protector,admin,Protector
SOPHIA (Schweiz) AG,Protector,root,root
SOPHIA (Schweiz),Protector,admin,Protector
SOPHIA (Schweiz),Protector,root,root
SSA,BPCS,SSA,SSA
SWEEX,,sweex,mysweex
SWEEX,Broadband Router,<blank>,<blank>
Sagem,F@st 1200 (Fast 1200),root,1234
Sagem,Fast 3504 v2,Menara,Menara
Sagem,Livebox,admin,admin
Sagemcom,FAST 5657,1234,1234
Samba,SWAT Package,Any Local User,Local User password
Samsung,IP Camera system,admin,4321 / 1111111
Samsung,IP Camera system,root,4321 / admin
Samsung,MagicLAN SWL-3500RG,public,public
Samsung,inforanger,<blank>,<blank>
Sanyo,IP Camera system,admin,admin
Schneider,BMENOC301,admin,factorycast
Schneider,BMENOC311,admin,factorycast
Schneider,BMENOC321,admin,factorycast
Schneider,Modicon M340,fdrusers,sresurdf
Schneider,Modicon M340,fwupgrade,FaAmU5p2F~
Schneider,Modicon M340,loki,ZfTljublsx
Schneider,Modicon M340,sysdiag,factorycast@schneider
Schneider,Modicon M340,USER,USER
Schneider,Modicon M340,USER,USERUSER
Schneider,Premium,sysdiag,factorycast@schneider
Schneider,Premium,USER,USER
Scientific Atlanta,DPX2100,admin,w2402
Scylla,ScyllaDB,cassandra,cassandra
Secure Computing,Webwasher,admin,<blank>
Securicor3NET,Cezzanne,manager,friend
Securicor3NET,Money,manager,friend
Semaphore,PICK O/S,DESQUETOP,<blank>
Semaphore,PICK O/S,DSA,<blank>
Sempre,54M Wireless Router,admin,admin
Senao,2611CB3+D (802.11b Wireless AP),admin,<blank>
Senao,2611CB3+D (802.11b,admin,<blank>
Sentry360,IP Camera system,Admin,1234
Sercom,IP806GA,admin,admin
Sercom,IP806GB,admin,admin
Server Technology,Sentry Remote Power Manager,ADMN,admn
Server Technology,Sentry Remote Power Manager,GEN1,gen1
Server Technology,Sentry Remote Power Manager,GEN2,gen2
Sharp,AL-1655CS,admin,Sharp
Sharp,AR-M155,admin,Sharp
Sharp,AR-M237,admin,Sharp
Sharp,AR-M237,admin,Sharp
Sharp,AR-M355N,admin,Sharp
Sharp,MX-3501n,Administrator,admin
Sharp,MX-5500,admin,admin
Shina,LANRover,root,<blank>
Shiva,AccessPort,hello,hello
Shiva,Integrator,admin,hello
Shoretel,ALL,admin,changeme
Shuttle,PC BIOS,<blank>,Spacve
Siemens Nixdorf,BIOS,<blank>,SKY_FOX
Siemens Nixdorf,PC BIOS,<blank>,SKY_FOX
Siemens Pro C5,Siemens,<blank>,<blank>
Siemens,5940 T1E1 Router,superuser,admin
Siemens,Gigaset,<blank>,0
Siemens,Hicom 100E PBX,31994,31994
Siemens,Hipath,31994,31994
Siemens,PhoneMail,poll,poll
Siemens,PhoneMail,poll,tech
Siemens,PhoneMail,sysadmin,sysadmin
Siemens,PhoneMail,system,field
Siemens,PhoneMail,tech,tech
Siemens,ROLM PBX,admin,pwp
Siemens,ROLM PBX,eng,engineer
Siemens,ROLM PBX,op,op
Siemens,ROLM PBX,op,operator
Siemens,ROLM PBX,su,super
Siemens,S7-1200,admin,<blank>
Siemens,SE560dsl,admin,admin
Siemens,Simatic S7-1200 / S7-1500,admin,<blank>
Siemens,SpeedStream 4100,admin,hagpolm1
Siemens,Speedstream SS2614,<blank>,admin
Sigma,Sigmacoma IPshare,admin,admin
Signamax,065-7726S,admin,admin
Siips,Trojan,Administrator,ganteng
Silex Technology,Generic USB Device Servers,root,<blank>
Silex Technology,SX-100,root,access
Silex Technology,SX-200,root,access
Silex Technology,SX-2933-S03,root,access
Silex Technology,SX-500,root,access
Silex Technology,SX-600,root,access
Silvercrest,WR-6640Sg,admin,admin
Sitecom,All WiFi routers,<blank>,sitecom
Sitecom,WL-0xx up to WL-17x,admin,admin
Sitecom,WL-108,admin,password
SliTaz (GNU/Linux),SliTaz Live Session,root,root
SliTaz (GNU/Linux),SliTaz Live Session,tux,<blank>
SmartRG,SR50x,admin,admin
SmartRG,SR808AC,admin,admin
SmartSwitch,Router 250 ssr2500,admin,<blank>
Snapgear,Pro,1.79,Multi
Software,,<blank>,<blank>
Solution 6,Viztopia Accounts,aaa,often blank
SonarSource,SonarQube,admin,admin
Sonic-X,SonicAnime,root,admin
Sonic-X,SonicAnime,root,admin
SonicWALL,ALL,admin,password
Sony,IP Camera system,admin,1234
Sony,IP Camera system,admin,admin
Sorenson,SR-200,<blank>,admin
Sparklan,Wx-6215 D and G,admin,admin
Speco,IP Camera system,admin,admin
Speco,IP Camera system,root,root
Spectra Logic,64000 Gator,administrator,<blank>
Spectra Logic,64000 Gator,operator,<blank>
SpeedStream 5200-Serie,SpeedStream,Administrator,admin
SpeedStream,5660,<blank>,adminttd
SpeedStream,SpeedStream,Administrator,admin
SpeedXess,HASE-120,<blank>,speedxess
Speedstream,5667,<blank>,admin
Speedstream,5861 SMT Router,admin,admin
Speedstream,5871 IDSL Router,admin,admin
Speedstream,DSL,admin,admin
Speedstream,Router 250 ssr250,admin,admin
Sphairon,(Versatel WLAN-Router),admin,passwort
Spike,CPE,enable,<blank>
Ssangyoung,SR2501,<blank>,2501
StarDot,IP Camera system,admin,admin
Starvedia,IP Camera system,admin,<blank>
Sun Microsystems,ILOM of X4100,root,changeme
Sun,,<blank>,<blank>
Sun,Cobalt,admin,admin
Sun,JavaWebServer,admin,admin
Sun,SunScreen,admin,admin
SuperMicro,PC BIOS,<blank>,ksdjfg934t
Swissvoice,IP 10S,target,password
Syabas Technology,Popcorn Hour A-110,ftpuser,1234
Syabas Technology,Popcorn Hour A-110,nmt,1234
Syabas Technology,Popcorn Hour C-200,nmt,1234
Sybase,Adaptive Server Enterprise,sa,<blank>
Sybase,EAServer,jagadmin,<blank>
Symantec,NAV CORP / ALL,admin,symantec
Symantec,Norton AntiVirus Corp. Edition,<blank>,admin
Symantec,Norton Antivirus Corporate Edition,<blank>,admin
Symantec,pcanywhere,Administrator,<blank>
Symbol,AP-2412,<blank>,Symbol
Symbol,AP-3020,<blank>,Symbol
Symbol,AP-4111,<blank>,Symbol
Symbol,AP-4121,<blank>,Symbol
Symbol,AP-4131,<blank>,Symbol
Symbol,CB3000,admin,symbol
Symbol,Spectrum,<blank>,Symbol
Symmetricom,NTS-200,guest,truetime
Symmetricom,NTS-200,operator,mercury
SysKonnect,6616,default.password,<blank>
SysMaster,M10,admin,12345
System/32,VOS,install,secret
T com,sinus,veda,12871
T-Com,Speedport 503V,<blank>,123456
T-Com,Speedport Router Family,<blank>,0
T-Com,Speedport W701V,<blank>,0
T-Com,Speedport W900V,<blank>,0
T-Com,Speedport,<blank>,0
T-Comfort,Routers,Administrator,<blank>
TANDBERG,TANDBERG,<blank>,TANDBERG
TMC,PC BIOS,<blank>,BIGO
TP-LINK,All Routers,admin,admin
TVT System,Expresse G5 DS1 Module,<blank>,enter
TVT System,Expresse G5,craft,<blank>
Tandberg Data,DLT8000 Autoloader 10x,<blank>,10023
Tandberg,6000MXP,Admin,<blank>
Tandem,TACL,super.super,<blank>
Tandem,TACL,super.super,master
Team Xodus,XeniumOS,xbox,xbox
Technicolor,TC4300,<blank>,admin
Technicolor,TC4400,admin,bEn2o#US9s
Technicolors,All Routers,admin,admin
Tekelec,Eagle STP,eagle,eagle
Teklogix,Accesspoint,Administrator,<blank>
Telco Systems,Edge Link 100,telco,telco
Telebit,NetBlazer,setup/snmp,setup/nopassword
Teledat,Routers,admin,1234
Telenor,4g Mifi,admin,admin
Teletronics,WL-CPE-Router,admin,1234
Teletronics,WL-CPE-Router,admin,1234
Telewell,TW-EA200,admin,password
Telewell,TW-EA501,admin,admin
Telindus,1124,<blank>,<blank>
Telindus,SHDSL1421,admin,admin
Tellabs,7120,root,admin_1
Tellabs,Titan 5500,tellabs,tellabs#1
Telus,Telephony Services,(created),telus00
Tenda,All Routers,admin,admin
Terayon,TeraLink 1000 Controller,user,password
Terayon,TeraLink Getaway / 1000 Controller,user,password
Terayon,TeraLink Getaway,user,password
Terayon,TeraLink,admin,nms
Terayon,Unknown,<blank>,<blank>
TextPortal,TextPortal,god2,12345
The qBittorrent project,qBittorrent Web UI,admin,adminadmin
Thomson,SpeedTouch AP,<blank>,admin
Thomson,TCW-710,<blank>,admin
Thomson,Wireless Cable Gateway,<blank>,admin
Tiara,1400,tiara,tiaranet
Tiara,Tiara,tiara,tiaranet
Tiny,PC BIOS,<blank>,Tiny
Titbas,,haasadm,lucy99
TopLayer,AppSwitch 2500,siteadmin,toplayer
Topcom,Skyr@cer Pro AP 554,admin,admin
Topcom,Wireless Webr@cer 1154+ PSTN (Annex A),admin,admin
Topcom,Wireless Webr@cer 1154+ PSTN (Annex A),admin,admin
Topcom,Wireless Webr@cer 1154+ PSTN (Annex A),admin,admin
Topcom,Wireless Webr@cer 1154+,admin,admin
Topcom,Wireless Webr@cer 1154+,admin,admin
Topcom,Wireless Webr@cer 1154+,admin,admin
Toshiba,E-Studio 3511c,Admin,123456
Toshiba,E-Studio 3511c,Admin,123456
Toshiba,E-Studio 4511c,admin,123456
Toshiba,IP Camera system,root,ikwb
Toshiba,Most e-Studio copiers,admin,123456
Toshiba,PC BIOS,<blank>,Toshiba
Toshiba,PC BIOS,<blank>,toshy99
Toshiba,PC BIOS,<blank>,toshy99
Toshiba,TR-650,admin,tr650
Toshiba,Tecra 8100,<blank>,admin
Toshiba,laptop,Administrator,<blank>
Toshiba,satellite 1800-s204,<blank>,<blank>
Toshiba,satellite pro 4310,<blank>,<blank>
TrendMicro,ISVW (VirusWall),admin,admin
TrendMicro,InterScan 7.0,admin,imss7.0
TrendNET,TEW-435BRM,admin,password
Trendnet,IP Camera system,admin,admin
Trintech,eAcquirer App/Data Servers,t3admin,Trintech
Troy,ExtendNet 100zx,admin,extendnet
Troy,ExtendNet 100zx,admin,extendnet
Tsurugi Linux project,Tsurugi Linux,root,<blank>
Tumbleweed,Message Management System,sa,<blank>
U.S. Robotics,SureConnect 9003 ADSL Ethernet/USB Router,root,12345
U.S. Robotics,SureConnect 9003 ADSL,root,12345
U.S. Robotics,SureConnect 9105 ADSL 4-Port Router,admin,admin
U.S. Robotics,SureConnect 9105 ADSL,admin,admin
UDP,IP Camera system,root,unknown
UNEX,Routers,<blank>,password
UNIX,Generic,adm,adm
UNIX,Generic,admin,admin
UNIX,Generic,administrator,<blank>
UNIX,Generic,bbs,bbs
UNIX,Generic,bin,sys
UNIX,Generic,checkfsys,checkfsys
UNIX,Generic,checksys,checksys
UNIX,Generic,daemon,<blank>
UNIX,Generic,demo,<blank>
UNIX,Generic,demos,<blank>
UNIX,Generic,dni,dni
UNIX,Generic,fal,fal
UNIX,Generic,fax,fax
UNIX,Generic,ftp,ftp
UNIX,Generic,games,<blank>
UNIX,Generic,gropher,<blank>
UNIX,Generic,guest,guestgue
UNIX,Generic,halt,halt
UNIX,Generic,informix,informix
UNIX,Generic,lp,lineprin
UNIX,Generic,lp,lp
UNIX,Generic,lpadm,lpadm
UNIX,Generic,lynx,lynx
UNIX,Generic,mail,<blank>
UNIX,Generic,man,man
UNIX,Generic,me,<blank>
UNIX,Generic,mountfs,mountfs
UNIX,Generic,mountsys,mountsys
UNIX,Generic,news,<blank>
UNIX,Generic,nobody,nobody
UNIX,Generic,operator,operator
UNIX,Generic,oracle,<blank>
UNIX,Generic,postmaster,<blank>
UNIX,Generic,rje,rje
UNIX,Generic,root,root
UNIX,Generic,shutdown,<blank>
UNIX,Generic,sync,<blank>
UNIX,Generic,sys,system
UNIX,Generic,sysadm,sysadm
UNIX,Generic,sysadmin,sysadmin
UNIX,Generic,system_admin,<blank>
UNIX,Generic,trouble,trouble
UNIX,Generic,umountfsys,umountfsys
UNIX,Generic,unix,unix
UNIX,Generic,uucp,uucp
UNIX,Generic,web,<blank>
UNIX,Generic,webmaster,webmaster
UNIX,Generic,www,<blank>
UNIX,Generic,service,smile
UNIX,Generic,setup,<blank>
UNIX,koppp,dream,trocse
US ROBOTICS,ADSL Ethernet Modem,<blank>,12345
US Robotics,SureConnect ADSL,support,support
US Robotics,USR5462,<blank>,admin
US Robotics,USR8000,root,admin
US Robotics,USR8550,Any,12345
US Robotics,USR9106,admin,admin
US Robotics,USR9110,admin,<blank>
USR,TOTALswitch,<blank>,amber
UTStarcom,,admin,admin
UTStarcom,B-NAS/B-RAS,dbase,dbase
UTStarcom,B-NAS/B-RAS,guru,*3noguru
Ubiquiti,All products,ubnt,ubnt
Ubiquiti,UniFi AP-AC-LR,ubnt,UBNT-Access
Ucopia,Wi-Fi appliance,admin,bhu85tgb
Ucopia,Wi-Fi appliance,admin,ucopia
Unex,NexIP Routers,<blank>,password
Unisys,ClearPath MCP,ADMINISTRATOR,ADMINISTRATOR
Unisys,ClearPath MCP,HTTP,HTTP
Unisys,ClearPath MCP,NAU,NAU
Unisys,ClearPath MCP,NAU,NAU
Unknown,POCSAG Radio Paging,<blank>,password
Unknown,System 88,overseer,overseer
VASCO,VACMAN Middleware,admin,<blank>
VMware Inc.,RabbitMQ,guest,guest
VPASP,VP-ASP Shopping Cart,admin,admin
Various,DD-WRT,root,admin
Verifone,Verifone Junior,<blank>,166816
Verilink,NE6100-4 NetEngine,<blank>,<blank>
Verint,IP Camera system,admin,admin
Vertex,VERTEX 1501,root,vertex25
VideoIQ,IP Camera system,supervisor,supervisor
Visual Networks,Visual Uptime T1 CSU/DSU,admin,visual
Vivotek,IP Camera system,root,<blank>
Vobis,PC BIOS,<blank>,merlin
Vodafone,wifi router,root,123456
VxWorks,misc,admin,admin
VxWorks,misc,guest,guest
W-Box,IP Camera system,admin,wbox / 123
WLAN_3D,Router,Administrator,admin
WWWBoard,WWWADMIN.PL,WebAdmin,WebBoard
Wanadoo,Livebox,admin,admin
Wang,Wang,CSG,SESAME
WashTec,SoftCare Evo,<blank>,0
WashTec,SoftCare Evo,<blank>,1
Watch guard,firebox 1000,admin,<blank>
Watchguard,Firebox,(blank),wg
Watchguard,Firebox,<blank>,wg (touch password)
Watchguard,SOHO and SOHO6,user,pass
Watchguard,SOHO and SOHO6,user,pass
WebRamp,410i,wradmin,tracell
WebTrends,Enterprise Reporting,Admin,<blank>
Webmin,Webmin,admin,<blank>
Weidmüeller,IE-SW16-M,admin,detmond
Westell,Ultraline Series3 A90-,admin,password1
Westell,Ultraline Series3 A90-9100EM15-10,admin,password1
Westell,Versalink 327,admin,<blank>
Westell,Wang,CSG,SESAME
Westell,Wirespeed wireless router,admin,sysAdmin
Westell,Wirespeed,admin,password
Win2000,Quick Time 4.0,<blank>,<blank>
Wodsee,IP Camera system,root,<blank>
WorldClient,AdminServer,WebAdmin,Admin
Wyse,Winterm 3150,<blank>,password
Wyse,Winterm,root,wyse
Wyse,Winterm,VNC,winterm
Wyse,Winterm,<blank>,Fireport
Wyse,Winterm,<blank>,Fireport
Wyse,rapport,rapport,r@p8p0r+
Wyse,rapport,rapport,r@p8p0r+
Wyse,winterm,root,<blank>
X-Micro,WLAN 11b Access Point,super,super
X-Micro,WLAN 11b Access Point,super,super
X-Micro,X-Micro WLAN 11b Broadband Router,super,super
X-Micro,X-Micro WLAN 11b Broadband Router,1502,1502
XAMPP,XAMPP Filezilla FTP Server,newuser,wampp
Xavi,7000-ABA-ST1,<blank>,<blank>
Xavi,7001,<blank>,<blank>
Xerox,240a,admin,x-admin
Xerox,6204,<blank>,0
Xerox,DocuCentre 425,admin,22222
Xerox,Document Centre 405,admin,admin
Xerox,Document Centre 425,admin,<blank>
Xerox,DocumentCenter 186,admin,x-admin
Xerox,Multi Function Equipment,admin,2222
Xerox,Multi Function Equipment,admin,2222
Xerox,WorkCenter Pro 428,admin,admin
Xerox,WorkCentre 7132,11111,x-admin
Xerox,Workcentre,admin,1111
Xylan,OmniStack 1032CF,admin,password
Xylan,Omniswitch,admin,switch
Xylan,Omniswitch,diag,switch
Xylan,Omniswitch,diag,switch
Xylan,Omniswitch,admin,switch
Xylan,omniswitch,admin,switch
Xyplex,MX-16XX,setpriv,system
Xyplex,Routers,<blank>,access
Xyplex,Routers,<blank>,system
Xyplex,Terminal Server,<blank>,access
Xyplex,Terminal Server,<blank>,system
Yakumo,Routers,admin,admin
Yuxin,IP Phone,User,1234
Yuxin,IP Phone,User,19750407
ZEOS,PC BIOS,<blank>,zeosx
ZOOM,ZOOM ADSL Modem,admin,zoomadsl
ZTE,F4XX-F6XX,root,Zte521
ZTE,F609,admin,Telkomdso123
ZTE,F660,admin,Web@0063
ZTE,F660,user,user
ZTE,F663,user,user
ZTE,F670L,user,user
ZTE,ZXDSL 831,ADSL,expert03
Zabbix LLC,Zabbix,Admin,zabbix
Zcom,,admin,password
Zcom,Wireless,root,admin
Zebra,10/100 Print Server,admin,1234
Zenith,PC BIOS,<blank>,3098z
Zeus,Zeus Admin Server,admin,<blank>
Zorin Group,Zorin OS,root,mecktech
ZyXEL Based (Generic),Broadband SOHO Router,admin,0
ZyXEL ZyWALL Series,Prestige 660R-61C,<blank>,admin
ZyXEL,641 ADSL,<blank>,1234
ZyXEL,660HW,admin,<blank>
ZyXEL,ES-2108,admin,1234
ZyXEL,G570S,<blank>,1234
ZyXEL,Generic Routers,<blank>,1234
ZyXEL,Generic Routers,<blank>,1234
ZyXEL,ISDN-Router Prestige 1000,<blank>,1234
ZyXEL,NWA1100,<blank>,1234
ZyXEL,Prestige 100IH,<blank>,1234
ZyXEL,Prestige 128 Modem-Router,<blank>,1234
ZyXEL,Prestige 643,<blank>,1234
ZyXEL,Prestige 645,admin,1234
ZyXEL,Prestige 650,1234,1234
ZyXEL,Prestige 650HW31,192.168.1.1 60020,@dsl_xilno
ZyXEL,Prestige 652HW-31 ADSL Router,admin,1234
ZyXEL,Prestige 652HW-31,1234,Administrator
ZyXEL,Prestige 660HW,admin,admin
ZyXEL,Prestige 900,webadmin,1234
ZyXEL,Prestige P660HW,admin,1234
ZyXEL,Prestige,root,1234
ZyXEL,Prestige,<blank>,1234
ZyXEL,Prestige,<blank>,1234
ZyXEL,Prestige,admin,1234
ZyXEL,Prestige,<blank>,1234
ZyXEL,Prestige,admin,1234
ZyXEL,Router,<blank>,1234
ZyXEL,ZyWall 2,<blank>,<blank>
ZyXEL,adsl routers,admin,1234
accton t-online,accton,<blank>,0
adtran,Agent Card,<blank>,ADTRAN
adtran,Atlas 800/800Plus/810Plus/,<blank>,Password
adtran,Atlas 800/800Plus/810Plus/550,<blank>,Password
adtran,Express 5110/5200/5210,<blank>,adtran
adtran,MX2800,<blank>,adtran
adtran,NxIQ,<blank>,adtran
adtran,Smart 16/16e,<blank>,<blank>
adtran,Smart 16/16e,<blank>,PASSWORD
adtran,T3SU 300,<blank>,adtran
adtran,TSU IQ/DSU IQ,<blank>,<blank>
adtran,TSU Router Module/,<blank>,<blank>
adtran,TSU Router Module/L128/L768/1.5,<blank>,<blank>
airtel,DigitalTV,root,123456
alcatel,,<blank>,<blank>
alcatel,speed touch home,<blank>,<blank>
apc,Smartups 3000,apc,apc
apc,Smartups 3000,apc,apc
apple,airport5,root,admin
asmack,router,admin,epicrouter
axis,2100,<blank>,<blank>
aztech,DSL-600E,admin,admin
bay,cv1001003,<blank>,<blank>
canyon,router,Administrator,admin
cisco,2600 router,cisco,<blank>
cisco,2600,Administrator,admin
cisco,3600,Administrator,admin
cisco,ESW-520-24-K9,cisco,cisco
cisco,GSR,admin,admin
cisco,IPS10,admin,admin
cisco,IPS20,admin,admin
cisco,IPS21,admin,admin
cisco,OBFR,admin,admin
cisco,WRVS4400N,admin,admin
cisco,cva 122,admin,admin
comtrend,ct536+,admin,<blank>
conexant,ACCESS RUNNER ADSL CONSOLE PORT 3.27,Administrator,admin
conexant,ACCESS RUNNER ADSL,Administrator,admin
corecess,3113,admin,<blank>
creative,2015U,<blank>,<blank>
cuproplus,bus,<blank>,<blank>
cyberguard,all firewalls,cgadmin,cgadmin
d-link,ads500g,admin,admin
d-link,adsl,admin,admin
d-link,di-524,admin,<blank>
decnet,decnet,operator,admin
dell,inspiron,<blank>,admin
digicom,Wavegate 54C,Admin,<blank>
dlink,adsl,admin,admin
draytek,Vigor3300 series,draytek,1234
edimax,wireless adsl router,admin,epicrouter
emai,hotmail,<blank>,<blank>
enCAD,XPO,<blank>,<blank>
ericsson,ericsson acc,<blank>,<blank>
ericsson,md110 pabx,<blank>,help
fon,La fonera,admin,admin
fore,,<blank>,<blank>
fujitsu,l460,<blank>,<blank>
gatway,solo9100,<blank>,<blank>
giga,8ippro1000,Administrator,admin
glFtpD,glFtpD,glftpd,glftpd
greatspeed,DSL,netadmin,nimdaten
hp,2300,admin,admin
hp,sa7200,admin,<blank>
hp,sa7200,admin,admin
huawei incorporate,k3765,admin,admin
iBall,iB-LR6111A,admin,admin
iBall,iB-WRB150N,admin,admin
iDirect,iNFINITY series,admin,P@55w0rd!
iDirect,iNFINITY series,root,iDirect
iPSTAR,iPSTAR Network Box,admin,operator
iPSTAR,iPSTAR Satellite Router/Radio,admin,operator
iblitzz,BWA711/All Models,admin,admin
ibm,a20m,<blank>,admin
ihoi,oihoh,Administrator,pilou
inchon,inchon,admin,admin
infacta,group mail,Administrator,<blank>
intel,netstructure,admin,<blank>
intex,organizer,<blank>,<blank>
ion,nelu,<blank>,admin
ion,nelu,Administrator,admin
kaptest,usmle,admin,<blank>
latis network,border guard,<blank>,<blank>
linksys,BEFW11S4,<blank>,admin
linksys,ap 1120,<blank>,<blank>
linksys,wag354g,admin,admin
linksys,wrt54g,admin,admin
longshine,isscfg,admin,0
lucent,Portmaster 3,!root,!ishtar
lucent,dsl,<blank>,<blank>
lxy_nrg,87418,<blank>,<blank>
m0n0wall,m0n0wall,admin,mono
maxdata,7000x,<blank>,<blank>
maxdata,ms2137,<blank>,<blank>
mediatrix 2102,mediatrix 2102,admin,1234
medion,Routers,<blank>,medion
microRouter,900i,<blank>,letmein
microcom,hdms,system,hdms
motorola,sgb900,admin,motorola
motorola,vanguard,<blank>,<blank>
mro software,maximo,SYSADM,sysadm
msdloto,msdloto,<blank>,<blank>
netgear,,<blank>,<blank>
netgear,DG834GT,admin,Password
netgear,FM114P,<blank>,<blank>
netgear,dg834,<blank>,admin
netgear,sc101,admin,password
netgear,sc101,admin,password
netlink,rt314,<blank>,<blank>
netscreen,firewall,Administrator,<blank>
netscreen,firewall,Administrator,<blank>
netscreen,firewall,admin,<blank>
netscreen,firewall,operator,<blank>
nortel,dms,<blank>,<blank>
nortel,p8600,<blank>,<blank>
novell,,<blank>,<blank>
olitec (Trendchip),sx 202 adsl modem router,admin,admin
olitec,sx 200 adsl modem router,admin,adslolitec
openELEC,openelec, root, openelec
openHAB,openHABian,openhabian,openhabian
openHAB,openHABian,openhab,habopen
openmediavault,openmediavault,admin,openmediavault
ovislink,WL-1120AP,root,<blank>
panasonic,cf 27,<blank>,<blank>
penril datability,vcp300 terminal server,<blank>,system
pfSense,pfSense Firewall,admin,pfsense
phpTest,phpTest,admin,1234
planet,Akcess Point,admin,admin
planet,akcess point,admin,admin
ptcl,zxdsl831cii,admin,admin
realtek,8139,<blank>,<blank>
realtek,RTL8723DE,admin,admin
sagem,fast 1400w,root,1234
samsung,modem/router,admin,password
samsung,n620,<blank>,<blank>
schoolgirl,member,ich,hci
security.org,lockpicking,admin,<blank>
seninleyimben,@skan,admin,admin
sharp,AR-407/S402,<blank>,<blank>
siemen,speedstream 5400,admin,<blank>
siemens,hipath,<blank>,<blank>
silex technology,PRICOM (Printserver),root,<blank>
sitara,qosworks,root,<blank>
smc,smc 7904BRA,<blank>,smcadmin
soho,nbg800,admin,1234
stratacom,all,stratacom,stratauser
surecom,ep3501/3506,admin,surecom
telecom,home hauwei,operator,<blank>
telindus,telindus,admin,admin
thomson,speedtouch 585 v7,admin,password
topsec,firewall,superman,talent
toshiba,480cdt,<blank>,<blank>
us robotic,adsl gateway wireless router,support,support
us21100060,hp omibook 6100,<blank>,<blank>
webmail,webmail v0.94,kol,gniffe
westell,2200,admin,password
winwork,iso sistemi,operator,<blank>
wline,w3000g,admin,1234
xerox,work centre pro 35,admin,1111
xerox,xerox,<blank>,admin
xerox,xerox,admin,admin
xerox,xerox,root,admin
xyplex,switch,<blank>,<blank>
zyxel,g-570s,<blank>,admin
zyxel,prestige 300 series,<blank>,1234



Swissvoice,IP 10S,target,password
SMC,SMCWBR14-G,(none),smcadmin
Signamax,065-7726S,admin,admin
Zebra,10/100 Print Server,admin,1234
Flowpoint,100 IDSN,admin,admin
Telindus,1124,n/a,(none)
Tiara,1400,tiara,tiaranet
creative,2015U,n/a,(none)
axis,2100,n/a,(none)
westell,2200,admin,password
Flowpoint,2200 SDSL,admin,admin
hp,2300,admin,admin
MERCURY,234234,Administrator,admin
Xerox,240a,admin,x-admin
cisco,2600,Administrator,admin
Senao,2611CB3+D (802.11b Wireless AP),admin,(none)
SMC,2804wr,(none),smcadmin
corecess,3113,admin,(none)
Mitel,3300 ICP,system,password
Netopia,3351,n/a,(none)
Micronet,3351 / 3354,admin,epicrouter
IBM,3534 F08 Fibre Switch,admin,password
IBM,3583 Tape Library,admin,secure
cisco,3600,Administrator,admin
IBM,390e,n/a,admin
3com,3C16405,admin,(none)
3COM,3C16406,admin,(none)
3COM,3C16450,admin,(none)
3com,3CRADSL72,(none),1234admin
3com,3Com SuperStack 3 Switch 3300XM,security,security
3ware,3DM,Administrator,3ware
3com,3c16405,n/a,(none)
3com,3c16405,Administrator,(none)
3com,3c16405,Administrator,(none)
Flowpoint,40 IDSL,admin,admin
ALCATEL,4400,mtcl,(none)
Netopia,4542,admin,noway
d-link,504g adsl router,admin,admin
Axis,540/542 Print Server,root,pass
SpeedStream,5660,n/a,adminttd
Speedstream,5667,(none),admin
Efficient,5851,login,password
Efficient Networks,5851 SDSL Router,(none),hs7mwxkk
Speedstream,5861 SMT Router,admin,admin
Efficient,5871 DSL Router,login,admin
Speedstream,5871 IDSL Router,admin,admin
Siemens,5940 T1E1 Router,superuser,admin
Tandberg,6000MXP,Admin,(none)
DLINK,604,n/a,admin
Corecess,6808 APC,corecess,corecess
Xavi,7000-ABA-ST1,n/a,(none)
Xavi,7001,n/a,(none)
Tellabs,7120,root,admin_1
SMC,7204BRA,smc,smcadmin
NOKIA,7360,(none),9999
SMC,7401BRA,admin,barricade
SMC,7401BRA,smc,smcadmin
3c om,812,Administrator,admin
IBM,8224 HUB,vt100,public
IBM,8239 Token Ring HUB,n/a,R1QTPS
giga,8ippro1000,Administrator,admin
microRouter,900i,n/a,letmein
Psion Teklogix,9150,support,h179350
Psionteklogix,9160,admin,admin
Psionteklogix,9160,admin,admin
APC,9606 Smart Slot,n/a,backdoor
Atlantis,A02-RA141,admin,atlantis
IBM,A21m,n/a,(none)
conexant,ACCESS RUNNER ADSL CONSOLE PORT 3.27,Administrator,admin
Aspect,ACD,customer,none
Aspect,ACD,DTA,TJM
Aspect,ACD,DTA,TJM
Aspect,ACD,DTA,TJM
Alteon,ACEDirector3,admin,(none)
Alteon,ACEswitch,admin,admin
Alteon,ACEswitch,admin,(none)
Alteon,ACEswitch,admin,linga
Alteon,AD4,admin,admin
Planet,ADE-4000,admin,epicrouter
Planet,ADE-4110,admin,epicrouter
AMBIT,ADSL,root,(none)
US ROBOTICS,ADSL Ethernet Modem,(none),12345
E-Tech,ADSL Ethernet Router,admin,epicrouter
Netgear,ADSL Modem DG632,admin,password
Cable And Wireless,ADSL Modem/Router,admin,1234
Linksys,AG 241 - ADSL2 Gateway with 4-Port Switch,admin,admin
Pirelli,AGE ADSL Router,admin,microbusiness
Pirelli,AGE ADSL Router,user,password
Allied Telesyn,ALAT8326GB,manager,manager
SonicWALL,ALL,admin,password
Allnet,ALL0275 802.11g AP,none,admin
Enterasys,ANG-1105,admin,netadmin
Enterasys,ANG-1105,(none),netadmin
Symbol,AP-2412,n/a,Symbol
Symbol,AP-3020,n/a,Symbol
Symbol,AP-4111,n/a,Symbol
Symbol,AP-4121,n/a,Symbol
Symbol,AP-4131,n/a,Symbol
Cisco,AP1200,Cisco,Cisco
Ricoh,AP410N,admin,(none)
sharp,AR-407/S402,n/a,(none)
Sharp,AR-M355N,admin,Sharp
ASMAX,AR701u / ASMAX AR6024,admin,epicrouter
ASMAX,AR800C2,admin,epicrouter
ASMAX,AR800C2,admin,epicrouter
Allied Telesyn,AT Router,root,(none)
Allied Telesyn,AT-8024(GB),n/a,admin
Allied Telesyn,AT-8024(GB),manager,admin
Allied Telesyn,AT-AR130 (U) -10,Manager,friend
Allied Telesyn,AT8016F,manager,friend
CTC Union,ATU-R130,root,root
AXUS,AXUS YOTTA,n/a,0
Nortel,Accelar (Passport) 1000 series routing switches,l2,l2
Nortel,Accelar (Passport) 1000 series routing switches,l3,l3
Nortel,Accelar (Passport) 1000 series routing switches,ro,ro
Nortel,Accelar (Passport) 1000 series routing switches,rw,rw
Nortel,Accelar (Passport) 1000 series routing switches,rwa,rwa
Micronet,Access Point,root,default
Intel/Shiva,Access Port,admin,hello
Teklogix,Accesspoint,Administrator,(none)
Ricoh,Aficio,sysadmin,password
Ricoh,Aficio 2020D,admin,password
Ricoh,Aficio 2228c,sysadmin,password
Ricoh,Aficio 2232C,n/a,password
Ricoh,Aficio AP3800C,(none),password
adtran,Agent Card,n/a,ADTRAN
Apple,AirPort Base Station (Graphite),(none),public
AirTies RT-210,AirTies RT-210,admin,admin
Cisco,Aironet,(none),_Cisco
Cisco,Aironet,Cisco,Cisco
Cisco,Aironet 1200,root,Cisco
Apple,Airport Base Station (Dual Ethernet),n/a,password
Apple,Airport Extreme Base Station,n/a,admin
planet,Akcess Point,admin,admin
Axis,All Axis Printserver,root,pass
Lockdown Networks,All Lockdown Products,setup,changeme(exclamation)
Extreme Networks,All Switches,admin,(none)
Sitecom,All WiFi routers,(none),sitecom
Lucent,Anymedia,LUCENT01,UI-PSWD-01
Lucent,Anymedia,LUCENT02,UI-PSWD-02
Asmax,Ar-804u,admin,epicrouter
LG,Aria iPECS,(none),jannie
Cisco-Arrowpoint,Arrowpoint,admin,system
IBM,Ascend OEM Routers,n/a,ascend
Ascom,Ascotel PBX,(none),3ascotel
adtran,Atlas 800/800Plus/810Plus/550,n/a,Password
Lucent,B-STDX9000,(any 3 characters),cascade
Lucent,B-STDX9000,n/a,cascade
Lucent,B-STDX9000,n/a,cascade
Cisco,BBSD MSDE Client,bbsd-client,NULL
Cisco,BBSM,bbsd-client,changeme2
Cisco,BBSM Administrator,Administrator,changeme
Cisco,BBSM MSDE Administrator,sa,(none)
Linksys,BEFSR41,(none),admin
Linksys,BEFW11S4,admin,(none)
F5-Networks,BIGIP,n/a,(none)
Freetech,BIOS,n/a,Posterie
Megastar,BIOS,n/a,star
Nimble,BIOS,n/a,xdfk9874t3
Research,BIOS,n/a,Col2ogro2
Siemens Nixdorf,BIOS,n/a,SKY_FOX
Billion,BIPAC-640 AC,(none),(none)
Ericsson,BP250,admin,default
SSA,BPCS,SSA,SSA
Datacom,BSASX/101,n/a,letmein
BBR-4MG and BBR-4HG,BUFFALO,root,n/a
iblitzz,BWA711/All Models,admin,admin
SMC,Barricade 7004 AWBR,admin,(none)
SMC,Barricade7204BRB,admin,smcadmin
Nortel,Baystack 350-24T,n/a,secure
Pyramid Computer,BenHur,admin,admin
BinTec,Bianca/Brick,n/a,snmp-Trap
Bintec,Bianka Routers,admin,bintec
F5,Bigip 540,root,default
Billion,Bipac 5100,admin,admin
IBM,BladeCenter Mgmt Console,USERID,PASSW0RD
Breezecom,Breezecom Adapters,n/a,Master
Breezecom,Breezecom Adapters,n/a,laflaf
Breezecom,Breezecom Adapters,n/a,Helpdesk
Breezecom,Breezecom Adapters,n/a,Super
Breezecom,Breezecom Adapters,n/a,Master
Breezecom,Breezecom Adapters,n/a,laflaf
Edimax,Broadband Router,admin,1234
Nortel,Business Communications Manager,supervisor,PlsChgMe
OKI,C5700,root,the 6 last digit of the MAC adress
Symbol,CB3000,admin,symbol
3com,CB9000 / 4007,Type User: FORCE,(none)
Lucent,CBX 500,(any 3 characters),cascade
Lucent,CBX 500,n/a,cascade
Cellit,CCPro,cellit,cellit
Panasonic,CF-28,n/a,(none)
Panasonic,CF-45,n/a,(none)
Netgear,CG814CCR,cusadmin,highspeed
Avaya,CMS Supervisor,root,cms500
CNET,CNET 4PORT ADSL MODEM,admin,epicrouter
Cisco,CNR,admin,changeme
Spike,CPE,enable,(none)
Perle,CS9000,admin,superuser
CNET,CSH-2400W,admin,1234
Ambit,Cable Modem,root,root
Ambit,Cable Modem 60678eu,root,root
Motorola,Cablerouter,cablecom,router
CISCO,Cache Engine,admin,diamond
Intersystems,Cache Post-RDMS,system,sys
Avaya,Cajun,diag,danger
Avaya,Cajun,manuf,xxyyzz
AVAYA,Cajun P33x,n/a,admin
Avaya,Cajun Pxxx,root,root
Kalatel,Calibur DSR-2000e,n/a,3477
Kalatel,Calibur DSR-2000e,n/a,8111
Cisco,CallManager,admin,admin
Cisco,Catalyst 4000/5000/6000,(none),public/private/secret
Cayman,Cayman DSL,n/a,(none)
3COM,CellPlex,tech,tech
3COM,CellPlex,admin,synnet
3COM,CellPlex,root,(none)
3COM,CellPlex,tech,(none)
3COM,CellPlex,admin,admin
3com,CellPlex,tech,tech
3com,CellPlex,root,(none)
3com,CellPlex,tech,(none)
Lucent,Cellpipe 22A-BX-AR USB D,admin,AitbISP4eCiG
Pentagram,Cerberus ADSL modem + router,admin,password
Cisco,Cisco Wireless Location Appliance,root,password
Cisco,CiscoWorks 2000,guest,(none)
Cisco,CiscoWorks 2000,admin,cisco
Cisco,Ciso Aironet 1100 series,(none),Cisco
Unisys,ClearPath MCP,NAU,NAU
Unisys,ClearPath MCP,ADMINISTRATOR,ADMINISTRATOR
Unisys,ClearPath MCP,HTTP,HTTP
Sun,Cobalt,admin,admin
ARtem,ComPoint - CPD-XT-b,(none),admin
Linksys,Comcast,comcast,1234
NetGear,Comcast,comcast,1234
Cisco,ConfigMaker,cmaker,cmaker
Cisco,ConfigMaker,cmaker,cmaker
Cisco,Content Engine,admin,default
Nortel,Contivity,admin,setup
3COM,CoreBuilder,debug,synnet
3COM,CoreBuilder,tech,tech
3COM,CoreBuilder,n/a,admin
3COM,CoreBuilder,n/a,(none)
Corecess,Corecess 3112,Administrator,admin
D-Link,D-704P,admin,(none)
D-Link,D-704P,admin,admin
DI624,D-LINK,admin,password
netgear,DG834GT,admin,Password
D-Link,DI-514,user,(none)
D-Link,DI-524,admin,(none)
D-Link,DI-524,user,(none)
D-Link,DI-604,admin,(none)
D-Link,DI-604,admin,(none)
D-Link,DI-604,admin,admin
D-Link,DI-614+,user,(none)
D-Link,DI-614+,admin,(none)
D-Link,DI-614+,admin,admin
D-Link,DI-624,admin,(none)
D-Link,DI-624,User,(none)
D-Link,DI-624+,admin,admin
D-Link,DI-634M,admin,(none)
D-Link,DI-704,(none),admin
D-Link,DI-704,n/a,admin
D-Link,DI-804,admin,(none)
Tandberg Data,DLT8000 Autoloader 10x,n/a,10023
Netgear,DM602,admin,password
Scientific Atlanta,DPX2100,admin,w2402
Flowpoint,DSL,n/a,password
Linksys,DSL,n/a,admin
Speedstream,DSL,admin,admin
Accelerated Networks,DSL CPE and DSLAM,sysadm,anicust
Nokia,DSL Router M1122,m1122,m1122
D-Link,DSL-300g+,admin,admin
D-Link,DSL-302G,admin,admin
Dlink,DSL-500,admin,admin
D-link,DSL-504T,admin,admin
aztech,DSL-600E,admin,admin
D-link,DSL-G604T,admin,admin
D-LINK,DSL-G664T,admin,admin
D-link,DSL500G,admin,admin
NRG or RICOH,DSc338 Printer,(none),password
D-Link,DWL 1000,admin,(none)
D-Link,DWL 2100AP,admin,(none)
D-Link,DWL 900AP,(none),public
D-Link,DWL-2000AP+,admin,(none)
D-Link,DWL-614+,admin,(none)
D-Link,DWL-614+,admin,(none)
D-Link,DWL-900+,admin,(none)
D-link,DWL-900AP+,admin,(none)
Omnitronix,Data-Link,(none),SUPER
Omnitronix,Data-Link,(none),SMDR
Avaya,Definity,craft,(none)
Avaya,Definity,dadmin,dadmin01
Konica/ Minolta,Di 2010f,n/a,0
D-link,Di-707p router,admin,(none)
IBM,Directory - Web Administration Tool,superadmin,secret
Xerox,DocuCentre 425,admin,22222
Xerox,Document Centre 405,admin,admin
Xerox,Document Centre 425,admin,(none)
D-Link,Dsl-300g+,(none),private
Sybase,EAServer,jagadmin,(none)
Efficient Networks,EN 5861,login,admin
Edimax,ES-5224RXM,admin,123
Lantronix,ETS16P,n/a,(none)
Lantronix,ETS32PR,n/a,(none)
Lantronix,ETS422PR,n/a,(none)
Lantronix,ETS4P,n/a,(none)
Mutare Software,EVM Admin,(none),admin
Edimax,EW-7205APL,guest,(none)
Kyocera,EcoLink,n/a,PASSWORD
E-Con,Econ DSL Router,admin,epicrouter
Telco Systems,Edge Link 100,telco,telco
NAI,Entercept,GlobalAdmin,GlobalAdmin
Ericsson,Ericsson Acc,netman,netman
Ericsson,Ericsson Acc,netman,netman
Linksys,EtherFast Cable/DSL ROuter,Administrator,admin
Netport,Express 10/100,setup,setup
adtran,Express 5110/5200/5210,n/a,adtran
Intel,Express 520T Switch,setup,setup
Intel,Express 9520 Router,NICONEX,NICONEX
TVT System,Expresse G5,craft,(none)
TVT System,Expresse G5 DS1 Module,(none),enter
Troy,ExtendNet 100zx,admin,extendnet
Nortel,Extranet Switches,admin,setup
Belkin,F5D6130,(none),MiniAP
Belkin,F5D7150,n/a,admin
Sagem,F@st 1200 (Fast 1200),root,1234
SAGEM,FAST 1400,admin,epicrouter
McData,FC Switches/Directors,Administrator,password
netgear,FM114P,n/a,(none)
Asante,FM2008,superuser,(none)
Asante,FM2008,admin,asante
Netgear,FR114P,admin,password
Netgea,FR314,admin,password
Datawizard.net,FTPXQ server,anonymous,any@
Netgear,FVS318,admin,password
Netgear,FWG114P,n/a,admin
Brocade,Fabric OS,root,fivranne
Brocade,Fabric OS,admin,password
Netscreen,Firewall,netscreen,netscreen
Flowpoint,Flowpoint DSL,admin,admin
Marconi,Fore ATM Switches,ami,(none)
Fortinet,Fortigate,admin,(none)
Netgear,GS724t,n/a,password
Netgear,GSM7224,admin,(none)
cisco,GSR,admin,admin
Lucent,GX 550,n/a,cascade
SpeedXess,HASE-120,(none),speedxess
Brother,HL-1270n,n/a,access
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPP187
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPP189
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPP196
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,INTX3
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,ITF3000
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,NETBASE
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,REGO
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,RJE
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,CONV
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,DISC
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,SYSTEM
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,SUPPORT
Hewlett-Packard,HP 2000/3000 MPE/xx,OPERATOR,COGNOS
Hewlett-Packard,HP 2000/3000 MPE/xx,PCUSER,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,RSBCMON,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,SPOOLMAN,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,WP,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,ADVMAIL,HPOFFICE DATA
Hewlett-Packard,HP 2000/3000 MPE/xx,ADVMAIL,HP
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,SUPPORT
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,MGR
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,SERVICE
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,MANAGER
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,HPP187 SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,LOTUS
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,HPWORD PUB
Hewlett-Packard,HP 2000/3000 MPE/xx,FIELD,HPONLY
Hewlett-Packard,HP 2000/3000 MPE/xx,HELLO,MANAGER.SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,HELLO,MGR.SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,HELLO,FIELD.SUPPORT
Hewlett-Packard,HP 2000/3000 MPE/xx,HELLO,OP.OPERATOR
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,MAIL
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,REMOTE
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,TELESUP
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,MAIL,MPE
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,TCH
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,SECURITY
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,ITF3000
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,COGNOS
Hewlett-Packard,HP 2000/3000 MPE/xx,MANAGER,TELESUP
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,SYS
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,CAROLIAN
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,VESOFT
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,XLSERVER
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,SECURITY
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,TELESUP
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPDESK
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,CCC
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,CNAS
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,WORD
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,COGNOS
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,ROBELLE
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPOFFICE
Hewlett-Packard,HP 2000/3000 MPE/xx,MGR,HPONLY
Cisco,HSE,root,blender
Cisco,HSE,hsa,hsadb
IBM,Hardware Management Console,hscroot,abc123
3COM,HiPerACT,admin,(none)
3com,HiPerACT,admin,(none)
3com,HiPerACT,admin,(none)
3COM,HiPerARC,adm,(none)
3COM,HiPerARC,adm,(none)
JDS Microprocessing,Hydra 3000,hydrasna,(none)
Atlantis,I-Storm Lan Router ADSL,admin,atlantis
IBM,IBM,n/a,(none)
LANCOM,IL11,n/a,(none)
Sun Microsystems,ILOM of X4100,root,changeme
Sercom,IP806GA,admin,admin
Sercom,IP806GB,admin,admin
Livingston,IRX Router,!root,(none)
HP,ISEE,admin,isee
Juniper,ISG2000,netscreen,netscreen
Andover Controls,Infinity,acc,acc
IBM,Infoprint 6700,root,(none)
Compaq,Insight Manager,administrator,administrator
Compaq,Insight Manager,anonymous,(none)
Compaq,Insight Manager,user,user
Compaq,Insight Manager,operator,operator
Compaq,Insight Manager,user,public
Compaq,Insight Manager,PFCUser,240653C9467E45
Interbase,Interbase Database Server,SYSDBA,masterkey
Kyocera,Intermate LAN FS Pro 10/100,admin,admin
3Com,Internet Firewall,admin,password
Intershop,Intershop,operator,$chwarzepumpe
Asante,IntraStack,IntraStack,Asante
Asante,IntraSwitch,IntraSwitch,Asante
NAI,Intrushield IPS,admin,admin123
CipherTrust,IronMail,admin,password
Foundry Networks,IronView Network Manager,admin,admin
Osicom,JETXPrint,sysadm,sysadm
Osicom,JETXPrint,sysadm,sysadm
Osicom,JETXPrint,sysadm,sysadm
Osicom,JETXPrint,sysadm,sysadm
Sun,JavaWebServer,admin,admin
KTI,KS-2260,superuser,123456
KTI,KS2260,admin,123
KTI,KS2600,admin,123456
MERCURY,KT133A/686B,Administrator,admin
Pansonic,KXTD1232,admin,1234
LG,LAM200E / LAM200R,admin,epicrouter
Elsa,LANCom Office ISDN Router,n/a,cisco
3COM,LANplex,debug,synnet
3COM,LANplex,tech,tech
3COM,LANplex,tech,(none)
3com,LANplex,n/a,admin
Lantronics,Lantronics Terminal Server,n/a,access
Lantronics,Lantronics Terminal Server,n/a,system
Lantronix,Lantronix Terminal,n/a,lantronix
Dell,Laser Printer 3000cn / 3100cn,admin,password
Hewlett-Packard,LaserJet Net Printers,(none),(none)
Hewlett-Packard,LaserJet Net Printers,(none),(none)
Hewlett-Packard,LaserJet Net Printers,Anonymous,(none)
Hewlett-Packard,LaserJet Net Printers,(none),(none)
3COM,LinkSwitch,tech,tech
Radware,Linkproof,lp,lp
Radware,Linkproof,radware,radware
Linksys,Linksys DSL,n/a,admin
Linksys,Linksys Router DSL/Cable,(none),admin
Wanadoo,Livebox,admin,admin
Livingston,Livingston Portmaster 3,!root,(none)
Logitech,Logitech Mobile Headset,(none),0
LUCENT,M770,super,super
Pacific Micro Data,MAST 9500 Universal Disk Array,pmd,(none)
Lucent,MAX-TNT,admin,Ascend
Ericsson,MD110,MD110,help
Deerfield,MDaemon,MDaemon,MServer
Netgear,ME102,(none),private
Netgear,MR-314,admin,1234
OMRON,MR104FH,n/a,(none)
Netgear,MR314,admin,1234
Netgear,MR814,admin,password
Openwave,MSP,cac_admin,cacadmin
Huawei,MT880r,TMAR#HWMT8007079,(none)
Nokia,MW1122,telecom,telecom
Sharp,MX-3501n,Administrator,admin
adtran,MX2800,n/a,adtran
Samsung,MagicLAN SWL-3500RG,public,public
Minolta QMS,Magicolor 3100,operator,(none)
Minolta QMS,Magicolor 3100,admin,(none)
Exabyte,Magnum20,anonymous,Exabyte
Nortel,Matra 6501 PBX,(none),0
Celerity,Mediator,mediator,mediator
Celerity,Mediator,root,Mau'dib
Cisco,MeetingPlace,technician,2 + last 4 of Audio Server chasis Serial case-sensitive + 561384
Nortel,Meridian,n/a,(none)
Nortel,Meridian CCR,service,smile
Nortel,Meridian CCR,disttech,4tas
Nortel,Meridian CCR,maint,maint
Nortel,Meridian CCR,ccrusr,ccrusr
Nortel,Meridian Link,disttech,4tas
Nortel,Meridian Link,maint,maint
Nortel,Meridian Link,mlusr,mlusr
Nortel,Meridian Link,service,smile
Nortel,Meridian MAX,service,smile
Nortel,Meridian MAX,root,3ep5w2u
Nortel,Meridian MAX,maint,ntacdmax
Nortel,Meridian PBX,login,0
Nortel,Meridian PBX,login,1111
Nortel,Meridian PBX,login,8429
Nortel,Meridian PBX,spcl,0
IronPort,Messaging Gateway Appliance,admin,ironport
Intel/Shiva,Mezza ISDN Router,admin,hello
Digicom,Michelangelo,admin,michelangelo
Digicom,Michelangelo,user,password
Mentec,Micro/RSX,MICRO,RSX
Mentec,Micro/RSX,MICRO,RSX
Micronet,Micronet SP5002,mac,(none)
Mintel,Mintel PBX,n/a,SYSTEM
Mintel,Mintel PBX,n/a,SYSTEM
Intermec,Mobile LAN,intermec,intermec
Aceex,Modem ADSL Router,admin,(none)
Aceex,Modem ADSL Router,admin,(none)
SMC,Modem/Router,cusadmin,highspeed
Motorola,Motorola Cablerouter,cablecom,router
Xerox,Multi Function Equipment,admin,2222
Netcomm,NB1300,admin,password
Brother,NC-2100p,(none),access
Brother,NC-3100h,(none),access
Brother,NC-4100h,(none),access
Verilink,NE6100-4 NetEngine,(none),(none)
Axis,NETCAM,root,pass
Axis,NETCAM,root,pass
Osicom,NETCommuter Remote Access Server,debug,d.e.b.u.g
Osicom,NETCommuter Remote Access Server,echo,echo
Osicom,NETCommuter Remote Access Server,guest,guest
Osicom,NETCommuter Remote Access Server,Manager,Manager
Osicom,NETCommuter Remote Access Server,sysadm,sysadm
Osicom,NETCommuter Remote Access Server,sysadm,sysadm
Osicom,NETPrint,Manager,Manager
Osicom,NETPrint,1500,and 2000 Series
Osicom,NETPrint and JETX Print,sysadm,sysadm
NGSec,NGSecureWeb,admin,(none)
NGSec,NGSecureWeb,admin,asd
Network Everywhere,NWR11B,(none),admin
NetGenesis,NetAnalysis Web Reporting,naadmin,naadmin
3COM,NetBuilder, ,ANYCOM
3COM,NetBuilder, ,ILMI
3com,NetBuilder,(none),admin
Network Appliance,NetCache,admin,NetCache
Niksun,NetDetector,vcr,NetVCR
Irongate,NetSurvibox 266,admin,NetSurvibox
3COM,Netbuilder,admin,(none)
3com,Netbuilder,admin,(none)
3COM,Netbuilder,Root,(none)
Cabletron,Netgear modem/router and SSR,netman,(none)
Netopia,Netopia 7100,(none),(none)
Netopia,Netopia 9500,netopia,netopia
Netopia,Netopia 9500,netopia,netopia
Netstar,Netpilot,admin,password
Cisco,Netranger/secure IDS,netrangr,attack
Cisco,Netranger/secure IDS,root,attack
Demarc,Network Monitor,admin,my_DEMARC
Prestigio,Nobile,n/a,(none)
Nortel,Norstar,266344,266344
adtran,NxIQ,n/a,adtran
OpenConnect,OC://WebConnect Pro,admin,OCS
OpenConnect,OC://WebConnect Pro,adminstat,OCS
OpenConnect,OC://WebConnect Pro,adminview,OCS
OpenConnect,OC://WebConnect Pro,adminuser,OCS
OpenConnect,OC://WebConnect Pro,adminview,OCS
OpenConnect,OC://WebConnect Pro,helpdesk,OCS
COM3,OLe,admin,admin
Alcatel,OXO,(none),admin
Alcatel,Office 4200,n/a,1064
3COM,Office Connect ISDN Routers,n/a,PASSWORD
3COM,Office Connect ISDN Routers,n/a,PASSWORD
3COM,OfficeConnect 812 ADSL,adminttd,adminttd
3com,OfficeConnect 812 ADSL,admin,(none)
3com,OfficeConnect 812 ADSL,admin,(none)
3COM,OfficeConnect ADSL Wireless 11g Firewall Router,(none),admin
3com,OfficeConnect Wireless 11g Cable/DSL Gateway,(none),admin
3com,OfficeConnect Wireless 11g Cable/DSL Gateway,(none),admin
Livingston,Officerouter,!root,(none)
Alcatel,OmniPCX Office,ftp_inst,pbxk1064
Alcatel,OmniPCX Office,ftp_admi,kilo1987
Alcatel,OmniPCX Office,ftp_oper,help1954
Alcatel,OmniPCX Office,ftp_nmc,tuxalize
Alcatel,OmniStack 6024,admin,switch
Alcatel,Omnistack/Omniswitch,diag,switch
Alcatel,Omnistack/omniswitch,diag,switch
Xylan,Omniswitch,admin,switch
Xylan,Omniswitch,diag,switch
Oracle,Oracle RDBMS,system/manager,sys/change_on_install
Develcon,Orbitor Default Console,n/a,BRIDGE
Develcon,Orbitor Default Console,n/a,password
Proxim,Orinoco 600/2000,(none),(none)
Osicom,Osicom Plus T1/PLUS 56k,write,private
Osicom,Osicom Plus T1/PLUS 56k,write,private
Asus,P5P800,n/a,admin
Alcatel,PBX,kermit,kermit
Alcatel,PBX,dhs3mt,dhs3mt
Alcatel,PBX,at4400,at4400
Alcatel,PBX,mtch,mtch
Alcatel,PBX,mtcl,mtcl
Alcatel,PBX,root,letacla
Alcatel,PBX,dhs3pms,dhs3pms
Alcatel,PBX,adfexc,adfexc
Alcatel,PBX,client,client
Alcatel,PBX,install,llatsni
Alcatel,PBX,halt,tlah
Meridian,PBX,service,smile
Panasonic,PBX TDA 100/200/400,(none),1234
Freetech,PC BIOS,n/a,Posterie
Nimble,PC BIOS,n/a,xdfk9874t3
Research,PC BIOS,n/a,Col2ogro2
Siemens Nixdorf,PC BIOS,n/a,SKY_FOX
Cisco,PIX firewall,(none),cisco
Cyclades,PR 1000,super,surt
silex technology,PRICOM (Printserver),root,(none)
Lucent,PSAX 1200 and below,root,ascend
Lucent,PSAX 1250 and above,readwrite,lucenttech1
Lucent,PSAX 1250 and above,readonly,lucenttech2
ADC Kentrox,Pacesetter Router,n/a,secret
Lucent,PacketStar,Administrator,(none)
BMC,Patrol,patrol,patrol
BMC Software,Patrol,Administrator,the same all over
Gericom,Phoenix,Administrator,(none)
Phoenix v1.14,Phoenix v1.14,Administrator,admin
Nortel,Phone System,n/a,266344
Siemens,PhoneMail,poll,tech
Siemens,PhoneMail,sysadmin,sysadmin
Siemens,PhoneMail,tech,tech
Siemens,PhoneMail,poll,tech
Siemens,PhoneMail,sysadmin,sysadmin
Siemens,PhoneMail,tech,tech
Pirelli,Pirelli AGE-SB,admin,smallbusiness
Pirelli,Pirelli Router,admin,mu
Pirelli,Pirelli Router,admin,microbusiness
Pirelli,Pirelli Router,user,password
Livingstone,Portmaster 2R,root,(none)
Hewlett Packard,Power Manager,admin,admin
EverFocus,PowerPlex,admin,admin
EverFocus,PowerPlex,supervisor,supervisor
EverFocus,PowerPlex,operator,operator
ZyXEL,Prestige,n/a,1234
ZyXEL,Prestige,root,1234
ZyXEL,Prestige,(none),1234
ZyXEL,Prestige 100IH,n/a,1234
ZyXEL,Prestige 643,(none),1234
ZyXEL,Prestige 645,admin,1234
ZyXEL,Prestige 650,1234,1234
ZyXEL,Prestige 652HW-31 ADSL Router,admin,1234
Zyxel,Prestige 660HW,admin,admin
ZyXEL ZyWALL Series,Prestige 660R-61C,n/a,admin
ZyXEL,Prestige 900,webadmin,1234
ZyXel,Prestige P660HW,admin,1234
Microplex,Print Server,root,root
Dictaphone,ProLog,PBX,PBX
Dictaphone,ProLog,NETWORK,NETWORK
Dictaphone,ProLog,NETOP,(none)
SOPHIA (Schweiz) AG,Protector,admin,Protector
SOPHIA (Schweiz) AG,Protector,root,root
Bausch Datacom,Proxima PRI ADSL PSTN Router4 Wireless,admin,epicrouter
Blue Coat Systems,ProxySG,admin,articon
Bluecoat,ProxySG (all model),admin,admin
Avaya,Pxxx,diag,danger
Avaya,Pxxx,manuf,xxyyzz
Minolta PagrPro,QMS 4100GN PagePro,n/a,sysadm
Netopia,R910,admin,(none)
Areca,RAID controllers,admin,0
RM,RM Connect,setup,changeme
RM,RM Connect,teacher,password
RM,RM Connect,temp1,password
RM,RM Connect,admin,rmnetlm
RM,RM Connect,admin2,changeme
RM,RM Connect,adminstrator,changeme
RM,RM Connect,deskalt,password
RM,RM Connect,deskman,changeme
RM,RM Connect,desknorm,password
RM,RM Connect,deskres,password
RM,RM Connect,guest,(none)
RM,RM Connect,replicator,replicator
RM,RM Connect,RMUser1,password
RM,RM Connect,topicalt,password
RM,RM Connect,topicnorm,password
RM,RM Connect,topicres,password
NetGear,RM356,(none),1234
Siemens,ROLM PBX,eng,engineer
Siemens,ROLM PBX,op,op
Siemens,ROLM PBX,op,operator
Siemens,ROLM PBX,su,super
Siemens,ROLM PBX,admin,pwp
Siemens,ROLM PBX,admin,pwp
Siemens,ROLM PBX,eng,engineer
Siemens,ROLM PBX,op,op
Siemens,ROLM PBX,op,operator
Siemens,ROLM PBX,su,super
Netgear,RP114,(none),1234
Netgear,RP114,admin,1234
Netgear,RP614,admin,password
Netgear,RT314,admin,admin
Dynalink,RTA230,admin,admin
Linksys/ Cisco,RTP300 w/2 phone ports,admin,admin
Linksys/ Cisco,RTP300 w/2 phone ports,user,tivonpw
RedHat,Redhat 6.2,piranha,q
RedHat,Redhat 6.2,piranha,piranha
Dell,Remote Access Card,root,calvin
Nortel,Remote Office 9150,admin,root
IBM,Remote Supervisor Adapter (RSA),USERID,PASSW0RD
Integral Technologies,RemoteView,Administrator,letmein
RoamAbout,RoamAbout R2 Wireless Access Platform,admin,password
Ascend,Router,n/a,ascend
Bay Networks,Router,User,(none)
Bay Networks,Router,Manager,(none)
Bay Networks,Router,User,(none)
Digicorp,Router,n/a,BRIDGE
Digicorp,Router,n/a,password
E-Tech,Router,(none),admin
SMC,Router,admin,admin
Conexant,Router,n/a,epicrouter
Conexant,Router,n/a,admin
Zyxel,Router,(none),1234
Speedstream,Router 250 ssr250,admin,admin
SmartSwitch,Router 250 ssr2500,admin,(none)
Mikrotik,Router OS,admin,(none)
Mikrotik,Router OS,admin,(none)
SMC,Router/Modem,admin,barricade
Netgear,Router/Modem,admin,password
Fujitsu Siemens,Routers,(none),connect
medion,Routers,n/a,medion
T-Comfort,Routers,Administrator,(none)
Teledat,Routers,admin,1234
UNEX,Routers,n/a,password
Xyplex,Routers,n/a,system
Xyplex,Routers,n/a,access
Xyplex,Routers,n/a,access
Yakumo,Routers,admin,admin
Motorola,SBG900,admin,motorola
McAfee,SCM 3100,scmadmin,scmchangeme
Lantronix,SCS100,n/a,access
Lantronix,SCS1620,sysadmin,PASS
Lantronix,SCS200,n/a,admin
Lantronix,SCS3200,login,access
Lantronix,SCS400,n/a,admin
SIEMENS,SE515,admin,n/a
Siemens,SE560dsl,admin,admin
Telindus,SHDSL1421,admin,admin
SMC,SMB2804WBR,Administrator,smcadmin
SMC,SMC broadband router,admin,admin
SMC,SMC2804WBR,(none),smcadmin
SMC,SMC7004VBR,n/a,smcadmin
SMC,SMCWBR14-G,n/a,smcadmin
Watchguard,SOHO and SOHO6,user,pass
Infosmart,SOHO router,admin,0
Sorenson,SR-200,(none),admin
3com,SS III Switch,recovery,recovery
3com,SS III Switch,recovery,recovery
Mitel,SX2000,n/a,(none)
Ascend,Sahara,root,ascend
Pentaoffice,Sat Router,(none),pento
ADIC,Scalar 100/1000,admin,secure
ADIC,Scalar i2000,admin,password
Checkpoint,SecurePlatform,admin,admin
Server Technology,Sentry Remote Power Manager,GEN1,gen1
Server Technology,Sentry Remote Power Manager,GEN2,gen2
Server Technology,Sentry Remote Power Manager,ADMN,admn
3Com,Shark Fin,User,Password
Intel,Shiva,root,(none)
Intel,Shiva,Guest,(none)
Intel,Shiva,root,(none)
Nullsoft,Shoutcast,admin,changeme
Siemens Pro C5,Siemens,n/a,(none)
Sigma,Sigmacoma IPshare,admin,admin
Brocade,Silkworm,admin,password
adtran,Smart 16/16e,n/a,(none)
adtran,Smart 16/16e,n/a,PASSWORD
APC,Smart UPS,apc,apc
apc,Smartups 3000,apc,apc
Sonic-X,SonicAnime,root,admin
Polycom,Soundpoint VoIP phones,Polycom,SpIp
Symbol,Spectrum,n/a,Symbol
Siemens,SpeedStream 4100,admin,hagpolm1
Efficient Networks,Speedstream 5711,n/a,4getme2
Efficient,Speedstream DSL,n/a,admin
Efficient,Speedstream DSL,n/a,admin
Aethra,Starbridge EU,admin,password
Funk Software,Steel Belted Radius,admin,radius
3COM,SuperStack 3,admin,(none)
3COM,SuperStack 3,monitor,monitor
3COM,SuperStack 3,manager,manager
Bay Networks,SuperStack II,security,security
Bay Networks,SuperStack II,security,security
3COM,SuperStack II Switch,debug,synnet
3COM,SuperStack II Switch,tech,tech
3COM,SuperStack II Switch,tech,tech
U.S. Robotics,SureConnect 9003 ADSL Ethernet/USB Router,root,12345
U.S. Robotics,SureConnect 9105 ADSL 4-Port Router,admin,admin
US Robotics,SureConnect ADSL,support,support
3com,Switch,admin,admin
3com,Switch,admin,admin
Bay Networks,Switch,n/a,NetICs
Bay Networks,Switch,n/a,NetICs
Lucent,System 75,bciim,bciimpw
Lucent,System 75,bcim,bcimpw
Lucent,System 75,bcms,bcmspw
Lucent,System 75,bcnas,bcnaspw
Lucent,System 75,blue,bluepw
Lucent,System 75,browse,browsepw
Lucent,System 75,browse,looker
Lucent,System 75,craft,craft
Lucent,System 75,craft,craftpw
Lucent,System 75,cust,custpw
Lucent,System 75,enquiry,enquirypw
Lucent,System 75,field,support
Lucent,System 75,inads,indspw
Lucent,System 75,inads,inads
Lucent,System 75,init,initpw
Lucent,System 75,locate,locatepw
Lucent,System 75,maint,maintpw
Lucent,System 75,maint,rwmaint
Lucent,System 75,nms,nmspw
Lucent,System 75,rcust,rcustpw
Lucent,System 75,support,supportpw
Lucent,System 75,tech,field
ALLNET,T-DSL Modem,admin,admin
Deutsch Telekomm,T-Sinus 130 DSL,(none),0
Deutsche Telekom,T-Sinus 154 DSL,(none),0
Deutsche Telekom,T-Sinus DSL 130,admin,(none)
IBM,T20,n/a,admin
adtran,T3SU 300,n/a,adtran
IBM,T42,Administrator,admin
Tandem,TACL,super.super,(none)
Tandem,TACL,super.super,master
TANDBERG,TANDBERG,(none),TANDBERG
Dallas Semiconductors,TINI embedded JAVA Module,root,tini
Cyclades,TS800,root,tslinux
adtran,TSU IQ/DSU IQ,n/a,(none)
"""

    if len(sys.argv) != 2:
        print("Usage: default-passwords.py <search_value>")
        sys.exit(1)

    partial_value = sys.argv[1]

    headers, data = parse_csv_from_string(csv_data)

    results = search_csv(headers, data, partial_value)

    print(f"Search Results for '{partial_value}'")
    display_results(results)
