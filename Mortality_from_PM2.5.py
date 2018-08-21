# This are lines of code that generate 206 plots of countries for Mortality from PM2.5 in diffrent countries
# Source: OECD, this is the link to the data where you can download. \
# https://stats.oecd.org/Index.aspx?DataSetCode=EXP_MORSC
# Change the argument in pd.read_csv() to read data.
# Warning: This will take some time. I used Spyder IDE for this Data Analysis.

import matplotlib.pyplot as plt
import pandas as pd
c = ['Country', 'Year', 'Value']
x = c[1]
y = c[2]
a = 'Year'
b = 'Mortality from PM2.5 (Per 1,000,000 inhabitants)'
df = pd.read_csv(r'C:\Users\jitpa\Desktop\EXP_MORSC_07082018033853673.csv')


aus = df.loc[0:5, c]
aut = df.loc[6:11, c]
bel = df.loc[12:17, c]
can = df.loc[18:23, c]
cze = df.loc[24:29, c]
dnk = df.loc[30:35, c]
fin = df.loc[36:41, c]
fra = df.loc[42:47, c]
deu = df.loc[48:53, c]
grc = df.loc[54:59, c]
hun = df.loc[60:65, c]
isl = df.loc[66:71, c]
irl = df.loc[72:77, c]
ita = df.loc[78:83, c]
jpn = df.loc[84:89, c]
kor = df.loc[90:95, c]
lux = df.loc[96:101, c]
mex = df.loc[102:107, c]
nld = df.loc[108:113, c]
nzl = df.loc[114:119, c]
nor = df.loc[120:125, c]
pol = df.loc[126:131, c]
prt = df.loc[132:137, c]
svk = df.loc[138:143, c]
esp = df.loc[144:149, c]
swe = df.loc[150:155, c]
che = df.loc[156:161, c]
tur = df.loc[162:167, c]
gbr = df.loc[168:173, c]
usa = df.loc[174:179, c]
g7m = df.loc[180:185, c]
afg = df.loc[186:191, c]
alb = df.loc[192:197, c]
dza = df.loc[198:203, c]
asm = df.loc[204:209, c]
and1 = df.loc[210:215, c]
ago = df.loc[216:221, c] 
atg = df.loc[222:227, c] 
arg = df.loc[228:233, c] 
arm = df.loc[234:239, c] 
aze = df.loc[240:245, c] 
bhs = df.loc[246:251, c] 
bhr = df.loc[252:257, c] 
bgd = df.loc[258:263, c] 
brb = df.loc[264:269, c] 
blr = df.loc[270:275, c] 
blz = df.loc[276:281, c] 
ben = df.loc[282:287, c] 
bmu = df.loc[288:293, c] 
btn = df.loc[294:299, c] 
bol = df.loc[300:305, c] 
bih = df.loc[306:311, c] 
bwa = df.loc[312:317, c] 
bra = df.loc[318:323, c] 
brn = df.loc[324:329, c] 
bgr = df.loc[330:335, c] 
bfa = df.loc[336:341, c]
bdi = df.loc[342:347, c] 
khm = df.loc[348:353, c] 
cmr = df.loc[354:359, c] 
cpv = df.loc[360:365, c] 
caf = df.loc[366:371, c] 
tcd = df.loc[372:377, c] 
chl = df.loc[378:383, c] 
chn = df.loc[384:389, c] 
col = df.loc[390:395, c] 
com = df.loc[396:401, c] 
cog = df.loc[402:407, c] 
cri = df.loc[408:413, c] 
civ = df.loc[414:419, c] 
hrv = df.loc[420:425, c] 
cub = df.loc[426:431, c] 
cyp = df.loc[432:437, c] 
prk = df.loc[438:443, c] 
cod = df.loc[444:449, c] 
dji = df.loc[450:455, c] 
dma = df.loc[456:461, c] 
dom = df.loc[462:467, c] 
ecu = df.loc[468:473, c] 
egy = df.loc[474:479, c] 
slv = df.loc[480:485, c] 
gnq = df.loc[486:491, c] 
eri = df.loc[492:497, c] 
est = df.loc[498:503, c] 
eth = df.loc[504:509, c] 
fji = df.loc[510:516, c] 
gab = df.loc[516:521, c] 
gmb = df.loc[522:527, c]
geo = df.loc[528:533, c] 
gha = df.loc[534:539, c] 
grl = df.loc[540:545, c] 
grd = df.loc[546:551, c] 
gum = df.loc[552:557, c] 
gtm = df.loc[558:563, c] 
gin = df.loc[564:569, c] 
gnb = df.loc[570:575, c]
guy = df.loc[576:581, c]
hti = df.loc[582:587, c] 
hnd = df.loc[588:593, c] 
ind = df.loc[594:599, c] 
idn = df.loc[600:605, c] 
irn = df.loc[606:611, c] 
irq = df.loc[612:617, c] 
isr = df.loc[618:623, c] 
jam = df.loc[624:629, c] 
jor = df.loc[630:635, c] 
kaz = df.loc[636:641, c] 
ken = df.loc[642:647, c] 
kir = df.loc[648:653, c] 
kgz = df.loc[654:659, c] 
lao = df.loc[660:665, c] 
lva = df.loc[666:671, c] 
lbn = df.loc[672:677, c] 
lso = df.loc[678:683, c] 
lbr = df.loc[684:689, c] 
lby = df.loc[690:695, c] 
ltu = df.loc[696:701, c] 
mkd = df.loc[702:707, c] 
mdg = df.loc[708:713, c] 
mwi = df.loc[714:719, c] 
mys = df.loc[720:725, c] 
mdv = df.loc[726:731, c] 
mli = df.loc[732:737, c]
mlt = df.loc[738:743, c] 
mhl = df.loc[744:749, c] 
mrt = df.loc[750:755, c] 
mus = df.loc[756:761, c] 
fsm = df.loc[762:767, c] 
mda = df.loc[768:773, c] 
mng = df.loc[774:779, c]
mar = df.loc[780:785, c] 
moz = df.loc[786:791, c] 
mmr = df.loc[792:797, c] 
nam = df.loc[798:803, c] 
npl = df.loc[804:809, c] 
noc = df.loc[810:815, c]
ner = df.loc[816:821, c] 
nga = df.loc[822:827, c] 
mnp = df.loc[828:833, c] 
pse = df.loc[834:839, c] 
omn = df.loc[840:845, c] 
pak = df.loc[846:851, c] 
pan = df.loc[852:857, c] 
png = df.loc[858:863, c] 
pry = df.loc[864:869, c] 
per = df.loc[870:875, c] 
phl = df.loc[876:881, c] 
pri = df.loc[882:887, c] 
qat = df.loc[888:893, c] 
rou = df.loc[894:899, c] 
rus = df.loc[900:905, c]
rwa = df.loc[906:911, c] 
lca = df.loc[912:917, c] 
vct = df.loc[918:923, c] 
wsm = df.loc[924:929, c] 
stp = df.loc[930:935, c] 
sau = df.loc[936:941, c] 
sen = df.loc[942:947, c] 
syc = df.loc[948:953, c] 
sle = df.loc[954:959, c] 
sgp = df.loc[960:965, c] 
svn = df.loc[966:971, c] 
slb = df.loc[972:977, c] 
som = df.loc[978:983, c] 
zaf = df.loc[984:989, c] 
lka = df.loc[990:995, c] 
sdn = df.loc[996:1001, c] 
sur = df.loc[1002:1007, c] 
swz = df.loc[1008:1013, c] 
syr = df.loc[1014:1019, c] 
twn = df.loc[1020:1025, c] 
tjk = df.loc[1026:1031, c] 
tza = df.loc[1032:1037, c] 
tha = df.loc[1038:1043, c] 
tls = df.loc[1044:1049, c] 
tgo = df.loc[1050:1055, c] 
ton = df.loc[1056:1061, c] 
tto = df.loc[1062:1067, c] 
tun = df.loc[1068:1073, c] 
tkm = df.loc[1074:1179, c] 
uga = df.loc[1080:1085, c] 
ukr = df.loc[1086:1091, c] 
are = df.loc[1092:1097, c] 
ury = df.loc[1098:1103, c] 
uzb = df.loc[1104:1109, c] 
vut = df.loc[1110:1115, c] 
ven = df.loc[1116:1121, c] 
vnm = df.loc[1122:1127, c]
vir = df.loc[1128:1133, c] 
yem = df.loc[1134:1139, c] 
zmb = df.loc[1140:1145, c] 
zwe = df.loc[1146:1151, c] 
wlb = df.loc[1152:1157, c] 
asean = df.loc[1158:1163, c] 
srb = df.loc[1164:1169, c] 
mne = df.loc[1170:1175, c] 
g20 = df.loc[1176:1181, c] 
briics = df.loc[1182:1187, c] 
ssd  = df.loc[1188:1193, c]
eu28 = df.loc[1194:1199, c] 
oecd = df.loc[1200:1205, c] 
oecde = df.loc[1206:1211, c] 
oecdao = df.loc[1212:1217, c] 
oecdam = df.loc[1218:1223, c] 
lac = df.loc[1224:1229, c] 
mena = df.loc[1230:1235, c]

