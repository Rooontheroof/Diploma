import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    bun = MagicMock(spec=Bun)
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_sauce():
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = 'hot sauce'
    ingredient.get_price.return_value = 50
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient


@pytest.fixture
def mock_filling():
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = 'cutlet'
    ingredient.get_price.return_value = 100
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient


@pytest.fixture
def burger_with_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger


class TestBurgerSetBuns:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


class TestBurgerAddIngredient:

    def test_add_ingredient(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        assert mock_sauce in burger_with_bun.ingredients

    def test_add_multiple_ingredients(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        assert len(burger_with_bun.ingredients) == 2


class TestBurgerRemoveIngredient:

    def test_remove_ingredient(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        burger_with_bun.remove_ingredient(0)
        assert mock_sauce not in burger_with_bun.ingredients

    def test_remove_ingredient_reduces_count(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.remove_ingredient(0)
        assert len(burger_with_bun.ingredients) == 0


class TestBurgerMoveIngredient:

    def test_move_ingredient(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        burger_with_bun.move_ingredient(1, 0)
        assert burger_with_bun.ingredients[0] == mock_filling
        assert burger_with_bun.ingredients[1] == mock_sauce


class TestBurgerGetPrice:

    def test_get_price_bun_only(self, burger_with_bun):
        assert burger_with_bun.get_price() == 200

    def test_get_price_with_ingredients(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        assert burger_with_bun.get_price() == 350

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected', [
        (100, [], 200),
        (100, [50], 250),
        (200, [100, 150], 650),
    ])
    def test_get_price_parametrized(self, bun_price, ingredient_prices, expected):
        bun = MagicMock(spec=Bun)
        bun.get_price.return_value = bun_price
        bun.get_name.return_value = 'bun'

        burger = Burger()
        burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = MagicMock(spec=Ingredient)
            ingredient.get_price.return_value = price
            ingredient.get_name.return_value = 'ing'
            ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected


class TestBurgerGetReceipt:

    def test_get_receipt_contains_bun_name(self, burger_with_bun):
        assert 'black bun' in burger_with_bun.get_receipt()

    def test_get_receipt_contains_price(self, burger_with_bun):
        assert 'Price: 200' in burger_with_bun.get_receipt()

    def test_get_receipt_contains_ingredient_name(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        assert 'hot sauce' in burger_with_bun.get_receipt()

    def test_get_receipt_contains_ingredient_type(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        assert 'sauce' in burger_with_bun.get_receipt()

    def test_get_receipt_format(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        receipt = burger_with_bun.get_receipt()

        lines = receipt.split('\n')

        assert lines[0] == '(==== black bun ====)'
        assert '(==== black bun ====)' in lines
