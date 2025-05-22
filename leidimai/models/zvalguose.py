from odoo import models, fields


class Zvalguose(models.Model):
    _name = 'leidimai.zvalguose'

    _description = 'Lentelė Žvalguose'

    route_no = fields.Char(string="Maršruto Nr.")
    route_name = fields.Char(string="Maršrutas")
    country = fields.Many2one('leidimai.salis', string="Šalis", required="True")
    permit_no = fields.Char(string="Leidimo Nr.")
    issued = fields.Date(string="Išduotas")
    valid_until = fields.Date(string="Galioja iki")