x1 = ['  ','Australia', 'Austria', 'Belgium', 'Canada', 'Czech Republic',
       'Denmark', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
       'Iceland', 'Ireland', 'Italy', 'Japan', 'Korea', 'Luxembourg',
       'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland',
       'Portugal', 'Slovak Republic', 'Spain', 'Sweden', 'Switzerland',
       'Turkey', 'United Kingdom', 'United States', 'G7', 'Afghanistan',
       'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
       'Antigua and Barbuda', 'Argentina', 'Armenia', 'Azerbaijan',
       'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
       'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
       'Bosnia and Herzegovina', 'Botswana', 'Brazil',
       'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi',
       'Cambodia', 'Cameroon', 'Cape Verde', 'Central African Republic',
       'Chad', 'Chile', "China (People's Republic of)", 'Colombia',
       'Comoros', 'Congo', 'Costa Rica', "Côte d'Ivoire", 'Croatia',
       'Cuba', 'Cyprus', "Democratic People's Republic of Korea",
       'Democratic Republic of the Congo', 'Djibouti', 'Dominica',
       'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
       'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji',
       'Gabon', 'Gambia', 'Georgia', 'Ghana', 'Greenland', 'Grenada',
       'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
       'Honduras', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel',
       'Jamaica', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
       'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia',
       'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania',
       'Former Yugoslav Republic of Macedonia', 'Madagascar', 'Malawi',
       'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
       'Mauritania', 'Mauritius', 'Micronesia', 'Moldova', 'Mongolia',
       'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal',
       'Nicaragua', 'Niger', 'Nigeria', 'Northern Mariana Islands',
       'Palestinian Authority or West Bank and Gaza Strip', 'Oman',
       'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
       'Philippines', 'Puerto Rico', 'Qatar', 'Romania', 'Russia',
       'Rwanda', 'Saint Lucia', 'Saint Vincent and the Grenadines',
       'Samoa', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
       'Seychelles', 'Sierra Leone', 'Singapore', 'Slovenia',
       'Solomon Islands', 'Somalia', 'South Africa', 'Sri Lanka', 'Sudan',
       'Suriname', 'Eswatini', 'Syrian Arab Republic', 'Chinese Taipei',
       'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo',
       'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkmenistan',
       'Uganda', 'Ukraine', 'United Arab Emirates', 'Uruguay',
       'Uzbekistan', 'Vanuatu', 'Venezuela', 'Viet Nam',
       'United States Virgin Islands', 'Yemen', 'Zambia', 'Zimbabwe',
       'World', 'ASEAN', 'Serbia', 'Montenegro', 'G20',
       'BRIICS economies - Brazil, Russia, India, Indonesia, China and South Africa',
       'South Sudan ', 'European Union (28 countries)', 'OECD - Total',
       'OECD - Europe', 'OECD Asia Oceania', 'OECD America',
       'Latin America and Caribbean', 'Middle East and North Africa']

