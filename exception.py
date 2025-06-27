try:
    a=2
    b=0
    print(a/b)
except ZeroDivisionError:
    print('there is zero division error')
finally:
    print('continue with the following code')