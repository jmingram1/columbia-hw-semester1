# Julia Ingram
# 2021-11-02
# Homework 2, Part 1

# PART ONE: Lists

#Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]

#Display the number of elements in the list.
print(len(numbers))

#Display the 4th element of this list.
print(numbers[3])

#Display the sum of the 2nd and 4th element of the list.
print(numbers[1] + numbers[3])

#Display the 2nd-largest value in the list.
print(sorted(numbers)[-2])

#Display the last element of the original unsorted list
print(numbers[-1])

#Display the sum of all of the numbers divided by two.
print(sum(numbers)/2)

#Print whether the median or the mean of the numbers is higher
def median(list):
    list = sorted(list)
    if len(list) % 2 != 0:
        return sorted(list)[int(len(list)/2)]
    else: 
        middle_numbers = [list[int(len(list)/2)], list[int(len(list)/2) + 1]]
        return sum(middle_numbers)/2
if median(numbers) > sum(numbers)/2:
    print("The median is higher than the mean")
else: print("The mean is higher than the median")

# PART TWO: Dictionaries

# Define a dictionary called movie that works with the following code.
# print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie = {
    'title': "Ferris Bueller's Day Off",
    'year': '1986',
    'director': 'John Hughes'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

# On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), 
# and print out the difference between the two.
movie['budget'] = 5000000
movie['revenue'] = 70700000

print(movie['revenue'] - movie['budget'])

# If the movie cost more to make than it made in theaters, print "That was a bad investment". 
# If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." 
# Otherwise print "That was an okay investment."
if movie['budget'] > movie['revenue']:
    print('That was a bad investment')
elif movie['revenue'] > 5 * movie['budget']:
    print('That was a great investment')
else: print('That was an okay investment')

# Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, 
# Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. 
borough_populations = {
    'Manhattan':1600000,
    'Brooklyn':2600000,
    'Bronx':1400000,
    'Queens':2300000,
    'Staten Island':470000
}
print(sum(borough_populations.values()))
print((borough_populations['Manhattan']))

#Display the population of Brooklyn.
print(f"Brooklyn's population is {borough_populations['Brooklyn']:,}")

#Display the combined population of all five boroughs.
print(f'The combined population of all five boroughs is {sum(borough_populations.values()):,}')

#Display what percent of NYC's population lives in Manhattan.
manhattan_fraction = (borough_populations['Manhattan'] / sum(borough_populations.values()))
print(f"{manhattan_fraction:.1%} of NYC's population lives in Manhattan")