def lastfirst(lst):
    fname = list()
    lname = list()

    for name in lst:
        nameV = name.split(',')
        fname.append(nameV[1])
        lname.append(nameV[0])
    print('First name: ' , fname)
    print('Last name: ', lname)

    allnames = list()
    allnames.append(fname)
    allnames.append(lname)
    return allnames

names = ['Gaaa,aaa','Haaa,kkk','JKKKK,llll']

mynames = lastfirst(names)
for alist in mynames:
    print(alist)
