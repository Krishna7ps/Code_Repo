import pprint

data='''2D Echo: RWMA+,Hypokinesia mid postero inferior segm,basal IVS,LVEF=40%,;SGOT=27;SGPT=64; ALP=108,creat=0.9
bilirubin:T=0.86,D=0.48;SGOT=45;SGPT=74;ALP=117, creat=0.67
2D ECHO: No RWMA, EF=55%; SGOT=62;SGPT=42; ALP=156,creat=0.89
2DECHO:EF=63%,Conc.LVH;SGOT=41;SGPT=32; ALP=122, creat=0.76
SGOT=60;SGPT=48; ALP=126,creat=0.55
SGOT=28;SGPT=30;ALP=42;Creat0.57
SGOT=23;SGPT=23;ALP=84; Creat=0.8
SGOT=19;SGPT=20;ALP=94; Creat=0.6
SGOT=27;SGPT=50;ALP=129;Urine:albumin=nil;sugar= +; Creat=0.7mg/dL
SGOT=67;SGPT=76;ALP=133;Creat=1.11; urine c/s: E.coli, B/L:immature cataract;
SGOT=15;SGPT=15;ALP=87,Albumin;Sugar-nil;Creat0.56
SGOT=35;SGPT=24;ALP=117;Creat=1.19
SGOT=30;SGPT=39;ALP=67;Creat=0.74
SGOT=77;SGPT=96;ALP=122;Creat=0.87
SGOT=31;SGPT=32;ALP=114; creat=1.07 spine xray=osteoporotic changes
SGOT=28;SGPT=30;ALP=141;Creat=1.13
SGOT=33;SGPT=40;ALP=114;Creat=0.67

OPTIONAL TEST [Name of the test & Report]



SGOT=13;SGPT=30;ALP=134;Creat=0.82
Urine: RBC6-8/WBC-MANY; CREAT=1.4;LFT-NORMAL,urinr c/s=sterile
2DECHO:RWMA+,mild LV dysfunction EF=48%,Hypokinesia inferior segment
SGOT=13;SGPT=30;ALP=134;Creat=0.82
SGOT=28;SGPT=41;ALP=150;Creat=1.01
SGOT=43;SGPT=77;ALP=145;Creat=0.66
SGOT=21;SGPT=20;ALP=62;Creat=0.83
FT4=0.8,anti TPO=1.2,Creat=0.7;SGOT=25;SGPT=21;ALP=111
BUN=17;Creat=1mg/dl;T.bilirubin=0.5mg/dl;D.bilirubun=0.14mg/dl;SGOT=23;SGPT=50;ALP=106
SGOT=25;SGPT=33;ALP=87;creat=0.99
SGOT=19; SGPT=26; ALP=71;creat=1.19
SGOT=31;SGPT=56;ALP=119;Creat=0.89
SGOT=27;SGPT=50;ALP=129;Urine:albumin=nil;sugar= +; Creat=0.7mg/dL
SGOT=27;SGPT=50;ALP=129;Urine:albumin=nil;sugar=nil;Creat=0.8;mg/dL
SGOT=17;SGPT=13;ALP=85;Urine:albumin=nil;sugar=ni;Creat=0.55;mg/dL
SGOT=27;SGPT=50;ALP=129;Urine:albumin=nil;sugar= +; Creat=0.7mg/dL
SGOT=27;SGPT=42;ALP=125;Urine:albumin=nil;sugar= +; Creat=0.7mg/dL
SGOT=16;SGPT=19;ALP=77;Urine:albumin=nil;sugar= +; Creat=0.67mg/Dl
OPTIONAL TEST [Name of the test & Report]


SGOT=15;SGPT=15;ALP=87 Urine Albumin;Sugar-nil;Creat0.56
SGOT=21;SGPT=31;ALP=67;Urine albumin=+;sugar=+;Creat=1.37
SGOT=18;SGPT=18;ALP=131 Creat=0.8;Urine albumin=nil,Sugar++,urine c/s=klebsiella Pneumonia
SGOT=16;SGPT=19;ALP=77;Urine:albumin=nil;sugar= +; Creat=0.67mg/Dl
SGOT=27;SGPT=50;ALP=129;Urine:albumin=nil;sugar= +; Creat=0.7mg/dL
SGOT=39;SGPT=43;ALP=162;Creat=1.03;Urinealbumin=nil,Sugar=+++
SGOT=14;SGPT=12;ALP=134;CREAT=1.09
SGOT=22;SGPT=30;ALP=103;Urine albumin=nil,sugar=+++ ;creat=0.76
SGOT=13,SGPT=24;ALP=97,Urine sugar=trace;Creat=1.1
SGOT=9;SGPT=11;ALP=85,TSH=4.8;Creat=0.6
SGOT=42;SGPT=70;ALP=150;Creat=0.73
SGOT=18;SGPT=24;ALP=100; Creat=0.69
SGOT=23,SGPT=19,ALP=84; Creat=0.5
SGOT=22;SGPT=26;;ALP=55;Creat=0.66
SGOT=25;SGPT=44;ALP=99;Creat=0.69
SGOT=28,SGPT=46,ALP=82,Creat=0.9
SGOT=13;SGPT=30;ALP=134;Creat=0.82
SGOT=17;SGPT=18;ALP=89;Creat=0.6
SGOT=20;SGPT=26;ALP=93;Creat=0.89
SGOT=30;SGPT=39;ALP=67;Creat=0.74
OPTIONAL TEST [Name of the test & Report]


SGOT=18;SGPT=14;ALP=140;Creat=1.18
SGOT=35;SGPT=24;ALP=117;Creat=1.19
SGOT=30;SGPT=39;ALP=67;Creat=0.74
SGOT=22;SGPT=24;ALP=104;Creat=0.53
SGOT=21;SGPT=13;ALP=122;Creat=1.43
SGOT=11;SGPT=6;ALP=138;Creat=1.46
SGOT=24;SGPT=19;ALP=98,Creat=0.83
SGOT=24;SGPT=14;ALP=117;Creat=0.6
SGOT=9;SGPT=8;ALP=92;Creat=0.8
SGOT=38,SGPT=5;ALP=93,Creat=1.1,
2D ECHO-EF=55%,SGOT=34,SGPT=0;ALP=73;Creat=0.77
SGOT=15;SGPT=16,ALP=79,Creat=1.2
SGOT=20;SGPT=26;ALP=97;Creat=1.3
SGOT=303;SGPT=141;ALP=196;Creat=0.8,NS1 ag= Positive
SGOT=28;SGPT=2;ALP=229;Creat=0.66
URINE CULTURE=E.COLI; SGOT=16, SGPT=18;ALP=100;Creat=0.8
SGOT=37;SGPT=33;ALP=98;Creat=0.4
SGOT=24;SGPT=26;ALP=100,Creat=0.5
SGOT=21;SGPT=20;ALP=62;Creat=0.83
SGOT=38,SGPT=47;ALP=116,Creat=0.6,
SGOT=15;SGPT=16,ALP=84,Creat=0.81
SGOT=43;SGPT=77;ALP=145;Creat=0.66
SGOT=28;SGPT=41;ALP=150;Creat=1.01
SGOT=17;SGPT=30;ALP=65; Creat=0.7 Pus C/S-Staph.Aureus
SGOT=23;SGPT=23;ALP=84; Creat=0.8
SGOT=19;SGPT=20;ALP=94; Creat=0.6
SGOT=37;SGPT=44;ALP=73; Creat=0.93 DENGUE NS +
SGOT=19;SGPT=17;ALP=123; Creat=1.9
SGOT=15;SGPT=17;ALP=125; Creat=0.6
SGOT=42;SGPT=79;ALP=78; Creat=0.68
SGOT=37;SGPT=40;ALP=85; Creat=0.98
SGOT=17;SGPT=24;ALP=147; Creat=0.77
SGOT=27;SGPT=20;ALP=72; Creat=0.82
SGOT=81;SGPT=74;ALP=144; Creat=0.69
SGOT=34;SGPT=48;ALP=129; Creat=0.78
SGOT=22;SGPT=22;ALP=141; Creat=0.97, 2D ECHO=NO RWMA, EF=48%
Dengue IgM +,SGOT=134;SGPT=99;ALP=188;Creat=1.2
BLOOD C/S-Pseudomonas Oryzihabitans;SGOT=36;SGPT=31;ALP=75; Creat=0.59
SGOT=21;SGPT=24;ALP=84; Creat=0.85
SGOT=29;SGPT=27;ALP=64; Creat=0.68
SGOT=36;SGPT=31;ALP=75; Creat=0.59
SGOT=40;SGPT=41;ALP=96; Creat=1.1
SGOT=26;SGPT=32;ALP=106;Creat=1.1 ; Urine R/M= RBC=2-3;WBC=4
SGOT=34;SGPT=45;ALP=100; creat=1.0
SGOT=21;SGPT=24;ALP=84; Creat=0.85
Urine Microscopy-wbc:many/HPF.1;rbc :3-4  URINE R/M-albumin +,SGOT=15;ALT=20;ALP=142;Creat=0.69
SGOT=19;SGPT=18;ALP=84; Creat=0.78
SGOT=21;SGPT=25;ALP=73; Creat=0.67
SGOT=20;SGPT=22;ALP=105; Creat=1.1
SGOT=23;SGPT=69;ALP=190;Creatinine=0.6
SGOT=23;SGPT=18;ALP=80;Creatinine=0.66
SGOT=26;SGPT=34;ALP=113;creat=0.97
SGOT=15;SGPT=15;ALP=103;Creatinine=0.64
SGOT=34;SGPT=29;ALP=74; Creat=0.65
SGOT=31;SGPT=36;ALP=141;Creat=1.1 2DECHO=Normal; EF=61%
SGOT=18;SGPT=29;ALP=126;Creat=0.44
SGOT=21;SGPT=24;ALP=92;Creat=0.8
SGOT=31;SGPT=20;ALP=95;Creat=0.56
SGOT=23;SGPT=24;ALP=109;Creat=0.49
SGOT=13;SGPT=20;ALP=78;Creat=0.73
SGOT=16;SGPT=20;ALP=86;Creat=0.87
SGOT=29;SGPT=22;ALP=91;Creat=0.98
URINE CULTURE=CITROBACTER;SGOT=70;SGPT=74;ALP=85;Creat=0.62
SGOT=22;SGPT=14;ALP=56;Creat=0.57
SGOT=22;SGPT=31,ALP=77;Creat=0.7
Urine C/S- CANDIDA,SGOT=27;SGPT=28;ALP=110;Creat=0.82
SGOT=27;SGPT=46;ALP=55; Creat=0.6
SGOT=28;SGPT=30;ALP=42;Creat0.57
SGOT=31;SGPT=38;ALP=75;Creat=0.88
SGOT=20;SGPT=19;ALP=167;Creat=1.01, S.IRON=17;TIBC=387;S.FERRITIN=6.5
Dengue NS1 +,IgM ELISA +,Urine C/S=CANDIDA spp, SGOT=188,SGPT=102;ALP=211;Creat=1.18
SGOT=21;SGPT=18;ALP=118;Creat=0.75
Dengue NS1 +,Urine C/S=E.COLI, SGOT=60,SGPT=95;ALP=240;Creat=0.8
SGOT=32;SGPT=31;ALP=101;Creat=0.77
Urine R/M=RBC-1,SGOT=17;SGPT=21;ALP=91;Creat=0.89
Urine R/M=WBC-10,LE +; GLU +++; SGOT=14;SGPT=26;ALP=103;Creat=0.7
Urine R/M=WBC-4,RBC=4; PROTEIN+; SGOT=15;SGPT=14;ALP=151;Creat=1.8
Urine R/M=PROTEIN +++, SGOT=21;SGPT=17;ALP=61;Creat=1.86
Urine R/M=KETONE+; SGOT=61;SGPT=85;ALP=96;Creat=0.67, 2D ECHO=EF-55:%
Urine R/M= GLU ++++;LE +,WBC=16; SGOT=13;SGPT=12;ALP=64;Creat=1.06
SGOT=21;SGPT=40;ALP=51;Creat=1.1
Dengue NS1 +; Urine R/M=KETONE++;GLU++++; SGOT=47;SGPT=73;ALP=105;Creat=1.07
Urine R/M=PROTEIN +,LE=+,RBC=5 SGOT=66;SGPT=55;ALP=232;Creat=1.68
S.IRON=11;S.TIBC=214;Urine R/M=Glu++++,KETONE ++ , LE +++, WBC=Many,RBC=++,  SGOT=17;SGPT=11;ALP=131;Creat=1.4
Urine R/M=GLU++,WBC=22, Urine C/S-E.COLI,SGOT=33;SGPT=30;ALP=127;Creat=0.66
Urine R/M- PROTEIN-TRACE,GLU ++++;SGOT=39;SGPT=44;ALP=107;Creat=0.91
2D ECHO-EF=55%,Conc LVH,MILD AVR;Urine R/M=GLU++++,WBC=12;RBC=16; SGOT=30,SGPT=36;ALP=70;Creat=0.77
SGOT=15;SGPT=18;ALP=82; Creat=0.82
SGOT=23;SGPT=19;ALP=46;Creat=1.34
UGI Endoscopy = H.Pyoric Gastritis, Urine R/M=GLU++++,Pus culture-Staph aureus, SGOT=20;SGPT=19;ALP=105;Creat=0.6
SGOT=20;SGPT=22;ALP=97;Creat=0.82;Urine R/M=PROTEIN ++++
SGOT=20;SGPT=25;ALP=81;Creat=0.97
SGOT=15;SGPT=22;ALP=69;Creat=0.77
2D ECHO=DCMD, EF=35%; Urine C/S=STAPH.HOMINIS;S.IRON=46;S.TIBC=346,SGOT=15;ALT=20;ALP=142;Creat=0.54
SGOT=30;SGPT=58;ALP=179;Creat=0.68
 SGOT=19;SGPT=21;ALP=117;Creat=1.74
S.FERRITIN=9.9;VIT B12=1041;S.FOLATE=8.11;SGOT=21;SGPT=20;ALP=201;Creat=0.50
SGOT=30;SGPT=38;ALP=70;Creat=0.4
SGOT=13;SGPT=12;ALP=100;Creat=1.1
SGOT=19;SGPT=33;ALP=290;Creat=0.84
SGOT=50;SGPT=39;ALP=77;Creat=0.68
SGOT=46;SGPT=99;ALP=105;Creat=0.76
SGOT=15;SGPT=23;ALP=71;Creat=0.5
SGOT=30;SGPT=40;Creat=1.24
SGOT=13;SGPT=30;ALP=134;Creat=0.82
Urine R/M=KETONE+; SGOT=21;SGPT=17;ALP=90;Creat=0.96
SGOT=43;SGPT=87;ALP=100;Creat=0.76
SGOT=32;SGPT=313;ALP=78;Creat=0.58
SGOT=32;SGPT=32;ALP=89;Creat=0.83
SGOT=13;SGPT=14;ALP=85;Creat=0.6
SGOT=18;SGPT=22;ALP=148;Creat=0.62
SGOT=21;SGPT=22;ALP=79;Creat=0.71
SGOT=45;SGPT=54;ALP=129;Creat=0.59
SGOT=18;SGPT=20;ALP=108;Creat=1.32
SGOT=15;ALT=20;ALP=142;Creat=0.54
SGOT=12;SGPT=17;ALP=99;Creat=1.1
SGOT=38;ALP=36;ALP=83;Creat=0.7
SGOT=25;SGPT=22;ALP=95;Creat=0.4640
SGOT=13;SGPT=16;ALP=79;Creat=0.73
SGOT=25;SGPT=28;ALP=144;Creat=0.61
SGOT=25;SGPT=28;ALP=144;Creat=0.61
SGOT=34;SGPT=23;ALP=104;Creat=0.97
SGOT=58;SGPT=109;ALP=98;Creat=0.40
SGOT=46;SGPT=56;ALP=99;Creat=1.51
SGOT=27;SGPT=16;ALP=134;Creat=0.5
SGOT=31;SGPT=29;ALP=42;Creat=1.09
SGOT=17;SGPT=22;ALP=117;Creat=0.57
SGOT=17;SGPT=15;ALP=110;Creat=0.68
SGOT=38;SGPT=34;ALP=119;Creat=0.92
SGOT=46;SGPT=27;Creat=0.83
SGOT=38;SGPT=26;ALP=103;Creat=1.09
SGOT=49;SGPT=76;ALP=91;Creat=0.82
SGOT=28;SGPT=40;ALP=142;Creat=0.62
SGOT=25;SGPT=57;ALP=143;Creat=0.93
SGOT=46;SGPT=55;ALP=133;Creat=1.03
SGOT=25;SGPT=44;ALP=141;Creat=0.69
SGOT=25;SGPT=29;ALP=71;Creat=0.85
Urine C/S=E.COLI,SGOT=15;SGPT=12;ALP=39;Creat=0.3
Urine R/M= RBC=++++,MANY WBC=4; SGOT=58;SGPT=127;ALP=127;Creat=0.79
SGOT=15;SGPT=14;ALP=85;Creat=0.70
SGOT=20;SGPT=21;ALP=101;Creat=0.77
SGOT=22;SGPT=13;ALP=100;Creat=0.6
SGOT=34;SGPT=28;ALP=139;Creat=0.5
SGOT=18;SGPT=17;ALP=129;Creat=0.68
SGOT=26;SGPT=37;ALP=172; creat=1.1'''.split()

