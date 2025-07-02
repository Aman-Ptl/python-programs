# FILTER
# filter(function, iterable)

ans = list(filter(lambda a: a%2==0 and a%10==0, range(1,100)))
print(ans)