# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Vitpranalyticaccount(models.Model):
    _inherit = "vit.product.request.line"

    def action_create_pr(self):
        res = super(Vitpranalyticaccount, self).action_create_pr()
        for x in self :
            pra = x.env['purchase.requisition.line'].search([('requisition_id.origin','=', x.product_request_id.name)])
            pra.account_analytic_id = x.department_id.analytic_account_id
        return res


class Vitpraccount(models.Model):
    _inherit = "vit.product.request"

    def action_create_pr(self):

        res = super(Vitpraccount, self).create_pr()
        for h in self :
            praa = h.env['purchase.requisition.line'].search([('requisition_id.origin','=', h.product_request_id.name)])
            praa.account_analytic_id = h.department_id.analytic_account_id
        return res