# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import time

class OdReport(models.Model):
    _name = "od.report"
    _description = "Od Report"

    start_date = fields.Date(string="Start Date", default=datetime.datetime.now(), required=True)
    end_date = fields.Date(string="End Date", default=datetime.datetime.now(), required=True)
    month_year = fields.Char(string="Mois de", compute="_compute_month_year")

    def generate_od_report(self):
        sd = self.start_date
        ed = self.end_date
        start_date_str = str(sd.day)+'-'+str(sd.month)+'-'+str(sd.year)
        end_date_str = str(ed.day)+'-'+str(ed.month)+'-'+str(ed.year)
        actions = {
            'type': 'ir.actions.act_url',
            'target': 'current',
            'url': '/web/binary/download_od_report_file?start_date='
                   + start_date_str
                   + '&end_date='
                   + end_date_str
                   + '&month_year='
                   + str(self.month_year)

        }
        return actions

    def _compute_month_year(self):
        for record in self:
            m = record.start_date.month
            y = record.start_date.year

            str_month = ['0','Janv', 'Fév', 'Mar', 'Avr', 'Mei', 'Juin', 'Jul', 'Août', 'Sept', 'Oct', 'Nov', 'Déc']

            result = str_month[m] + ' '+ str(y)
            record.month_year = result