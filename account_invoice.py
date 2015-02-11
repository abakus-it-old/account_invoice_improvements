from openerp import models, fields, api

class account_next_sequence(models.Model):
    _inherit = ['account.invoice']
    next_number = fields.Char(compute='_compute_next_number',string="Next invoice number", store=False)
    
    @api.depends('journal_id')
    def _compute_next_number(self):
        if self.state in ("","draft"):
            nn_int = self.journal_id.sequence_id.number_next
            nn_string = str(nn_int)
            
            #new API does not work!
            #nn_ex_string = self.env['account.invoice'].search([['journal_id','=',self.journal_id.id],['number', '!=', '']], limit=1).number
            
            #own old api integration
            cr = self.env.cr
            uid = self.env.user.id
            obj = self.pool.get('account.invoice')
            invoice_id = obj.search(cr, uid, [('journal_id','=',self.journal_id.id),('number', '!=', '')])
            
            nn_ex_string = ""
            if invoice_id:
                nn_ex_string = (obj.browse(cr, uid, invoice_id[0]))[0].number#len(invoice_id)-1
            
            l = len(nn_ex_string)-1
            if l > 0:
                cpt = 0;
                for i in range(l,0,-1):
                    if nn_ex_string[i].isnumeric():
                        cpt+=1
                    else:
                        break
                seq = int(nn_ex_string[-cpt:])+1
                nn = nn_ex_string[:-cpt]
                self.next_number = nn + str(seq)
            else:
                self.next_number = '1'
        else:
            self.next_number = ""
    
    @api.onchange('supplier_invoice_number')
    def update_reference(self):
        self.reference = self.supplier_invoice_number
