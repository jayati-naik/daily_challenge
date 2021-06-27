def main():
    
    l = [1, 2, 3, 4, 5]

    o = list()

    product = 1
    for i in l:
        product *= i

    for i in range(len(l)):
        o.append(product//l[i])

    print(o)

    return o


if __name__ == "__main__":
    main()
