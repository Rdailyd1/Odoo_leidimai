from odoo import models, fields


class Marsruto_nr(models.Model):
    _name = 'leidimai.marsruto_nr'
    _description = 'Klasifikatorius Maršruto Nr.'
    _rec_name = 'route_no'

    route_no = fields.Char(string="Maršruto Nr.")
