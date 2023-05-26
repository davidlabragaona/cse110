#Author: David Labra Gaona
#Purpose: Life Expectancy program

lowest_life_expectancy_country = ""
lowest_life_expectancy_year = 0
lowest_life_expectancy = 99999.9

highest_life_expectancy_country = ""
highest_life_expectancy_year = 0
highest_life_expectancy = 0

with open("life-expectancy.csv", ) as dataset:
  for i, line in enumerate(dataset):
    
    #We skeep the first line because it's the header
    if i == 0:
      continue

    line = line.strip().split(",")
    #print(line)

    country_name = line[0]
    year = int(line[2])
    life_expectancy = float(line[3])

    if life_expectancy < lowest_life_expectancy:
      lowest_life_expectancy_country = country_name
      lowest_life_expectancy_year = year
      lowest_life_expectancy = life_expectancy
    
    if life_expectancy > highest_life_expectancy:
      highest_life_expectancy_country = country_name
      highest_life_expectancy_year = year
      highest_life_expectancy = life_expectancy

print(f"Lowest life expectancy: {lowest_life_expectancy}")
print(f"Higest life expectancy: {highest_life_expectancy}")