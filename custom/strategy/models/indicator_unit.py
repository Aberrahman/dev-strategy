from odoo import models, fields, api, exceptions


class IndicatorUnit(models.Model):
    _name = 'indicator.unit'
    _description = 'Unité de mesure de l\'indicateur'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    name = fields.Char(required=True, string='Unité')
    description = fields.Char(string='Description')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('indicator.unit') or 'New'
        return super(IndicatorUnit, self).create(vals)