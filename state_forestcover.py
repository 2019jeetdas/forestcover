# -*- coding: utf-8 -*-
#-----(3) data analysis of forestcover statewise -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/Data-store/project-3-forestcover_India/statewise_forest_cover_2009_2015.csv',encoding="cp1252")
print("\n------- output data :-----------\n")
print("Agriculture data analysis:")
print("\n-----------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :


print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

#------------------[A] State/Union Territory--- Geographical Area plot------------- 

state_union = df['State/Union Territory']

geo_area = df['Geographical Area']

plt.title('Statewise/Union Territory Geographical Area Plot :')
plt.xlabel('state sl. no. -->')
plt.ylabel('Geographical Area -->')
plt.plot(geo_area)
plt.show()


#--------------[B] Actual forest cover (2009 to 2015)------


plt.title('[B] Actual forest cover (2009,2011,2013,2015): ')
plt.xlabel("year--- >")
plt.ylabel("Forest cover --- >")
    
Actual_2009 = df['Actual Forest Cover - 2009']

plt.plot(Actual_2009,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2009 ")

Actual_2011 = df['Actual Forest Cover - 2011']
                     
plt.plot(Actual_2011,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011")
            
Actual_2013 = df['Actual Forest Cover - 2013']

plt.plot(Actual_2013,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2013")

Actual_2015 = df['Actual Forest Cover - 2015'] 

plt.plot(Actual_2015,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[4] 2015")

plt.legend()
plt.show()

#--------------[C] Dense  - Very Dense Forest (2009 to 2015)------


plt.title('[C] Dense  - Very Dense Forest (2009,2011,2013,2015): ')
plt.xlabel("year--- >")
plt.ylabel("Forest cover --- >")
    
Dense_2009 = df['Dense  - Very Dense Forest - 2009']

plt.plot(Dense_2009,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2009 ")

Dense_2011 = df['Dense  - Very Dense Forest - 2011']
                     
plt.plot(Dense_2011,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011")
            
Dense_2013 = df['Dense  - Very Dense Forest - 2013']

plt.plot(Dense_2013,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2013")

Dense_2015 = df['Dense  - Very Dense Forest - 2015'] 

plt.plot(Dense_2015,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[4] 2015")

plt.legend()
plt.show()

#--------------[D] Dense - Moderately Dense forest (2009 to 2015)------


plt.title('[D] Dense - Moderately Dense forest (2009,2011,2013,2015): ')
plt.xlabel("year--- >")
plt.ylabel("Forest cover --- >")
    
DenseM_2009 = df['Dense - Moderately Dense forest - 2009']

plt.plot(DenseM_2009,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2009 ")

DenseM_2011 = df['Dense - Moderately Dense forest - 2011']
                     
plt.plot(DenseM_2011,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011")
            
DenseM_2013 = df['Dense - Moderately Dense forest - 2013']

plt.plot(DenseM_2013,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2013")

DenseM_2015 = df['Dense - Moderately Dense forest - 2015'] 

plt.plot(DenseM_2015,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[4] 2015")

plt.legend()
plt.show()

#--------------[E] Open Forest (2009 to 2015)------


plt.title('[E] Open Forest (2009,2011,2013,2015): ')
plt.xlabel("year--- >")
plt.ylabel("Forest cover --- >")
    
Open_2009 = df['Open Forest - 2009']

plt.plot(Open_2009,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2009 ")

Open_2011 = df['Open Forest - 2011']
                     
plt.plot(Open_2011,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011")
            
Open_2013 = df['Open Forest - 2013']

plt.plot(Open_2013,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2013")

Open_2015 = df['Open Forest - 2015'] 

plt.plot(Open_2015,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[4] 2015")

plt.legend()
plt.show()
  
#--------------[F] Mangrove (2009 to 2015)------

plt.title('[F] Mangrove (2009,2011,2013,2015): ')
plt.xlabel("year--- >")
plt.ylabel("Forest cover --- >")
    
Man_2009 = df['Mangrove - 2009']

plt.plot(Man_2009,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2009 ")

Man_2011 = df['Mangrove - 2011']
                     
plt.plot(Man_2011,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011")
            
Man_2013 = df['Mangrove - 2013']

plt.plot(Man_2013,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2013")

Man_2015 = df['Mangrove - 2015'] 

plt.plot(Man_2015,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[4] 2015")

plt.legend()
plt.show()          

#--------------[G] Scrub(2009 to 2015)------

plt.title('[G] Scrub(2009,2011,2013,2015): ')
plt.xlabel("year--- >")
plt.ylabel("Forest cover --- >")
    
Scrub_2009 = df['Scrub - 2009']

plt.plot(Scrub_2009,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2009 ")

Scrub_2011 = df['Scrub - 2011']
                     
plt.plot(Scrub_2011,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011")
            
Scrub_2013 = df['Scrub - 2013']

plt.plot(Scrub_2013,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2013")

Scrub_2015 = df['Scrub - 2015'] 

plt.plot(Scrub_2015,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[4] 2015")

plt.legend()
plt.show()          

#--------------[H] Non-Forest(2009 to 2015)------

plt.title('[H] Non-Forest (2009,2011,2013,2015): ')
plt.xlabel("year--- >")
plt.ylabel("Forest cover --- >")
    
NF_2009 = df['Non-Forest - 2009']

plt.plot(NF_2009,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2009 ")

NF_2011 = df['Non-Forest - 2011']
                     
plt.plot(NF_2011,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011")
            
NF_2013 = df['Non-Forest - 2013']

plt.plot(NF_2013,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2013")

NF_2015 = df['Non-Forest - 2015'] 

plt.plot(NF_2015,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[4] 2015")

plt.legend()
plt.show()          