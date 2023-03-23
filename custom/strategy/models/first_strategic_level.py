from odoo import models, fields, api, exceptions


class FirstStrategicLevel(models.Model):
    _name = 'strategy.firstlevel'
    _description = '1er Niveau stratégique'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    name = fields.Char(required=True, string='Nom')
    level_id = fields.Char(required=True, string='ID 1er Niveau')
    managers = fields.Many2many('hr.employee', string='Responsables')
    departments = fields.Many2many('hr.department', string='Départements')
    strategy_id = fields.Many2one('strategy.strategy', string='stratégie')
    cost = fields.Monetary(string='Coût')
    currency_id = fields.Many2one('res.currency', string='Devise')
    tag_ids = fields.Many2many('strategy.tag', string='Étiquettes')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('strategy.firstlevel') or 'New'
        return super(FirstStrategicLevel, self).create(vals)
