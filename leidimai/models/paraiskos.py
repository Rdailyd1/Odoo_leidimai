from odoo import models, fields


class Paraiskos(models.Model):
    _name = 'leidimai.paraiskos'

    _description = 'Lentelė Paraiškos'

    code = fields.Char(string="Kodas")
    route_name = fields.Char(string="Maršrutas")
    departure_vilnius = fields.Char(string="Išvykimas iš Vilniaus")
    departure_end = fields.Char(string="Išvykimas iš galinio")
    partner_ids = fields.Many2many('leidimai.vezejai', string="Partneriai")
    delivered = fields.Date(string="VKTI Priduota")
    eleven_eur = fields.Boolean(string="VKTI 11.0 eur")
    two_ninty = fields.Boolean(string="VKTI 2.90 eur")
    note = fields.Text(string="Pastaba")

