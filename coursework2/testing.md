# Results of the unit tests

### Note: As instead of pytest, unittest is used no fixtures are created (although in conftest.py within docstrings I have provided the fixtures that I have initially created through pytest - but instead decided to use the appropriate version setUp() to build the common function)

.F.F...FF
======================================================================
FAIL: test_repr (test_shopping_basket.TestItem)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 60, in test_repr
    self.assertEqual(repr(item), "Brand, Product, Description, 10.50")
AssertionError: ' Brand, Product, Description, 10.50' != 'Brand, Product, Description, 10.50'
-  Brand, Product, Description, 10.50
? -
+ Brand, Product, Description, 10.50


======================================================================
FAIL: test_get_total_cost (test_shopping_basket.TestBasket)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 110, in test_get_total_cost
    self.assertEqual(self.basket.get_total_cost(), Decimal("81.00"))
AssertionError: Decimal('72.50') != Decimal('81.00')

======================================================================
FAIL: test_update_item (test_shopping_basket.TestBasket)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 92, in test_update_item
    self.assertEqual(self.basket.items, {self.item1: 5, self.item2: 2})
AssertionError: { Bra[18 chars]cription1, 10.50: 2,  Brand2, Product2, Description2, 20.50: 2} != { Bra[18 chars]cription1, 10.50: 5,  Brand2, Product2, Description2, 20.50: 2}
  { Brand2, Product2, Description2, 20.50: 2,
-   Brand1, Product1, Description1, 10.50: 2}
?                                          ^

+   Brand1, Product1, Description1, 10.50: 5}
?                                          ^


======================================================================
FAIL: test_view (test_shopping_basket.TestBasket)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zeynepandsoy/comp0035 - cw2/comp0035-cw-i-zeynepandsoy/coursework2/test/test_shopping_basket.py", line 105, in test_view
    self.assertEqual(self.basket.view(), {self.item1: 3, self.item2: 2})
AssertionError: None != { Brand1, Product1, Description1, 10.50: [40 chars]0: 2}

----------------------------------------------------------------------
Ran 9 tests in 0.006s

FAILED (failures=4)

## 9 unit tests ran, 5 tests PASSED and 4 tests FAILED

# Code Coverage
<img width="339" alt="Screenshot 2023-01-04 at 16 01 02" src="https://user-images.githubusercontent.com/115081167/210562312-0c622e1c-5600-438b-9d1f-42a43c5d9a36.png">

