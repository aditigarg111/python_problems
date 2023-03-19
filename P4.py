# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
def numbers(num1,num2):
    product = num1*num2
    if product <= 1000:
        return product
    else:
        return num1+num2

result =numbers(80,10)
print(result)