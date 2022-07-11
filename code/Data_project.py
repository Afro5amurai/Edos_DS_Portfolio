#!/usr/bin/env python
# coding: utf-8

# # Structure and preparations.
# MAIN GOAL : produce a data overview and conclusion
# 
# Questions i asked myself before i started:
# 1. how to deal with file errors (not well formatted data)?  
# 2. how to deal with missing values?
# 3. how to evaluate incorrect/invalid data?
# 4. what to measure success?
# 5. what data is relevent?
# 6. which correlations are the most effective?
# 7. what data is relevent?
# 
# As i don't come from a data science background I learned most of the things presented here from the libraries documentation
# which was challenging and intreresting.

# ## Flow of work
# First of all i tried to set goals and have a clear path to what to do next in the project.
# after importing the initial data i tried to understand the data by using the info and describe methods.
# 
# #### Clearing the data
# First of all i wanted to see if the data is valid, i checked for null values in the data and saw that most entries were full with the exception of 'LSOA_of_Accident_Location' field, which was mostly NaN.
# 
# ####  Understanding the data
# Sfter seeing that all fields are pretty much numeric even though it doesn't fit well with logic (gender or day of week for example) i opened the context csv files to understand the logic behind the numbers of some of the importent key data in my opinion
# 
# #### Approach to displaying data 
# After getting an idea of what i'm working with i decided to plot a heatmap of the accident data file to see what correlates best and to figure out what fields should i do additional analysis on.

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import folium
from folium.plugins import HeatMap


# Including the libraries i used for the project

# In[2]:


accidents_data = pd.read_csv('data/Accidents0515.csv',index_col='Accident_Index')
casualties_data = pd.read_csv('data/Casualties0515.csv',on_bad_lines = 'skip',index_col='Accident_Index')
vehicles_data = pd.read_csv('data/Vehicles0515.csv',on_bad_lines = 'skip',index_col='Accident_Index')


# Clearing the data as some entries were probably unsutible to the csv format

# In[3]:


accidents_data = accidents_data.dropna(how = "all")
casualties_data = casualties_data.dropna(how = "all")
vehicles_data = vehicles_data.dropna(how = "all")


# deleting rows that are fully null if there are any as they don't benefit the analysis

# In[4]:


accidents_data['Date'] = pd.to_datetime(accidents_data['Date'], infer_datetime_format=True)
accidents_data['Year']= accidents_data['Date'].dt.year
accidents_data['Month']=accidents_data['Date'].dt.month
accidents_data['Day']=accidents_data['Date'].dt.day
accidents_data.drop('Date' , axis = 1, inplace = True)


# In[5]:


accidents_data['Hour'] = accidents_data['Time'].apply(lambda x:str(x).split(':')[0])


# ## representing data more intuatively using context files
# 
# used the CSVcontext files to translate some of the data i'll use later from numbers to logical meanings 

# In[6]:


accidents_data_int = accidents_data
casualties_data_int = casualties_data
vehicles_data_int = vehicles_data


# In[7]:


accidents_data_int = accidents_data_int.replace({'Accident_Severity': {1: 'Fatal accident', 2: 'Serious accident', 3:'Slight accident'}})
accidents_data_int = accidents_data_int.replace({"Day_of_Week":{ 1:"Sunday" , 2:"Monday",3:"Tuesday" , 4:"Wednsday", 5:"Thursday", 6:"Friday", 7:"Saturday"}})
vehicles_data_int = vehicles_data_int.replace({'Sex_of_Driver': {-1: 'Missing gender data',1: 'Male', 2: 'Female', 3:'Unknown gender'}})
casualties_data_int = casualties_data_int.replace({'Casualty_Severity': {1: 'Fatal wound', 2: 'Serious wound', 3:'Slight wound'}})


# ## Key matrics
# I decided to show some key data as key matrics, this is data that i viewed as easiest to digest in numeric form.

# In[8]:


yearly_mean = accidents_data.shape[0]/accidents_data['Year'].nunique()
monthly_mean = accidents_data.shape[0]/(12*accidents_data['Year'].nunique())
daily_mean = accidents_data.shape[0]/(365*accidents_data['Year'].nunique())
accident_severity_mean = accidents_data['Accident_Severity'].mean()
casualties_per_accident = accidents_data['Number_of_Casualties'].mean()

casualty_age_mean = casualties_data['Age_of_Casualty'].mean()

driver_age_mean = vehicles_data['Age_of_Driver'].mean()
car_age_mean = vehicles_data['Age_of_Vehicle'].mean()


# In[9]:


print(f"the average number of accidents per year in the years 2005-2015 {'%.2f' % yearly_mean}, per month is {'%.2f' % monthly_mean}, and per day is {'%.2f' % daily_mean}.")
print(f"the average severity of an accident is {'%.2f' % accident_severity_mean} where 1 is low severity, 2 is medium severity and 3 is high severity.")
print(f"there were {'%.2f' % casualties_per_accident} casualties per accident and the average casualty age is {'%.2f' % casualty_age_mean}")
print(f"the drivers average age was {'%.2f' % driver_age_mean} where the average vehicle age was {'%.2f' % car_age_mean}")


