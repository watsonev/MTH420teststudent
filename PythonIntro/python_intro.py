# python_intro.py
"""Python Essentials: Introduction to Python.
Evan Watson
MTH-420
1-8-21
"""
def sphere_volume(r):
    """Returns the volume of a sphere with radius r"""
    return (4 / 3) * 3.14159 * r ** 3
	
def isolate(a,b,c,d,e):
    return str(a)+"     "+str(b)+"     "+str(c)+" "+str(d)+" "+str(e)+"\n"
	
from math import floor
def first_half(string):
    length = int(floor(len(string)/2))
    return string[:length]
def backward(string):
    return string[::-1]

def list_ops():
    list.append("eagle")
    list[2] = "fox"
    list.remove(list[1])
    list.sort(reverse=True)
    list[list.index("eagle")] = "hawk"
    list[len(list)-1] = list[len(list)-1]+"hunter"
	
def pig_latin_v(input):
    return input+"hay"

def pig_latin_c(input):
    return input[1:]+input[0]+"ay"


def pig_latin(input):
    if input[:1] in vowels:
        return pig_latin_v(input)
    else:
        return pig_latin_c(input)
		
def palindrome(p):
    i = 10**(p-1)
    maximum = 0
    while i < (10**p):
        j = 10**(p-1)
        while j < (10**p):
            product = i*j
            if str(product) == str(product)[::-1]:
                if product > maximum:
                    maximum = product
            j = j + 1
        i = i + 1
    return maximum
	
def alt_harmonic(n):
    i = 1
    sum = 0
    while i < n + 1:
        value_i = ((-1)**(i+1))/i
        sum = sum + value_i
        i = i + 1
    return sum	

if __name__ == "__main__":
    print(sphere_volume(3))
	print(isolate(1,2,3,4,5)
    print(first_half("lemon"))
    print(backward("potato"))
	list_ops()
	print(list)
	print(pig_latin("applesauce"))
    print(palindrome(3))
    print(alt_harmonic(500000))
	
