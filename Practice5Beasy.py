#Gross profit = gp
#Expenses = ex
#Net profit = np

gp = 20000
ex = 35000
x = 1
y = 1

while x <= 20:
    x = x+1
    gp = gp*1.1
    ex = ex*1.04
    np = gp - ex

    if np <= 0:
        print('Net Loss : ' + str(-np))
    elif np > 0 and y == 1:
        print('* Net Profit : '+ str(np))
        y = 2
    elif np > 0 and y == 2:
        print('Net Profit : ' + str(np))

    

