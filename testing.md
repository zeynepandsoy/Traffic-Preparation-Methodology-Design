.F.F...FF
======================================================================
FAIL: test_repr (test_shopping_basket.TestItem)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 18, in test_repr
    self.assertEqual(repr(item), "Brand, Product, Description, 10.50")
AssertionError: ' Brand, Product, Description, 10.50' != 'Brand, Product, Description, 10.50'
-  Brand, Product, Description, 10.50
? -
+ Brand, Product, Description, 10.50


======================================================================
FAIL: test_get_total_cost (test_shopping_basket.TestBasket)
GIVEN 2 items with positive quantity
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 100, in test_get_total_cost
    self.assertEqual(self.basket.get_total_cost(), Decimal("81.00"))
AssertionError: Decimal('72.50') != Decimal('81.00')

======================================================================
FAIL: test_update_item (test_shopping_basket.TestBasket)
GIVEN 1 item with positive and 1 item with negative quantity
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 70, in test_update_item
    self.assertEqual(self.basket.items, {self.item1: 5, self.item2: 2})
AssertionError: { Bra[18 chars]cription1, 10.50: 2,  Brand2, Product2, Description2, 20.50: 2} != { Bra[18 chars]cription1, 10.50: 5,  Brand2, Product2, Description2, 20.50: 2}
- { Brand1, Product1, Description1, 10.50: 2,
?                                          ^

+ { Brand1, Product1, Description1, 10.50: 5,
?                                          ^

    Brand2, Product2, Description2, 20.50: 2}

======================================================================
FAIL: test_view (test_shopping_basket.TestBasket)
GIVEN 2 items with positive quantity
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 89, in test_view
    self.assertEqual(self.basket.view(), {self.item1: 3, self.item2: 2})
AssertionError: None != { Brand1, Product1, Description1, 10.50: [40 chars]0: 2}

----------------------------------------------------------------------
Ran 9 tests in 0.003s

FAILED (failures=4)
