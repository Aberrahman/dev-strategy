from odoo import models, fields, api, exceptions


class ProjectMarketType(models.Model):
    _name = 'project.market_type'
    _description = 'Project market types'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