count=0
extract=[]
for i in range(len(data)):
    extract.append(data[i].lower().split(','))


'''
for i in range(len(extract)):
    for j in range(len(extract[i])):
        if 'cr' in extract[i][j]:
#            print(extract[i][j])
            count=count+1
#        else:
#            print("--------ERROR RECORD----------------->")

#print(extract)
print("Input data records=",count)
'''


'''
# For Creat -----------------------------------------------------------------
temp=[]
for i in range(len(extract)):
    for j in range(len(extract[i])):
        if 'cr' in extract[i][j]:
            temp.append(extract[i][j].split(';'))
#print("Temp is", temp)

end_data=[]
for i in range(len(temp)):
    end_data=end_data+temp[i]


for i in range(len(end_data)):
    end_data[i]=end_data[i].strip()

print("End data is \n")
#pprint.pprint(end_data)

l=len(end_data)
for i in range(l):    
    if not end_data[i].startswith('cr'):
        end_data[i]=0

for i in range(len(end_data)):
    try:
        end_data.remove(0)
    except:
        pass
for i in range(len(end_data)):
    end_data[i]=end_data[i].strip('creat=').strip('inine=').rstrip('mg/dl')        
#print("end data is ")
print(end_data)
print("Total Valid Records",len(end_data))

sum=0
for i in range(len(end_data)):
    sum=sum+float(end_data[i])

print("Creat_sum=",sum, "Mean=", sum/len(end_data))
'''


