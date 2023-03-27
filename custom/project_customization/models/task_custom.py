from odoo import models, fields, api, exceptions


class TaskCustom(models.Model):
    _inherit = 'project.task'

    weight = fields.Float(string='Pondération', store=True, tracking=True, required=True)
    achievement = fields.Float(string='Avancement', store=True, tracking=True)
    weighted_achievement = fields.Float(string='Avancement pondérée', readonly=True,
                                        compute='_compute_weighted_achievement', store=True, tracking=True)

    @api.depends('weight', 'achievement')
    def _compute_weighted_achievement(self):
        for record in self:
            if record.weight and record.achievement:
                record.weighted_achievement = record.weight * record.achievement
            else:
                record.weighted_achievement = 0.0
