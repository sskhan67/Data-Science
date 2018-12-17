import pandas as pd
import matplotlib.pyplot as plt


file= pd.read_csv("/Users/sayedkhan/Desktop/MC2/Boonsong Lekagul waterways readings.csv")


# vlues only water temp and location= Boonsri
file[(file.measure=='Water temperature') & (file.location=='Boonsri')]
# onle value->  Boonsri-> water temperature 
file[(file.measure=='Water temperature') & (file.location=='Boonsri')]['value']
# two columns -> value and sample date -> boonsri
file[(file.measure=='Water temperature') & (file.location=='Boonsri')][['value','sample date']]


                                            # Boonsri


# water temperature 
WT_sampledate_Boonsri=file[(file.measure=='Water temperature') & (file.location=='Boonsri')][['sample date']] 
WT_value_Boonsri=file[(file.measure=='Water temperature') & (file.location=='Boonsri')][['value']]
WT_Boonsri=WT_sampledate_Boonsri.join(WT_value_Boonsri)  
# Dissolved oxygen in Boonsri
D_oxygen_sampledate_Boonsri=file[(file.measure=='Dissolved oxygen') & (file.location=='Boonsri')][['sample date']] 
D_oxygen_value_Boonsri=file[(file.measure=='Dissolved oxygen') & (file.location=='Boonsri')][['value']]
D_oxygen_Boonsri=D_oxygen_sampledate_Boonsri.join(D_oxygen_value_Boonsri)
D_oxygen_value_Boonsri_avg=D_oxygen_Boonsri['value'].mean()
#Biochemical Oxygen
B_oxygen_sampledate_Boonsri=file[(file.measure=='Biochemical Oxygen') & (file.location=='Boonsri')][['sample date']] 
B_oxygen_value_Boonsri=file[(file.measure=='Biochemical Oxygen') & (file.location=='Boonsri')][['value']]
B_oxygen_Boonsri=B_oxygen_sampledate_Boonsri.join(B_oxygen_value_Boonsri)
# Ammonium
Ammonium_sampledate_Boonsri=file[(file.measure=='Ammonium') & (file.location=='Boonsri')][['sample date']] 
Ammonium_value_Boonsri=file[(file.measure=='Ammonium') & (file.location=='Boonsri')][['value']]
Ammonium_Boonsri=Ammonium_sampledate_Boonsri.join(Ammonium_value_Boonsri)
#Nitrates
Nitrates_sampledate_Boonsri=file[(file.measure=='Nitrates') & (file.location=='Boonsri')][['sample date']] 
Nitrates_value_Boonsri=file[(file.measure=='Nitrates') & (file.location=='Boonsri')][['value']]
Nitrates_Boonsri=Nitrates_sampledate_Boonsri.join(Nitrates_value_Boonsri)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Boonsri=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Boonsri')][['sample date']] 
Orthophosphate_phosphorus_value_Boonsri=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Boonsri')][['value']]
Orthophosphate_phosphorus_Boonsri=Orthophosphate_phosphorus_sampledate_Boonsri.join(Orthophosphate_phosphorus_value_Boonsri)

                                            #Somchair

# water temperature data 
WT_sampledate_Somchair=file[(file.measure=='Water temperature') & (file.location=='Somchair')][['sample date']] 
WT_value_Somchair=file[(file.measure=='Water temperature') & (file.location=='Somchair')][['value']]
WT_Somchair=WT_sampledate_Somchair.join(WT_value_Somchair)
# Dissolved oxygen 
D_oxygen_sampledate_Somchair=file[(file.measure=='Dissolved oxygen') & (file.location=='Somchair')][['sample date']] 
D_oxygen_value_Somchair=file[(file.measure=='Dissolved oxygen') & (file.location=='Somchair')][['value']]
D_oxygen_Somchair=D_oxygen_sampledate_Somchair.join(D_oxygen_value_Somchair)
D_oxygen_value_Somchair_avg=D_oxygen_Somchair['value'].mean()
#Biochemical Oxygen
B_oxygen_sampledate_Somchair=file[(file.measure=='Biochemical Oxygen') & (file.location=='Somchair')][['sample date']] 
B_oxygen_value_Somchair=file[(file.measure=='Biochemical Oxygen') & (file.location=='Somchair')][['value']]
B_oxygen_Somchair=B_oxygen_sampledate_Somchair.join(B_oxygen_value_Somchair)
# Ammonium
Ammonium_sampledate_Somchair=file[(file.measure=='Ammonium') & (file.location=='Somchair')][['sample date']] 
Ammonium_value_Somchair=file[(file.measure=='Ammonium') & (file.location=='Somchair')][['value']]
Ammonium_Somchair=Ammonium_sampledate_Somchair.join(Ammonium_value_Somchair)
#Nitrates
Nitrates_sampledate_Somchair=file[(file.measure=='Nitrates') & (file.location=='Somchair')][['sample date']] 
Nitrates_value_Somchair=file[(file.measure=='Nitrates') & (file.location=='Somchair')][['value']]
Nitrates_Somchair=Nitrates_sampledate_Somchair.join(Nitrates_value_Somchair)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Somchair=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Somchair')][['sample date']] 
Orthophosphate_phosphorus_value_Somchair=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Somchair')][['value']]
Orthophosphate_phosphorus_Somchair=Orthophosphate_phosphorus_sampledate_Somchair.join(Orthophosphate_phosphorus_value_Somchair)


                                            #Achara

