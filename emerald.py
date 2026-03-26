shelf = [2,3,4,4,5,6,1,2,2,2,1,8,2]
count = 0
highest = 0 

for numbers in shelf :
    if numbers % 2 ==0:
        count = count + numbers
        if count > highest :
            highest = count
    else:
        count = 0
print(highest)