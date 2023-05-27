#Author: David Labra Gaona
#Purpose: Life Expectancy program

lowest_life_expectancy_country = ""
lowest_life_expectancy_year = 0
lowest_life_expectancy = 99999.9

highest_life_expectancy_country = ""
highest_life_expectancy_year = 0
highest_life_expectancy = 0

year = 0
year_user = 0
year_cases = []
average = 0.00
counter = 0
countries = []

with open("life-expectancy.csv", ) as dataset:

  year_user = input("Enter the year of interest: ")
  if not year_user.isnumeric:
    print("Invalid option")
    print()
    exit(1)
  else:
    year_user = int(year_user)
    print()

  for i, line in enumerate(dataset):
    #We skip the first line because it's the header
    if i == 0:
      continue

    line = line.strip().split(",")

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

    if year == year_user:
      year_cases.append(line)
    
print(f"The overall max life expectancy is: {highest_life_expectancy:.2f} from {highest_life_expectancy_country} in {highest_life_expectancy_year}")
print(f"The overall min life expectancy is: {lowest_life_expectancy:.2f} from {lowest_life_expectancy_country} in {lowest_life_expectancy_year}")
print()

highest_life_expectancy = 0
lowest_life_expectancy = 99999.9
for line in year_cases:
  country_name = line[0]
  life_expectancy = float(line[3])
  average += life_expectancy

  if life_expectancy < lowest_life_expectancy:
    lowest_life_expectancy_country = country_name
    lowest_life_expectancy = life_expectancy
  
  if life_expectancy > highest_life_expectancy:
    highest_life_expectancy_country = country_name
    highest_life_expectancy = life_expectancy

average /= len(year_cases)
print(f"For the year {year_user}:")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {highest_life_expectancy_country:.2f} with {highest_life_expectancy:.2f}")
print(f"The min life expectancy was in {lowest_life_expectancy_country:.2f} with {lowest_life_expectancy:.2f}")
print()

#Creativity
country = input("Enter the name of a country: ")

