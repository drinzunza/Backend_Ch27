#### Lists
from mock_data import mock_catalog



def test_1():
    print("basic python lists")

    nums = [1,2,3,89,56,3456,1234,123,435]

    # read
    print(nums[0])
    print(nums[3])

    # add 
    nums.append(42)
    nums.append(-1)

    # remove by element
    nums.remove(56)

    # remove by index
    del nums[0]

    print(nums)



    # loop
    for n in nums:
        print(n)




def test_2():
    print("Sum numbers")

    prices = [12.23,345,123.2,542,65,123.2,0.223,-23, 123.2,6,171,5678]


    # for and print every number
    # q1 - print the sum of all number
    # q2 - find the cheapest product
    # q3 - find the most expensive product

    total = 0
    cheapest = prices[0]
    most_expensive = prices[0]
    for num in prices:
        total += num

        # compare
        if num < cheapest:
            cheapest = num


        if num > most_expensive:
            most_expensive = num

    print(total)
    print(f"The cheapest price is: {cheapest}")
    print(f"The most expensive price is: {most_expensive}")



def test_3():
    print("cheapest product")

    # for print every dict/prod from mock_catalog
    # print only the title of every product
    solution = mock_catalog[0]
    for prod in mock_catalog:
        if prod["price"] < solution["price"]:
            solution = prod


    # The cheapest product is: TITLE - $Price
    print(f"The cheapest product is: {solution['title']} - ${solution['price']}")

# call
#test_1()
#test_2()
test_3()