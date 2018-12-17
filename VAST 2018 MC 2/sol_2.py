import pandas as pd
import matplotlib.pyplot as plt


file= pd.read_csv("/Users/sayedkhan/Desktop/MC2/Boonsong Lekagul waterways readings.csv")


# values only water temp and location= Boonsri
file[(file.measure=='Water temperature') & (file.location=='Boonsri')]
# onle value->  Boonsri-> water temperature 
file[(file.measure=='Water temperature') & (file.location=='Boonsri')]['value']
# two columns -> value and sample date -> boonsri
file[(file.measure=='Water temperature') & (file.location=='Boonsri')][['value','sample date']]

                            # Boonsri
# 1. Pyrene in Boonsri
Pyrene_sampledate_Boonsri=file[(file.measure=='Pyrene') & (file.location=='Boonsri')][['sample date']] 
Pyrene_value_Boonsri=file[(file.measure=='Pyrene') & (file.location=='Boonsri')][['value']]
Pyrene_Boonsri=Pyrene_sampledate_Boonsri.join(Pyrene_value_Boonsri)
# 2. Acenaphthylene
Acenaphthylene_sampledate_Boonsri=file[(file.measure=='Acenaphthylene') & (file.location=='Boonsri')][['sample date']] 
Acenaphthylene_value_Boonsri=file[(file.measure=='Acenaphthylene') & (file.location=='Boonsri')][['value']]
Acenaphthylene_Boonsri=Acenaphthylene_sampledate_Boonsri.join(Acenaphthylene_value_Boonsri)


                            # Kohsoom
 #1. Pyrene in Kohsoom
Pyrene_sampledate_Kohsoom=file[(file.measure=='Pyrene') & (file.location=='Kohsoom')][['sample date']] 
Pyrene_value_Kohsoom=file[(file.measure=='Pyrene') & (file.location=='Kohsoom')][['value']]
Pyrene_Kohsoom=Pyrene_sampledate_Kohsoom.join(Pyrene_value_Kohsoom)
# 2. Acenaphthylene
Acenaphthylene_sampledate_Kohsoom=file[(file.measure=='Acenaphthylene') & (file.location=='Kohsoom')][['sample date']] 
Acenaphthylene_value_Kohsoom=file[(file.measure=='Acenaphthylene') & (file.location=='Kohsoom')][['value']]
Acenaphthylene_Kohsoom=Acenaphthylene_sampledate_Kohsoom.join(Acenaphthylene_value_Kohsoom)

# plot data
#  Pyrene
fig=plt.figure(1)
ax1=fig.add_subplot(1,2,1)
Pyrene_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Pyrene data  ',legend=False)
plt.axhline(y=Pyrene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

fig=plt.figure(1)
ax1=fig.add_subplot(1,2,2)
Pyrene_Kohsoom.plot(x='sample date',y='value',ax=ax1,title='Kohsoom: Pyrene data  ',legend=False)
plt.axhline(y=Pyrene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

# #1. Pyrene in Kohsoom
Pyrene_sampledate_Kohsoom=file[(file.measure=='Pyrene') & (file.location=='Kohsoom')][['sample date']] 
Pyrene_value_Kohsoom=file[(file.measure=='Pyrene') & (file.location=='Kohsoom')][['value']]
Pyrene_Kohsoom=Pyrene_sampledate_Kohsoom.join(Pyrene_value_Kohsoom)
# 2. Acenaphthylene
Acenaphthylene_sampledate_Kohsoom=file[(file.measure=='Acenaphthylene') & (file.location=='Kohsoom')][['sample date']] 
Acenaphthylene_value_Kohsoom=file[(file.measure=='Acenaphthylene') & (file.location=='Kohsoom')][['value']]
Acenaphthylene_Kohsoom=Acenaphthylene_sampledate_Kohsoom.join(Acenaphthylene_value_Kohsoom)

#  Acenaphthylene
fig=plt.figure(2)
ax1=fig.add_subplot(1,2,1)
Acenaphthylene_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Acenaphthylene data  ',legend=False)
#plt.axhline(y=Pyrene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

fig=plt.figure(2)
ax1=fig.add_subplot(1,2,2)
Acenaphthylene_Kohsoom.plot(x='sample date',y='value',ax=ax1,title='Kohsoom: Acenaphthylene data  ',legend=False)
#plt.axhline(y=Pyrene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
plt.show()