x2 = 'blue'
x3 = 'red'
x4 = 'orange'
x5 = 'green'
x6 = 'purple'

plt.figure(1)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(aus[x], aus[y], color=x2)
plt.title(x1[1])

plt.figure(2)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(aut[x], aut[y], color=x3)
plt.title(x1[2])

plt.figure(3)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bel[x], bel[y], color=x4)
plt.title(x1[3])

plt.figure(4)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(can[x], can[y], color=x5)
plt.title(x1[4])

plt.figure(5)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(cze[x], cze[y], color=x6)
plt.title(x1[5])

plt.figure(6)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(dnk[x], dnk[y], color=x2)
plt.title(x1[6])

plt.figure(7)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(fin[x], fin[y], color=x3)
plt.title(x1[7])

plt.figure(8)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(fra[x], fra[y], color=x4)
plt.title(x1[8])

plt.figure(9)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(deu[x], deu[y], color=x5)
plt.title(x1[9])

plt.figure(10)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(grc[x], grc[y], color=x6)
plt.title(x1[10])

plt.figure(11)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(hun[x], hun[y], color=x2)
plt.title(x1[11])

plt.figure(12)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(isl[x], isl[y], color=x3)
plt.title(x1[12])

plt.figure(13)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(irl[x], irl[y], color=x4)
plt.title(x1[13])

