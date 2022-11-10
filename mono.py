pt = input("Enter the plain text:")
str = pt.upper()
l = len(pt)
key = int(input("Enter the key:"))
list = []
for i in str:
    if(i==" "):
        list.append(i)
    elif(i=="!" or i=="@" or i=="#" or i=="$" or i=="%" or i=="&" or i=="*" or i=="(" or i==")"):
        list.append(i)
    else:
        m = (ord(i)+key-65)%26
        list.append(chr(m+65))
print(list)
str1 = ""
for i in list:
    str1 = str1 + i
print("Encrypted part:"+str1)

list1 = []
for i in str1:
    if(i==" "):
        list1.append(i)
    elif(i=="!" or i=="@" or i=="#" or i=="$" or i=="%" or i=="&" or i=="*" or i=="(" or i==")"):
        list1.append(i)
    else:
        m = (ord(i)-key+65)%26
        list1.append(chr(m+65))
print(list1)
str2 = ""
for i in list1:
    str2 = str2 + i
print("Decrypted part:"+str2)