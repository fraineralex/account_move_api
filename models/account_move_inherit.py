from odoo import models, api
import os

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals_list):
        file_path = os.path.join(os.path.dirname(__file__), 'vals_list.txt')
        with open(file_path, 'w') as file:
            file.write(str(vals_list))
        return super(AccountMove, self).create(vals_list)

    @api.model
    def create_move(self, vals_list):
        for vals in vals_list:
            vals['journal_id'] = self.env['account.journal'].search([('name', '=', vals['journal_id'])], limit=1).id
            vals['currency_id'] = self.env['res.currency'].search([('name', '=', vals['currency_id'])], limit=1).id
          
            line_ids = vals.get('line_ids', [])
            for line in line_ids:
                line_dict = line[2]
                line_dict['partner_id'] = self.env['res.partner'].search([('name', '=', line_dict['partner_id'])], limit=1).id
                line_dict['currency_id'] = self.env['res.currency'].search([('name', '=', line_dict['currency_id'])], limit=1).id
                line_dict['account_id'] = self.env['account.account'].search([('name', '=', line_dict['account_id'])], limit=1).id

            vals['line_ids'] = line_ids

        created_moves = super(AccountMove, self).create(vals_list)

        return created_moves