# #### I decided to merge all the data to get an overview of how certain criteria correlates to each other
# To make the chart readable i decided to pick three parameters as my benchmark,
# 
# accident severity 
# number of casualties 
# casualty severity
# 
# and decided to drop some of the data that was least correlated to the benchmark or didn't make logical sense for it to be correlated.

# In[10]:


all_data = accidents_data.join(vehicles_data.drop('Vehicle_Reference',axis = 1), how='right').join(casualties_data, how='right')
all_data_int = accidents_data_int.join(vehicles_data_int.drop('Vehicle_Reference',axis = 1), how='right').join(casualties_data_int, how='right')


# In[11]:


heatmap_accidents_data = all_data.drop(['Vehicle_Reference','Casualty_Reference','Carriageway_Hazards','Journey_Purpose_of_Driver','Engine_Capacity_(CC)' ,'Casualty_Home_Area_Type' ,'Propulsion_Code' ,'Driver_IMD_Decile','Junction_Location' ,'Vehicle_Location-Restricted_Lane' ,'Pedestrian_Road_Maintenance_Worker' ,'Bus_or_Coach_Passenger', 'Towing_and_Articulation' ,'Was_Vehicle_Left_Hand_Drive?', 'Age_Band_of_Driver', 'Hit_Object_off_Carriageway' ,'Hit_Object_in_Carriageway','Pedestrian_Crossing-Physical_Facilities','2nd_Road_Class','2nd_Road_Number','Pedestrian_Crossing-Human_Control','Junction_Detail','Junction_Control','Location_Northing_OSGR','Location_Easting_OSGR','1st_Road_Number','Longitude','Latitude','1st_Road_Class','Local_Authority_(District)','Police_Force','Month','Year','Day'],axis = 1)
corr =  heatmap_accidents_data.corr()
plt.subplots(figsize=(20,9))
sns.heatmap(corr)


# After getting a general picture of how our data looks we want to see which craiterias are valid, relevent to our analysis
# and how are they gauged.
# 

# ## ACCIDENTS & CASUALTIES
# 
# In this section we'll want to see how accidents and casualties are distributed over certain parameters
# 
# The guidelines i used for selecting the parameters for the analysis are from the correlations from the heatmap and logical correlations that I wanted to highlight in the conclusion 
#  
# I decided to focus more on the fatal accidents as they correlates more strongly to number of casualties and severity of casualties.

# The parameters I see as the most relevent are:
# ## 1. accident severity 
# ## 2. number of casualties 
# ## 3. casualty severity
# 
# As i believe diving deep into these parameters will allow the UK ministy to achieve best results in metigating car accidents and deaths.
# 
# Accident severity and number of casualties are correlated to weather conditions but we dont have a description on how to gauge weather in the context csv so we'll use light conditions instead as it correlates too but not as strongly and logically corelated to car accidents.
# 
# Accident Severity:
# Accident Severity correlates with the weather conditions , did officer arrive at scene, gender of driver and casualty severity parameters
# As I see it, an officer will arrive to the scene usually if the accident is fatal, therefore the correlation so i decided to not further focus on this parameter.
# casualty severity also correlates positivly as it is logically tied to accident severity.
# 
# Number of causalties:
# Accident Severity correlates with the speed limit and weather condition parameters.
# 
# Casualty Severity:
# Accident Severity correlates with the gender of driver and age of the driver , did officer arrive at scene and gender parameters
# again, we won't use the officer arrived parameter for the same resoning.
# 
# I also decided to add yearly monthly and daily data to get a meaningful idea of how the trends look.

# In[12]:


fig = px.histogram(all_data_int, x = 'Casualty_Severity',histnorm = 'percent')
fig.update_xaxes(categoryorder = 'total ascending')
fig.update_layout( title="Casualty Severity") 
fig.show()


# In[13]:


fig = px.histogram(accidents_data_int, x = 'Accident_Severity' ,histnorm = 'percent')
fig.update_xaxes(categoryorder = 'total ascending')
fig.update_layout( title="Accidents Severity") 
fig.show()


# As we can see most accidents are not fatal or serious

# In[14]:


casualties_data = casualties_data.replace({'Accident_Severity': {1: 'Fatal', 2: 'Serious', 3:'Slight'}})
fig = px.histogram(all_data_int, x = 'Day_of_Week', color = "Accident_Severity", pattern_shape = "Casualty_Severity" )
fig.update_xaxes(categoryorder = 'total ascending')
fig.update_layout( title="Accidents by day of week") 
fig.show()


# Wanted to add last period, divide by quarter/seasonality but didn't make it in time

# In[15]:


