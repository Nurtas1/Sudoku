import sys

print('Введите N')
N=int(sys.stdin.readline())
print('Введите число i и координату по x в формате: i1,x1;i2,x2')
st=sys.stdin.readline()
st=st.rstip()
s1=st.split(';')
lst=[]
for i in range(0,len(s1)):
    lst[i]=s1[i].split(',')[0]
lst=[x]
# g
def f1(lst,N):
    unq=None
    for i in range(1,N+2):
        if i not in lst:
            unq=i
            break
    return unq


for i in range(0,N):
    lst.append(f1(lst,N))
print(lst)
