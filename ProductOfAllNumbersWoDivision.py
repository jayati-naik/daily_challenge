'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

def main():
    
    l = [1, 2, 3, 4, 5]
    list_size = len(l)
    o = list()

    for_dict = dict()
    back_dict = dict()

    prev = 1
    prev_last = 1

    # Two nested for loops O(n^2)
    # Can we do soemthing with lesst hen O(n^2)
    for i in range(list_size):
        prev *= l[i]

        if list_size - i >= 0:
            print(list_size-i)
            prev_last *= l[list_size-1 - i]

        for_dict[l[i]] = prev
        back_dict[l[list_size-1 - i]] = prev_last

    for j in range(list_size):
        if j-1 >= 0:
            prev_product = for_dict[l[j-1]]
        else:
            prev_product = 1
        if j+1 < list_size:
            next_product = back_dict[l[j+1]]
        else:
            next_product = 1
        print(j)
        o.append(prev_product * next_product)

    return o


if __name__ == "__main__":
    main()
