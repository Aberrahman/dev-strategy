from odoo import models, fields, api, exceptions


class Strategy(models.Model):
    _name = 'strategy.strategy'
    _description = 'Stratégie'

    reference = fields.Char(string='Reference', default='New', readonly=True, required=True)
    strategy_id = fields.Char(required=True, string='ID Stratégie')
    name = fields.Char(required=True, string='Stratégie')
    cost = fields.Monetary(currency_field='currency_id', string='Coût')
    manager_ids = fields.Many2many('hr.employee', string='Responsables')
    currency_id = fields.Many2one('res.currency', string='Devise')
    start_date = fields.Date(string='Date début')
    end_date = fields.Date(string='Date fin')
    description = fields.Html(string='Description')
    tag_ids = fields.Many2many('strategy.tag', string='Étiquettes')
    first_level_ids = fields.One2many('strategy.firstlevel', 'strategy_id', string='1er Niveau stratégique')
    second_level_ids = fields.One2many('strategy.secondlevel', 'strategy_id', string='2ème Niveau stratégique')
    third_level_ids = fields.One2many('strategy.thirdlevel', 'strategy_id', string='3ème Niveau stratégique')
    fourth_level_ids = fields.One2many('strategy.fourthlevel', 'strategy_id', string='4ème Niveau stratégique')
    indicator_ids = fields.One2many('strategy.indicator', 'strategy_id', string='Indicateurs de performance')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise exceptions.ValidationError('Start date must be less than end date!')

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('strategy.strategy') or 'New'
        return super(Strategy, self).create(vals)

