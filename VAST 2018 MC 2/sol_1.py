import pandas as pd
import matplotlib.pyplot as plt

# read csv as pandas dataframe 
file= pd.read_csv("/Users/sayedkhan/Desktop/MC2/Boonsong Lekagul waterways readings.csv")
'''

pandas 'file' strcture:

file.head()

     id  value location sample date            measure
0  2221   2.00  Boonsri   11-Jan-98  Water temperature
1  2223   9.10  Boonsri   11-Jan-98   Dissolved oxygen

I will collect data for location and measure. For each location and measure, I will get value vs sample date plot. That will show the change of value within the time period.For example:

Phenanthrene_sampledate_Boonsri=file[(file.measure=='Water temperature') & (file.location=='Boonsri')][['sample date']] # if measure ==Water temperature && file.location==Boonsri, the command will give me th sample date
Phenanthrene_value_Boonsri=file[(file.measure=='Water temperature') & (file.location=='Boonsri')][['value']]## if measure ==Water temperature && file.location==Boonsri, the command will give me th value 




'''



	
                                            # Boonsri
# 1. Phenanthrene in Boonsri
Phenanthrene_sampledate_Boonsri=file[(file.measure=='Phenanthrene') & (file.location=='Boonsri')][['sample date']] 
Phenanthrene_value_Boonsri=file[(file.measure=='Phenanthrene') & (file.location=='Boonsri')][['value']]
Phenanthrene_Boonsri=Phenanthrene_sampledate_Boonsri.join(Phenanthrene_value_Boonsri)
# 2. Pyrene in Boonsri
Pyrene_sampledate_Boonsri=file[(file.measure=='Pyrene') & (file.location=='Boonsri')][['sample date']] 
Pyrene_value_Boonsri=file[(file.measure=='Pyrene') & (file.location=='Boonsri')][['value']]
Pyrene_Boonsri=Pyrene_sampledate_Boonsri.join(Pyrene_value_Boonsri)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Boonsri=file[(file.measure=='Acenaphthylene') & (file.location=='Boonsri')][['sample date']] 
Acenaphthylene_value_Boonsri=file[(file.measure=='Acenaphthylene') & (file.location=='Boonsri')][['value']]
Acenaphthylene_Boonsri=Acenaphthylene_sampledate_Boonsri.join(Acenaphthylene_value_Boonsri)
# 4. Anthracene
Anthracene_sampledate_Boonsri=file[(file.measure=='Anthracene') & (file.location=='Boonsri')][['sample date']] 
Anthracene_value_Boonsri=file[(file.measure=='Anthracene') & (file.location=='Boonsri')][['value']]
Anthracene_Boonsri=Anthracene_sampledate_Boonsri.join(Anthracene_value_Boonsri)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Boonsri=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Boonsri')][['sample date']] 
Trichlorobenzene_value_Boonsri=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Boonsri')][['value']]
Trichlorobenzene_Boonsri=Trichlorobenzene_sampledate_Boonsri.join(Trichlorobenzene_value_Boonsri)
# 6 Endosulfan
Endosulfan_sampledate_Boonsri=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Boonsri')][['sample date']] 
Endosulfan_value_Boonsri=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Boonsri')][['value']]
Endosulfan_Boonsri=Endosulfan_sampledate_Boonsri.join(Endosulfan_value_Boonsri)
# 7 Methoxychlor
Methoxychlor_sampledate_Boonsri=file[(file.measure=='Methoxychlor') & (file.location=='Boonsri')][['sample date']] 
Methoxychlor_value_Boonsri=file[(file.measure=='Methoxychlor') & (file.location=='Boonsri')][['value']]
Methoxychlor_Boonsri=Methoxychlor_sampledate_Boonsri.join(Methoxychlor_value_Boonsri)

# 8.    Lead
Lead_sampledate_Boonsri=file[(file.measure=='Lead') & (file.location=='Boonsri')][['sample date']] 
Lead_value_Boonsri=file[(file.measure=='Lead') & (file.location=='Boonsri')][['value']]
Lead_Boonsri=Lead_sampledate_Boonsri.join(Lead_value_Boonsri)
Lead_value_Boonsri_avg=Lead_Boonsri['value'].mean()
# 9.    Mercury
Mercury_sampledate_Boonsri=file[(file.measure=='Mercury') & (file.location=='Boonsri')][['sample date']] 
Mercury_value_Boonsri=file[(file.measure=='Mercury') & (file.location=='Boonsri')][['value']]
Mercury_Boonsri=Mercury_sampledate_Boonsri.join(Mercury_value_Boonsri)

# 10  Cadmium
Cadmium_sampledate_Boonsri=file[(file.measure=='Cadmium') & (file.location=='Boonsri')][['sample date']] 
Cadmium_value_Boonsri=file[(file.measure=='Cadmium') & (file.location=='Boonsri')][['value']]
Cadmium_Boonsri=Cadmium_sampledate_Boonsri.join(Cadmium_value_Boonsri)


                                            #Somchair

# 1. Phenanthrene in Somchair
Phenanthrene_sampledate_Somchair=file[(file.measure=='Phenanthrene') & (file.location=='Somchair')][['sample date']] 
Phenanthrene_value_Somchair=file[(file.measure=='Phenanthrene') & (file.location=='Somchair')][['value']]
Phenanthrene_Somchair=Phenanthrene_sampledate_Somchair.join(Phenanthrene_value_Somchair)
# 2. Pyrene in Somchair
Pyrene_sampledate_Somchair=file[(file.measure=='Pyrene') & (file.location=='Somchair')][['sample date']] 
Pyrene_value_Somchair=file[(file.measure=='Pyrene') & (file.location=='Somchair')][['value']]
Pyrene_Somchair=Pyrene_sampledate_Somchair.join(Pyrene_value_Somchair)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Somchair=file[(file.measure=='Acenaphthylene') & (file.location=='Somchair')][['sample date']] 
Acenaphthylene_value_Somchair=file[(file.measure=='Acenaphthylene') & (file.location=='Somchair')][['value']]
Acenaphthylene_Somchair=Acenaphthylene_sampledate_Somchair.join(Acenaphthylene_value_Somchair)
# 4. Anthracene
Anthracene_sampledate_Somchair=file[(file.measure=='Anthracene') & (file.location=='Somchair')][['sample date']] 
Anthracene_value_Somchair=file[(file.measure=='Anthracene') & (file.location=='Somchair')][['value']]
Anthracene_Somchair=Anthracene_sampledate_Somchair.join(Anthracene_value_Somchair)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Somchair=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Somchair')][['sample date']] 
Trichlorobenzene_value_Somchair=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Somchair')][['value']]
Trichlorobenzene_Somchair=Trichlorobenzene_sampledate_Somchair.join(Trichlorobenzene_value_Somchair)
# 6 Endosulfan
Endosulfan_sampledate_Somchair=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Somchair')][['sample date']] 
Endosulfan_value_Somchair=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Somchair')][['value']]
Endosulfan_Somchair=Endosulfan_sampledate_Somchair.join(Endosulfan_value_Somchair)
# 7 Methoxychlor
Methoxychlor_sampledate_Somchair=file[(file.measure=='Methoxychlor') & (file.location=='Somchair')][['sample date']] 
Methoxychlor_value_Somchair=file[(file.measure=='Methoxychlor') & (file.location=='Somchair')][['value']]
Methoxychlor_Somchair=Methoxychlor_sampledate_Somchair.join(Methoxychlor_value_Somchair)

