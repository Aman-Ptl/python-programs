def add(i,j):
    return i+j
def call(i,j):
    return add(i,j)
def pas(i,j,Fn):
    return Fn(i,j)
res=pas(3,4,call)
print(res)