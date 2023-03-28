# Write a user defined function to find out the key with prime
# numbers.
# Note:
# ● If the start or end number is negative, then display the message "Invalid range".
# ● If there are no prime numbers between the starting and ending range, then display the
# message "There are no prime numbers in this range".
# ● If the start and end numbers are the same, then display the message "There are no prime
# numbers in this range".
# ● If the start number is greater than the end number, then display the message "Invalid
# range".
# ● The function definition should be : find_prime(start,end) - This function should take start
# and end numbers as parameters and return the prime numbers as a list.

# function for checking prime number
def is_prime(num):
    if num == 1:
        return False
    elif num > 1:
    # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False
    

def find_prime(start,end):
    if start < 0 or end < 0:
        print("Invalid range")
    elif start == end:
        print("There are no prime numbers in this range")
    elif start > end:
        print("Invalid range")
    else:
        prime_numbers = []
        for i in range(start,end+1):
            if is_prime(i):
                prime_numbers.append(i)
        if len(prime_numbers) == 0:
            print("There are no prime numbers in this range")
        return prime_numbers
    
print(find_prime(20,20))
            
    
    

