# def outer_function(message):
#     def inner_function():
#         print(message)
#     return inner_function
#
# mihail_tell_about_day_function = outer_function('Good')
#
# mihail_tell_about_day_function()

# @decorators
# def func()
#     pass
#
# def decorated(func):
#     pass

# def my_decorator(func):
#     def wrapper():
#         print('Wrapper before function')
#         func()
#         print('Wrapper after function')
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print('hello world')
#
# say_hello = my_decorator(say_hello)
# say_hello()

# def decorator_with_arg(arg1, arg2):
#     def actual_decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f'Decorator take arguments {arg1} and {arg2}')
#             func(*args, **kwargs)
#         return wrapper
#     return actual_decorator
#
# @decorator_with_arg("Nihao", 3.141592)
# def my_func():
#     print("Function is done!")
#
# my_func()

# import functools
#
# def decorator_with_arg(command):
#     """Dec params"""
#     init_dict = {}
#     def actual_decorator(func):
#         """Actual decorator"""
#         @functools.wraps(func)
#         def wrapper():
#             """Wrapper"""
#             # print(f"Decorator take arguments: {arg1}, {arg2}")
#             init_dict[command] = func
#             # func()
#         return wrapper
#     return actual_decorator
#
# @decorator_with_arg(command="start")
# def my_func():
#     """Main func"""
#     print("Function is done!")
#     # print(args)
#     # print(kwargs)
#
# # my_func()
#
# print(my_func.__name__)
# print(my_func.__doc__)

# import functools
# import time
# import datetime
# import random
#
# def simple_logger_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Call function: {func.__name__}.")
#         result = func(*args, **kwargs)
#         print(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Function: {func.__name__} end processing.")
#         return result
#     return wrapper
#
# @simple_logger_decorator
# def add_number(digit1, digit2):
#     print(f"Add two digits: {digit1} + {digit2}")
#     return digit1 + digit2
#
# @simple_logger_decorator
# def sub_number(digit1, digit2):
#     print(f"Sub two digits: {digit1} - {digit2}")
#     return digit1 - digit2
#
# print(add_number(37, 73))
# print(30 * "-")
# print(sub_number(102, 45))
