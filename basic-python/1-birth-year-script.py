# Julia Ingram
# 2021-10-31
# Homework 1

import random

birth_year = input("What year were you born?") #Get the user's birth year
while(int(birth_year)) > 2021: #Make sure it's not in the future
    input('That year is in the future! What year were you born?')
birth_year = int(birth_year) #Convert string input to integer
age = 2021 - birth_year #Store age for later reference

print(f'You are {age} years old') #Print how old the user is

print(f'In your lifetime, your heart has beaten about {35000000*age:,} times') #Multiply annual heartrate by age

whale_beats = 0 
whale_range = int(round(24*365.25*age)) #Can't iterate through a float, need to convert
for i in range(whale_range): #Loop through all the days the user has been alive
    whale_beats += random.randint(2, 37) #Add a random heartrate within the whale's large range
whale_beats = whale_beats*60
print(f"In your lifetime, a blue whale's heart has beaten about {whale_beats:,} times")

rabbit_beats = 0
rabbit_range = int(round(24*365.25*age)) #Can't iterate through a float, need to convert
for i in range(rabbit_range): #Loop through all the days the user has been alive
    rabbit_beats += random.randint(120,150) #Add a random heartrate within healthy rabbit range
rabbit_beats = rabbit_beats * 60 
if rabbit_beats > 1000000:
    rabbit_beats = str(round(rabbit_beats / 1000000)) + " million" #Convert heartrate in millions rather than raw number
print(f"In your lifetime, a rabbit's heart has beaten about {rabbit_beats} times") #Print how many times rabbit heart has beaten

print(f"You are {round(age/0.62)} years old in Venus years") #A Venus year is 224.7 Earth days, approximately 0.62 of an Earth year
print(f'You are {round(age/164.79*365.25)} days old in Neptune years') #A Neptune year is 164.79 Earth years, converted to days here 

compared_to_me = "" 
#Find out if user is older, younger, or the same age 
if age > 22:
    compared_to_me = "older than me"
elif age < 22: 
    compared_to_me = "younger than me"
else: 
    compared_to_me = "the same age as me"
print(f'You are {compared_to_me}') 
if compared_to_me != "the same age as me": #Only print age difference if user is not the same age
    print(f'You are {abs(age-22)} years {compared_to_me}')

if birth_year % 2 != 0: #Find if a birth year is even or odd
    year_type = 'odd'
else: year_type = 'even'
print(f"You were born in an {year_type} numbered year")

# Find out how many Democratic presidents served since they were born (from 1960 on)
number_of_dems = 0
dem_president_elect_years = [1961, 1963, 1977, 1993, 2009, 2021]
for year in dem_president_elect_years:
    if birth_year <= year:
        number_of_dems+=1
print(f"There have been {number_of_dems} Democratic Presidents in office in your lifetime")

presidents = {
1961:"John F. Kennedy", 
1963:"Lyndon B. Johnson", 
1969:"Richard M. Nixon",
1974:"Gerald R. Ford",
1977:"Jimmy Carter",
1981:"Ronald Reagan", 
1989:"George Bush", 
1993:"Bill Clinton", 
2001:"George W. Bush", 
2009:"Barack Obama", 
2017:"Donald J. Trump", 
2021:"Joe Biden"
}
birth_president = ""
for year, president in presidents.items():
    if birth_year >= year:
        birth_president = president
print(f"When you were born, {birth_president} was the President")

# Human heartrate source: https://www.pbs.org/wgbh/nova/heart/heartfacts.html
# Whale heartrate source: https://www.smithsonianmag.com/smart-news/researchers-measure-blue-whales-heart-rate-first-time-180973662/
# Rabbit heartrate source: https://rabbit.org/temperature-and-respiration-rates/ 
# Planet years source: https://www.exploratorium.edu/ronh/age/ 
# Democratic president years source: https://simple.wikipedia.org/wiki/Democratic_Party_(United_States)
# All presidents source: http://goodcsv.com/politics/us-presidents/ 