fig = px.histogram(all_data_int, x = 'Month',color = "Accident_Severity", pattern_shape = "Casualty_Severity")
fig.update_xaxes(categoryorder = 'total ascending')
fig.update_layout( title="Accident count by month" , bargap=0.4, height = 500) 
fig.show()


# It looks like most of the months are equal when it comes to car accidents and severity, it seems like the summer months(6-10)
# have the most car accidents occurrences.

# In[16]:


fig = px.histogram(all_data_int, x = 'Year',color = "Accident_Severity", pattern_shape = "Casualty_Severity")
fig.update_xaxes(categoryorder = 'total ascending')
fig.update_layout( title="Accident count by Year" , bargap=0.4, height = 500) 
fig.show()


# we can see a clear, positive trend here, car accidents are decreasing year over year for the most part.

# In[17]:


data_Severity_equal_1 = heatmap_accidents_data[heatmap_accidents_data['Accident_Severity']==1]
data_Severity_equal_1 =data_Severity_equal_1.replace({'Light_Conditions':{-1: 'Missing light condition data',1: 'Daylight', 4: 'dakness - lights lit', 5:'darkness - light until', 6:'no lighting', 7:'unknown lighting'}})
fig = px.histogram(data_Severity_equal_1,height=400, x='Speed_limit', y = 'Number_of_Casualties', color = "Light_Conditions")
fig.update_xaxes(categoryorder = 'total ascending')
fig.update_layout( title="Number of casualties severity by speed limit divided to light conditions" ,bargap = 0.2) 
fig.show()


# We can obviously see that the number of casualties goes up as the speed limit raises which correlates nicely to the data.
# we can also see that most of the casualties happen at daylight but a big chunk does happen at no lightning conditions.

# In[18]:


heatmap_accidents_data_age_severity = heatmap_accidents_data[(heatmap_accidents_data['Age_of_Driver']>0) & (heatmap_accidents_data['Accident_Severity'] == 1)]
heatmap_accidents_data_age_severity = heatmap_accidents_data_age_severity.replace({'Sex_of_Driver': {-1: 'Missing gender data',1: 'Male', 2: 'Female', 3:'unknown gender'}})                                                    
fig = px.histogram(heatmap_accidents_data_age_severity,height=400, x='Age_of_Driver', y = 'Casualty_Severity', histnorm = 'percent',color = "Sex_of_Driver")
fig.update_xaxes(categoryorder = 'total ascending')
fig.update_layout( title="High severity accidents by driver age",bargap = 0.2 ) 
fig.show()



# Unfortunatly unknown gender makes a big chunk of the data BUT we can see a big spike in Casualty severity around the age of 30

# In[19]:


heatmap_accidents_data_age_severity = heatmap_accidents_data[(heatmap_accidents_data['Age_of_Vehicle']>0) & (heatmap_accidents_data['Accident_Severity'] == 1)]
heatmap_accidents_data_age_severity = heatmap_accidents_data_age_severity.replace({'Light_Conditions': {-1: 'Missing light condition data',1: 'Daylight', 4: 'dakness - lights lit', 5:'darkness - light until', 6:'no lighting', 7:'unknown lighting'}})                                                    
heatmap_accidents_data_age_severity = heatmap_accidents_data_age_severity.replace({'Sex_of_Casualty': {-1: 'Missing gender data',1: 'Male', 2: 'Female', 3:'unknown gender'}})                                                   
fig = px.histogram(heatmap_accidents_data_age_severity,height=400, x='Sex_of_Casualty', y = 'Accident_Severity', histnorm = 'percent',color = "Light_Conditions")
fig.update_xaxes(categoryorder = 'total ascending')
fig.update_layout( title="High severity accidents by Driver gender",bargap = 0.2 ) 
fig.show()


# We can see that mostly men do severe accidents with lightning conditions distributing pretty evenly.

# ## A heatmap that shows where most accidents occured
# 
# At last i decided to add a neat feature that shows where most accidents occured.
# we can see that most accidents occured in crowded areas and main cities which is logical because these cities are the most crowded places usually.

# In[21]:


acc_data_loc_no_nans = accidents_data.drop('LSOA_of_Accident_Location', axis = 1).dropna()
m_1 = folium.Map(locations = [51.500153, -0.1262362],tiles = 'cartodbpositron')
HeatMap(data = acc_data_loc_no_nans[['Latitude','Longitude']], zoom_start=5,radius = 10).add_to(m_1)
m_1


# # CONCLUSION
# 
# in conclusion we can see that most accidents happen in crowded areas,
# Fatal accidents are preformed by men more than by women around the age of 30 in high speed limit areas.
# If I could give some tips for the UK government I would suggest:
# 1. A campaign targeting men in their 30's that would encourage them to drive slower in high speed 
# limit areas
# 2. Put up signs for slowing down in highways.
# 3. Put up more streetlights as we can see a big chunk of the accidents happen in no light condition 
# 
# This is my first time using python for data science and it was really fun and educating, 
# ### thanks for reading my analysis!