# 8.    Lead
Lead_sampledate_Somchair=file[(file.measure=='Lead') & (file.location=='Somchair')][['sample date']] 
Lead_value_Somchair=file[(file.measure=='Lead') & (file.location=='Somchair')][['value']]
Lead_Somchair=Lead_sampledate_Somchair.join(Lead_value_Somchair)
Lead_value_Somchair_avg=Lead_Somchair['value'].mean()
# 9.    Mercury
Mercury_sampledate_Somchair=file[(file.measure=='Mercury') & (file.location=='Somchair')][['sample date']] 
Mercury_value_Somchair=file[(file.measure=='Mercury') & (file.location=='Somchair')][['value']]
Mercury_Somchair=Mercury_sampledate_Somchair.join(Mercury_value_Somchair)

# 10  Cadmium
Cadmium_sampledate_Somchair=file[(file.measure=='Cadmium') & (file.location=='Somchair')][['sample date']] 
Cadmium_value_Somchair=file[(file.measure=='Cadmium') & (file.location=='Somchair')][['value']]
Cadmium_Somchair=Cadmium_sampledate_Somchair.join(Cadmium_value_Somchair)


                                            #Achara

# 1. Phenanthrene in Achara
Phenanthrene_sampledate_Achara=file[(file.measure=='Phenanthrene') & (file.location=='Achara')][['sample date']] 
Phenanthrene_value_Achara=file[(file.measure=='Phenanthrene') & (file.location=='Achara')][['value']]
Phenanthrene_Achara=Phenanthrene_sampledate_Achara.join(Phenanthrene_value_Achara)
# 2. Pyrene in Achara
Pyrene_sampledate_Achara=file[(file.measure=='Pyrene') & (file.location=='Achara')][['sample date']] 
Pyrene_value_Achara=file[(file.measure=='Pyrene') & (file.location=='Achara')][['value']]
Pyrene_Achara=Pyrene_sampledate_Achara.join(Pyrene_value_Achara)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Achara=file[(file.measure=='Acenaphthylene') & (file.location=='Achara')][['sample date']] 
Acenaphthylene_value_Achara=file[(file.measure=='Acenaphthylene') & (file.location=='Achara')][['value']]
Acenaphthylene_Achara=Acenaphthylene_sampledate_Achara.join(Acenaphthylene_value_Achara)
# 4. Anthracene
Anthracene_sampledate_Achara=file[(file.measure=='Anthracene') & (file.location=='Achara')][['sample date']] 
Anthracene_value_Achara=file[(file.measure=='Anthracene') & (file.location=='Achara')][['value']]
Anthracene_Achara=Anthracene_sampledate_Achara.join(Anthracene_value_Achara)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Achara=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Achara')][['sample date']] 
Trichlorobenzene_value_Achara=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Achara')][['value']]
Trichlorobenzene_Achara=Trichlorobenzene_sampledate_Achara.join(Trichlorobenzene_value_Achara)
# 6 Endosulfan
Endosulfan_sampledate_Achara=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Achara')][['sample date']] 
Endosulfan_value_Achara=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Achara')][['value']]
Endosulfan_Achara=Endosulfan_sampledate_Achara.join(Endosulfan_value_Achara)
# 7 Methoxychlor
Methoxychlor_sampledate_Achara=file[(file.measure=='Methoxychlor') & (file.location=='Achara')][['sample date']] 
Methoxychlor_value_Achara=file[(file.measure=='Methoxychlor') & (file.location=='Achara')][['value']]
Methoxychlor_Achara=Methoxychlor_sampledate_Achara.join(Methoxychlor_value_Achara)

# 8.    Lead
Lead_sampledate_Achara=file[(file.measure=='Lead') & (file.location=='Achara')][['sample date']] 
Lead_value_Achara=file[(file.measure=='Lead') & (file.location=='Achara')][['value']]
Lead_Achara=Lead_sampledate_Achara.join(Lead_value_Achara)
Lead_value_Achara_avg=Lead_Achara['value'].mean()
# 9.    Mercury
Mercury_sampledate_Achara=file[(file.measure=='Mercury') & (file.location=='Achara')][['sample date']] 
Mercury_value_Achara=file[(file.measure=='Mercury') & (file.location=='Achara')][['value']]
Mercury_Achara=Mercury_sampledate_Achara.join(Mercury_value_Achara)

# 10  Cadmium
Cadmium_sampledate_Achara=file[(file.measure=='Cadmium') & (file.location=='Achara')][['sample date']] 
Cadmium_value_Achara=file[(file.measure=='Cadmium') & (file.location=='Achara')][['value']]
Cadmium_Achara=Cadmium_sampledate_Achara.join(Cadmium_value_Achara)




                                            #Sakda