plt.figure(14)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ita[x], ita[y], color=x5)
plt.title(x1[14])

plt.figure(15)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(jpn[x], jpn[y], color=x6)
plt.title(x1[15])

plt.figure(16)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(kor[x], kor[y], color=x2)
plt.title(x1[16])

plt.figure(17)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lux[x], lux[y], color=x3)
plt.title(x1[17])

plt.figure(18)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mex[x], mex[y], color=x4)
plt.title(x1[18])

plt.figure(19)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(nld[x], nld[y], color=x5)
plt.title(x1[19])

plt.figure(20)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(nzl[x], nzl[y], color=x6)
plt.title(x1[20])

plt.figure(21)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(nor[x], nor[y], color=x2)
plt.title(x1[21])

plt.figure(22)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(pol[x], pol[y], color=x3)
plt.title(x1[22])

plt.figure(23)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(prt[x], prt[y], color=x4)
plt.title(x1[23])

plt.figure(24)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(svk[x], svk[y], color=x5)
plt.title(x1[24])

plt.figure(25)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(esp[x], esp[y], color=x6)
plt.title(x1[25])

plt.figure(26)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(swe[x], swe[y], color=x3)
plt.title(x1[26])

plt.figure(27)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(che[x], che[y], color=x4)
plt.title(x1[27])

plt.figure(28)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tur[x], tur[y], color=x5)
plt.title(x1[28])

plt.figure(29)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gbr[x], gbr[y], color=x6)
plt.title(x1[29])

plt.figure(30)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(usa[x], usa[y], color=x2)
plt.title(x1[30])

plt.figure(31)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(g7m[x], g7m[y], color=x3)
plt.title(x1[31])

plt.figure(32)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(afg[x], afg[y], color=x4)
plt.title(x1[32])

plt.figure(33)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(alb[x], alb[y], color=x5)
plt.title(x1[33])

plt.figure(34)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(dza[x], dza[y], color=x6)
plt.title(x1[34])

plt.figure(35)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(asm[x], asm[y], color=x2)
plt.title(x1[35])

plt.figure(36)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(and1[x], and1[y], color=x3)
plt.title(x1[36])

plt.figure(37)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ago[x], ago[y], color=x4)
plt.title(x1[37])

plt.figure(38)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(atg[x], atg[y], color=x5)
plt.title(x1[38])

