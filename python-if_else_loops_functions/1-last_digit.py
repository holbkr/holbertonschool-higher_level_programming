#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit=abs(number)%10
<<<<<<< HEAD

if number<0:
    last_digit = last_digit*-1

=======
>>>>>>> 19f664480b7ce4a10ae87f8e0058fef56d1e53e3
if last_digit > 5:
    msg="and is greater than 5"
elif last_digit ==0:
    msg="and is 0"
else:
    msg="and is less than 6 and not 0"

<<<<<<< HEAD

print(f"Last digit of {number} is {last_digit} {msg}")
=======
print("Last digit of",number,"is",last_digit,msg)

>>>>>>> 19f664480b7ce4a10ae87f8e0058fef56d1e53e3
