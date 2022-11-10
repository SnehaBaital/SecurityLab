pt = input("Enter the plain text:")

l1 = len(pt)
list1 = list(pt.upper())
kt= input("Enter the key:")

l2 = len(kt)
list2 = list(kt.upper())
list = list()
listM = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l3 =l1 -l2
l4 = l3 - l2

if(l1>l2):
    for i in range(0,l2):
        list.append(list2[i])
    if(l3>l2):
        for i in range(0,l2):
            list.append(list2[i])
    else:
        for i in range(0,l3):
            list.append(list2[i])
    if(l4>l2):
        for i in range(0,l2):
            list.append(list2[i])
    else:
        for i in range(0,l4):
            list.append(list2[i])

elif(l1 == l2):
    for i in range(0,l2):
        list.append(list2[i])
    
else:
    for i in range(0,l1):
        list.append(list2[i])
        
print(list)

ct = ""
listindexkw=[]
for i in range(0,l1):
    m = (listM.index(list[i]) + listM.index(list1[i]))%26
    ct = ct + listM[m]
print(ct)