plt.figure(39)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(arg[x], arg[y], color=x6)
plt.title(x1[39])

plt.figure(40)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(arm[x], arm[y], color=x2)
plt.title(x1[40])

plt.figure(41)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(aze[x], aze[y], color=x3)
plt.title(x1[41])

plt.figure(42)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bhs[x], bhs[y], color=x4)
plt.title(x1[42])

plt.figure(43)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bhr[x], bhr[y], color=x5)
plt.title(x1[43])

plt.figure(44)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bgd[x], bgd[y], color=x6)
plt.title(x1[44])

plt.figure(45)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(brb[x], brb[y], color=x2)
plt.title(x1[45])

plt.figure(46)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(blr[x], blr[y], color=x3)
plt.title(x1[46])

plt.figure(47)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(blz[x], blz[y], color=x4)
plt.title(x1[47])

plt.figure(48)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ben[x], ben[y], color=x5)
plt.title(x1[48])

plt.figure(49)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bmu[x], bmu[y], color=x6)
plt.title(x1[49])

plt.figure(50)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(btn[x], btn[y], color=x2)
plt.title(x1[50])

plt.figure(51)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bol[x], bol[y], color=x3)
plt.title(x1[51])

plt.figure(52)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bih[x], bih[y], color=x4)
plt.title(x1[52])

plt.figure(53)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bwa[x], bwa[y], color=x5)
plt.title(x1[53])

plt.figure(54)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bra[x], bra[y], color=x6)
plt.title(x1[54])

plt.figure(55)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(brn[x], brn[y], color=x2)
plt.title(x1[55])

plt.figure(56)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bgr[x], bgr[y], color=x3)
plt.title(x1[56])

plt.figure(57)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bfa[x], bfa[y], color=x4)
plt.title(x1[57])

plt.figure(58)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(bdi[x], bdi[y], color=x5)
plt.title(x1[58])

plt.figure(59)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(khm[x], khm[y], color=x6)
plt.title(x1[59])

plt.figure(60)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(cmr[x], cmr[y], color=x2)
plt.title(x1[60])

plt.figure(61)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(cpv[x], cpv[y], color=x3)
plt.title(x1[61])

plt.figure(62)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(caf[x], caf[y], color=x4)
plt.title(x1[62])

plt.figure(63)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tcd[x], tcd[y], color=x5)
plt.title(x1[63])

plt.figure(64)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(chl[x], chl[y], color=x6)
plt.title(x1[64])

plt.figure(65)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(chn[x], chn[y], color=x2)
plt.title(x1[65])

plt.figure(66)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(col[x], col[y], color=x3)
plt.title(x1[66])

plt.figure(67)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(com[x], com[y], color=x4)
plt.title(x1[67])

plt.figure(68)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(cog[x], cog[y], color=x5)
plt.title(x1[68])

plt.figure(69)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(cri[x], cri[y], color=x6)
plt.title(x1[69])

plt.figure(70)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(civ[x], civ[y], color=x2)
plt.title(x1[70])

plt.figure(71)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(hrv[x], hrv[y], color=x3)
plt.title(x1[71])

plt.figure(72)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(cub[x], cub[y], color=x4)
plt.title(x1[72])

plt.figure(73)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(cyp[x], cyp[y], color=x5)
plt.title(x1[73])

plt.figure(74)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(prk[x], prk[y], color=x6)
plt.title(x1[74])

plt.figure(75)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(cod[x], cod[y], color=x2)
plt.title(x1[75])

plt.figure(76)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(dji[x], dji[y], color=x3)
plt.title(x1[76])

plt.figure(77)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(dma[x], dma[y], color=x4)
plt.title(x1[77])

plt.figure(78)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(dom[x], dom[y], color=x5)
plt.title(x1[78])

plt.figure(79)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ecu[x], ecu[y], color=x6)
plt.title(x1[79])

plt.figure(80)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(egy[x], egy[y], color=x2)
plt.title(x1[80])

