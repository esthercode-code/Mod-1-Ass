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