'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def findNumSumUptoK(k, l):

    if not l:
        return False

    for i in range(len(l)-1):
        remaining = abs(l[i] - k)

        if remaining in l:
            print("True")
            return True

    print("False")
    return False

def main():
    k = 17 
    l = [5, 10, 11, 7]

    findNumSumUptoK(k, l)
    

if __name__ == "__main__":
    main()