# water temperature 
WT_sampledate_Achara=file[(file.measure=='Water temperature') & (file.location=='Achara')][['sample date']] 
WT_value_Achara=file[(file.measure=='Water temperature') & (file.location=='Achara')][['value']]
WT_Achara=WT_sampledate_Achara.join(WT_value_Achara)  
# Dissolved oxygen 
D_oxygen_sampledate_Achara=file[(file.measure=='Dissolved oxygen') & (file.location=='Achara')][['sample date']] 
D_oxygen_value_Achara=file[(file.measure=='Dissolved oxygen') & (file.location=='Achara')][['value']]
D_oxygen_Achara=D_oxygen_sampledate_Achara.join(D_oxygen_value_Achara)
D_oxygen_value_Achara_avg=D_oxygen_Achara['value'].mean()
#Biochemical Oxygen
B_oxygen_sampledate_Achara=file[(file.measure=='Biochemical Oxygen') & (file.location=='Achara')][['sample date']] 
B_oxygen_value_Achara=file[(file.measure=='Biochemical Oxygen') & (file.location=='Achara')][['value']]
B_oxygen_Achara=B_oxygen_sampledate_Achara.join(B_oxygen_value_Achara)
# Ammonium
Ammonium_sampledate_Achara=file[(file.measure=='Ammonium') & (file.location=='Achara')][['sample date']] 
Ammonium_value_Achara=file[(file.measure=='Ammonium') & (file.location=='Achara')][['value']]
Ammonium_Achara=Ammonium_sampledate_Achara.join(Ammonium_value_Achara)
#Nitrates
Nitrates_sampledate_Achara=file[(file.measure=='Nitrates') & (file.location=='Achara')][['sample date']] 
Nitrates_value_Achara=file[(file.measure=='Nitrates') & (file.location=='Achara')][['value']]
Nitrates_Achara=Nitrates_sampledate_Achara.join(Nitrates_value_Achara)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Achara=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Achara')][['sample date']] 
Orthophosphate_phosphorus_value_Achara=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Achara')][['value']]
Orthophosphate_phosphorus_Achara=Orthophosphate_phosphorus_sampledate_Achara.join(Orthophosphate_phosphorus_value_Achara)




                                            #Sakda

# water temperature 
WT_sampledate_Sakda=file[(file.measure=='Water temperature') & (file.location=='Sakda')][['sample date']] 
WT_value_Sakda=file[(file.measure=='Water temperature') & (file.location=='Sakda')][['value']]
WT_Sakda=WT_sampledate_Sakda.join(WT_value_Sakda)  
# Dissolved oxygen 
D_oxygen_sampledate_Sakda=file[(file.measure=='Dissolved oxygen') & (file.location=='Sakda')][['sample date']] 
D_oxygen_value_Sakda=file[(file.measure=='Dissolved oxygen') & (file.location=='Sakda')][['value']]
D_oxygen_Sakda=D_oxygen_sampledate_Sakda.join(D_oxygen_value_Sakda)
D_oxygen_value_Achara_avg=D_oxygen_Sakda['value'].mean()
 #Biochemical Oxygen
