import pytest
from decimal import Decimal
from coursework2.src.shopping_basket import Item, Basket

"""
def test_item(item):
    
    GIVEN 
    WHEN
    THEN
    
    assert item.brand_name == "Heinz"
    assert item.product_name == "Tomato Ketchup"
    assert item.description == "Red"
    assert item.price == Decimal(3.98)
"""

# Tests of the methods in Basket class
def test_basket(basket, item):
    # Test the add_item method
    basket.add_item(item, 4) # must add 4 items to the basket
    assert basket.items[item] == 4 # number of items in the basket must be 4

    # Test the update_item method
    basket.update_item(item, 5) #updates the quantity of items in the basket to 5
    assert basket.items[item] == 5 # number of items in the basket must be updated to 5

    # Test the remove_item method
    basket.remove_item(item, 2) # must remove 2 items from the basket
    assert basket.items[item] == 3 # number of items in the basket must be reduced to 3

    # Test the view method
    basket.view()  # Prints contents of the basket including quantity, price and total cost.

    # Test the get_total_cost method
    assert basket.get_total_cost() == Decimal(10.5)  # Total cost of the basket must be 11.94

    # Test the reset method
    basket.reset() # reset/empty the basket
    assert len(basket.items) == 0  # Content of the basket must be emptied / reduced to 0

    # Test the is_empty method
    assert basket.is_empty() == True  # Basket should now be empty

   # i1 = Item("Warburtons", "Toastie", "800g white sliced loaf", '1.52')
   # i2 = Item("Flora", "Buttery", "Buttery spread", '0.89')
   # basket = Basket()
   # basket_items