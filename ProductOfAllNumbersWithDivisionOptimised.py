'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''
import math

def main():
    
    l = [1, 2, 3, 4]
    list_size = len(l)
    o = list()

    for_dict = dict()
    back_dict = dict()

    prev = 1
    prev_last = 1

    # Two nested for loops O(n^2)
    # Can we do soemthing with lesst hen O(n^2)
    # WE reduced TC to O(n/2 + n) => O(n) and SC to O(n) from O(2n)
    # but we have to use division here
    for i in range(math.ceil(list_size/2)):
        prev *= l[i]

        if list_size - i >= 0:
            prev_last *= l[list_size-1 - i]

        for_dict[l[i]] = prev
        back_dict[l[list_size-1 - i]] = prev_last

    o.append(1)
    
    for j in range(1, list_size):
        # Calculating product for last element
        if j == list_size-1:
            product = ( o[1] // l[list_size-1] ) * l[1]
            o.append(product)
            break

        prev_product = for_dict[l[j-1]]
        next_product = back_dict[l[j+1]]

        o.append(prev_product * next_product)
    
    # Calculate product for first element
    last_product = o[list_size-1]
    first_product = (last_product * l[list_size-1] )// l[0]

    o[0] = first_product
    
    print(o)
    return o


if __name__ == "__main__":
    main()