B_oxygen_sampledate_Sakda=file[(file.measure=='Biochemical Oxygen') & (file.location=='Sakda')][['sample date']] 
B_oxygen_value_Sakda=file[(file.measure=='Biochemical Oxygen') & (file.location=='Sakda')][['value']]
B_oxygen_Sakda=B_oxygen_sampledate_Sakda.join(B_oxygen_value_Sakda)
# Ammonium
Ammonium_sampledate_Sakda=file[(file.measure=='Ammonium') & (file.location=='Sakda')][['sample date']] 
Ammonium_value_Sakda=file[(file.measure=='Ammonium') & (file.location=='Sakda')][['value']]
Ammonium_Sakda=Ammonium_sampledate_Sakda.join(Ammonium_value_Sakda)
#Nitrates
Nitrates_sampledate_Sakda=file[(file.measure=='Nitrates') & (file.location=='Sakda')][['sample date']] 
Nitrates_value_Sakda=file[(file.measure=='Nitrates') & (file.location=='Sakda')][['value']]
Nitrates_Sakda=Nitrates_sampledate_Sakda.join(Nitrates_value_Sakda)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Sakda=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Sakda')][['sample date']] 
Orthophosphate_phosphorus_value_Sakda=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Sakda')][['value']]
Orthophosphate_phosphorus_Sakda=Orthophosphate_phosphorus_sampledate_Sakda.join(Orthophosphate_phosphorus_value_Sakda)


                                            #Kannika

# water temperature 
WT_sampledate_Kannika=file[(file.measure=='Water temperature') & (file.location=='Kannika')][['sample date']] 
WT_value_Kannika=file[(file.measure=='Water temperature') & (file.location=='Kannika')][['value']]
WT_Kannika=WT_sampledate_Kannika.join(WT_value_Kannika)  

# Dissolved oxygen 
D_oxygen_sampledate_Kannika=file[(file.measure=='Dissolved oxygen') & (file.location=='Kannika')][['sample date']] 
D_oxygen_value_Kannika=file[(file.measure=='Dissolved oxygen') & (file.location=='Kannika')][['value']]
D_oxygen_Kannika=D_oxygen_sampledate_Kannika.join(D_oxygen_value_Kannika)
D_oxygen_value_Kannika_avg=D_oxygen_Kannika['value'].mean()

 #Biochemical Oxygen
B_oxygen_sampledate_Kannika=file[(file.measure=='Biochemical Oxygen') & (file.location=='Kannika')][['sample date']] 
B_oxygen_value_Kannika=file[(file.measure=='Biochemical Oxygen') & (file.location=='Kannika')][['value']]
B_oxygen_Kannika=B_oxygen_sampledate_Kannika.join(B_oxygen_value_Kannika)
# Ammonium
Ammonium_sampledate_Kannika=file[(file.measure=='Ammonium') & (file.location=='Kannika')][['sample date']] 
Ammonium_value_Kannika=file[(file.measure=='Ammonium') & (file.location=='Kannika')][['value']]
Ammonium_Kannika=Ammonium_sampledate_Kannika.join(Ammonium_value_Kannika)
#Nitrates
Nitrates_sampledate_Kannika=file[(file.measure=='Nitrates') & (file.location=='Kannika')][['sample date']] 
Nitrates_value_Kannika=file[(file.measure=='Nitrates') & (file.location=='Kannika')][['value']]
Nitrates_Kannika=Nitrates_sampledate_Kannika.join(Nitrates_value_Kannika)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Kannika=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Kannika')][['sample date']] 
Orthophosphate_phosphorus_value_Kannika=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Kannika')][['value']]
Orthophosphate_phosphorus_Kannika=Orthophosphate_phosphorus_sampledate_Kannika.join(Orthophosphate_phosphorus_value_Kannika)


                                            #Chai
# water temperature 
WT_sampledate_Chai=file[(file.measure=='Water temperature') & (file.location=='Chai')][['sample date']] 
WT_value_Chai=file[(file.measure=='Water temperature') & (file.location=='Chai')][['value']]
WT_Chai=WT_sampledate_Chai.join(WT_value_Chai)  


# Dissolved oxygen 
D_oxygen_sampledate_Chai=file[(file.measure=='Dissolved oxygen') & (file.location=='Chai')][['sample date']] 
D_oxygen_value_Chai=file[(file.measure=='Dissolved oxygen') & (file.location=='Chai')][['value']]
D_oxygen_Chai=D_oxygen_sampledate_Chai.join(D_oxygen_value_Chai)
D_oxygen_value_Chai_avg=D_oxygen_Chai['value'].mean()

 #Biochemical Oxygen
