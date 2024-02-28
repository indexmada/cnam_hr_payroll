# -*- coding: utf-8 -*-

import base64
import xlsxwriter as xlsxwriter

from odoo import http
from odoo.http import request

import io
from ast import literal_eval

from datetime import date,datetime

MONTH_LIST = [('0', '0'), ('1','Janvier'), ('2', 'Février'), ('3', 'Mars'), ('4', 'Avril'), ('5', 'Mei'), ('6', 'Juin'), 
                ('7', 'Juillet'),('8', 'Août'), ('9','Septembre'), ('10','Octobre'), ('11','Novembre'), ('12','Décembre')]

class StcReportControllers(http.Controller):

    @http.route('/web/binary/download_stc_report_file', auth='public')
    def  download_stc_report_file(self, employee_id, contract_id):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)

        employee = request.env['hr.employee'].sudo().browse(int(employee_id))
        contract = request.env['hr.contract'].sudo().browse(int(contract_id))

        self.report_excel_stc(workbook, employee, contract)
        workbook.close()
        output.seek(0)

        file_name = "SOLDE_DE_TOUT_COMPTE"+".xlsx"

        xlsheader = [('Content-Type', 'application/octet-stream'),
                     ('Content-Disposition', 'attachment; filename=%s;' % file_name)]
        return request.make_response(output, xlsheader)

    def report_excel_stc(self, workbook, employee, contract):
        left_12 = workbook.add_format({
            'align': 'left',
            'valign': 'vcenter',
            "font_size": 12,
            })
        center_12 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 12,
            })
        left_12_bold = workbook.add_format({
            'align': 'left',
            'valign': 'vcenter',
            "font_size": 12,
            "bold": True,
            "underline": True,
            })
        center_12_bold = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 12,
            "bold": True,
            "underline": True,
            })

        worksheet_ost = workbook.add_worksheet(employee.name)
        self.style(worksheet_ost)

        logo_image = io.BytesIO(base64.b64decode(request.env.company.logo))
        worksheet_ost.insert_image('A1', "image.png", {'image_data': logo_image,'x_scale': 1.30,'y_scale':1.30})

        worksheet_ost.write("A10", "Maison des produits 6ème Etage-67ha", left_12)
        worksheet_ost.write("A11", "Antananarivo 101", left_12)

        worksheet_ost.merge_range("A13:F13", "ETAT DE SOLDE DE TOUT COMPTE", center_12_bold)
        worksheet_ost.write("A15", "NOMS ET PRENOMS ", left_12)
        worksheet_ost.write("B15",  employee.name,center_12_bold)
        worksheet_ost.write("A16", "NUMERO MATRICULE", left_12)
        worksheet_ost.write("B16", employee.matricule, center_12_bold)
        worksheet_ost.write("A17", "FONCTION", left_12)
        worksheet_ost.write("B17", contract.job_id.name, center_12_bold)
        worksheet_ost.write("A18", "DATE DE PRISE EN SERVICE", left_12)
        worksheet_ost.write("B18", str(contract.date_start), center_12_bold)
        worksheet_ost.write("A19", "DATE DE DEPART", left_12)
        worksheet_ost.write("B19", str(contract.date_end), center_12_bold)

        worksheet_ost.write("A22", "I) - LES ELEMENTS POSITIFS", left_12_bold)

        payslip_id = request.env['hr.payslip'].sudo().search([('employee_id', '=', employee.id), ('contract_id', '=', contract.id), ('stc', '=', True)], order='id DESC', limit=1)

        if not payslip_id:
            return 0

        month_list = MONTH_LIST

        if payslip_id:
            val = "Salaire du mois de "+ month_list[payslip_id.date_from.month][1] +" "+str(payslip_id.date_from.year)
        worksheet_ost.write("A23", val, left_12)

        worksheet_ost.write("A25", "Salaire de base X NB de jours", center_12_bold)
        worksheet_ost.write("A26", "30", center_12)

        # Calcul Montant A
        sba = payslip_id.line_ids.filtered(lambda line: line.code == 'SBA').total if payslip_id else contract.wage
        nb_jours = contract.date_end.day
        amount_a = sba * nb_jours /30
        worksheet_ost.write("B25", amount_a, center_12_bold)

        # Indemnités Diverses
        worksheet_ost.write("A28", "Indemnités Diverses", left_12)

        amount_b = payslip_id.line_ids.filtered(lambda line: line.code == 'DVR').total if payslip_id else 0
        worksheet_ost.write("B28", amount_b, center_12_bold)

        worksheet_ost.write("A30", "////", left_12)

        # Congé
        worksheet_ost.write("A31", "Situation de congé ( en jour)", left_12)
        worksheet_ost.write("A32", "Congé pris", left_12)
        worksheet_ost.write("B32", employee.allocation_used_display, left_12)

        solde_conge = employee.allocation_count - employee.allocation_used_count
        worksheet_ost.write("A33", "Solde de congé", left_12)
        worksheet_ost.write("B33", solde_conge, left_12)

        worksheet_ost.write("A35", "Salaire brut x Solde congé ", center_12_bold)
        worksheet_ost.write("A36", "30", center_12)

        # Montant C
        sbr = payslip_id.line_ids.filtered(lambda line: line.code == 'SBR').total if payslip_id else contract.wage

        amount_c = sbr * solde_conge / 30
        worksheet_ost.write("B35", amount_c, center_12_bold)

        worksheet_ost.write("A38", "TOTAL DES ELEMENTS POSITIFS ", left_12_bold)
        # Total des éléments positifs
        el_positifs = amount_a + amount_b + amount_c
        worksheet_ost.write("B38", el_positifs, center_12_bold)

        # ELEMENTS NEGATIFS

        worksheet_ost.write("A41", "II) - LES ELEMENTS NEGATIFS", left_12_bold)

        worksheet_ost.write("A42", "CNaPS 1%", left_12)
        cnaps = payslip_id.line_ids.filtered(lambda line: line.code == 'CNAPS').total if payslip_id else 0
        worksheet_ost.write("B42",cnaps, center_12_bold)

        worksheet_ost.write("A43", "OSTIE 1% ou OSIEF 2% ou OMSI 1,5%", left_12)
        ostie = payslip_id.line_ids.filtered(lambda line: line.code == 'OSTIE').total if payslip_id else 0
        osief = payslip_id.line_ids.filtered(lambda line: line.code == 'OSIEF').total if payslip_id else 0
        omsi = payslip_id.line_ids.filtered(lambda line: line.code == 'OMSI').total if payslip_id else 0

        ost = ostie or osief or omsi

        worksheet_ost.write("B43", str(ost), center_12_bold)

        worksheet_ost.write("A44", "IRSA", left_12)
        irsa = payslip_id.line_ids.filtered(lambda line: line.code == 'IRSA').total if payslip_id else 0
        worksheet_ost.write("B44", irsa, center_12_bold)

        worksheet_ost.write("A45", "AVANCE ET ACOMPTE", left_12)
        avs = payslip_id.line_ids.filtered(lambda line: line.code == 'AVS').total if payslip_id else 0
        worksheet_ost.write("B45", avs, center_12_bold)

        worksheet_ost.write("A47", "TOTAL DES ELEMENTS NEGATIFS ", left_12_bold)

        el_negatifs = cnaps + ost + irsa + avs
        worksheet_ost.write("B47", el_negatifs, center_12_bold)

        worksheet_ost.write("A50", "NET A PAYER ", left_12_bold)
        net_a_payer = abs(el_positifs - el_negatifs)
        worksheet_ost.write("B50", net_a_payer, center_12_bold)

        # Montant en lettre
        amount_text = payslip_id.currency_id.with_context(lang='fr_FR').amount_to_text(net_a_payer)

        worksheet_ost.write("A53", "Arrêté le présent état à la somme de : "+amount_text, left_12)
        d = date.today()
        date_str = str(d.day) +' '+month_list[d.month][1]+' '+str(d.year)

        worksheet_ost.write("B55", "Antananarivo , le "+date_str, left_12_bold)
        worksheet_ost.write("B58", "Le Directeur ", center_12_bold)
        worksheet_ost.write("B63", "Jocelyn RASOANAIVO", center_12_bold)

    def style(self, worksheet):
        worksheet.set_column('A:A', 35)
        worksheet.set_column('B:B', 20)
        worksheet.set_column("C:M", 8)