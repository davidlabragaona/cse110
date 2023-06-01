#Author: David Labra Gaona
#Purpose: Program a wind chill calculator

def calculate_wind_chill(temperature, speed):
    return 35.74 + (0.6215 * temperature) - (35.75 * speed ** 0.16) + (0.4275 * temperature * speed ** 0.16)

def convert_celcius_to_farenheit(temperature):
    return 32.00 + (temperature * 9.00 / 5.00)

temperature = 0.00
wind_speed = 0.00
#Farenheit: f
#Celcius: c
isFarenheit = False

temperature = float(input("What is the temperature? "))
isFarenheit = (input("Fahrenheit or Celsius (F/C)? ").lower() == "f")
if not isFarenheit:
    temperature = convert_celcius_to_farenheit(temperature)

for speed in range(5, 65, 5):
    temp = calculate_wind_chill(temperature, speed)
    print(f"At temperature {temperature:-5.2f}F, and wind speed {speed:2d} mph, the windchill is: {temp:-3.2f}F")
    

    
