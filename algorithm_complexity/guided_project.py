import re

# function used as key to sorted built-in function
# that especify the last column as parameter
def row_price(row):
    return row[-1] 

class Inventory():
    """
    This is a class that receives a csv document,
    specifically containing laptop especifications for a commerce
    * Attributes:
        - Header: It's a list that contains the tittle of all columns,
        indicating the meaning of each element.
        - Rows: It's a list that contains all the characteristics of 
        the laptops.
        - Ids_to_row: It's a dictionary where the ids are keys and rows are
        values .
        - Prices: A list that contains all laptop prices.
        - Rows sorted by price: A list sorted by price.
    
    """
    
    # This function just initiate the class when it's instantiate
    def __init__(self, csv_filename): # N log N + 3N + 7C /// big  O(NlogN), big omega(NlogN), big theta(NlogN)
        self.header = [] # C
        self.rows = [] # C
        self.id_to_row = {} # C
        self.prices = [] # C
        self.read_csv(csv_filename) # 3N+3C
        self.rows_by_price = sorted(self.rows, key=row_price) # Timsort nlog n

    def read_csv(self, csv_filename): # 3N+3C /// big  O(NlogN), big omega(N), big theta(N)
        """
        This function reads the csv file, separates the header from 
        rows.
        Reorganizes the rows into a dictionary with the ids as keys
        and remaining data as values.
        And compiles all laptop prices into a list.
        """
        with open(csv_filename, newline='', encoding='utf-8') as file: # C
            data = csv.reader(file) # C
            self.header = next(data) # C
            self.rows = [row[:-1]+[int(row[-1])] for row in data] # N
            self.id_to_row = {row[0]: row[1:] for row in self.rows} # N
            self.prices = [row[-1] for row in self.rows] # N

    # Search a laptop from the laptop_id using array
    def get_laptop_from_id(self, laptop_id): # 2N+C /// big O(N) big omega(1) big theta(N)
        for row in self.rows: # N
            if row[0] == laptop_id: # worst case N
                return row # C
        return None # C
    
    # Search a laptop from the laptop_id using a dictonary
    def get_laptop_from_id_fast(self, laptop_id): # N + C /// big O(N) big omega(1) big theta(N)
        if laptop_id in self.id_to_row: # worst case N
            return self.id_to_row[laptop_id] # C
        return None # C
    
    
    def check_promotion_dollars(self, dollars): # 3/2 N^2 + 13/2 N +  2C /// big O(N^2) big omega(N^2) big theta(N^2)
        """
        Calculates the possible sums of all laptops by
        summing the value of laptop one with laptop one,
        laptop one with laptop two, laptop one with laptop three,
        and so on. Use a set to ensure that duplicate numbers are not
        included.
        """
                
        possibles_buys = set() # C
        for i in range(len(self.rows)): # N
            price = self.rows[i][-1] # N
            possibles_buys.add(price) # N
            possibles_buys.add(2*price) # N
            
            for j in range(i, len(self.rows)): # N^2 remember it's a sum of AP with N elements starting in N and R is -1  => (N^2+N)/2
                price_2 = self.rows[j][-1] # N^2
                possibles_buys.add(price+price_2) # N^2
                
        if dollars in possibles_buys: # worst case N
            return True # C
        else:
            return False # C
        
    # As the check_promotion_dollars function above but with a fast methodology
    def check_promotion_dollars_fast(self, dollars): # 3N + C /// big O(N) big omega(1) big theta(N)
        if dollars in self.prices: # worst N
            return True # C
        
        for price in self.prices: # N
            if dollars - price in self.prices: # worst case N
                return True # C
        return False # C
    
    def find_laptop_with_price(self, target_price): #  log N + 3 C // big O(log N) big omega(1) big theta(log N)
        """
        This function finds all laptops with a price equal or
        less than the target price.
        """
        range_start = 0 # C
        range_end = len(self.rows_by_price) - 1 # C
        while range_start < range_end: # how it halves the range, the complexity is log N
            range_middle = (range_end + range_start) // 2  
            price = self.rows_by_price[range_middle][-1]
            if price == target_price:                            
                return range_middle+1                   
            elif price < target_price:                           
                range_start = range_middle + 1             
            else:                                          
                range_end = range_middle
        if self.rows_by_price[range_start][-1] <= target_price: # C    
            return -1 # C
        return range_start # C
    
    def find_laptop_between_two_prices(self, min_price, max_price): # N + 2 Log N /// big O(N) big omega(1) big theta(N)
        """
        This function finds all laptops with a price between min price
        and max price.
        """
        range_min = self.find_laptop_with_price(min_price) # log N
        range_max = self.find_laptop_with_price(max_price) # log N
        
        return self.rows_by_price[range_miN : range_max-1] # worst case N
    
    def find_cheapest_specific_laptop(self, desired_ram, desired_hd): # 5N + C /// big O(N) big omega(1) big theta(N)
        """
        Retrieve the memory ram located at index 7 and hd located at
        index 8, take only the numbers and compare with desired specifics,
        how the rows_by_price, the first laptop matches is the cheapest.
        """
        for row in self.rows_by_price: # N
            mem_ram = int(re.sub(r'\D', '', row[7])) # N
            mem_hd = int(re.sub(r'\D', '', row[8])) # N
            if mem_ram == desired_ram: # worst case N
                if mem_hd == desired_hd: # worst case N
                    return row # C
        return -1 # C
