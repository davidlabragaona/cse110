# Author: Group 8pm
# Purpose: Read an HR file and parse the information

with open("hr_system.txt") as employees_data:
    for employee in employees_data:
        line = employee.split()
        name = line[0].strip()
        id = line[1].strip()
        job_title = line[2].strip()
        salary = float(line[3].strip()) / 24 #stretch challenge #2

        #Stretch challenge #3
        if job_title.lower() == "engineer":
            salary += 1000

        #stretch challenge #1
        #name (ID: id_number), job_title - $salary 
        print(f"{name} (ID: {id}), {job_title} - ${salary:.2f}")

