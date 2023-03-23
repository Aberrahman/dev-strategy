from odoo import models, fields, api, exceptions


class IndicatorCategory(models.Model):
    _name = 'indicator.category'
    _description = 'Catégorie de l\'indicateur'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    name = fields.Char(required=True, string='Catégorie')
    description = fields.Char(string='Description')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('indicator.category') or 'New'
        return super(IndicatorCategory, self).create(vals)