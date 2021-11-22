from odoo import fields, models, api


class Contacts(models.Model):
    _inherit = 'sale.order'

    def auto_confirm_sale(self):
        orders = self.env['sale.order'].search([('state', '=', 'draft')])
        fil_orders = orders.filtered(lambda x: x.amount_total > 5000)
        for order in fil_orders:
            count = 0
            for line in order.order_line:
                count += 1
            if count <= 3:
                order.action_confirm()
