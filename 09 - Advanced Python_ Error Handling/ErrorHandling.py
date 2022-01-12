# error handling:
while True:
    try:
        age = int(input('Please enter your age:'))
        a = 10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('age is > 0')
    else:
        print(age)
    finally:
        print('heloo')
    print('thank you')
# def sum(num1, num2):
#     try:
#         return num1+num2
#     except (ValueError,ZeroDivisionError) as err:
#         print(err)


# print(sum(1,'2'))

# Built-in-Exceptions
# https://docs.python.org/3/library/exceptions.html