# 1. Phenanthrene in Sakda
Phenanthrene_sampledate_Sakda=file[(file.measure=='Phenanthrene') & (file.location=='Sakda')][['sample date']] 
Phenanthrene_value_Sakda=file[(file.measure=='Phenanthrene') & (file.location=='Sakda')][['value']]
Phenanthrene_Sakda=Phenanthrene_sampledate_Sakda.join(Phenanthrene_value_Sakda)
# 2. Pyrene in Sakda
Pyrene_sampledate_Sakda=file[(file.measure=='Pyrene') & (file.location=='Sakda')][['sample date']] 
Pyrene_value_Sakda=file[(file.measure=='Pyrene') & (file.location=='Sakda')][['value']]
Pyrene_Sakda=Pyrene_sampledate_Sakda.join(Pyrene_value_Sakda)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Sakda=file[(file.measure=='Acenaphthylene') & (file.location=='Sakda')][['sample date']] 
Acenaphthylene_value_Sakda=file[(file.measure=='Acenaphthylene') & (file.location=='Sakda')][['value']]
Acenaphthylene_Sakda=Acenaphthylene_sampledate_Sakda.join(Acenaphthylene_value_Sakda)
# 4. Anthracene
Anthracene_sampledate_Sakda=file[(file.measure=='Anthracene') & (file.location=='Sakda')][['sample date']] 
Anthracene_value_Sakda=file[(file.measure=='Anthracene') & (file.location=='Sakda')][['value']]
Anthracene_Sakda=Anthracene_sampledate_Sakda.join(Anthracene_value_Sakda)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Sakda=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Sakda')][['sample date']] 
Trichlorobenzene_value_Sakda=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Sakda')][['value']]
Trichlorobenzene_Sakda=Trichlorobenzene_sampledate_Sakda.join(Trichlorobenzene_value_Sakda)
# 6 Endosulfan
Endosulfan_sampledate_Sakda=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Sakda')][['sample date']] 
Endosulfan_value_Sakda=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Sakda')][['value']]
Endosulfan_Sakda=Endosulfan_sampledate_Sakda.join(Endosulfan_value_Sakda)
# 7 Methoxychlor
Methoxychlor_sampledate_Sakda=file[(file.measure=='Methoxychlor') & (file.location=='Sakda')][['sample date']] 
Methoxychlor_value_Sakda=file[(file.measure=='Methoxychlor') & (file.location=='Sakda')][['value']]
Methoxychlor_Sakda=Methoxychlor_sampledate_Sakda.join(Methoxychlor_value_Sakda)

# 8.    Lead
Lead_sampledate_Sakda=file[(file.measure=='Lead') & (file.location=='Sakda')][['sample date']] 
Lead_value_Sakda=file[(file.measure=='Lead') & (file.location=='Sakda')][['value']]
Lead_Sakda=Lead_sampledate_Sakda.join(Lead_value_Sakda)
Lead_value_Sakda_avg=Lead_Sakda['value'].mean()
# 9.    Mercury
Mercury_sampledate_Sakda=file[(file.measure=='Mercury') & (file.location=='Sakda')][['sample date']] 
Mercury_value_Sakda=file[(file.measure=='Mercury') & (file.location=='Sakda')][['value']]
Mercury_Sakda=Mercury_sampledate_Sakda.join(Mercury_value_Sakda)

# 10  Cadmium
Cadmium_sampledate_Sakda=file[(file.measure=='Cadmium') & (file.location=='Sakda')][['sample date']] 
Cadmium_value_Sakda=file[(file.measure=='Cadmium') & (file.location=='Sakda')][['value']]
Cadmium_Sakda=Cadmium_sampledate_Sakda.join(Cadmium_value_Sakda)

                                            #Kannika

# 1. Phenanthrene in Kannika
Phenanthrene_sampledate_Kannika=file[(file.measure=='Phenanthrene') & (file.location=='Kannika')][['sample date']] 
Phenanthrene_value_Kannika=file[(file.measure=='Phenanthrene') & (file.location=='Kannika')][['value']]
Phenanthrene_Kannika=Phenanthrene_sampledate_Kannika.join(Phenanthrene_value_Kannika)
# 2. Pyrene in Kannika
Pyrene_sampledate_Kannika=file[(file.measure=='Pyrene') & (file.location=='Kannika')][['sample date']] 
Pyrene_value_Kannika=file[(file.measure=='Pyrene') & (file.location=='Kannika')][['value']]
Pyrene_Kannika=Pyrene_sampledate_Kannika.join(Pyrene_value_Kannika)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Kannika=file[(file.measure=='Acenaphthylene') & (file.location=='Kannika')][['sample date']] 
Acenaphthylene_value_Kannika=file[(file.measure=='Acenaphthylene') & (file.location=='Kannika')][['value']]
Acenaphthylene_Kannika=Acenaphthylene_sampledate_Kannika.join(Acenaphthylene_value_Kannika)
# 4. Anthracene
Anthracene_sampledate_Kannika=file[(file.measure=='Anthracene') & (file.location=='Kannika')][['sample date']] 
Anthracene_value_Kannika=file[(file.measure=='Anthracene') & (file.location=='Kannika')][['value']]
Anthracene_Kannika=Anthracene_sampledate_Kannika.join(Anthracene_value_Kannika)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Kannika=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Kannika')][['sample date']] 
Trichlorobenzene_value_Kannika=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Kannika')][['value']]
Trichlorobenzene_Kannika=Trichlorobenzene_sampledate_Kannika.join(Trichlorobenzene_value_Kannika)
# 6 Endosulfan
Endosulfan_sampledate_Kannika=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Kannika')][['sample date']] 
Endosulfan_value_Kannika=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Kannika')][['value']]
Endosulfan_Kannika=Endosulfan_sampledate_Kannika.join(Endosulfan_value_Kannika)
# 7 Methoxychlor
Methoxychlor_sampledate_Kannika=file[(file.measure=='Methoxychlor') & (file.location=='Kannika')][['sample date']] 
Methoxychlor_value_Kannika=file[(file.measure=='Methoxychlor') & (file.location=='Kannika')][['value']]
Methoxychlor_Kannika=Methoxychlor_sampledate_Kannika.join(Methoxychlor_value_Kannika)

