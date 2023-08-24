from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create_move(self, vals_list):
        """
        Create accounting moves based on provided values and perform validations.
        """
        error_messages = self.move_validations(vals_list)
        if error_messages:
            return {'error': error_messages}

        for vals in vals_list:
            company = self.env['res.company'].search(
                [('name', '=', vals['company_id'])], limit=1)
            if company:
                vals['company_id'] = company.id
            else:
                return {'error': "Company not found"}

            journal = self.env['account.journal'].search(
                [('name', '=', vals['journal_id']), ('company_id', '=', company.id)], limit=1)
            if journal:
                vals['journal_id'] = journal.id
            else:
                return {'error': "Journal not found"}

            currency = self.env['res.currency'].search(
                [('name', '=', vals['currency_id'])], limit=1)
            if currency:
                vals['currency_id'] = currency.id
            else:
                return {'error': "Currency not found"}

            line_ids = vals.get('line_ids', [])
            for line in line_ids:
                line_dict = line[2]
                partner = self.env['res.partner'].search(
                    [('name', '=', line_dict['partner_id'])], limit=1)
                if partner:
                    line_dict['partner_id'] = partner.id
                else:
                    return {'error': "Partner not found"}

                line_currency = self.env['res.currency'].search(
                    [('name', '=', line_dict['currency_id'])], limit=1)
                if line_currency:
                    line_dict['currency_id'] = line_currency.id
                else: # if currency not found, set it to company currency
                    line_dict['currency_id'] = company.currency_id.id                                           

                account = self.env['account.account'].search(
                    [('name', '=', line_dict['account_id']), ('company_id', '=', company.id)], limit=1)
                if account:
                    line_dict['account_id'] = account.id
                else:
                    return {'error': "Account not found"}

            vals['line_ids'] = line_ids

        created_moves = super(AccountMove, self).create(vals_list)

        return created_moves

    def move_validations(self, vals_list):
        """
        Perform validations on provided values before creating accounting moves.
        """
        error_messages = []
        for vals in vals_list:
            if not vals.get('journal_id'):
                error_messages.append("Invalid field 'journal_id'")
            if not vals.get('currency_id'):
                error_messages.append("Invalid field 'currency_id'")
            if not vals.get('company_id'):
                error_messages.append("Invalid field 'company_id'")
            if not vals.get('line_ids'):
                error_messages.append("move lines are required")
            else:
                line_ids = vals.get('line_ids', [])
                for line in line_ids:
                    if not line[2].get('partner_id'):
                        error_messages.append(
                            "Invalid field 'partner_id' in the move line")
                    if not line[2].get('currency_id'):
                        error_messages.append(
                            "Invalid field 'currency_id' in the move line")
                    if not line[2].get('account_id'):
                        error_messages.append(
                            "Invalid field 'account_id' in the move line")
                    if not line[2].get('debit') and line[2].get('debit') != 0.0:
                        error_messages.append(
                            "Invalid field 'debit' in the move line")
                    if not line[2].get('credit') and line[2].get('credit') != 0.0:
                        error_messages.append(
                            "Invalid field 'credit' in the move line")

        return error_messages
