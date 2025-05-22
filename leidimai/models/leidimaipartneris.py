from odoo import models, fields


class Leidimai_Partneris(models.Model):
    _name = 'leidimai.leidimaipartneris'

    _description = 'Lentelė Leidimai_Partneris'

    route_no = fields.Many2one('leidimai.marsruto_nr', string="Maršruto Nr.")
    route = fields.Many2one('leidimai.marsrutas', string="Maršrutas", required="True")
    departure = fields.Char(string="Išvykimas iš Vilniaus")
    number_of_permits = fields.Integer(string="Leidimų skaičius")
    country = fields.Many2one('leidimai.salis', string="Šalis", required="True")
    permit_no = fields.Char(string="Leidimo Nr.")
    issued = fields.Date(string="Išduotas")
    valid_until = fields.Date(string="Galioja iki")
    carrier_ids = fields.Many2many('leidimai.vezejai', string="Vežėjai")
    note = fields.Text(string="Pastaba")
