from __future__ import print_function
import sys,csv,os

day = 1
file_name=str(day)+'.cisdl'#sys.argv[1]
f=open("output.csv", 'w')
writer = csv.writer(f)
li='''Day
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
ALC'''.split("\n")
writer.writerow(li)
with open(file_name) as fil:
    for j in fil.readlines()[18:48]:
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
        pr=[day,umax,umin,CAh,LAh,imaxload,imaxpv,umaxmodul,uminmodul,SOC,TMax,TMin,night,ALC]
        #[print(li[i],pr[i]) for i in range(len(li))]
        writer.writerow(pr)
f.close()
content = open("output.csv", "r").read().replace('\r\n','\n')
with open("output2.csv", "w") as g:
    g.write(content)
