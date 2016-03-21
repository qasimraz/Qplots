# Place this file in the folder containing .cisdl files

import sys,csv,os

'''Strings'''
li='''File_name
Time
Max. Battery Voltage (V)
Min. Battery Voltage (V)
Charge Amp Hours (Ah)
Load Amp Hours (A)
Max Load Current (A)
Max. PV Current (A)
Max. PV Voltage (V)
Min. PV Voltage (V)
Batt State of Charge (SOC%)
Max Battery Temp
Min Battery Temp
Length of Night (h)
ALC
Flags'''.split("\n")

months='''January 
February 
March 
April 
May 
June 
July 
August 
September 
October 
November 
December'''.split("\n")

# get files
files=os.listdir('.')
files=[i for i in files if i.endswith('.cisdl')]
'''Day file'''
f=open("day2.csv", 'w')
writer = csv.writer(f)
writer.writerow(li)
'''Month file'''
d=open("month2.csv", 'w')
month = csv.writer(d)
month.writerow(li)

for i in files:
    c=0
    with open(i) as fil:
        '''Process Days 1 - 30'''
        for j in fil.readlines()[18:72]: #18-48 for days
            c+=1
            byt_day=list(map(int,j.split(";")[:-1]))
            umax = (9.0 + byt_day[0] * 0.1) # Max Battery Voltage
            umin = (9.0 + byt_day[1] * 0.1) # Min Battery Voltage
            CAh=2.56*byt_day[3]+byt_day[2]/100.0 # Charge Amp Hours
            LAh=2.56*byt_day[5]+byt_day[4]/100.0 # Load Amp Hours
            umaxmodul=byt_day[6]/2.0 #max pv voltage
            uminmodul=byt_day[7]/2.0 #min pv voltage
            imaxload=byt_day[8]/2.0 #Max load current
            imaxpv=byt_day[9]/2.0 #PV current
            SOC=int(6.66*(byt_day[10]%16)+.5)
            ALC=int(0.4166*(byt_day[10]-byt_day[10]%16)+.5)
            TMax=[byt_day[11],byt_day[11]-256][byt_day[11]>128]
            TMin = [byt_day[12],byt_day[12]-256][byt_day[12]>128]
            night=byt_day[13]/6.0
            flags=str(bin(byt_day[14])).lstrip('0')
            if night==42.5: # check if data is valid
                continue
            pr=[i,c,umax,umin,CAh,LAh,imaxload,imaxpv,umaxmodul,uminmodul,SOC,TMax,TMin,night,ALC,flags]
            #[print(li[i],pr[i]) for i in range(len(li))]
            if c<31: writer.writerow(pr)
            else:
                pr[1]-=30
                month.writerow(pr)
            
        c=0
'''Post - Processing of csv'''
f.close()
d.close()

content = open("day2.csv", "r").read().replace('\r\n','\n')
with open("day.csv", "w") as g:
    g.write(content)
os.remove('day2.csv')

content = open("month2.csv", "r").read().replace('\r\n','\n')
with open("month.csv", "w") as g:
    g.write(content)
os.remove('month2.csv')