plt.figure(81)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(slv[x], slv[y], color=x3)
plt.title(x1[81])

plt.figure(82)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gnq[x], gnq[y], color=x4)
plt.title(x1[82])

plt.figure(83)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(eri[x], eri[y], color=x5)
plt.title(x1[83])

plt.figure(84)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(est[x], est[y], color=x2)
plt.title(x1[84])

plt.figure(85)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(eth[x], eth[y], color=x3)
plt.title(x1[85])

plt.figure(86)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(fji[x], fji[y], color=x4)
plt.title(x1[86])

plt.figure(87)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gab[x], gab[y], color=x5)
plt.title(x1[87])

plt.figure(88)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gmb[x], gmb[y], color=x6)
plt.title(x1[88])

plt.figure(89)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(geo[x], geo[y], color=x2)
plt.title(x1[89])

plt.figure(90)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gha[x], gha[y], color=x3)
plt.title(x1[90])

plt.figure(91)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(grl[x], grl[y], color=x4)
plt.title(x1[91])

plt.figure(92)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(grd[x], grd[y], color=x5)
plt.title(x1[92])

plt.figure(93)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gum[x], gum[y], color=x6)
plt.title(x1[93])

plt.figure(94)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gtm[x], gtm[y], color=x2)
plt.title(x1[94])

plt.figure(95)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gin[x], gin[y], color=x3)
plt.title(x1[95])

plt.figure(96)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(gnb[x], gnb[y], color=x4)
plt.title(x1[96])

plt.figure(97)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(guy[x], guy[y], color=x5)
plt.title(x1[97])

plt.figure(98)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(hti[x], hti[y], color=x6)
plt.title(x1[98])

plt.figure(99)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(hnd[x], hnd[y], color=x2)
plt.title(x1[99])

plt.figure(100)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ind[x], ind[y], color=x3)
plt.title(x1[100])

plt.figure(101)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(idn[x], idn[y], color=x4)
plt.title(x1[101])

plt.figure(102)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(irn[x], irn[y], color=x5)
plt.title(x1[102])

plt.figure(103)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(irq[x], irq[y], color=x6)
plt.title(x1[103])

plt.figure(104)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(isr[x], isr[y], color=x2)
plt.title(x1[104])

plt.figure(105)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(jam[x], jam[y], color=x3)
plt.title(x1[105])

plt.figure(106)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(jor[x], jor[y], color=x4)
plt.title(x1[106])

plt.figure(107)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(kaz[x], kaz[y], color=x5)
plt.title(x1[107])

plt.figure(108)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ken[x], ken[y], color=x6)
plt.title(x1[108])

plt.figure(109)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(kir[x], kir[y], color=x2)
plt.title(x1[109])

plt.figure(110)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(kgz[x], kgz[y], color=x3)
plt.title(x1[110])

plt.figure(111)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lao[x], lao[y], color=x4)
plt.title(x1[111])

plt.figure(112)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lva[x], lva[y], color=x5)
plt.title(x1[112])

plt.figure(113)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lbn[x], lbn[y], color=x6)
plt.title(x1[113])

plt.figure(114)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lso[x], lso[y], color=x2)
plt.title(x1[114])

plt.figure(115)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lbr[x], lbr[y], color=x3)
plt.title(x1[115])

plt.figure(116)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lby[x], lby[y], color=x4)
plt.title(x1[116])

plt.figure(117)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ltu[x], ltu[y], color=x5)
plt.title(x1[117])

plt.figure(118)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mkd[x], mkd[y], color=x6)
plt.title(x1[118])

plt.figure(119)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mdg[x], mdg[y], color=x2)
plt.title(x1[119])

plt.figure(120)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mwi[x], mwi[y], color=x3)
plt.title(x1[120])

plt.figure(121)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mys[x], mys[y], color=x4)
plt.title(x1[121])

plt.figure(122)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mdv[x], mdv[y], color=x5)
plt.title(x1[122])

