# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    end_customer = fields.Many2one('res.partner', string="End Customer")
