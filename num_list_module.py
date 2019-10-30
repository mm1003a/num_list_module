
list = [1,2,3,4,5,6,7,8,9]

def Helloworld():
    print('S\'up World, Malachy here')



def backwardslist(array):
    print('Malachy')
    print(array[-1::-1])

def min(array):
    min = array[1]
    print('Malachy')
    for i in array:
        if i <= min:
            min = i
    print(min)

def firsthalfsum(array):
    length_half = len(array)//2
    half_bit = 0.5*(array[length_half])
    sum_half = sum(array[0:length_half]) + half_bit
    print(sum_half)


def divisibleby(array, divisor):
    array2 = []
    for i in array:
        if i % divisor ==0:
            array2.append(i)
    print(array2)

def max(array):
    
    """ Returns the highest number in a list of numbers """

def avg(array):
    """ Returns the average of a list of numbers"""

def suprise():
    """ Create a surprise function for the person that receives your code.
        Feel free to get creative change parameters, print out shapes,  etc.

        """


################################
####    BONUS FUNCTION       ###
################################
def gcd(array):
    """ Returns the greatest common Divisor of a list of numbers """
    """ Greatest Common Divisor is the greatest number that each number in the list is 
        divisible by. 
        EXAMPLE: [500, 50, 20] Greatest Common Divisor = 10
                 [18, 30, 42]  Greatest Common Divisor = 6
                 [33, 66, 99, 101] Greatest Common Divisor = 1
                 
                 """


