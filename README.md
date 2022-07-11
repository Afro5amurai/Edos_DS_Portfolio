# Edos_Portfolio
Example data science project
Structure and preparations.
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

Flow of work
First of all i tried to set goals and have a clear path to what to do next in the project. after importing the initial data i tried to understand the data by using the info and describe methods.

Clearing the data
First of all i wanted to see if the data is valid, i checked for null values in the data and saw that most entries were full with the exception of 'LSOA_of_Accident_Location' field, which was mostly NaN.

Understanding the data
Sfter seeing that all fields are pretty much numeric even though it doesn't fit well with logic (gender or day of week for example) i opened the context csv files to understand the logic behind the numbers of some of the importent key data in my opinion

Approach to displaying data
After getting an idea of what i'm working with i decided to plot a heatmap of the accident data file to see what correlates best and to figure out what fields should i do additional analysis on.
