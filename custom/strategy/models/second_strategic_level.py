from odoo import models, fields, api, exceptions


class SecondStrategicLevel(models.Model):
    _name = 'strategy.secondlevel'
    _description = '2ème Niveau stratégique'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    name = fields.Char(required=True, string='Nom')
    level_id = fields.Char(required=True, string='ID 2ème Niveau')
    managers = fields.Many2many('hr.employee', string='Responsables')
    departments = fields.Many2many('hr.department', string='Départements')
    strategy_id = fields.Many2one('strategy.strategy', string='stratégie')
    first_level_id = fields.Many2one('strategy.firstlevel', string='1er Niveau stratégique')
    cost = fields.Monetary(string='Coût')
    currency_id = fields.Many2one('res.currency', string='Devise')
    tag_ids = fields.Many2many('strategy.tag', string='Étiquettes')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('strategy.secondlevel') or 'New'
        return super(SecondStrategicLevel, self).create(vals)

