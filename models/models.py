# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class rsh_account(models.Model):
#     _name = 'rsh_account.rsh_account'
#     _description = 'rsh_account.rsh_account'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_categ = fields.Many2one('product.category', related='product_id.categ_id', readonly=True, store=True, string='Category', help="Product Category")

