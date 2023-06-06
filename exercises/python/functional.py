## Functional python

# Exercise 10.1
import copy


numLst = [1, 2, 3, 4, 5]

def sumList(list, acc = 0):
    list = copy.copy(list)
    if len(list): 
        return sumList(list, acc + list.pop())
    return acc
        
    
print("1. ", sumList(numLst))
print("2. ", sumList(numLst))

def fun_list_sum_iter(list, iteration = 0, sum = 0):
    if (iteration == len(list)):
        return sum
    return fun_list_sum_iter(list, iteration + 1, sum + list[iteration])

print("iter ", fun_list_sum_iter(numLst))

sumListLambda = lambda list, iter = 0, sum = 0: sum if(iter == len(list)) else sumListLambda(list, iter+1, sum+list[iter])

print("lambda ", sumListLambda(numLst))


# Exercise 10.2 – Recursion

def recursiveFactorial(n, acc = 1):
    if n > 0:
        return recursiveFactorial(n-1, acc*n)
    return acc

print(recursiveFactorial(7))

# 10.2b 

sumOfSquares = lambda a, b: a*a + b*b

print(sumOfSquares(5, 10))


# Exercise 10.3 – Higher-order, lambda

naturalNumbers = [0,1,2,3,4,5,6,7,8,9]
def getEvenNumbers(list):
    return filter(lambda x: x % 2 == 0, list)

print(list(getEvenNumbers(naturalNumbers)))


# Exercise 10.4 – Higher-order, lambda

gtgSales = [
    ('Coffee', 2018, 525.05), 
    ('Juice', 2021, 526.03), 
    ('Apple', 2020, 525.12), 
    ('Green Tea', 2019, 525.02), 
    ('Banana', 2022, 524.08)
]
gtgSales.sort(key=lambda item: item[1])

print(gtgSales)

# without chaning the original list
sortedByPrice = sorted(gtgSales, key=lambda item: item[2])

print(sortedByPrice)
print(gtgSales)