B_oxygen_sampledate_Chai=file[(file.measure=='Biochemical Oxygen') & (file.location=='Chai')][['sample date']] 
B_oxygen_value_Chai=file[(file.measure=='Biochemical Oxygen') & (file.location=='Chai')][['value']]
B_oxygen_Chai=B_oxygen_sampledate_Chai.join(B_oxygen_value_Chai)
# Ammonium
Ammonium_sampledate_Chai=file[(file.measure=='Ammonium') & (file.location=='Chai')][['sample date']] 
Ammonium_value_Chai=file[(file.measure=='Ammonium') & (file.location=='Chai')][['value']]
Ammonium_Chai=Ammonium_sampledate_Chai.join(Ammonium_value_Chai)
#Nitrates
Nitrates_sampledate_Chai=file[(file.measure=='Nitrates') & (file.location=='Chai')][['sample date']] 
Nitrates_value_Chai=file[(file.measure=='Nitrates') & (file.location=='Chai')][['value']]
Nitrates_Chai=Nitrates_sampledate_Chai.join(Nitrates_value_Chai)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Chai=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Chai')][['sample date']] 
Orthophosphate_phosphorus_value_Chai=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Chai')][['value']]
Orthophosphate_phosphorus_Chai=Orthophosphate_phosphorus_sampledate_Chai.join(Orthophosphate_phosphorus_value_Chai)
                                            #Decha

# water temperature 
WT_sampledate_Decha=file[(file.measure=='Water temperature') & (file.location=='Decha')][['sample date']] 
WT_value_Decha=file[(file.measure=='Water temperature') & (file.location=='Decha')][['value']]
WT_Decha=WT_sampledate_Decha.join(WT_value_Decha)  

# Dissolved oxygen 
D_oxygen_sampledate_Decha=file[(file.measure=='Dissolved oxygen') & (file.location=='Decha')][['sample date']] 
D_oxygen_value_Decha=file[(file.measure=='Dissolved oxygen') & (file.location=='Decha')][['value']]
D_oxygen_Decha=D_oxygen_sampledate_Decha.join(D_oxygen_value_Decha)
D_oxygen_value_Decha_avg=D_oxygen_Decha['value'].mean()

 #Biochemical Oxygen
B_oxygen_sampledate_Decha=file[(file.measure=='Biochemical Oxygen') & (file.location=='Decha')][['sample date']] 
B_oxygen_value_Decha=file[(file.measure=='Biochemical Oxygen') & (file.location=='Decha')][['value']]
B_oxygen_Decha=B_oxygen_sampledate_Decha.join(B_oxygen_value_Decha)
# Ammonium
Ammonium_sampledate_Decha=file[(file.measure=='Ammonium') & (file.location=='Decha')][['sample date']] 
Ammonium_value_Decha=file[(file.measure=='Ammonium') & (file.location=='Decha')][['value']]
Ammonium_Decha=Ammonium_sampledate_Decha.join(Ammonium_value_Decha)
#Nitrates
Nitrates_sampledate_Decha=file[(file.measure=='Nitrates') & (file.location=='Decha')][['sample date']] 
Nitrates_value_Decha=file[(file.measure=='Nitrates') & (file.location=='Decha')][['value']]
Nitrates_Decha=Nitrates_sampledate_Decha.join(Nitrates_value_Decha)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Decha=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Decha')][['sample date']] 
Orthophosphate_phosphorus_value_Decha=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Decha')][['value']]
Orthophosphate_phosphorus_Decha=Orthophosphate_phosphorus_sampledate_Decha.join(Orthophosphate_phosphorus_value_Decha)


                                            #Tansanee
# water temperature 
WT_sampledate_Tansanee=file[(file.measure=='Water temperature') & (file.location=='Tansanee')][['sample date']] 
WT_value_Tansanee=file[(file.measure=='Water temperature') & (file.location=='Tansanee')][['value']]
WT_Tansanee=WT_sampledate_Tansanee.join(WT_value_Tansanee)  


# Dissolved oxygen 
D_oxygen_sampledate_Tansanee=file[(file.measure=='Dissolved oxygen') & (file.location=='Tansanee')][['sample date']] 
D_oxygen_value_Tansanee=file[(file.measure=='Dissolved oxygen') & (file.location=='Tansanee')][['value']]
D_oxygen_Tansanee=D_oxygen_sampledate_Tansanee.join(D_oxygen_value_Tansanee)
D_oxygen_value_Tansanee_avg=D_oxygen_Tansanee['value'].mean()

 #Biochemical Oxygen