plt.figure(123)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mli[x], mli[y], color=x6)
plt.title(x1[123])

plt.figure(124)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mlt[x], mlt[y], color=x2)
plt.title(x1[124])

plt.figure(125)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mhl[x], mhl[y], color=x3)
plt.title(x1[125])

plt.figure(126)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mrt[x], mrt[y], color=x4)
plt.title(x1[126])

plt.figure(127)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mus[x], mus[y], color=x5)
plt.title(x1[127])

plt.figure(128)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(fsm[x], fsm[y], color=x6)
plt.title(x1[128])

plt.figure(129)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mda[x], mda[y], color=x2)
plt.title(x1[129])

plt.figure(130)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mng[x], mng[y], color=x3)
plt.title(x1[130])

plt.figure(131)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mar[x], mar[y], color=x4)
plt.title(x1[131])

plt.figure(132)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(moz[x], moz[y], color=x5)
plt.title(x1[132])

plt.figure(133)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mmr[x], mmr[y], color=x2)
plt.title(x1[133])

plt.figure(134)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(nam[x], nam[y], color=x3)
plt.title(x1[134])

plt.figure(135)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(npl[x], npl[y], color=x4)
plt.title(x1[135])

plt.figure(136)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(noc[x], noc[y], color=x5)
plt.title(x1[136])

plt.figure(137)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ner[x], ner[y], color=x6)
plt.title(x1[137])

plt.figure(138)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(nga[x], nga[y], color=x2)
plt.title(x1[138])

plt.figure(139)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mnp[x], mnp[y], color=x3)
plt.title(x1[139])

plt.figure(140)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(pse[x], pse[y], color=x4)
plt.title(x1[140])

plt.figure(141)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(omn[x], omn[y], color=x5)
plt.title(x1[141])

plt.figure(142)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(pak[x], pak[y], color=x6)
plt.title(x1[142])

plt.figure(143)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(pan[x], pan[y], color=x2)
plt.title(x1[143])

plt.figure(144)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(png[x], png[y], color=x3)
plt.title(x1[144])

plt.figure(145)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(pry[x], pry[y], color=x4)
plt.title(x1[145])

plt.figure(146)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(per[x], per[y], color=x5)
plt.title(x1[146])

plt.figure(147)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(phl[x], phl[y], color=x6)
plt.title(x1[147])

plt.figure(148)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(pri[x], pri[y], color=x2)
plt.title(x1[148])

plt.figure(149)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(qat[x], qat[y], color=x3)
plt.title(x1[149])

plt.figure(150)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(rou[x], rou[y], color=x4)
plt.title(x1[150])

plt.figure(151)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(rus[x], rus[y], color=x5)
plt.title(x1[151])

plt.figure(152)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(rwa[x], rwa[y], color=x6)
plt.title(x1[152])

plt.figure(153)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lca[x], lca[y], color=x2)
plt.title(x1[153])

plt.figure(154)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(vct[x], vct[y], color=x3)
plt.title(x1[154])

plt.figure(155)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(wsm[x], wsm[y], color=x4)
plt.title(x1[155])

plt.figure(156)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(stp[x], stp[y], color=x5)
plt.title(x1[156])

plt.figure(157)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(sau[x], sau[y], color=x6)
plt.title(x1[157])

plt.figure(158)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(sen[x], sen[y], color=x2)
plt.title(x1[158])

plt.figure(159)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(syc[x], syc[y], color=x3)
plt.title(x1[159])

plt.figure(160)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(sle[x], sle[y], color=x4)
plt.title(x1[160])

plt.figure(161)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(sgp[x], sgp[y], color=x5)
plt.title(x1[161])

plt.figure(162)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(svn[x], svn[y], color=x6)
plt.title(x1[162])

plt.figure(163)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(slb[x], slb[y], color=x2)
plt.title(x1[163])

plt.figure(164)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(som[x], som[y], color=x3)
plt.title(x1[164])

plt.figure(165)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(zaf[x], zaf[y], color=x4)
plt.title(x1[165])

