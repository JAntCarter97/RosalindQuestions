#Rabbits and Recurrence relations
#ID: FIB

#It takes a month for a pair to turn into a breeding pair.
#Given n in months and k in offspring from one breeding pair
#return the number of breeding pairs after n months.

def countRabbitPairs(months, offspringMultiplier):
    num = num2 = 0
    num1 = 1
    for i in range(months-1):
        num = num1 + (num2 * offspringMultiplier)
        num2 = num1
        num1 = num 
    return num 

#Test code
#numRabbitPairs = countRabbitPairs(5, 3)
#print(numRabbitPairs)