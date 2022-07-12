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

## Analysis
### Key metrics
<br>
I decided to show some key data as key matrics, this is data that i viewed as easiest to digest in numeric form.
<br>
<br>
<br>

Average number of accidents between 2005-2015:
#### Yearly: 161877.55
#### Monthly: 13489.80
#### Daily: 443.50.

<br>
<br>

Casualties statistics:
#### 1.35 casualties per accident
#### average casualty age 34.35
#### average vehicle age was 4.84
<hr>

## Correlation Table

I decided to merge all the data to get an overview of how certain criteria correlates to each other 
<br> <br>
To make the chart readable i decided to pick three parameters as my benchmark,

accident severity number of casualties casualty severity

and decided to drop some of the data that was least correlated to the benchmark or didn't make logical sense for it to be correlated.
<br> <br>

![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/Correlation_table.png
)
<br> <br>
After getting a general picture of how our data looks we want to see which craiterias are valid, relevent to our analysis and how are they gauged.
<br> <br>


<hr>
<br> <br>

## ACCIDENTS & CASUALTIES
In this section we'll want to see how accidents and casualties are distributed over certain parameters

The guidelines i used for selecting the parameters for the analysis are from the correlations from the heatmap and logical correlations that I wanted to highlight in the conclusion

I decided to focus more on the fatal accidents as they correlates more strongly to number of casualties and severity of casualties.

The parameters I see as the most relevent are:

1. accident severity
2. number of casualties
3. casualty severity
As i believe diving deep into these parameters will allow the UK ministy to achieve best results in metigating car accidents and deaths.

Accident severity and number of casualties are correlated to weather conditions but we dont have a description on how to gauge weather in the context csv so we'll use light conditions instead as it correlates too but not as strongly and logically corelated to car accidents.

Accident Severity: Accident Severity correlates with the weather conditions , did officer arrive at scene, gender of driver and casualty severity parameters As I see it, an officer will arrive to the scene usually if the accident is fatal, therefore the correlation so i decided to not further focus on this parameter. casualty severity also correlates positivly as it is logically tied to accident severity.

Number of causalties: Accident Severity correlates with the speed limit and weather condition parameters.

Casualty Severity: Accident Severity correlates with the gender of driver and age of the driver , did officer arrive at scene and gender parameters again, we won't use the officer arrived parameter for the same resoning.

I also decided to add yearly monthly and daily data to get a meaningful idea of how the trends look.
<br> <br>

![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/graph1.png
)


![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/g2.png
)
<br> <br>

As we can see most accidents are not fatal or serious
<br> <br>

## Periodic data 
<br> <br>

![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/g3.png
)
<br> 
Friday is the day in which the biggest amount of accidents happened in my opinion because of the increased amount of vehicles on the roads on fridays and maybe drivers driving drunk after hanging out on friday eve.
<br> <br>


![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/g4.png
)
<br> 
It looks like most of the months are equal when it comes to car accidents and severity, it seems like the summer months(6-10) have the most car accidents occurrences.
<br> <br>

![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/g5.png
)
<br> 
we can see a clear, positive trend here, car accidents are decreasing year over year for the most part.

<br> <br>

## Main comparisons
<br><br>
![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/g6.png
) 
<br> 

We can obviously see that the number of casualties goes up as the speed limit raises which correlates nicely to the data. we can also see that most of the casualties happen at daylight but a big chunk does happen at no lightning conditions.

<br> <br>

![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/g7.png
)
<br> 

Unfortunatly unknown gender makes a big chunk of the data BUT we can see a big spike in Casualty severity around the age of 30

<br> <br>

![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/g8.png
)
<br> 

We can see that mostly men do severe accidents with lightning conditions distributing pretty evenly.
<br> 

<hr>
<br>

### Accident Heatmap
Below is a Heatmap that shows where most accidents occured. we can see that most accidents occured in crowded areas and main cities which is logical because these cities are the most crowded places usually.

<br> <br>

![alt text](https://github.com/Afro5amurai/Edos_Portfolio/blob/main/images/Heat_map.png
)
<br> <br>

## CONCLUSION
in conclusion we can see that most accidents happen in crowded areas, Fatal accidents are preformed by men more than by women around the age of 30 in high speed limit areas. If I could give some tips for the UK government I would suggest:

1. A campaign targeting men in their 30's that would encourage them to drive slower in high speed limit areas
2. Put up signs for slowing down in highways.
3. Put up more streetlights as we can see a big chunk of the accidents happen in no light condition
<br><br>
This is my first time using python for data science and it was really fun and educating,

thanks for reading my analysis!

###### note: unfortunatly I didn't found (yet) a solution so show the the heatmap and graphs embedded in HTML so i uploaded pictures, but if you run the code you can see it's full features, and the graph's features too :)
