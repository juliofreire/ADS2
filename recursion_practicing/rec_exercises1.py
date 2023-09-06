def list_len(lst):

    # base case: that doesnt allow to call infinites 
    # times the functions
    if not lst:
        return 0
    
    lenght = 1 + list_len(lst[1:])
    return lenght

fruits = ["apple", "orange", "pear", "fig", "passionfruit"]

num_fruits = list_len(fruits)

print(num_fruits)
