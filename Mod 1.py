 #Your task is to develop a Python program to facilitate the weekly payments of workers. 
#Assignment Description
#The program should accomplish the following tasks:
#Use variables to create a list of workers dynamically (at least 400 workers).
#Utilize a for loop to generate payment slips for each of the 400 workers.
#Implement the following conditional statements within the for loop:If the salary is greater than $10,000 and less than $20,000, assign the Employee level as "A1."
#If the salary is greater than $7,500 and less than $30,000 and the employee is female, set the Employee level as "A5-F."
#
#Add exception handling to your Python code to address potential errors.
import random
try:
    workers = []
    genders = ["Male", "Female"]
    
    #for loop
    for i in range(400):
        worker = {
            "id": i + 1,
            "name": f"Worker_{i + 1}",
            "gender": random.choice(genders),  
            "salary": random.randint(1000, 35000) #radom salary between $1000 and $35000
        }
        workers.append(worker)
        
    #generating payment slip for each worker
    for worker in workers:
        salary = worker["salary"]
        gender = worker["gender"]
        level = "None"
        
        #assignibng levels to workers
        if salary > 10000 and salary  < 20000:
            level = "A1"
            
        if salary > 7500 and salary < 30000 and gender == "Female":
            level = "A5-F"
            
        print(f"Payment Slip: ID={worker["id"]}, Name={worker["name"]}, Gender={gender}, " f"Salary=${salary}, Level={level}")    
    
except Exception as error:
    print("You encountered an error", error)