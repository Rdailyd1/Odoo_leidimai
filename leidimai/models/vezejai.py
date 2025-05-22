from odoo import models, fields


class Vezejai(models.Model):
    _name = 'leidimai.vezejai'
    _description = 'Klasifikatorius Vežėjai'
    _rec_name = 'carrier_name'

    carrier_name = fields.Char(string="Vežėjas")
