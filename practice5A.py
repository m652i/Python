USA = 315
MEX = 121

def growth(u,m):
    x=0
    while u >= m:
        u = u*0.85
        m = m*1.01
        x = x+1
        print('USA: ' + str(int(u)) + ' million')
        print('MEX: '+ str(int(m)) + ' million')
        print(str(x) + ' years')
    print('Mexico population surpassed the US in ' + str(x) + ' years')
growth(USA,MEX)