# 8.    Lead
Lead_sampledate_Kannika=file[(file.measure=='Lead') & (file.location=='Kannika')][['sample date']] 
Lead_value_Kannika=file[(file.measure=='Lead') & (file.location=='Kannika')][['value']]
Lead_Kannika=Lead_sampledate_Kannika.join(Lead_value_Kannika)
Lead_value_Kannika_avg=Lead_Kannika['value'].mean()
# 9.    Mercury
Mercury_sampledate_Kannika=file[(file.measure=='Mercury') & (file.location=='Kannika')][['sample date']] 
Mercury_value_Kannika=file[(file.measure=='Mercury') & (file.location=='Kannika')][['value']]
Mercury_Kannika=Mercury_sampledate_Kannika.join(Mercury_value_Kannika)

# 10  Cadmium
Cadmium_sampledate_Kannika=file[(file.measure=='Cadmium') & (file.location=='Kannika')][['sample date']] 
Cadmium_value_Kannika=file[(file.measure=='Cadmium') & (file.location=='Kannika')][['value']]
Cadmium_Kannika=Cadmium_sampledate_Kannika.join(Cadmium_value_Kannika)


                                            #Chai
# 1. Phenanthrene in Chai
Phenanthrene_sampledate_Chai=file[(file.measure=='Phenanthrene') & (file.location=='Chai')][['sample date']] 
Phenanthrene_value_Chai=file[(file.measure=='Phenanthrene') & (file.location=='Chai')][['value']]
Phenanthrene_Chai=Phenanthrene_sampledate_Chai.join(Phenanthrene_value_Chai)
# 2. Pyrene in Chai
Pyrene_sampledate_Chai=file[(file.measure=='Pyrene') & (file.location=='Chai')][['sample date']] 
Pyrene_value_Chai=file[(file.measure=='Pyrene') & (file.location=='Chai')][['value']]
Pyrene_Chai=Pyrene_sampledate_Chai.join(Pyrene_value_Chai)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Chai=file[(file.measure=='Acenaphthylene') & (file.location=='Chai')][['sample date']] 
Acenaphthylene_value_Chai=file[(file.measure=='Acenaphthylene') & (file.location=='Chai')][['value']]
Acenaphthylene_Chai=Acenaphthylene_sampledate_Chai.join(Acenaphthylene_value_Chai)
# 4. Anthracene
Anthracene_sampledate_Chai=file[(file.measure=='Anthracene') & (file.location=='Chai')][['sample date']] 
Anthracene_value_Chai=file[(file.measure=='Anthracene') & (file.location=='Chai')][['value']]
Anthracene_Chai=Anthracene_sampledate_Chai.join(Anthracene_value_Chai)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Chai=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Chai')][['sample date']] 
Trichlorobenzene_value_Chai=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Chai')][['value']]
Trichlorobenzene_Chai=Trichlorobenzene_sampledate_Chai.join(Trichlorobenzene_value_Chai)
# 6 Endosulfan
Endosulfan_sampledate_Chai=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Chai')][['sample date']] 
Endosulfan_value_Chai=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Chai')][['value']]
Endosulfan_Chai=Endosulfan_sampledate_Chai.join(Endosulfan_value_Chai)
# 7 Methoxychlor
Methoxychlor_sampledate_Chai=file[(file.measure=='Methoxychlor') & (file.location=='Chai')][['sample date']] 
Methoxychlor_value_Chai=file[(file.measure=='Methoxychlor') & (file.location=='Chai')][['value']]
Methoxychlor_Chai=Methoxychlor_sampledate_Chai.join(Methoxychlor_value_Chai)

# 8.    Lead
Lead_sampledate_Chai=file[(file.measure=='Lead') & (file.location=='Chai')][['sample date']] 
Lead_value_Chai=file[(file.measure=='Lead') & (file.location=='Chai')][['value']]
Lead_Chai=Lead_sampledate_Chai.join(Lead_value_Chai)
Lead_value_Chai_avg=Lead_Chai['value'].mean()
# 9.    Mercury
Mercury_sampledate_Chai=file[(file.measure=='Mercury') & (file.location=='Chai')][['sample date']] 
Mercury_value_Chai=file[(file.measure=='Mercury') & (file.location=='Chai')][['value']]
Mercury_Chai=Mercury_sampledate_Chai.join(Mercury_value_Chai)

# 10  Cadmium
Cadmium_sampledate_Chai=file[(file.measure=='Cadmium') & (file.location=='Chai')][['sample date']] 
Cadmium_value_Chai=file[(file.measure=='Cadmium') & (file.location=='Chai')][['value']]
Cadmium_Chai=Cadmium_sampledate_Chai.join(Cadmium_value_Chai)

                                            #Decha

# 1. Phenanthrene in Decha
Phenanthrene_sampledate_Decha=file[(file.measure=='Phenanthrene') & (file.location=='Decha')][['sample date']] 
Phenanthrene_value_Decha=file[(file.measure=='Phenanthrene') & (file.location=='Decha')][['value']]
Phenanthrene_Decha=Phenanthrene_sampledate_Decha.join(Phenanthrene_value_Decha)
# 2. Pyrene in Decha
Pyrene_sampledate_Decha=file[(file.measure=='Pyrene') & (file.location=='Decha')][['sample date']] 
Pyrene_value_Decha=file[(file.measure=='Pyrene') & (file.location=='Decha')][['value']]
Pyrene_Decha=Pyrene_sampledate_Decha.join(Pyrene_value_Decha)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Decha=file[(file.measure=='Acenaphthylene') & (file.location=='Decha')][['sample date']] 
Acenaphthylene_value_Decha=file[(file.measure=='Acenaphthylene') & (file.location=='Decha')][['value']]
Acenaphthylene_Decha=Acenaphthylene_sampledate_Decha.join(Acenaphthylene_value_Decha)
# 4. Anthracene
Anthracene_sampledate_Decha=file[(file.measure=='Anthracene') & (file.location=='Decha')][['sample date']] 
Anthracene_value_Decha=file[(file.measure=='Anthracene') & (file.location=='Decha')][['value']]
Anthracene_Decha=Anthracene_sampledate_Decha.join(Anthracene_value_Decha)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Decha=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Decha')][['sample date']] 
Trichlorobenzene_value_Decha=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Decha')][['value']]
Trichlorobenzene_Decha=Trichlorobenzene_sampledate_Decha.join(Trichlorobenzene_value_Decha)
# 6 Endosulfan
Endosulfan_sampledate_Decha=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Decha')][['sample date']] 
Endosulfan_value_Decha=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Decha')][['value']]
Endosulfan_Decha=Endosulfan_sampledate_Decha.join(Endosulfan_value_Decha)
# 7 Methoxychlor
Methoxychlor_sampledate_Decha=file[(file.measure=='Methoxychlor') & (file.location=='Decha')][['sample date']] 
Methoxychlor_value_Decha=file[(file.measure=='Methoxychlor') & (file.location=='Decha')][['value']]
Methoxychlor_Decha=Methoxychlor_sampledate_Decha.join(Methoxychlor_value_Decha)

