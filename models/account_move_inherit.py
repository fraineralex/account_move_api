from odoo import models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create_from_dict(self, vals_list):
        for vals in vals_list:
          vals['journal_id'] = self.env['account.journal'].search([('name', '=', vals['journal_id'])]).id
          vals['company_id'] = self.env['res.company'].search([('name', '=', vals['company_id'])]).id
          vals['partner_id'] = self.env['res.partner'].search([('name', '=', vals['partner_id'])]).id
          vals['currency_id'] = self.env['res.currency'].search([('name', '=', vals['currency_id'])]).id
          
          move_lines = vals.get('invoice_line_ids', [])
          for line in move_lines:
              line_dict = line[2]
              #line['product_id'] = self.env['product.product'].search([('name', '=', line['product_id'])]).id
              line_dict['partner_id'] = self.env['res.partner'].search([('name', '=', line_dict['partner_id'])]).id
              line_dict['currency_id'] = self.env['res.currency'].search([('name', '=', line_dict['currency_id'])]).id
          
          vals['invoice_line_ids'] = move_lines
        
        created_moves = super(AccountMove, self).create(vals_list)
        
        return created_moves