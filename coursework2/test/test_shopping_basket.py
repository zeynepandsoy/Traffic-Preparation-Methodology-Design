"""
import pytest
from decimal import Decimal
from coursework2.src.shopping_basket import Item, Basket


def test_update_item():
    
    GIVEN an item with positive quantity and an item with negative quantity
    WHEN the items are passed to update_item function
    THEN the result is apple item is removed and pear items quantity is increased by 1
   

 # i1 = Item("Warburtons", "Toastie", "800g white sliced loaf", '1.52')
   # i2 = Item("Flora", "Buttery", "Buttery spread", '0.89')
   # basket = Basket()
   # basket_items

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
"""
import unittest
from decimal import Decimal
from shopping_basket import Item, Basket

class TestItem(unittest.TestCase):  #Create a TestItem class extending the class unittest.TestCase
    def test_init(self):   # the method test_init accepts self as an argument
        item = Item("Brand", "Product", "Description", Decimal("10.50"))
        self.assertEqual(item.brand_name, "Brand")
        self.assertEqual(item.product_name, "Product")
        self.assertEqual(item.description, "Description")
        self.assertEqual(item.price, Decimal("10.50"))

    def test_repr(self):
        item = Item("Brand", "Product", "Description", Decimal("10.50"))
        self.assertEqual(repr(item), "Brand, Product, Description, 10.50")

class TestBasket(unittest.TestCase):  #Create a TestBasket class extending the class unittest.TestCase
    def setUp(self):
        self.item1 = Item("Brand1", "Product1",
                          "Description1", Decimal("10.50"))
        self.item2 = Item("Brand2", "Product2",
                          "Description2", Decimal("20.50"))
        self.basket = Basket()

    def test_add_item(self):
        self.basket.add_item(self.item1)
        self.assertEqual(self.basket.items, {self.item1: 1})
        self.basket.add_item(self.item1, 3)
        self.assertEqual(self.basket.items, {self.item1: 4})
        self.basket.add_item(self.item2, 2)
        self.assertEqual(self.basket.items, {self.item1: 4, self.item2: 2})

    def test_remove_item(self):
        self.basket.add_item(self.item1, 3)
        self.basket.add_item(self.item2, 2)
        self.basket.remove_item(self.item1)
        self.assertEqual(self.basket.items, {self.item2: 2})
        self.basket.remove_item(self.item2, 1)
        self.assertEqual(self.basket.items, {self.item2: 1})
        self.basket.remove_item(self.item2, 1)
        self.assertEqual(self.basket.items, {})

    def test_update_item(self):
        self.basket.add_item(self.item1, 3)
        self.basket.add_item(self.item2, 2)
        self.basket.update_item(self.item1, 2)
        self.assertEqual(self.basket.items, {self.item1: 5, self.item2: 2})
        self.basket.update_item(self.item1, -2)
        self.assertEqual(self.basket.items, {self.item1: 3, self.item2: 2})
        self.basket.update_item(self.item1, -5)
        self.assertEqual(self.basket.items, {self.item1: 0, self.item2: 2})
        self.basket.update_item(self.item1, -1)
        self.assertEqual(self.basket.items, {self.item2: 2})
        self.basket.update_item(self.item1, 1)
        self.assertEqual(self.basket.items, {self.item1: 1, self.item2: 2})

    def test_view(self):
        self.basket.add_item(self.item1, 3)
        self.basket.add_item(self.item2, 2)
        self.assertEqual(self.basket.view(), {self.item1: 3, self.item2: 2})

    def test_get_total_cost(self):
        self.basket.add_item(self.item1, 3)
        self.basket.add_item(self.item2, 2)
        self.assertEqual(self.basket.get_total_cost(), Decimal("81.00"))

    def test_reset(self):
        self.basket.add_item(self.item1, 3)
        self.basket.add_item(self.item2, 2)
        self.basket.reset()
        self.assertEqual(self.basket.items, {})
        self.assertFalse(self.basket.checkout)

    def test_is_empty(self):
        self.assertTrue(self.basket.is_empty())
        self.basket.add_item(self.item1, 3)
        self.assertFalse(self.basket.is_empty())
        self.basket.reset()
        self.assertTrue(self.basket.is_empty())


suite = unittest.TestSuite() #create a test suite from the the classes TestItem and TestBasket
suite.addTest(unittest.makeSuite(TestItem))
suite.addTest(unittest.makeSuite(TestBasket))

with open("testing.md", "w") as f:
    runner = unittest.TextTestRunner(stream=f)
    # Run the tests and redirect the output to the file
    res = runner.run(suite)

#if __name__ == '__main__':
#    unittest.main()