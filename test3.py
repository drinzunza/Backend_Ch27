
def numbers():
    for n in range(1, 21):
        if n is not 11 and n is not 13:
        # if n is not in [11, 13]:
            print(n)


def lowest():
    nums = [12,234,123,56,678,45,7,3,567,2423,56,-2,345,6752,-34,345,0,0,2]
    # find the smallest/min number and print it

    min = nums[0]
    for n in nums:
        if n < min:
            min = n

    print(f"The result is: {min}")



numbers()
lowest()