plt.figure(166)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lka[x], lka[y], color=x5)
plt.title(x1[166])

plt.figure(167)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(sdn[x], sdn[y], color=x6)
plt.title(x1[167])

plt.figure(168)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(sur[x], sur[y], color=x2)
plt.title(x1[168])

plt.figure(169)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(swz[x], swz[y], color=x3)
plt.title(x1[169])

plt.figure(170)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(syr[x], syr[y], color=x4)
plt.title(x1[170])

plt.figure(171)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(twn[x], twn[y], color=x5)
plt.title(x1[171])

plt.figure(172)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tjk[x], tjk[y], color=x6)
plt.title(x1[172])

plt.figure(173)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tza[x], tza[y], color=x2)
plt.title(x1[173])

plt.figure(174)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tha[x], tha[y], color=x3)
plt.title(x1[174])

plt.figure(175)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tls[x], tls[y], color=x4)
plt.title(x1[175])

plt.figure(176)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tgo[x], tgo[y], color=x5)
plt.title(x1[176])

plt.figure(177)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ton[x], ton[y], color=x6)
plt.title(x1[177])

plt.figure(178)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tto[x], tto[y], color=x2)
plt.title(x1[178])

plt.figure(179)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tun[x], tun[y], color=x3)
plt.title(x1[179])

plt.figure(180)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(tkm[x], tkm[y], color=x4)
plt.title(x1[180])

plt.figure(181)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(uga[x], uga[y], color=x5)
plt.title(x1[181])

plt.figure(182)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ukr[x], ukr[y], color=x6)
plt.title(x1[182])

plt.figure(183)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(are[x], are[y], color=x2)
plt.title(x1[183])

plt.figure(184)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ury[x], ury[y], color=x3)
plt.title(x1[184])

plt.figure(185)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(uzb[x], uzb[y], color=x4)
plt.title(x1[185])

plt.figure(186)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(vut[x], vut[y], color=x5)
plt.title(x1[186])

plt.figure(187)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ven[x], ven[y], color=x6)
plt.title(x1[187])

plt.figure(188)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(vnm[x], vnm[y], color=x2)
plt.title(x1[188])

plt.figure(189)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(vir[x], vir[y], color=x3)
plt.title(x1[189])

plt.figure(190)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(yem[x], yem[y], color=x4)
plt.title(x1[190])

plt.figure(191)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(zmb[x], zmb[y], color=x5)
plt.title(x1[191])

plt.figure(192)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(zwe[x], zwe[y], color=x6)
plt.title(x1[192])

plt.figure(193)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(wlb[x], wlb[y], color=x2)
plt.title(x1[193])

plt.figure(194)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(asean[x], asean[y], color=x3)
plt.title(x1[194])

plt.figure(195)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(srb[x], srb[y], color=x4)
plt.title(x1[195])

plt.figure(196)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mne[x], mne[y], color=x5)
plt.title(x1[196])

plt.figure(197)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(g20[x], g20[y], color=x6)
plt.title(x1[197])

plt.figure(198)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(briics[x], briics[y], color=x2)
plt.title(x1[198])

plt.figure(199)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(ssd[x], ssd[y], color=x3)
plt.title(x1[199])

plt.figure(200)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(eu28[x], eu28[y], color=x4)
plt.title(x1[200])

plt.figure(201)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(oecd[x], oecd[y], color=x5)
plt.title(x1[201])

plt.figure(202)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(oecde[x], oecde[y], color=x6)
plt.title(x1[202])

plt.figure(203)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(oecdao[x], oecdao[y], color=x2)
plt.title(x1[203])

plt.figure(204)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(oecdam[x], oecdam[y], color=x3)
plt.title(x1[204])

plt.figure(205)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(lac[x], lac[y], color=x4)
plt.title(x1[205])

plt.figure(206)
plt.xlabel(a)
plt.ylabel(b)
plt.plot(mena[x], mena[y], color=x5)
plt.title(x1[206])



plt.show()
