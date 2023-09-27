# Studying Algorithmic Time Complexity in the Guided Project

I will analyse each function in the worst case, $O$, (or the upper bound limit of a function), the better case, $\Omega$ (or the lower bound limit) and the mean case, $\Theta$ (limiting for upper and lower bounds).

Here I just analyse for function in general, the details can be read in [guided_project](https://github.com/juliofreire/ADS2/blob/main/algorithm_complexity/guided_project.py) file. Also, I used $C$ to a constant to execute one line, keep in mind all the lines have differents constants, but to simplify I just used C.

## Constructor Function: \__init__

In this function it always apply a timsort algorithm to organize the data in crescent price, because that it's become a $\Theta (N log N)$ complexity time algorithm.

## Function: read_csv

This function does not interfer in general way, once this function is called one time and just in the constructor, but it contributes with $3N+C$. In worst and better case the time complexity is $N$, so
$\Theta(N)$.

## Function: get_laptop_from_id

In this function the worst case is if the ID's laptop is the last one, so the function have to go throug all the list to find it and the better case is if the ID's laptop is the first one, therefore $O(N)$ and $\Omega(1)$, so the mean complexity is $\Theta(N)$.

## Function: get_laptop_from_id_fast

This works same with get_laptop_from_id, but the function the determines the velocity is more fast than the above. However, analyses a complexity time just takes the slowest function into account, thus $O(N)$, $\Omega(1)$ and $\Theta(N)$, for the same reason.


## Function: check_promotion_dollars

Independent of the worst or better case, it will execute the lines with the quadratic polynomial order, so $O(N^2)$, $\Omega(N^2)$ and $\Theta(N^2)$,

## Function: check_promotion_dollars_fast

This function works by searching an ID in a dictonary, and its complexity can be $O(N)$, $\Omega(1)$ and $\Theta(N)$. This depends on how the dictionary maps id into keys.

## Function: find_laptop_with_price

This function employs a well-known m called binary search that has the $O(log N)$, $\Omega(1)$ and $\Theta(logN)$.

## Function: find_laptop_between_two_prices

It calls the previous function twice to find the index is near the price inputed, after that print the rows between the ranges of the index found. The first part has complexity time equals doubled the complexity the function above, the second one has, in the worst case, to print all the list and otherwise, in better, print just one value. Thereforte the complexity time of all function is the sum, resulting in $O(N)$, $\Omega(1)$ and $\Theta(N)$.

## Function: find_cheapest_specific_laptop

To find the cheapest laptop with specifics, it's has two options, the laptop is the first at the list or the last, this is the better and worst case, so its time complexity is $O(N)$, $\Omega(1)$ and $\Theta(N)$.
