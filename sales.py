import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    ''' 
    if current_day % 7 != 0 and available_items != None: # If it is not the end of the week and there is still units available
        sales = random.randint(1, 200) # Generates a random amount of sales for each day
        available_items = available_items - sales # Decreases the amount of stock according to the number of sales made
        inventory_tuple = (current_day, sales, 0, available_items)
        inventory_records.append(inventory_tuple) # Adds the inventory sales 
    return available_items