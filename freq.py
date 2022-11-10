pt = input("Enter the plain text:")
l = len(pt)
set1 = set()
for i in pt:
    set1.add(i)
print(set1)

list = list(set1)
print(list)

for i in range(0,len(list)):
    m = pt.count(list[i])
    print("Frequency of letter "+list[i]+":")
    print((m/l)*100)