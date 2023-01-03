import pytest
from decimal import Decimal
from coursework2.src.shopping_basket import Basket, Item

@pytest.fixture(scope="function")
def basket():
    yield Basket()

#@pytest.fixture(scope="function")
#def item():
#    yield Item()

@pytest.fixture(scope='function')
def item():
    items = Item(brand_name='Heinz', product_name='Tomato Ketchup', description='Red', price= Decimal(3.5))
    yield items