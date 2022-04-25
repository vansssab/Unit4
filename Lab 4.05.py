'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])
​
    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program
    It wont print the first number in the list(for ex: 2, 3, 4, 5, 6 instead of 1, 2, 3, 4, 5, 6 )
    There is no need for the +1 since it wont go any farther then the length of the list.

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program
    There is unneccessary indentation.
    There maybe 2 stars next to each other.

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''
#1
def print_numbers(list):
    for i in range(0, len(list)):
        print(list[i])

num_list = [1, 2, 3, 4, 5, 6]
print_numbers(num_list)



#2
def swapping_stars():
    line_str = ""
    for line in range(0, 6):
        for char in range(0,6):
            if line % 1 == char % 2:
                    line_str += "*"
            else:
                    line_str += "-"
    print(line_str)

swapping_stars()

#Which one
option = input("Which function would you like to run? ('print numbers' or 'swapping stars') ")
if option == 'print numbers':
   num_list = [1, 2, 3, 4, 5, 6]
   print_numbers(num_list)
elif option == 'swapping stars':
    swapping_stars()
else:
    print("That is not an option. Try again.")
