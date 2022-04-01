'''
Do Now 4.02

1. In your console
Type the following code
    for i in range(0, 10):
        print(i)
In your notebook
Respond to the following
Write down what the range function does. 
    #prints the numbers one by one starting at 0 and ending at 9.

2. In your console
Type the following
    a_list = ['apple', 'orange', 'pear', 'strawberry', 'grape']
    print(len(a_list))
    print(list(range(0, len(a_list)))
Continue in your notebook
Write down what range(0, len(a_list)) does.
    #prints the number of items of the list from 0 to 4. (5 items)

3. In your console
Use the range and len functions to make a for loop that prints the elements of a_list, one at a time.
'''
#1
for i in range(0, 10):
    print(i)

#2
a_list = ['apple', 'orange', 'pear', 'strawberry', 'grape']
print(len(a_list))
print(list(range(0, len(a_list))))

#3
list = ['apple', 'orange', 'pear', 'strawberry', 'grape', 'peaches']

for i in range(0, len(list)):
    print(list[i])