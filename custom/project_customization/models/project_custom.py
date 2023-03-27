from odoo import models, fields, api, exceptions


class ProjectCustom(models.Model):
    _inherit = 'project.project'

    prerequisite = fields.Char(string='Prérequis')
    impacts = fields.Char(string='Impacts')
    risks = fields.Char(string='Risques')
    remarks = fields.Char(string='Remarques')
    department_id = fields.Many2one('hr.department', string='Département')
    handling_type = fields.Selection(
        [('PAA', 'Plan d’achat annuel (PAA)'), ('PPM', 'Plan de Passation de Marche (PPM)')],
        string='Type de passation')
    funding_mode_ids = fields.Many2many('project.funding_mode', string='Modes de financement')
    market_type_ids = fields.Many2many('project.market_type', string='Types de marché')
    handling_mode_ids = fields.Many2many('project.handling_mode', string='Modes de passation')
    budget = fields.Monetary(currency_field='currency_id', string='Coût du projet')
    sponsor_ids = fields.Many2many('res.partner', string='Porteurs de projet')
    alignment_ids = fields.Many2many('strategy.alignment', string='Alignemnts strategiques')
    calculated_achievement = fields.Float(string='Avancement calculé', readonly=True,
                                          compute='_compute_calculated_achievement', store=True, tracking=True)

    @api.depends('task_ids.weighted_achievement')
    def _compute_calculated_achievement(self):
        for record in self:
            if record.task_ids:
                record.calculated_achievement = sum(record.task_ids.mapped('weighted_achievement'))
            else:
                record.calculated_achievement = 0.0
