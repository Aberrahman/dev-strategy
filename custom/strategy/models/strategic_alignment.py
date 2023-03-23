from odoo import models, fields, api, exceptions


class StrategyAlignment(models.Model):
    _name = 'strategy.alignment'
    _description = 'Alignement stratégique'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    name = fields.Char(required=True, string='Alignement')
    strategy_id = fields.Many2one('strategy.strategy', string='stratégie')
    first_level_id = fields.Many2one('strategy.firstlevel', string='1er Niveau stratégique')
    second_level_id = fields.Many2one('strategy.secondlevel', string='2ème Niveau stratégique')
    third_level_id = fields.Many2one('strategy.thirdlevel', string='3ème Niveau stratégique')
    fourth_level_id = fields.Many2one('strategy.fourthlevel', string='4ème Niveau stratégique')
    project_ids = fields.Many2many('project.project', string='Projets')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('strategy.alignment') or 'New'
        return super(StrategyAlignment, self).create(vals)
