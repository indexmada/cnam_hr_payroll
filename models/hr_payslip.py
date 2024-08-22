# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HRSalaryRule(models.Model):
	_inherit = "hr.salary.rule"

	display_od = fields.Boolean(string = "Afficher dans OD", default = True)