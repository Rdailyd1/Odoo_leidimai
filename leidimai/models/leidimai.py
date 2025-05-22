from odoo import models, fields, api
from datetime import date, timedelta


class Leidimai(models.Model):
    _name = 'leidimai.leidimai'

    _description = 'Lentelė Leidimai'

    route_no = fields.Many2one('leidimai.marsruto_nr', string="Maršruto Nr.")
    route = fields.Many2one('leidimai.marsrutas', string="Maršrutas", required="True")
    departure = fields.Char(string="Išvykimas iš Vilniaus")
    number_of_permits = fields.Integer(string="Leidimų skaičius")
    country = fields.Many2one('leidimai.salis', string="Šalis", required="True")
    permit_no = fields.Char(string="Leidimo Nr.")
    issued = fields.Date(string="Išduotas")
    vezejas_partneris = fields.Selection(
        [('toks_vezejas', "TOKS vežėjas"), ('toks_partneris', "TOKS parneris")],
        string="TOKS vežėjas/TOKS partneris?")
    sent_message90 = fields.Boolean(string="Laiškas išsiųstas prieš 90 d.", default=False)
    sent_message30 = fields.Boolean(string="Laiškas išsiųstas prieš 30 d.", default=False)
    valid_until = fields.Date(string="Galioja iki")
    carrier_ids = fields.Many2many('leidimai.vezejai', string="Vežėjai")
    onbus = fields.Text(string="Autobuse")

    @api.model
    def sent_email_to_res_empl(self, vals):
        today = date.today()
        before_90_days = today + timedelta(days=90)
        before_30_days = today + timedelta(days=30)

        leidimai_records90 = self.env['leidimai.leidimai'].search([
            ('valid_until', '=', before_90_days),
            ('sent_message90', '=', False)
        ])
        leidimai_records30 = self.env['leidimai.leidimai'].search([
            ('valid_until', '=', before_30_days),
            ('sent_message30', '=', False)
        ])

        template = self.env.ref('leidimai.leidimai_mail_template')
        # Siuntimas prieš 90 d.
        if leidimai_records90:
            print('leidimai_records90:', leidimai_records90)
        else:
            print('leidimų nėra90')
        for rec in leidimai_records90:
            if template:
                template.send_mail(rec.id, force_send=True)
                # rec.sent_message = True  # Pažymim, kad išsiųsta

        # Siuntimas prieš 30 d.
        if leidimai_records30:
            print('leidimai_records30:', leidimai_records30)
        else:
            print('leidimų nėra30')
        for rec in leidimai_records30:
            if template:
                template.send_mail(rec.id, force_send=True)
                # rec.sent_message = True  # Pažymim, kad išsiųsta

        return True
