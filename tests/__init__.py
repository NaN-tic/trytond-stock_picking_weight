#This file is part stock_picking_weight module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

try:
    from trytond.modules.stock_picking_weight.tests.test_stock_picking_weight import suite
except ImportError:
    from .test_stock_picking_weight import suite

__all__ = ['suite']
