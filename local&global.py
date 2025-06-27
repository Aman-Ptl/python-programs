n=1 #global variable

def fn():
    global a
    a=10
    print(a)
    n=5 #local variable
    print("in",n)

fn()

print('out',n)   #global variable