B_oxygen_sampledate_Tansanee=file[(file.measure=='Biochemical Oxygen') & (file.location=='Tansanee')][['sample date']] 
B_oxygen_value_Tansanee=file[(file.measure=='Biochemical Oxygen') & (file.location=='Tansanee')][['value']]
B_oxygen_Tansanee=B_oxygen_sampledate_Tansanee.join(B_oxygen_value_Tansanee)
# Ammonium
Ammonium_sampledate_Tansanee=file[(file.measure=='Ammonium') & (file.location=='Tansanee')][['sample date']] 
Ammonium_value_Tansanee=file[(file.measure=='Ammonium') & (file.location=='Tansanee')][['value']]
Ammonium_Tansanee=Ammonium_sampledate_Tansanee.join(Ammonium_value_Tansanee)
#Nitrates
Nitrates_sampledate_Tansanee=file[(file.measure=='Nitrates') & (file.location=='Tansanee')][['sample date']] 
Nitrates_value_Tansanee=file[(file.measure=='Nitrates') & (file.location=='Tansanee')][['value']]
Nitrates_Tansanee=Nitrates_sampledate_Tansanee.join(Nitrates_value_Tansanee)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Tansanee=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Tansanee')][['sample date']] 
Orthophosphate_phosphorus_value_Tansanee=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Tansanee')][['value']]
Orthophosphate_phosphorus_Tansanee=Orthophosphate_phosphorus_sampledate_Tansanee.join(Orthophosphate_phosphorus_value_Tansanee)


                                            #Busarakhan
# water temperature 
WT_sampledate_Busarakhan=file[(file.measure=='Water temperature') & (file.location=='Busarakhan')][['sample date']] 
WT_value_Busarakhan=file[(file.measure=='Water temperature') & (file.location=='Busarakhan')][['value']]
WT_Busarakhan=WT_sampledate_Busarakhan.join(WT_value_Busarakhan)  

# Dissolved oxygen 
D_oxygen_sampledate_Busarakhan=file[(file.measure=='Dissolved oxygen') & (file.location=='Busarakhan')][['sample date']] 
D_oxygen_value_Busarakhan=file[(file.measure=='Dissolved oxygen') & (file.location=='Busarakhan')][['value']]
D_oxygen_Busarakhan=D_oxygen_sampledate_Busarakhan.join(D_oxygen_value_Busarakhan)
D_oxygen_value_Busarakhan_avg=D_oxygen_Busarakhan['value'].mean()

 #Biochemical Oxygen
B_oxygen_sampledate_Busarakhan=file[(file.measure=='Biochemical Oxygen') & (file.location=='Busarakhan')][['sample date']] 
B_oxygen_value_Busarakhan=file[(file.measure=='Biochemical Oxygen') & (file.location=='Busarakhan')][['value']]
B_oxygen_Busarakhan=B_oxygen_sampledate_Busarakhan.join(B_oxygen_value_Busarakhan)
# Ammonium
Ammonium_sampledate_Busarakhan=file[(file.measure=='Ammonium') & (file.location=='Busarakhan')][['sample date']] 
Ammonium_value_Busarakhan=file[(file.measure=='Ammonium') & (file.location=='Busarakhan')][['value']]
Ammonium_Busarakhan=Ammonium_sampledate_Busarakhan.join(Ammonium_value_Busarakhan)
#Nitrates
Nitrates_sampledate_Busarakhan=file[(file.measure=='Nitrates') & (file.location=='Busarakhan')][['sample date']] 
Nitrates_value_Busarakhan=file[(file.measure=='Nitrates') & (file.location=='Busarakhan')][['value']]
Nitrates_Busarakhan=Nitrates_sampledate_Busarakhan.join(Nitrates_value_Busarakhan)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Busarakhan=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Busarakhan')][['sample date']] 
Orthophosphate_phosphorus_value_Busarakhan=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Busarakhan')][['value']]
Orthophosphate_phosphorus_Busarakhan=Orthophosphate_phosphorus_sampledate_Busarakhan.join(Orthophosphate_phosphorus_value_Busarakhan)

                                            #Kohsoom
# water temperature 
WT_sampledate_Kohsoom=file[(file.measure=='Water temperature') & (file.location=='Kohsoom')][['sample date']] 
WT_value_Kohsoom=file[(file.measure=='Water temperature') & (file.location=='Kohsoom')][['value']]
WT_Kohsoom=WT_sampledate_Kohsoom.join(WT_value_Kohsoom)  


# Dissolved oxygen 
D_oxygen_sampledate_Kohsoom=file[(file.measure=='Dissolved oxygen') & (file.location=='Kohsoom')][['sample date']] 
D_oxygen_value_Kohsoom=file[(file.measure=='Dissolved oxygen') & (file.location=='Kohsoom')][['value']]
D_oxygen_Kohsoom=D_oxygen_sampledate_Kohsoom.join(D_oxygen_value_Kohsoom)

 #Biochemical Oxygen
