#solution 1
def vowelcount():
    x = input('Enter a word or phrase : \n')
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for a1 in str(x):
        if a1 == 'a':
            a = a + 1
        if a1 == 'e':
            e = e + 1
        if a1 == 'i':
            i = i + 1
        if a1 == 'o':
            o = o + 1
        if a1 == 'u':
            u = u + 1
    print('a, e, i, o, u appear respectively ' + '{}, {}, {}, {}, {}'.format(a, e, i, o, u) + ' times.')
    
vowelcount()

#solution 2
def vcount():
    y = input('Enter a word or phrase 2: \n')
    A = y.count('a')
    E = y.count('e')
    I = y.count('i')
    O = y.count('o')
    U = y.count('u')
    print('a, e, i, o, u appear respectively ' + '{}, {}, {}, {}, {}'.format(A, E, I, O, U) + ' times.')

vcount()

