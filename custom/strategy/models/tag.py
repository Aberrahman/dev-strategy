from odoo import models, fields, api, exceptions


class StrategyTag(models.Model):
    _name = 'strategy.tag'
    _description = 'Étiquettes de stratégie'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    name = fields.Char(required=True, string='Étiquette')
    description = fields.Char(string='Description')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('strategy.tag') or 'New'
        return super(StrategyTag, self).create(vals)