B_oxygen_sampledate_Kohsoom=file[(file.measure=='Biochemical Oxygen') & (file.location=='Kohsoom')][['sample date']] 
B_oxygen_value_Kohsoom=file[(file.measure=='Biochemical Oxygen') & (file.location=='Kohsoom')][['value']]
B_oxygen_Kohsoom=B_oxygen_sampledate_Kohsoom.join(B_oxygen_value_Kohsoom)
# Ammonium
Ammonium_sampledate_Kohsoom=file[(file.measure=='Ammonium') & (file.location=='Kohsoom')][['sample date']] 
Ammonium_value_Kohsoom=file[(file.measure=='Ammonium') & (file.location=='Kohsoom')][['value']]
Ammonium_Kohsoom=Ammonium_sampledate_Kohsoom.join(Ammonium_value_Kohsoom)
#Nitrates
Nitrates_sampledate_Kohsoom=file[(file.measure=='Nitrates') & (file.location=='Kohsoom')][['sample date']] 
Nitrates_value_Kohsoom=file[(file.measure=='Nitrates') & (file.location=='Kohsoom')][['value']]
Nitrates_Kohsoom=Nitrates_sampledate_Kohsoom.join(Nitrates_value_Kohsoom)
#Orthophosphate_phosphorus
Orthophosphate_phosphorus_sampledate_Kohsoom=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Kohsoom')][['sample date']] 
Orthophosphate_phosphorus_value_Kohsoom=file[(file.measure=='Orthophosphate-phosphorus') & (file.location=='Kohsoom')][['value']]
Orthophosphate_phosphorus_Kohsoom=Orthophosphate_phosphorus_sampledate_Kohsoom.join(Orthophosphate_phosphorus_value_Kohsoom)


# water temp plot                                           
fig=plt.figure(1)
ax1=fig.add_subplot(10,2,1)
WT_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Water Temp data  ',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
WT_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
WT_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
WT_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
WT_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
WT_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
WT_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
WT_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
WT_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
WT_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Water Temp data',legend=False)
plt.axhline(y=24, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
# Dissolved oxyzen plot

fig=plt.figure(2)
ax1=fig.add_subplot(10,2,1)
D_oxygen_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Dissolved oxyzen data  ',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
D_oxygen_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
D_oxygen_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
D_oxygen_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
D_oxygen_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
D_oxygen_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
D_oxygen_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
D_oxygen_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
D_oxygen_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
D_oxygen_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Dissolved oxyzen data',legend=False)
plt.axhline(y=11, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

#Biochemical Oxygen
fig=plt.figure(3)
ax1=fig.add_subplot(10,2,1)
B_oxygen_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Biochemical Oxygen data  ',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
B_oxygen_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
B_oxygen_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
B_oxygen_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
B_oxygen_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
B_oxygen_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
B_oxygen_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
B_oxygen_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
B_oxygen_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
B_oxygen_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Biochemical Oxygen data',legend=False)
plt.axhline(y=5, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

#Ammonium
fig=plt.figure(4)
ax1=fig.add_subplot(10,2,1)
Ammonium_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Ammonium data  ',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
Ammonium_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Ammonium_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Ammonium_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
Ammonium_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Ammonium_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Ammonium_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Ammonium_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
Ammonium_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
Ammonium_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Ammonium data',legend=False)
plt.axhline(y=0.002, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

#Nitrates
fig=plt.figure(5)
ax1=fig.add_subplot(10,2,1)
Nitrates_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Nitrates data  ',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
Nitrates_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Nitrates_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Nitrates_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
Nitrates_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Nitrates_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Nitrates_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Nitrates_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
Nitrates_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
Nitrates_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Nitrates data',legend=False)
plt.axhline(y=1, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

#Orthophosphate_phosphorus
fig=plt.figure(6)
ax1=fig.add_subplot(10,2,1)
Orthophosphate_phosphorus_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Orthophosphate_phosphorus data  ',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
Orthophosphate_phosphorus_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Orthophosphate_phosphorus_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Orthophosphate_phosphorus_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
Orthophosphate_phosphorus_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Orthophosphate_phosphorus_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Orthophosphate_phosphorus_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Orthophosphate_phosphorus_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
Orthophosphate_phosphorus_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
Orthophosphate_phosphorus_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Orthophosphate_phosphorus data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
plt.show()

plt.show()