# 8.    Lead
Lead_sampledate_Decha=file[(file.measure=='Lead') & (file.location=='Decha')][['sample date']] 
Lead_value_Decha=file[(file.measure=='Lead') & (file.location=='Decha')][['value']]
Lead_Decha=Lead_sampledate_Decha.join(Lead_value_Decha)
Lead_value_Decha_avg=Lead_Decha['value'].mean()
# 9.    Mercury
Mercury_sampledate_Decha=file[(file.measure=='Mercury') & (file.location=='Decha')][['sample date']] 
Mercury_value_Decha=file[(file.measure=='Mercury') & (file.location=='Decha')][['value']]
Mercury_Decha=Mercury_sampledate_Decha.join(Mercury_value_Decha)

# 10  Cadmium
Cadmium_sampledate_Decha=file[(file.measure=='Cadmium') & (file.location=='Decha')][['sample date']] 
Cadmium_value_Decha=file[(file.measure=='Cadmium') & (file.location=='Decha')][['value']]
Cadmium_Decha=Cadmium_sampledate_Decha.join(Cadmium_value_Decha)

                                            #Tansanee
# 1. Phenanthrene in Tansanee
Phenanthrene_sampledate_Tansanee=file[(file.measure=='Phenanthrene') & (file.location=='Tansanee')][['sample date']] 
Phenanthrene_value_Tansanee=file[(file.measure=='Phenanthrene') & (file.location=='Tansanee')][['value']]
Phenanthrene_Tansanee=Phenanthrene_sampledate_Tansanee.join(Phenanthrene_value_Tansanee)
# 2. Pyrene in Tansanee
Pyrene_sampledate_Tansanee=file[(file.measure=='Pyrene') & (file.location=='Tansanee')][['sample date']] 
Pyrene_value_Tansanee=file[(file.measure=='Pyrene') & (file.location=='Tansanee')][['value']]
Pyrene_Tansanee=Pyrene_sampledate_Tansanee.join(Pyrene_value_Tansanee)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Tansanee=file[(file.measure=='Acenaphthylene') & (file.location=='Tansanee')][['sample date']] 
Acenaphthylene_value_Tansanee=file[(file.measure=='Acenaphthylene') & (file.location=='Tansanee')][['value']]
Acenaphthylene_Tansanee=Acenaphthylene_sampledate_Tansanee.join(Acenaphthylene_value_Tansanee)
# 4. Anthracene
Anthracene_sampledate_Tansanee=file[(file.measure=='Anthracene') & (file.location=='Tansanee')][['sample date']] 
Anthracene_value_Tansanee=file[(file.measure=='Anthracene') & (file.location=='Tansanee')][['value']]
Anthracene_Tansanee=Anthracene_sampledate_Tansanee.join(Anthracene_value_Tansanee)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Tansanee=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Tansanee')][['sample date']] 
Trichlorobenzene_value_Tansanee=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Tansanee')][['value']]
Trichlorobenzene_Tansanee=Trichlorobenzene_sampledate_Tansanee.join(Trichlorobenzene_value_Tansanee)
# 6 Endosulfan
Endosulfan_sampledate_Tansanee=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Tansanee')][['sample date']] 
Endosulfan_value_Tansanee=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Tansanee')][['value']]
Endosulfan_Tansanee=Endosulfan_sampledate_Tansanee.join(Endosulfan_value_Tansanee)
# 7 Methoxychlor
Methoxychlor_sampledate_Tansanee=file[(file.measure=='Methoxychlor') & (file.location=='Tansanee')][['sample date']] 
Methoxychlor_value_Tansanee=file[(file.measure=='Methoxychlor') & (file.location=='Tansanee')][['value']]
Methoxychlor_Tansanee=Methoxychlor_sampledate_Tansanee.join(Methoxychlor_value_Tansanee)

# 8.    Lead
Lead_sampledate_Tansanee=file[(file.measure=='Lead') & (file.location=='Tansanee')][['sample date']] 
Lead_value_Tansanee=file[(file.measure=='Lead') & (file.location=='Tansanee')][['value']]
Lead_Tansanee=Lead_sampledate_Tansanee.join(Lead_value_Tansanee)
Lead_value_Tansanee_avg=Lead_Tansanee['value'].mean()
# 9.    Mercury
Mercury_sampledate_Tansanee=file[(file.measure=='Mercury') & (file.location=='Tansanee')][['sample date']] 
Mercury_value_Tansanee=file[(file.measure=='Mercury') & (file.location=='Tansanee')][['value']]
Mercury_Tansanee=Mercury_sampledate_Tansanee.join(Mercury_value_Tansanee)

# 10  Cadmium
Cadmium_sampledate_Tansanee=file[(file.measure=='Cadmium') & (file.location=='Tansanee')][['sample date']] 
Cadmium_value_Tansanee=file[(file.measure=='Cadmium') & (file.location=='Tansanee')][['value']]
Cadmium_Tansanee=Cadmium_sampledate_Tansanee.join(Cadmium_value_Tansanee)


                                            #Busarakhan
