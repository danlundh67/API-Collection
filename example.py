#!/usr/bin/env python

# Import library for fetching Elspot data
from nordpool import elspot, elbas
from pprint import pprint
import matplotlib.pyplot as plt


# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()

# Initialize class for fetching Elsbas prices
prices_bas = elbas.Prices()

# Fetch hourly Elspot prices for Finland and print the resulting dictionary
#pprint(prices_spot.hourly(areas=['SE3']))

Dictionary=prices_spot.hourly(areas=['SE3'])
ae1=Dictionary['areas']
ae2=ae1['SE3']
ae3=ae2['values'] 

min=float(ae2['Min'])
ave=float(ae2['Average'])

# genomsnittlig forbrukning timme kwh

forb=23.200

kost=0.000

antal=0

x2 = []
y=[]

i=0

#print(ae3)

for x in range(len(ae3)):
    a1=ae3[x]
    a2=a1['start']
   
    a3=a1['end']
    
    a4=a1['value']
    x2.append(i)
    i=i+1
    
    sdd=a2.strftime("%d")
    sdh=a2.strftime("%H")
    edd=a3.strftime("%d")
    edh=a3.strftime("%H")
    y.append(a4)
    
    if ((2*min)>=a4) :
        print(sdd,sdh,edd,edh, a4,"*")
        kost=kost+a4*forb
        antal=antal+1
    else :
        print(sdd,sdh,edd,edh, a4)


print('------------------------------------------------------------')
print('baserat pa en kwh per dygn :',forb)
print('kostnad min :',kost)
print('kostnad genomsnitt :', ave*antal*forb)
print('antal effekttimmar enligt rekommendation (less 2*min)',antal)
print('------------------------------------------------------------')
print('manadskostnad min ',kost*30)
print('manadskostnad avg ',ave*antal*forb*30)

plt.plot(x2,y)
plt.xlabel('start tid 0 ar 22-23 samma dag')
plt.ylabel('kr/kWh')
plt.show()



# Fetch hourly Elbas prices for Finland and print the resulting dictionary
#pprint(prices_bas.hourly(areas=['SE3']))

