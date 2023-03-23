from odoo import models, fields, api, exceptions
from dateutil import relativedelta


class ThirdStrategicLevel(models.Model):
    _name = 'strategy.thirdlevel'
    _description = '3ème Niveau stratégique'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    name = fields.Char(required=True, string='Nom')
    level_id = fields.Char(required=True, string='ID 3ème Niveau')
    managers = fields.Many2many('hr.employee', string='Responsables')
    departments = fields.Many2many('hr.department', string='Départements')
    strategy_id = fields.Many2one('strategy.strategy', string='stratégie')
    first_level_id = fields.Many2one('strategy.firstlevel', string='1er Niveau stratégique')
    second_level_id = fields.Many2one('strategy.secondlevel', string='2ème Niveau stratégique')
    cost = fields.Monetary(string='Coût')
    currency_id = fields.Many2one('res.currency', string='Devise')
    tag_ids = fields.Many2many('strategy.tag', string='Étiquettes')
    maturity_level = fields.Selection(
        [('Moyen', 'Moyen'), ('Faible', 'Faible'), ('Elevée', 'Elevée'), ('En exécution', 'En exécution')], string='Niveau de maturité')
    type = fields.Selection([('Strategic', 'Strategic'), ('Quick Win', 'Quick Win')], string='Type')
    start_date = fields.Date(string='Date début')
    end_date = fields.Date(string='Date fin')
    duration = fields.Float(string='Durée(mois)', compute='_compute_duration', store=True)

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                delta = relativedelta.relativedelta(record.end_date, record.start_date)
                record.duration = delta.years * 12 + delta.months
            else:
                record.duration = 0.0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise exceptions.ValidationError('Start date must be less than end date!')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('strategy.thirdlevel') or 'New'
        return super(ThirdStrategicLevel, self).create(vals)

