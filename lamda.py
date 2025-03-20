# Lambda (Anonymous)
'''
def add_numbers(n1,n2,n3):
    return n1+n2+n3

print(add_numbers(10,20,30))
'''

'''add_numbers=lambda n1,n2,n3:n1+n2+n3
print(add_numbers(10,20,30))'''


'''# Take a argument which will be number
#Make a list 0 to N

make_list = lambda n:[i for i in range(0,n+1)]

length = int(input("Enter the length: "))

l1 = make_list(length)
l2 = make_list(15)

print(f"{l1= }")
print(f"{l2= }")'''

'''
# Even return True else False

check_even=lambda num: num % 2 == 0

if check_even(100):
    print("Even")
else:
    print("odd")

'''

check_even=lambda num:print("even") if num % 2 == 0 else print("odd")

check_even(12)
check_even(33)