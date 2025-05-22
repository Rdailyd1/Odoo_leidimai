from odoo import models, fields


class Marsrutas(models.Model):
    _name = 'leidimai.marsrutas'
    _description = 'Klasifikatorius Maršrutas'
    _rec_name = 'route_name'

    route_name = fields.Char(string="Maršrutas")