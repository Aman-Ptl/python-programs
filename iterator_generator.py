#iterator


list=[1,2,3,4,5]
iteration=iter(list)
print(iteration.__next__())


#GENERATOR

def fn():
    yield 1
    yield 2
    yield 3
values = fn()
print(values.__next__())


for i in  values:
    print(i)


# NEW GENERATOR FOR SQUARE

def square():
    n=1
    while n<=5:
        sq=n**2
        yield sq
        n=n+1
values=square()
for i in values:
    print(i)