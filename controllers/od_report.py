# -*- coding: utf-8 -*-

import io
from ast import literal_eval

import xlsxwriter as xlsxwriter

from odoo import http
from odoo.http import request

from datetime import date,datetime

class ExportOdReportController(http.Controller):

    @http.route('/web/binary/download_od_report_file', type='http', auth="public")
    def download_od_report_file(self, start_date, end_date, month_year):  

        filename = "od_report-"+str(date.today())+".xlsx"
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)

        self.report_excel_od(workbook, start_date, end_date, month_year)  
        workbook.close()
        output.seek(0)
        xlsheader = [('Content-Type', 'application/octet-stream'),
                     ('Content-Disposition', 'attachment; filename=%s;' % filename)]
        return request.make_response(output, xlsheader)

    def report_excel_od(self, workbook, start_date, end_date, month_year):
        worksheet_ost = workbook.add_worksheet("DNS")
        self.style(worksheet_ost)

        # Style
        g_14_center = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 14,
            "bold": True,
            })
        gi_12_center = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 12,
            "bold": True,
            "italic": True,
            })

        cell_g_10_center = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
                'bold': True,
                'border': 1,
            })
        g_10_right = workbook.add_format({
                'align': 'right',
                'valign': 'vright',
                'font_size': 10,
                'bold': True,
            })
        simple_10_center = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
            })
        simple_10_left = workbook.add_format({
                'align': 'left',
                'valign': 'vleft',
                'font_size': 10,
            })
        g_10_right_b = workbook.add_format({
                'align': 'right',
                'valign': 'vright',
                'bottom': 1,
                'bottom_color': 'black',
                'font_size': 10,
                'bold': True,
            })

        cell_g_10_center_tlb = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
                'bold': True,
                'top': 1,
                'left': 1,
                'bottom': 1,
                'top_color': 'black',
                'left_color': 'black',
                'bottom_color': 'black',
            })
        cell_g_10_center_trb = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
                'bold': True,
                'top': 1,
                'right': 1,
                'bottom': 1,
                'top_color': 'black',
                'right_color': 'black',
                'bottom_color': 'black',
            })
        cell_10_center_lr = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
                'left': 1,
                'right': 1,
                'left_color': 'black',
                'right_color': 'black',
            })
        cell_10_center_lrb = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
                'left': 1,
                'right': 1,
                'bottom': 1,
                'left_color': 'black',
                'right_color': 'black',
                'bottom_color': 'black',
               })
        cell_10_center_l = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
                'left': 1,
                'left_color': 'black',
            })
        cell_10_center_lb = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
                'left': 1,
                'bottom': 1,
                'left_color': 'black',
                'bottom_color': 'black',
            })
        cell_10_center_r = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 10,
                'right': 1,
                'right_color': 'black',
            })

        worksheet_ost.write('A1', 'CNAM', g_14_center)
        worksheet_ost.merge_range('A3:E3', 'O D Salaires mois de : '+month_year+' MENSUELLE', gi_12_center)

        worksheet_ost.write('A6', 'Compte', cell_g_10_center)
        worksheet_ost.write('B6', 'Libellé', cell_g_10_center_tlb)
        worksheet_ost.write('C6', '', cell_g_10_center_trb)
        worksheet_ost.write('D6', 'Débit', cell_g_10_center)
        worksheet_ost.write('E6', 'Crédit', cell_g_10_center)

        worksheet_ost.write('A7', '', cell_10_center_lr)
        worksheet_ost.write('B7', '', cell_10_center_l)
        worksheet_ost.write('C7', '', cell_10_center_r)
        worksheet_ost.write('D7', '', cell_10_center_lr)
        worksheet_ost.write('E7', '', cell_10_center_lr)

        # 
        date_from = datetime.strptime(start_date, '%d-%m-%Y')
        date_to = datetime.strptime(end_date, '%d-%m-%Y')
        move_ids = request.env['hr.payslip'].sudo().search([('date_from', '>=', date_from),('date_to', '<=', date_to), ('state', 'in', ['done', 'paid', 'verify'])]).mapped('move_id')
        move_line_ids = move_ids.mapped('line_ids')



        row = 8
        sum_debit = 0
        sum_credit = 0
        for line in move_line_ids:
            cell = 'A'+str(row)
            worksheet_ost.write(cell, line.account_id.code, cell_10_center_lr)
            cell = 'B'+str(row)
            worksheet_ost.write(cell, line.name or 'paie mois de', cell_10_center_l)
            cell = 'C'+str(row)
            worksheet_ost.write(cell, month_year, cell_10_center_r)

            if line.debit:
                cell = 'D'+str(row)
                worksheet_ost.write(cell, '{:,}' .format(line.debit), cell_10_center_lr)
                cell = 'E'+str(row)
                worksheet_ost.write(cell, '', cell_10_center_lr)
                sum_debit += line.debit

            elif line.credit:
                cell = 'D'+str(row)
                worksheet_ost.write(cell, '', cell_10_center_lr)
                cell = 'E'+str(row)
                worksheet_ost.write(cell, '{:,}' .format(line.credit), cell_10_center_lr)
                sum_credit += line.credit

            row += 1

        worksheet_ost.write('A'+str(row), '', cell_10_center_lr)
        worksheet_ost.write('B'+str(row), '', cell_10_center_l)
        worksheet_ost.write('C'+str(row), '', cell_10_center_r)
        worksheet_ost.write('D'+str(row), '', cell_10_center_lr)
        worksheet_ost.write('E'+str(row), '', cell_10_center_lr)
        row += 1 

        worksheet_ost.write('A'+str(row), '', cell_10_center_lrb)
        worksheet_ost.write('B'+str(row), '', cell_10_center_lb)
        worksheet_ost.write('C'+str(row), 'Totaux', g_10_right_b)

        worksheet_ost.write('D'+str(row), '{:,}' .format(sum_debit), cell_g_10_center)
        worksheet_ost.write('E'+str(row), '{:,}' .format(sum_credit), cell_g_10_center)

        row += 3
        worksheet_ost.write('B'+str(row), 'Antananarivo, le '+self.today_string(), simple_10_left)

        row += 2
        worksheet_ost.merge_range('D'+str(row)+':E'+str(row), 'Le Directeur', simple_10_center)

        row += 7
        worksheet_ost.merge_range('D'+str(row)+':E'+str(row), 'Jocelyn RASOANAIVO', simple_10_center)

    def style(self, worksheet):
        # worksheet.set_row(13, 30)
        worksheet.set_column('A:A', 8)
        worksheet.set_column('B:B', 15)
        worksheet.set_column('C:C', 8)
        worksheet.set_column('D:D', 22)
        worksheet.set_column('E:E', 22)

    def today_string(self):
        d = date.today()
        m = d.month
        str_month = ['0','Janvier', 'Février', 'Mars', 'Avril', 'Mei', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

        result = str(d.day) + ' ' + str_month[m] + ' ' + str(d.year)
        return result