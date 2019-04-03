#This file is part stock_picking_weight module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from . import shipment

def register():
    Pool.register(
        shipment.ShipmentOutPicking,
        shipment.ShipmentOutScanningStart,
        module='stock_picking_weight', type_='model')
    Pool.register(
        shipment.ShipmentOutPacked,
        shipment.ShipmentOutScanning,
        module='stock_picking_weight', type_='wizard')
