#iterators and genrators

# def gen():
# 	for i in range(10):
# 		yield i
# a = gen()
# type(a)
# next(a)

# Generator Expression

# list comperhension
# a = [for i in range(5)]
#   print(a)

 #generator expression

# g = (i for i in range(5))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# list(g)


#Generator function
#return from function
# def gen():
# 	for i in range(5):
# 		return i
# print(gen())

#yield for a generator function
#pause function execution
# def gen():
# 	for i in range(5):
# 		yield i
# g = gen()
# print(next(g))
# print(next(g))
# set(g)

# iterable to iterator
#list comprehension
# a = [i for i in range(5)] #container --> itself iterable
# b = iter(a)# b is iterator from iterable a
# print(next(b))
# print(next(b))

# iterator itself is iterable
#generator expression produce generator object
# a = (i for i in range(5)) # a is iterator i.e. generator object itself an iterator
# #iterator is always an iterable
# for i in a:
# 	print(i)
# next(a)

#slicing on iterator

# from itertools import islice
# a = (i for i in range(5))
# s = islice(a, 2)
# for i in s:
# 	print(1)

# print(next(a))
# print(next(a))

#containers:
#iterable:
#iterators:

