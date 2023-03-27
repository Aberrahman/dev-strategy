from odoo import models, fields

class ProjectPartner(models.Model):
    _name = 'project.partner'

    project_id = fields.Many2one('project.project', string='Project')
    partner_id = fields.Many2one('res.partner', string='Partner')
