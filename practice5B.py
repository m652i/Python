#Gross profit = gp
#Expenses = ex
#Net profit = np
gp = 20000
ex = 35000
x = 1
file = open('Profit Data.txt','w')
def calc(x,gp,ex):
    y = 1
    while x <= 20:
        x = x+1
        gp = gp*1.1
        ex = ex*1.04
        np = gp - ex
        if np <= 0:
            dis(np,y)
            savefile1(np)
        elif np > 0 and y == 1:
            dis2(np,y)
            savefile2(np)
            y = 2
        elif np > 0 and y == 2:
            dis3(np,y)
            savefile3(np)

def dis(np,y):
    print('Net Loss : ' + str(-np))               
def dis2(np,y):   
    print('* Net Profit : '+ str(np))              
def dis3(np,y):
    print('Net Profit : ' + str(np))

def savefile1(np):
    file = open('Profit Data.txt','a')
    file.write('Net Loss: ' + str(-np) + '\n')
    file.close

def savefile2(np):
    file = open('Profit Data.txt','a')
    file.write('* Net Gain: ' + str(np) + '\n')
    file.close

def savefile3(np):
    file = open('Profit Data.txt','a')
    file.write('Net Gain: ' + str(np) + '\n')
    file.close
calc(x,gp,ex)

