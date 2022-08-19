# find the sum of all numbers divisible by 3 or 5 below 1000

# user input of the lower and upper bound
maximum = input('What is the upper limit?')
minimum = input('What is the lower limit?')

# test input validation
try:
    i_maximum = int(maximum)
    i_minimum = int(minimum)
except TypeError:
    print('Please enter valid numbers')
    exit()

# variable
div_nums = None
# finding numbers
for nums in range(i_minimum, i_maximum):
    if nums % 3 == 0 or nums % 5 == 0:
        if div_nums is None:
            div_nums = nums
        else:
            div_nums = div_nums + nums

# print
print('sum:', div_nums)
