
def find_max(Arr):
    my_max = Arr[0]
    for i in range(1, len(Arr)):
        if Arr[i] > my_max:
            my_max = Arr[i]
    return my_max

print ("Hello world!")
print (find_max([-1, 2, 10, 4, 5]))