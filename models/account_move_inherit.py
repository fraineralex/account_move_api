from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create_from_dict(self, vals_list):
        for vals in vals_list:
            vals['journal_id'] = self.env['account.journal'].search([('name', '=', vals['journal_id'])], limit=1).id
            vals['company_id'] = self.env['res.company'].search([('name', '=', vals['company_id'])], limit=1).id
            vals['partner_id'] = self.env['res.partner'].search([('name', '=', vals['partner_id'])], limit=1).id
            vals['currency_id'] = self.env['res.currency'].search([('name', '=', vals['currency_id'])], limit=1).id
          
            move_lines = vals.get('invoice_line_ids', [])
            for line in move_lines:
                line_dict = line[2]
                line_dict['partner_id'] = self.env['res.partner'].search([('name', '=', line_dict['partner_id'])], limit=1).id
                line_dict['currency_id'] = self.env['res.currency'].search([('name', '=', line_dict['currency_id'])], limit=1).id
                if line_dict['product_id']:
                    line_dict['name'] = line_dict['product_id']
                    line_dict['product_id'] = self.env['product.product'].search([('name', '=', line_dict['product_id'])]).id
                    line_dict['product_uom_id'] = self.env['uom.uom'].search([('name', '=', line_dict['product_uom_id'])]).id

                tax_lines = line_dict.get('tax_ids', [])
                for index, tax in enumerate(tax_lines[0][2]):
                  tax_lines[0][2][index] = self.env['account.tax'].search([('name', '=', tax)], limit=1).id

                line_dict['tax_ids'] = tax_lines


            vals['invoice_line_ids'] = move_lines

        created_moves = super(AccountMove, self).create(vals_list)

        return created_moves
