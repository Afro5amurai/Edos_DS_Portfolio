# Structure and preparations.
MAIN GOAL : produce a data overview and conclusion

Questions i asked myself before i started:

1. how to deal with missing values?
2. how to evaluate incorrect/invalid data?
3. what to measure success?
4. what data is relevent?
5. which correlations are the most effective?
6. what data is relevent?
7. how to deal with file errors (not well formatted data)?

As i don't come from a data science background I learned most of the things presented here from the libraries documentation which was challenging and intreresting.

## Flow of work
First of all i tried to set goals and have a clear path to what to do next in the project. after importing the initial data i tried to understand the data by using the info and describe methods.

Clearing the data
First of all i wanted to see if the data is valid, i checked for null values in the data and saw that most entries were full with the exception of 'LSOA_of_Accident_Location' field, which was mostly NaN.

Understanding the data
Sfter seeing that all fields are pretty much numeric even though it doesn't fit well with logic (gender or day of week for example) i opened the context csv files to understand the logic behind the numbers of some of the importent key data in my opinion

Approach to displaying data
After getting an idea of what i'm working with i decided to plot a heatmap of the accident data file to see what correlates best and to figure out what fields should i do additional analysis on.

### CODE BLOCK 1 IMPORTS

import pandas as pd

import numpy as np

import seaborn as sns 

import matplotlib.pyplot as plt

import plotly.express as px

import plotly.graph_objects as go

import folium

from folium.plugins import HeatMap

### CODE BLOCK 2
Reading the data and understanding how my database looks, arranging the data so it fits my desired format 
and clearing null data, in addition sheding light on data provided in numbers through the contexCSV file.

accidents_data = pd.read_csv('data/Accidents0515.csv',index_col='Accident_Index')

casualties_data = pd.read_csv('data/Casualties0515.csv',on_bad_lines = 'skip',index_col='Accident_Index')

vehicles_data = pd.read_csv('data/Vehicles0515.csv',on_bad_lines = 'skip',index_col='Accident_Index')


accidents_data = accidents_data.dropna(how = "all")

casualties_data = casualties_data.dropna(how = "all")

vehicles_data = vehicles_data.dropna(how = "all")


accidents_data['Date'] = pd.to_datetime(accidents_data['Date'], infer_datetime_format=True)

accidents_data['Year']= accidents_data['Date'].dt.year

accidents_data['Month']=accidents_data['Date'].dt.month

accidents_data['Day']=accidents_data['Date'].dt.day

accidents_data.drop('Date' , axis = 1, inplace = True)


accidents_data_int = accidents_data

casualties_data_int = casualties_data

vehicles_data_int = vehicles_data


accidents_data_int = accidents_data_int.replace({'Accident_Severity': {1: 'Fatal accident', 2: 'Serious accident', 3:'Slight accident'}})

accidents_data_int = accidents_data_int.replace({"Day_of_Week":{ 1:"Sunday" , 2:"Monday",3:"Tuesday" , 4:"Wednsday", 5:"Thursday", 6:"Friday", 7:"Saturday"}})

vehicles_data_int = vehicles_data_int.replace({'Sex_of_Driver': {-1: 'Missing gender data',1: 'Male', 2: 'Female', 3:'Unknown gender'}})

casualties_data_int = casualties_data_int.replace({'Casualty_Severity': {1: 'Fatal wound', 2: 'Serious wound', 3:'Slight wound'}})
