.F.F...FF
======================================================================
FAIL: test_repr (__main__.TestItem)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 61, in test_repr
    self.assertEqual(repr(item), "Brand, Product, Description, 10.50")
AssertionError: ' Brand, Product, Description, 10.50' != 'Brand, Product, Description, 10.50'
-  Brand, Product, Description, 10.50
? -
+ Brand, Product, Description, 10.50


======================================================================
FAIL: test_get_total_cost (__main__.TestBasket)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 112, in test_get_total_cost
    self.assertEqual(self.basket.get_total_cost(), Decimal("81.00"))
AssertionError: Decimal('72.50') != Decimal('81.00')

======================================================================
FAIL: test_update_item (__main__.TestBasket)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 94, in test_update_item
    self.assertEqual(self.basket.items, {self.item1: 5, self.item2: 2})
AssertionError: { H&M, t-shirt, white, 10.50: 2,  Zara, Pants, blue, 20.50: 2} != { H&M, t-shirt, white, 10.50: 5,  Zara, Pants, blue, 20.50: 2}
- { H&M, t-shirt, white, 10.50: 2,  Zara, Pants, blue, 20.50: 2}
?                               ^

+ { H&M, t-shirt, white, 10.50: 5,  Zara, Pants, blue, 20.50: 2}
?                               ^


======================================================================
FAIL: test_view (__main__.TestBasket)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 107, in test_view
    self.assertEqual(self.basket.view(), {self.item1: 3, self.item2: 2})
AssertionError: None != { H&M, t-shirt, white, 10.50: 3,  Zara, Pants, blue, 20.50: 2}

----------------------------------------------------------------------
Ran 9 tests in 0.003s

FAILED (failures=4)
