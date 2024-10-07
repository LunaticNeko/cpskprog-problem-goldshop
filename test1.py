"""

TEST CODE
01219114 Computer Programming
Week 8, Long Program Assignment: Mother Tux's Gold Shop (V1)
(C) 2024 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

from gold import Gold
from random import randint
from random import random
import copy

def test_1a_init():
    g = Gold()
    assert g.markup_add == 0
    g.markup_add = 100
    assert g.markup_add == 100
    assert g.name == "Gold"
    assert g.gold_mass == 0
    assert g.total_mass == 0
    assert Gold("name").name == "name"
    assert Gold("").name == ""
    assert Gold("namename", 100).markup_add == 100

def test_1b_add():
    g = Gold()
    g.add(False, 10)
    assert g.total_mass == 10
    assert g.gold_mass == 0
    g.add(True, 10)
    assert g.total_mass == 20
    assert g.gold_mass == 10

def test_1c_remove():
    g = Gold()
    g.add(False, 10)
    g.add(True, 10)
    r = g.remove(False, 5)
    assert r == 5
    r = g.remove(False, 10)
    assert r == 5
    r = g.remove(True, 5)
    assert r == 5
    r = g.remove(True, 10)
    assert r == 5

def gen_random_gold_pricing():
    g = Gold()
    g.add(False, randint(10, 500))
    g.add(True, randint(100, 1000))
    g.markup_add = 100*randint(1,20)
    return g

def test_1d_price_simple():
    gold_price = 2000
    for i in range(10):
        g = gen_random_gold_pricing()
        assert g.price() == g.gold_mass * gold_price + g.markup_add
        assert g.price(include_markup = False) == g.gold_mass * gold_price

def test_1e_price_floating():
    for i in range(10):
        gold_price = randint(1000, 5000)
        g = gen_random_gold_pricing()
        assert g.price(gold_price) == g.gold_mass * gold_price + g.markup_add
        assert g.price(gold_price, include_markup = False) == g.gold_mass * gold_price

def test_1f_price_adjust():
    for i in range(10):
        gold_price = randint(1000, 5000)
        purity = round(random(), 2)
        g = gen_random_gold_pricing()
        test_price = g.price(gold_price, include_markup = False, force_purity = purity)
        expected_price = int(purity * g.total_mass * gold_price)
        assert test_price == expected_price

def test_1g_purity():
    for i in range(10):
        g = gen_random_gold_pricing()
        test_purity = g.purity()
        expected_purity = round(g.gold_mass / g.total_mass, 4)

def test_1h_eq1():
    for i in range(10):
        g = gen_random_gold_pricing()
        g2 = copy.copy(g)
        assert g2 == g

def test_1i_eq2():
    for i in range(10):
        g = gen_random_gold_pricing()
        g2 = copy.copy(g)
        g2.add(False, 1)
        assert g2 != g

def test_1j_repr():
    for i in range(10):
        g = gen_random_gold_pricing()
        assert repr(g) == f"Gold: {g.name}, {g.gold_mass} g / {g.total_mass} g"

