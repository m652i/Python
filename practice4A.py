# name = full name
# a = marital status
# k = number of kids
# g = gross income
# p = pension
# exe = exemption
# t = total people in household
################################
def computetax(G, EXE, P, T):

    tax = G - EXE - (G*P) - T*1500
    return tax

def getdata ():

    #NAME
    name = input('Please enter your first name followed by your last : \n')
    print('Hi! ' +  str(name) + '.')

    #MARITAL STATUS & KIDS
    exe = 0
    t = 1
    a = input('Are you single or married? (type s or m) : \n')
    while a != 's' and a != 'm':
        print('Please type s for single (not married) or m for married.')
        a = input('Are you married : ')
    else:
        if a == 's':
            exe = 4000
            print('Marital Status : Not married')
        if a == 'm':
            exe = 7000
            t = t + 1
            print('Marital Status : Married')
            k = int(input('How many kids under the age of 14? : \n'))
            if k > 0:
                t = t + k
    #GROSS INCOME
    if a == 'm':
        g = float(input('Enter combined household salary : \n'))
    if a == 's':
        g = float(input('Enter salary : \n'))
    #PENSION
    p = float(input('Percentage of income for pension fund (enter in decimal 6% = 0.06): \n'))

    #COMPUTE TAX
    taxes = computetax(float(g), int(exe), float(p), int(t))
    print('Taxable income : ')
    if taxes <= 0:
        print('0')
        print('Salary amount after tax: ')
        print(g)
    else:
        print(str(taxes))
        aftertax = 0
        if g <= 15000:
            aftertax = taxes*0.15
            print('Tax amount : ')
            print(str(aftertax))
        if g >= 15001:
            aftertax = taxes*0.25 + 2250
            print('Tax amount : ')
            print(str(aftertax))
        print('Salary amount after tax: ')
        print(g - aftertax)

getdata()

