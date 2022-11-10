def matrix(text,size = 5):
    t1 = [list(text[i:i+size]) for i in range(0,len(text),size)]
    t1[-1] += ['']*(size-len(t1[-1]))
    return t1



def encrypt(text):
    mat = matrix(text)
    return "".join([mat[j][i] for i in range(len(mat[0])) for j in range(len(mat))])



pt = input("Enter the plain text:")
print(encrypt(pt))