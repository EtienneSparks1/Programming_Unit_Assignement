def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
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


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''

    if current_day == 0:
        available_items = 2000 
        inventory_tuple = (current_day, 0, 2000, 2000) # Sets a base for the stock of units at the start
        inventory_records.append(inventory_tuple) # Adds inventory_tuple to the list of inventory records
    elif current_day % 7 == 0: # If the current day is a Sunday
        inventory_tuple = (current_day, 0, 2000 - available_items, 2000) # adds a row in the list for each restock at the end of the week, calculates what needs to be restocked based on sales
        inventory_records.append(inventory_tuple) # adds inventory_tuple to the inventory report
    return available_items