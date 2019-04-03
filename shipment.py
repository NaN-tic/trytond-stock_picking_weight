#This file is part stock_picking_weight module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Bool, Eval, Id

__all__ = ['ShipmentOutPicking', 'ShipmentOutPacked',
    'ShipmentOutScanningStart', 'ShipmentOutScanning']


class ShipmentOutPicking:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.picking'
    weight_uom = fields.Many2One('product.uom', 'Weight Uom',
        domain=[('category', '=', Id('product', 'uom_cat_weight'))],
        states={
            'required': Bool(Eval('weight')),
        }, depends=['weight'])
    weight_digits = fields.Function(fields.Integer('Weight Digits'),
        'on_change_with_weight_digits')
    weight = fields.Float('Weight', digits=(16, Eval('weight_digits', 2)),
        depends=['weight_digits'])

    @classmethod
    def default_weight_uom(cls):
        Configuration = Pool().get('stock.configuration')
        config = Configuration(1)
        return config.weight_uom.id if config.weight_uom else None


class ShipmentOutPacked:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.packed'

    def set_shipment(self, shipment):
        shipment = super(ShipmentOutPacked, self).set_shipment(shipment)
        if self.picking.weight:
            shipment.weight_uom = self.picking.weight_uom
            shipment.weight = self.picking.weight
        return shipment


class ShipmentOutScanningStart:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.scanning.start'
    weight_uom = fields.Many2One('product.uom', 'Weight Uom',
        domain=[('category', '=', Id('product', 'uom_cat_weight'))],
        states={
            'required': Bool(Eval('weight')),
        }, depends=['weight'])
    weight_digits = fields.Function(fields.Integer('Weight Digits'),
        'on_change_with_weight_digits')
    weight = fields.Float('Weight', digits=(16, Eval('weight_digits', 2)),
        depends=['weight_digits'])

    @classmethod
    def default_weight_uom(cls):
        Configuration = Pool().get('stock.configuration')
        config = Configuration(1)
        return config.weight_uom.id if config.weight_uom else None


class ShipmentOutScanning:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.scanning'

    def set_shipment(self, shipment):
        shipment = super(ShipmentOutScanning, self).set_shipment(shipment)
        if self.start.weight:
            shipment.weight_uom = self.start.weight_uom
            shipment.weight = self.start.weight
        return shipment
