# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import time

class StcReport(models.Model):
    _name = "stc.report"
    _description = "Rapport excel sur solde de tout Compte"

    employee_id = fields.Many2one(string="Employé", comodel_name = "hr.employee")
    contract_id = fields.Many2one(string="Contrat", comodel_name="hr.contract")

    def generate_stc_report(self):
        url = '/web/binary/download_stc_report_file?employee_id='+str(self.employee_id.id) + '&contract_id=' + str(self.contract_id.id)
        actions = {
            'type': 'ir.actions.act_url',
            'target': 'current',
            'url': url,
        }
        return actions