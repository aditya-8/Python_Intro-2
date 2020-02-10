Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
>>> c=b=e=f=0
>>> for i in str:
	if (i=='A'):
	 c=c+1
	if (i=='C'):
	 b=b+1
	if (i=='G'):
	 e=e+1
	if (i=='T'):
	 f=f+1

	 
>>> print("A =",+c)
A = 20
>>> print("C =",+b)
C = 12
>>> print("G =",+e)
G = 17
>>> print("T =",+f)
T = 21
>>> 