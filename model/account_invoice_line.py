from openerp import models, fields, api, _
from openerp.exceptions import except_orm

class account_line_analytic_mandatory(models.Model):
    _inherit = ['account.invoice.line']
    account_analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account', required=True) # Make this field mandatory