# 1. Phenanthrene in Busarakhan
Phenanthrene_sampledate_Busarakhan=file[(file.measure=='Phenanthrene') & (file.location=='Busarakhan')][['sample date']] 
Phenanthrene_value_Busarakhan=file[(file.measure=='Phenanthrene') & (file.location=='Busarakhan')][['value']]
Phenanthrene_Busarakhan=Phenanthrene_sampledate_Busarakhan.join(Phenanthrene_value_Busarakhan)
# 2. Pyrene in Busarakhan
Pyrene_sampledate_Busarakhan=file[(file.measure=='Pyrene') & (file.location=='Busarakhan')][['sample date']] 
Pyrene_value_Busarakhan=file[(file.measure=='Pyrene') & (file.location=='Busarakhan')][['value']]
Pyrene_Busarakhan=Pyrene_sampledate_Busarakhan.join(Pyrene_value_Busarakhan)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Busarakhan=file[(file.measure=='Acenaphthylene') & (file.location=='Busarakhan')][['sample date']] 
Acenaphthylene_value_Busarakhan=file[(file.measure=='Acenaphthylene') & (file.location=='Busarakhan')][['value']]
Acenaphthylene_Busarakhan=Acenaphthylene_sampledate_Busarakhan.join(Acenaphthylene_value_Busarakhan)
# 4. Anthracene
Anthracene_sampledate_Busarakhan=file[(file.measure=='Anthracene') & (file.location=='Busarakhan')][['sample date']] 
Anthracene_value_Busarakhan=file[(file.measure=='Anthracene') & (file.location=='Busarakhan')][['value']]
Anthracene_Busarakhan=Anthracene_sampledate_Busarakhan.join(Anthracene_value_Busarakhan)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Busarakhan=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Busarakhan')][['sample date']] 
Trichlorobenzene_value_Busarakhan=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Busarakhan')][['value']]
Trichlorobenzene_Busarakhan=Trichlorobenzene_sampledate_Busarakhan.join(Trichlorobenzene_value_Busarakhan)
# 6 Endosulfan
Endosulfan_sampledate_Busarakhan=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Busarakhan')][['sample date']] 
Endosulfan_value_Busarakhan=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Busarakhan')][['value']]
Endosulfan_Busarakhan=Endosulfan_sampledate_Busarakhan.join(Endosulfan_value_Busarakhan)
# 7 Methoxychlor
Methoxychlor_sampledate_Busarakhan=file[(file.measure=='Methoxychlor') & (file.location=='Busarakhan')][['sample date']] 
Methoxychlor_value_Busarakhan=file[(file.measure=='Methoxychlor') & (file.location=='Busarakhan')][['value']]
Methoxychlor_Busarakhan=Methoxychlor_sampledate_Busarakhan.join(Methoxychlor_value_Busarakhan)

# 8.    Lead
Lead_sampledate_Busarakhan=file[(file.measure=='Lead') & (file.location=='Busarakhan')][['sample date']] 
Lead_value_Busarakhan=file[(file.measure=='Lead') & (file.location=='Busarakhan')][['value']]
Lead_Busarakhan=Lead_sampledate_Busarakhan.join(Lead_value_Busarakhan)
Lead_value_Busarakhan_avg=Lead_Busarakhan['value'].mean()
# 9.    Mercury
Mercury_sampledate_Busarakhan=file[(file.measure=='Mercury') & (file.location=='Busarakhan')][['sample date']] 
Mercury_value_Busarakhan=file[(file.measure=='Mercury') & (file.location=='Busarakhan')][['value']]
Mercury_Busarakhan=Mercury_sampledate_Busarakhan.join(Mercury_value_Busarakhan)

# 10  Cadmium
Cadmium_sampledate_Busarakhan=file[(file.measure=='Cadmium') & (file.location=='Busarakhan')][['sample date']] 
Cadmium_value_Busarakhan=file[(file.measure=='Cadmium') & (file.location=='Busarakhan')][['value']]
Cadmium_Busarakhan=Cadmium_sampledate_Busarakhan.join(Cadmium_value_Busarakhan)

                                            #Kohsoom
# 1. Phenanthrene in Kohsoom
Phenanthrene_sampledate_Kohsoom=file[(file.measure=='Phenanthrene') & (file.location=='Kohsoom')][['sample date']] 
Phenanthrene_value_Kohsoom=file[(file.measure=='Phenanthrene') & (file.location=='Kohsoom')][['value']]
Phenanthrene_Kohsoom=Phenanthrene_sampledate_Kohsoom.join(Phenanthrene_value_Kohsoom)
# 2. Pyrene in Kohsoom
Pyrene_sampledate_Kohsoom=file[(file.measure=='Pyrene') & (file.location=='Kohsoom')][['sample date']] 
Pyrene_value_Kohsoom=file[(file.measure=='Pyrene') & (file.location=='Kohsoom')][['value']]
Pyrene_Kohsoom=Pyrene_sampledate_Kohsoom.join(Pyrene_value_Kohsoom)
# 3. Acenaphthylene
Acenaphthylene_sampledate_Kohsoom=file[(file.measure=='Acenaphthylene') & (file.location=='Kohsoom')][['sample date']] 
Acenaphthylene_value_Kohsoom=file[(file.measure=='Acenaphthylene') & (file.location=='Kohsoom')][['value']]
Acenaphthylene_Kohsoom=Acenaphthylene_sampledate_Kohsoom.join(Acenaphthylene_value_Kohsoom)
# 4. Anthracene
Anthracene_sampledate_Kohsoom=file[(file.measure=='Anthracene') & (file.location=='Kohsoom')][['sample date']] 
Anthracene_value_Kohsoom=file[(file.measure=='Anthracene') & (file.location=='Kohsoom')][['value']]
Anthracene_Kohsoom=Anthracene_sampledate_Kohsoom.join(Anthracene_value_Kohsoom)
#5 1,2,3-Trichlorobenzene
Trichlorobenzene_sampledate_Kohsoom=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Kohsoom')][['sample date']] 
Trichlorobenzene_value_Kohsoom=file[(file.measure=='1,2,3-Trichlorobenzene') & (file.location=='Kohsoom')][['value']]
Trichlorobenzene_Kohsoom=Trichlorobenzene_sampledate_Kohsoom.join(Trichlorobenzene_value_Kohsoom)
# 6 Endosulfan
Endosulfan_sampledate_Kohsoom=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Kohsoom')][['sample date']] 
Endosulfan_value_Kohsoom=file[(file.measure=='Endosulfan (alpha)') & (file.location=='Kohsoom')][['value']]
Endosulfan_Kohsoom=Endosulfan_sampledate_Kohsoom.join(Endosulfan_value_Kohsoom)
# 7 Methoxychlor
Methoxychlor_sampledate_Kohsoom=file[(file.measure=='Methoxychlor') & (file.location=='Kohsoom')][['sample date']] 
Methoxychlor_value_Kohsoom=file[(file.measure=='Methoxychlor') & (file.location=='Kohsoom')][['value']]
Methoxychlor_Kohsoom=Methoxychlor_sampledate_Kohsoom.join(Methoxychlor_value_Kohsoom)

