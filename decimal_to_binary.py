result = 0
# This is where we will store the modulus / reminder of division by 2
open_list = []
# This is an open list where we will append the result 

#Define the function
def binary_function(n):
    # n must be greater than 0 at all times
    if n > 0:
        # result is the reminder of n divide by 2
        result = n % 2
        # append the reminder in the open_list
        open_list.append(result)
        # we need to create a recursive function to pass the absolute of n divide 2
        return binary_function(n // 2)
    open_list.reverse()
    # reverse the contents of open_list.
    for i in open_list:
        print(int(i), end="")
        # this helps to arrange the result horizontally

print(binary_function(1000))
# call the function
