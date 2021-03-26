from math import log2 
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

f1 = open("f1.txt", "r")
text1=f1.read()
t1=text1.split(" ")
f2 = open("f2.txt", "r")
text2=f2.read()
t2=text2.split(" ")
f3 = open("f3.txt", "r")
text3=f3.read()
t3=text3.split(" ")
f1.close()
f2.close()
f3.close()

voca=set(t1+t2+t3)
vocab=list()
for word in list(voca):
    if word not in en_stops:
        vocab.append(word)
print(vocab)

enc=[]

for word in vocab:
    f1=[]
    f2=[]
    f3=[]
    st=0
    print(word, end=" : ")
    while text1.find(word,st)!=-1:
        st=text1.find(word)
        f2.append(st)
        st+=1
    st=0
    while text2.find(word,st)!=-1:
        st=text2.find(word)
        f2.append(st)
        st+=1
    st=0
    while text3.find(word,st)!=-1:
        st=text3.find(word)
        f3.append(st)
        st+=1
    if len(f1)>0:
        print("file1:",end=" ")
        print("freq: "+str(len(f1)),end=" ")
        for num in f1:
            print(num,end=" ")
        print()
    if len(f2)>0:
        print("file2:",end=" ")
        print("freq: "+str(len(f2)),end=" ")
        for num in f2:
            print(num,end=" ")
        print()
    if len(f3)>0:
        print("file3:",end=" ")
        print("freq: "+str(len(f3)),end=" ")
        for num in f3:
            print(num,end=" ")
        print()
    enc+=f1+f2+f3
enc=list(set(enc))

# Encoding
def Elias_Gamma(num):
    l = bin(int(log2(num))).replace('0b','')
    code='0'*(len(l)-1)
    code+=l
    bnum=bin(num).replace('0b','')
    code+=bnum[1:]
    return code

def Var_byte(num):
    num=bin(num).replace("0b", "")
    ind=len(num)%7 
    code='0'*(7-ind)
    s=0
    e=ind
    while e<len(num):
        code+=num[s:e]
        if ind<len(num):
            code+='1'
        else:
            code+='0'
        s=e
        e+=7
    code+=num[s:e]
    code+='0'
    return code

for num in enc:
    if num>0:
        print("Elias Gamma encoding of "+str(num) +" : "+ str(Elias_Gamma(num)))
        print("Variable Byte encoding of "+str(num)+" : "+ str(Var_byte(num)))