# 8.    Lead
Lead_sampledate_Kohsoom=file[(file.measure=='Lead') & (file.location=='Kohsoom')][['sample date']] 
Lead_value_Kohsoom=file[(file.measure=='Lead') & (file.location=='Kohsoom')][['value']]
Lead_Kohsoom=Lead_sampledate_Kohsoom.join(Lead_value_Kohsoom)
Lead_value_Kohsoom_avg=Lead_Kohsoom['value'].mean()
# 9.    Mercury
Mercury_sampledate_Kohsoom=file[(file.measure=='Mercury') & (file.location=='Kohsoom')][['sample date']] 
Mercury_value_Kohsoom=file[(file.measure=='Mercury') & (file.location=='Kohsoom')][['value']]
Mercury_Kohsoom=Mercury_sampledate_Kohsoom.join(Mercury_value_Kohsoom)

# 10  Cadmium
Cadmium_sampledate_Kohsoom=file[(file.measure=='Cadmium') & (file.location=='Kohsoom')][['sample date']] 
Cadmium_value_Kohsoom=file[(file.measure=='Cadmium') & (file.location=='Kohsoom')][['value']]
Cadmium_Kohsoom=Cadmium_sampledate_Kohsoom.join(Cadmium_value_Kohsoom)


                                            
# 1. Phenanthrene plot 
fig=plt.figure(1)
ax1=fig.add_subplot(10,2,1)
Phenanthrene_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Phenanthrene data  ',legend=False)
#plt.axhline(y=Phenanthrene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
Phenanthrene_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Phenanthrene data',legend=False)
#plt.axhline(y=Phenanthrene_Somchair['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''
ax2=fig.add_subplot(10,2,5)
Phenanthrene_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Phenanthrene data',legend=False)
plt.axhline(y=Phenanthrene_Achara['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''
ax2=fig.add_subplot(10,2,5)
Phenanthrene_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Phenanthrene data',legend=False)
#plt.axhline(y=Phenanthrene_Sakda['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Phenanthrene_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Phenanthrene data',legend=False)
#plt.axhline(y=Phenanthrene_Chai['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''
ax2=fig.add_subplot(10,2,10)
Phenanthrene_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Phenanthrene data',legend=False)
plt.axhline(y=Phenanthrene_Decha['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''
ax2=fig.add_subplot(10,2,9)
Phenanthrene_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Phenanthrene data',legend=False)
#plt.axhline(y=Phenanthrene_Tansanee['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Phenanthrene_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Phenanthrene data',legend=False)
#plt.axhline(y=Phenanthrene_Busarakhan['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Phenanthrene_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Phenanthrene data',legend=False)
#plt.axhline(y=Phenanthrene_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Phenanthrene_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Phenanthrene data',legend=False)
#plt.axhline(y=Phenanthrene_Kannika['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')


                            
# 2. Pyrene
fig=plt.figure(2)
ax1=fig.add_subplot(1,2,1)
Pyrene_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Pyrene data  ',legend=False)
plt.axhline(y=Pyrene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(1,2,2)
Pyrene_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Pyrene data',legend=False)
plt.axhline(y=Pyrene_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''
ax2=fig.add_subplot(10,2,2)
Pyrene_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Pyrene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Pyrene_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Pyrene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Pyrene_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Pyrene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
Pyrene_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Pyrene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Pyrene_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Pyrene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Pyrene_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Pyrene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Pyrene_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Pyrene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
ax2=fig.add_subplot(10,2,18)
Pyrene_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Pyrene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''

# 3 Acenaphthylene plot
fig=plt.figure(3)
ax1=fig.add_subplot(1,2,1)
Acenaphthylene_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Acenaphthylene data  ',legend=False)
#plt.axhline(y=Acenaphthylene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')


ax2=fig.add_subplot(1,2,2)
Acenaphthylene_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Acenaphthylene data',legend=False)
#plt.axhline(y=Acenaphthylene_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''
ax2=fig.add_subplot(10,2,2)
Acenaphthylene_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Acenaphthylene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Acenaphthylene_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Acenaphthylene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Acenaphthylene_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Acenaphthylene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
Acenaphthylene_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Acenaphthylene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Acenaphthylene_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Acenaphthylene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Acenaphthylene_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Acenaphthylene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Acenaphthylene_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Acenaphthylene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
ax2=fig.add_subplot(10,2,18)
Acenaphthylene_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Acenaphthylene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''




# 4 Anthracene
fig=plt.figure(4)
ax1=fig.add_subplot(7,2,1)
Anthracene_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Anthracene data  ',legend=False)
plt.axhline(y=Anthracene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,2)
Anthracene_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Anthracene data',legend=False)
plt.axhline(y=Anthracene_Somchair['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,5)
Anthracene_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Anthracene data',legend=False)
plt.axhline(y=Anthracene_Sakda['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,6)
Anthracene_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Anthracene data',legend=False)
plt.axhline(y=Anthracene_Chai['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,9)
Anthracene_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Anthracene data',legend=False)
plt.axhline(y=Anthracene_Tansanee['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,10)
Anthracene_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Anthracene data',legend=False)
plt.axhline(y=Anthracene_Busarakhan['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,13)
Anthracene_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Anthracene data',legend=False)
plt.axhline(y=Anthracene_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,14)
Anthracene_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Anthracene data',legend=False)
plt.axhline(y=Anthracene_Kannika['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''
ax2=fig.add_subplot(10,2,5)
Anthracene_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Anthracene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')


ax2=fig.add_subplot(10,2,10)
Anthracene_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Anthracene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''








# 5 Trichlorobenzene
fig=plt.figure(5)
ax1=fig.add_subplot(1,2,1)
Trichlorobenzene_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Trichlorobenzene data  ',legend=False)
#plt.axhline(y=Trichlorobenzene_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(1,2,2)
Trichlorobenzene_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Trichlorobenzene data',legend=False)
#plt.axhline(y=Trichlorobenzene_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

'''
ax2=fig.add_subplot(10,2,2)
Trichlorobenzene_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Trichlorobenzene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Trichlorobenzene_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Trichlorobenzene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Trichlorobenzene_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Trichlorobenzene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')


ax2=fig.add_subplot(10,2,9)
Trichlorobenzene_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Trichlorobenzene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Trichlorobenzene_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Trichlorobenzene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Trichlorobenzene_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Trichlorobenzene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Trichlorobenzene_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Trichlorobenzene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
Trichlorobenzene_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Trichlorobenzene data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''

# 6 Endosulfan
fig=plt.figure(6)
ax1=fig.add_subplot(7,2,1)
Endosulfan_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Endosulfan data  ',legend=False)
plt.axhline(y=Endosulfan_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,2)
Endosulfan_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Endosulfan data',legend=False)
plt.axhline(y=Endosulfan_Somchair['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,5)
Endosulfan_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Endosulfan data',legend=False)
plt.axhline(y=Endosulfan_Sakda['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,6)
Endosulfan_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Endosulfan data',legend=False)
plt.axhline(y=Endosulfan_Chai['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,9)
Endosulfan_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Endosulfan data',legend=False)
plt.axhline(y=Endosulfan_Busarakhan['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,10)
Endosulfan_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Endosulfan data',legend=False)
plt.axhline(y=Endosulfan_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(7,2,13)
Endosulfan_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Endosulfan data',legend=False)
plt.axhline(y=Endosulfan_Kannika['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')


'''
ax2=fig.add_subplot(10,2,5)
Endosulfan_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Endosulfan data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Endosulfan_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Endosulfan data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Endosulfan_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Endosulfan data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''






# 7 Methoxychlor
fig=plt.figure(7)
ax1=fig.add_subplot(5,2,1)
Methoxychlor_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Methoxychlor data  ',legend=False)
plt.axhline(y=Methoxychlor_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(5,2,2)
Methoxychlor_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Methoxychlor data',legend=False)
#plt.axhline(y=EMethoxychlor_Somchair['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(5,2,5)
Methoxychlor_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Methoxychlor data',legend=False)
plt.axhline(y=Methoxychlor_Sakda['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(5,2,6)
Methoxychlor_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Methoxychlor data',legend=False)
plt.axhline(y=Methoxychlor_Chai['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(5,2,9)
Methoxychlor_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Methoxychlor data',legend=False)
#plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(5,2,10)
Methoxychlor_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Methoxychlor data',legend=False)
#plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

'''
ax2=fig.add_subplot(10,2,5)
Methoxychlor_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Methoxychlor data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Methoxychlor_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Methoxychlor data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Methoxychlor_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Methoxychlor data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')


ax2=fig.add_subplot(10,2,18)
Methoxychlor_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Methoxychlor data',legend=False)
plt.axhline(y=0.05, color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')
'''
# 8 Lead plot 
fig=plt.figure(8)
ax1=fig.add_subplot(10,2,1)
Lead_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Lead data  ',legend=False)
plt.axhline(y=Lead_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
Lead_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Lead data',legend=False)
plt.axhline(y=Lead_Somchair['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Lead_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Lead data',legend=False)
plt.axhline(y=Lead_Achara['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Lead_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Lead data',legend=False)
plt.axhline(y=Lead_Sakda['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
Lead_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Lead data',legend=False)
plt.axhline(y=Lead_Chai['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Lead_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Lead data',legend=False)
plt.axhline(y=Lead_Decha['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Lead_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Lead data',legend=False)
plt.axhline(y=Lead_Tansanee['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Lead_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Lead data',legend=False)
plt.axhline(y=Lead_Busarakhan['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
Lead_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Lead data',legend=False)
plt.axhline(y=Lead_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
Lead_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Lead data',legend=False)
plt.axhline(y=Lead_Kannika['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

# 9 Mercury 
fig=plt.figure(9)
ax1=fig.add_subplot(10,2,1)
Mercury_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Mercury data  ',legend=False)
plt.axhline(y=Mercury_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
Mercury_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Mercury data',legend=False)
plt.axhline(y=Mercury_Somchair['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Mercury_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Mercury data',legend=False)
plt.axhline(y=Mercury_Achara['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Mercury_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Mercury data',legend=False)
plt.axhline(y=Mercury_Sakda['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
Mercury_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Mercury data',legend=False)
plt.axhline(y=Mercury_Chai['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Mercury_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Mercury data',legend=False)
plt.axhline(y=Mercury_Decha['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Mercury_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Mercury data',legend=False)
plt.axhline(y=Mercury_Tansanee['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Mercury_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Mercury data',legend=False)
plt.axhline(y=Mercury_Busarakhan['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
Mercury_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Mercury data',legend=False)
plt.axhline(y=Mercury_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
Mercury_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Mercury data',legend=False)
plt.axhline(y=Mercury_Kannika['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

# 10    Cadmium plot 
fig=plt.figure(10)
ax1=fig.add_subplot(10,2,1)
Cadmium_Boonsri.plot(x='sample date',y='value',ax=ax1,title='Boonsri: Cadmium data  ',legend=False)
plt.axhline(y=Cadmium_Boonsri['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,2)
Cadmium_Somchair.plot(x='sample date',y='value',ax=ax2,title='Somchair: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Somchair['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,5)
Cadmium_Achara.plot(x='sample date',y='value',ax=ax2,title='Achara: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Achara['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,6)
Cadmium_Sakda.plot(x='sample date',y='value',ax=ax2,title='Sakda: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Sakda['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,9)
Cadmium_Chai.plot(x='sample date',y='value',ax=ax2,title='Chai: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Chai['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,10)
Cadmium_Decha.plot(x='sample date',y='value',ax=ax2,title='Decha: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Decha['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,13)
Cadmium_Tansanee.plot(x='sample date',y='value',ax=ax2,title='Tansanee: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Tansanee['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,14)
Cadmium_Busarakhan.plot(x='sample date',y='value',ax=ax2,title='Busarakhan: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Busarakhan['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,17)
Cadmium_Kohsoom.plot(x='sample date',y='value',ax=ax2,title='Kohsoom: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Kohsoom['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

ax2=fig.add_subplot(10,2,18)
Cadmium_Kannika.plot(x='sample date',y='value',ax=ax2,title='Kannika: Cadmium data',legend=False)
plt.axhline(y=Cadmium_Kannika['value'].mean(), color='r', linestyle='-')
plt.xlabel('Sample Date')
plt.ylabel('Values')

                                     
plt.show()

