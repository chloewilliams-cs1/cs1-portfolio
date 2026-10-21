#PayCheck.py


"""This program gets the number or hours an employee works in a week and their hourly rate and then outputs their pay."""


hours = float(input("How many hours did you work this week?"))
hourly_rate = float(input("What is your hour rate?"))



if hours < 0:
    print("Error: You cannot enter a negative number.")
    
    
    
if hourly_rate < 0:
    print("Error: You cannot enter a negative number.")
  
    
if hourly_rate > 0:
    if hours > 0:
        
        product1 = hours * hourly_rate
        if hours <= 40:
            print("Your paycheck before deductions is $", product1)
    

        if hours > 40:
            subtraction1 = hours - 40
        
            product2 = hourly_rate * 1.5
    
            addition1 = subtraction1 * product2 + 40 * hourly_rate
    
            print("Your paycheck before deductions is $", addition1)


