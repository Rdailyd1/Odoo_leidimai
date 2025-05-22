from odoo import models, fields


class Šalis(models.Model):
    _name = 'leidimai.salis'
    _rec_name = 'country'

    _description = 'Klasifikatorius Šalis'

    country = fields.Char(string="Šalis")
