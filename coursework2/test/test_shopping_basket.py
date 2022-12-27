import pytest
from decimal import Decimal
from coursework2.src.shopping_basket import Item, Basket

# Test Item class
def test_item(item):
    """
    GIVEN 
    WHEN
    THEN
    """
    assert item.brand_name == "Heinz"
    assert item.product_name == "Tomato Ketchup"
    assert item.description == "Red"
    assert item.price == Decimal(3.98)

# Test  Basket class
def test_basket(basket, item):
    # Test the add_item method
    basket.add_item(item, 2)
    assert basket.items[item] == 2

    # Test the remove_item method
    basket.remove_item(item, 1)
    assert basket.items[item] == 1

   # i1 = Item("Warburtons", "Toastie", "800g white sliced loaf", '1.52')
   # i2 = Item("Flora", "Buttery", "Buttery spread", '0.89')
   # basket = Basket()
   # basket_items