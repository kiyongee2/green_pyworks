import myfunctions
from myfunctions import mypow, print_string

# import myfunctions 인 경우
value1 = myfunctions.mypow(3, 4)
print(value1)

myfunctions.print_string('hello')
myfunctions.print_string('hello', 2)

# from myfunctions import mypow, print_string 인 경우
value2 = mypow(3, 4)
print(value1)

print_string('hello')
print_string('hello', 2)
