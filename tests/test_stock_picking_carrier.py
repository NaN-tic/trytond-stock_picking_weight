# This file is part of the stock_picking_weight module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockPickingWeightTestCase(ModuleTestCase):
    'Test Stock Picking Weight module'
    module = 'stock_picking_weight'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockPickingWeightTestCase))
    return suite
