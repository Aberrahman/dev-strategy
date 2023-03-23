from odoo import models, fields, api, exceptions


class PerformanceIndicator(models.Model):
    _name = 'strategy.indicator'
    _description = 'Indicateurs de performance'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    name = fields.Char(required=True, string='Indicateur')
    strategy_id = fields.Many2one('strategy.strategy', string='stratégie')
    first_level_id = fields.Many2one('strategy.firstlevel', string='1er Niveau stratégique')
    second_level_id = fields.Many2one('strategy.secondlevel', string='2ème Niveau stratégique')
    third_level_id = fields.Many2one('strategy.thirdlevel', string='3ème Niveau stratégique')
    fourth_level_id = fields.Many2one('strategy.fourthlevel', string='4ème Niveau stratégique')
    category_id = fields.Many2one('indicator.category', string='Catégorie')
    date = fields.Date(string='Date')
    target_value = fields.Float(string='Valeur cible')
    real_value = fields.Float(string='Valeur réelle')
    uom_id = fields.Many2one('indicator.unit', string='Unité de mesure')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('strategy.indicator') or 'New'
        return super(PerformanceIndicator, self).create(vals)
