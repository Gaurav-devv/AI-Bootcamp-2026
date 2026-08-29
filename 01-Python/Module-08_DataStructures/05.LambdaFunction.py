#Lambda Function

addition = lambda a,b : a+b

print(addition(12,13))
# odd - even
number = lambda a : "even" if a % 2 == 0 else "odd"
print(number(12))


#Map

a = [1,2,3,4,5]

def double(x):
    return x*2

result = map(double,a)

print(list(result))


#Filter
def even(x):
    if x % 2 ==0:
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9]
result = filter(even,a)
print(list (result))

#or using lambda
a = [1,2,3,4,5,6,7,8,9]
result = filter(lambda x : True if x%2 == 0 else False , a)
print(list(result))