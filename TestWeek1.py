# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:23:37 2021

@author: ilq00444
"""

import unittest
from Assignment2 import *

class TestWeek2(unittest.TestCase):
    def test_calc_sum_one_item(self):
        self.assertEqual(1,calc_sum([1]))
    def test_calc_sum_multiple_items(self):
        self.assertEqual(2, calc_sum([1,1]))
        self.assertEqual(45, calc_sum(range(1,10)))
    def test_calc_mean(self):
        self.assertEqual(5, calc_mean(range(1,10)))
    def test_calc_mean_int(self):
        self.assertEqual(2, calc_mean(range(1,4)))
    def test_calc_mean_float(self):
        self.assertEqual(2.5, calc_mean(range(1,5)))
    def test_std_same_numbers(self):
        self.assertEqual(0, calc_std([1,1,1,1,1]))
    def test_std_range(self):
        self.assertAlmostEqual(2.449489743, calc_std(range(1,9)),)
    def test_calc_sum_one_item_np(self):
        self.assertEqual(1,calc_sum_np(np.array([1])))
    def test_calc_sum_multiple_items_np(self):
        self.assertEqual(2, calc_sum_np(np.array([1,1])))
        self.assertEqual(45, calc_sum_np(np.array(range(1,10))))
    def test_std_same_numbers_np(self):
        self.assertEqual(0, calc_std(np.array([1,1,1,1,1])))
    def test_std_range_np(self):
        self.assertAlmostEqual(2.449489743, calc_std(np.array(range(1,9))),)


# running the tests
unittest.main()