# For SGPT---------------------------------------------------------------------

temp=[]
for i in range(len(extract)):
    for j in range(len(extract[i])):
        if 'sgpt' in extract[i][j]:
            temp.append(extract[i][j].split(';'))
print("Temp is", temp)

end_data=[]
for i in range(len(temp)):
    end_data=end_data+temp[i]


for i in range(len(end_data)):
    end_data[i]=end_data[i].strip()

print("End data is \n")
#pprint.pprint(end_data)

l=len(end_data)
for i in range(l):    
    if not end_data[i].startswith('sgpt'):
        end_data[i]=0
#region

for i in range(len(end_data)):
    try:
        end_data.remove(0)
    except:
        pass
for i in range(len(end_data)):
    end_data[i]=end_data[i].strip('sgpt=')        
print("end data is ")
print(end_data)
print("Total Valid Records",len(end_data))

sum=0
for i in range(len(end_data)):
    sum=sum+int(end_data[i])

print("sgpt_sum=",sum, "Mean=", sum/len(end_data))


# For SGOT ---------------------------------------------------------------
'''
temp=[]
for i in range(len(extract)):
    for j in range(len(extract[i])):
        if 'sgot' in extract[i][j]:
            temp.append(extract[i][j].split(';'))
print("Temp is", temp)

end_data=[]
for i in range(len(temp)):
    end_data=end_data+temp[i]


for i in range(len(end_data)):
    end_data[i]=end_data[i].strip()

print("End data is \n")
#pprint.pprint(end_data)

l=len(end_data)
for i in range(l):    
    if not end_data[i].startswith('sgot'):
        end_data[i]=0

for i in range(len(end_data)):
    try:
        end_data.remove(0)
    except:
        pass
for i in range(len(end_data)):
    end_data[i]=end_data[i].strip('sgot=')        
print("end data is ")
print(end_data)
print("Total Valid Records",len(end_data))

sum=0
for i in range(len(end_data)):
    sum=sum+int(end_data[i])

print("sgot_sum=",sum, "Mean=", sum/len(end_data))
'''
# For ALP --------------------------------------------------------------
'''
temp=[]
for i in range(len(extract)):
    for j in range(len(extract[i])):
        if 'alp' in extract[i][j]:
            temp.append(extract[i][j].split(';'))
print("Temp is", temp)

end_data=[]
for i in range(len(temp)):
    end_data=end_data+temp[i]


for i in range(len(end_data)):
    end_data[i]=end_data[i].strip()

print("End data is \n")
#pprint.pprint(end_data)

l=len(end_data)
for i in range(l):    
    if not end_data[i].startswith('alp'):
        end_data[i]=0

for i in range(len(end_data)):
    try:
        end_data.remove(0)
    except:
        pass
for i in range(len(end_data)):
    end_data[i]=end_data[i].strip('alp=')        
print("end data is ")
print(end_data)
print("Total Valid Records",len(end_data))

sum=0
for i in range(len(end_data)):
    sum=sum+int(end_data[i])

print("alp_sum=",sum, "Mean=", sum/len(end_data))

'''








