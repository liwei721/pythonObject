import sys
# import fileA
# from fileA import *

def methodB():
	print('fileB.py methodB........')

if __name__ == '__main__':
	methodB()
	# fileA.testA()
	# fileA.__testAAA()
	print(globals())
	print(locals())