'''
Do Now 4.01

1. In your console
Type the following Code
    single_fruit = ['apple', 'banana', 'watermelon', 'grape']
    multi_fruit = []
    multi_fruit.append(single_fruit[0] + 's')
    multi_fruit.append(single_fruit[1] + 's')
    multi_fruit.append(single_fruit[2] + 's')
    multi_fruit.append(single_fruit[3] + 's')
    print(multi_fruit)

In your notebook
Respond to the following
Briefly write down what happened. What would happen if you added 100 items to the list single_fruit? 
Write down how you would update multi_fruit.
    The append function added and 's' to each index of the list.  So, when the list is printed again, the items in the list appear to be plural.
    I would add a loop to add 100 items to single_fruit.
2. In your console
Type the following
    list_of_numbers = [3, 5, 10, 23]
    for num in list_of_numbers:
        print(f"num is " + {num})
        
Continue in your notebook
Respond to the following
Briefly write down what happened. How would this change if you added 100 items to list_of_numbers?
    It looped through the list one at a time. It would print 100 statements at a time.
3. In your console
Rewrite the code from part 1 using knowledge from part 2.
'''
