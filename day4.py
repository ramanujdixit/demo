# prime number for loop and controlling statement
# num=int(input('enter any number:'))

# isprime=True

# if num<2:
#     print('Prime Number')
# else:
#     for i in range(2,(num//2)+1):
#         if num%i==0:
#             isprime=False

# if isprime:
#     print('Prime Number')
# else:
#     print('Not a prime number')


# reverse a number for while loop practice
# num=int(input('enter any number:'))
# rem=0
# rev_num=0

# while num>0:
#     rem=num%10
#     rev_num=rev_num*10+rem
#     num=num//10
    
# print(rev_num)

# def information(name='Varun', salary=2000):
#     return f"My name is {name} and my salary is {salary}"

# print(information())
# print(information(name='Lal', salary=3500))

# def local_scope():
#     name='Rakul'
#     print(name)

# local_scope()
# print(name)    cannot access it as its scope is local

# def global_scope():
#     global l_name
#     l_name='aaron'
#     print(l_name)
# global_scope()
# print(l_name)       it is accessible as its scope is global


# def outer():
#     a='raj'
    
#     def inner():
#         print(a)      it will be printed as outer scope variable is accessed in inner function
        
#     inner()
# outer()


# def outer():
    # print(a)    it will not printed as its in inner function variable and we are trying to access it in outer function
    
#     def inner():
#         a='raj'
#         print(a)     this will get executed
#     inner()
# outer()


# import os

# print(os.getcwd())

# print(os.listdir())

# os.mkdir('test')
# print(os.listdir())

# os.rmdir('test')
# print(os.listdir())


# *args
# def sum(*args):
#     total=0
#     for i in args:
#         total+=i
#     print(total)
# sum(1,2,3)

# def print_i(*args):
#     print(args)
# print_i(1,2,3,4,5,6,7,8,9,10)

# def get_number(*number):
#     for i in number:
#         print(i)

# get_number(1,2,3)


# **kwargs
# def print_details(**kwargs):
#     print(kwargs)

# print_details(name='lala', age=25)

# def func(**info):
#     return info["name"]

# print(func(name="Ram", age=22))

# def func(a, *args, **kwargs):
#     print(a, args, kwargs)

# func(10, 20, 30, x=40)