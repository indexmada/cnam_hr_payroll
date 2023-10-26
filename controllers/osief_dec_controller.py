# -*- coding: utf-8 -*-

import io
from ast import literal_eval

import xlsxwriter as xlsxwriter

from odoo import http
from odoo.http import request

from datetime import date


class ExportReportOsiefController(http.Controller):

    @http.route('/web/binary/download_report_osief_file', type='http', auth="public")
    def download_report_osief_file(self, sante, plf, y, eff, mc, plf32, trim, eft):  #
        plf = literal_eval(plf)

        filename = "OSIEF.xlsx"
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        mc_ = literal_eval(mc)
        eff_ = literal_eval(eff)
        plf32_ = literal_eval(plf32)

        omsi_info = literal_eval(sante)
        row_count = len(omsi_info)

        self.report_excel_employer(workbook, sante, plf, y, trim, eff_, row_count)  
        workbook.close()
        output.seek(0)
        xlsheader = [('Content-Type', 'application/octet-stream'),
                     ('Content-Disposition', 'attachment; filename=%s;' % filename)]
        return request.make_response(output, xlsheader)

    def bold(self, workbook, align, size, border, bol):
        bold_ = workbook.add_format({
            'align': align,
            'valign': 'vcenter',
            'font_size': size,
            'bold': bol,
            'border': border,
        })
        return bold_


    def report_excel_employer(self, workbook, sante, plf, y, trim, eff, row_count):  #

        worksheet_ost = workbook.add_worksheet("DNS")
        wrap = workbook.add_format({
            'text_wrap': True,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 8
        })
        worksheet_ost.set_row(13, 30)
        self.style(worksheet_ost)

        topleft_border = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "top": 1,
            "left": 1,
            "top_color": "black",
            "left_color": "black",
            "font_size": 10,
            'bold': True,
        })
        toprigth_border = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "top": 1,
            "right": 1,
            "top_color": "black",
            "right_color": "black",
            'font_size': 10
        })

        left_border = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "left": 1,
            "left_color": "black",
            'font_size': 10,
            'bold': True,
        })

        left_border2 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "left": 1,
            "left_color": "black",
            'font_size': 8,
            'bold': True,
        })
        left_border3 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "left": 1,
            "left_color": "black",
            'font_size': 8,

        })
        right_border = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "right": 1,
            "right_color": "black",
            'font_size': 10
        })
        leftbotom_border = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "left": 1,
            "bottom": 1,
            "bottom_color": "black",
            "left_color": "black",
            'font_size': 8
        })
        rightbotom_border = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "right": 1,
            "bottom": 1,
            "bottom_color": "black",
            "right_color": "black"
        })
        botom_border = workbook.add_format({
            "bottom": 1,
            "bottom_color": "black"
        })
        top_border = workbook.add_format({
            "top": 1,
            "top_color": "black"
        })
        top_bottom = workbook.add_format({
            "bottom": 1,
            "top": 1,
            "font_size": 10,
            "top_color": "black",
            "bottom_color": "black"
        })
        left_rigth = workbook.add_format({
            "left": 1,
            "right": 1,
            "font_size": 10,
            "left_color": "black",
            "right_color": "black",
            "align": "center"
        })
        left_rigth_7 = workbook.add_format({
            "left": 1,
            "right": 1,
            "font_size": 7,
            "left_color": "black",
            "right_color": "black",
            "align": "center"
        })

        left_rigth_12 = workbook.add_format({
            "left": 3,
            "right": 3,
            "font_size": 12,
            "left_color": "black",
            "right_color": "black",
            "align": "center"
        })
        left_rigth_top_12 = workbook.add_format({
            "left": 3,
            "right": 3,
            "top":1,
            "font_size": 12,
            "left_color": "black",
            "right_color": "black",
            "top_color": "black",
            "align": "left",
            "bold": True
        })
        left_rigth_bottom_12 = workbook.add_format({
            "left": 3,
            "right": 3,
            "bottom":1,
            "font_size": 12,
            "left_color": "black",
            "right_color": "black",
            "bottom_color": "black",
            "align": "left"
        })

        left_rigth_bottom = workbook.add_format({
            "left": 1,
            "right": 1,
            "bottom": 1,
            "font_size": 10,
            "left_color": "black",
            "right_color": "black",
            "bottom_color": "black",
            "align": "center"
        })
        left_rigth_bottom_7 = workbook.add_format({
            "left": 1,
            "right": 1,
            "bottom": 1,
            "font_size": 7,
            "left_color": "black",
            "right_color": "black",
            "bottom_color": "black",
            "align": "center"
        })
        left_rigth_top_7 = workbook.add_format({
            "left": 1,
            "right": 1,
            "top": 1,
            "font_size": 7,
            "left_color": "black",
            "right_color": "black",
            "top_color": "black",
            "align": "center"
        })
        font_10 = workbook.add_format({
            "font_size": 10
        })

        cust_1 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "top": 1,
            "left": 1,
            "right": 1,
            "top_color": "black",
            "left_color": "black",
            "right_color": "black",
            "font_size": 14,
            'bold': True,
            })
        cust_12 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "left": 1,
            "right": 1,
            "top":1,
            "bottom":1,
            "left_color": "black",
            "right_color": "black",
            "top_color": "black",
            "bottom_color": "black",
            "font_size": 12,
            'bold': True,
            })
        cust_3 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "left": 1,
            "right": 1,
            "left_color": "black",
            "right_color": "black",
            "font_size": 12,
            'bold': False,
            })
        cust_4 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "left": 1,
            "right": 1,
            "left_color": "black",
            "right_color": "black",
            "font_size": 8,
            'bold': False,
            })

        center_bol_12 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 12,
            'bold': True,
            })
        center_bol_12_not_bol = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 12,
            'bold': False,
            })
        center_bol_14 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 14,
            'bold': True,
            })

        left_12 = workbook.add_format({
            'align': 'left',
            'valign': 'vleft',
            "font_size": 12,
            })

        center_7_bold = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 7,
            "bold": True,
            })
        cell_left_12 = workbook.add_format({
            'align': 'left',
            'valign': 'vleft',
            "font_size": 12,
            "border": True
            })
        cell_right_12 = workbook.add_format({
            'align': 'right',
            'valign': 'vright',
            "font_size": 12,
            "border": True
            })
        left_12_bold = workbook.add_format({
            'align': 'left',
            'valign': 'vleft',
            "font_size": 12,
            "bold": True,
            })
        center_15 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 15,
            })
        cell_8 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'top': 1,
            'left': 1,
            'right': 1,
            'bottom': 1,
            'right_color': 'black',
            'bottom_color': 'black',
            'top_color': 'black',
            'left_color': 'black',
            "font_size": 8,
            })
        cell_10 = workbook.add_format({
            'align': 'left',
            'valign': 'vleft',
            'top': 1,
            'left': 1,
            'right': 1,
            'bottom': 1,
            'right_color': 'black',
            'bottom_color': 'black',
            'top_color': 'black',
            'left_color': 'black',
            "font_size": 10,
            "bold": True,
            })
        cell_10_center = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'top': 1,
            'left': 1,
            'right': 1,
            'bottom': 1,
            'right_color': 'black',
            'bottom_color': 'black',
            'top_color': 'black',
            'left_color': 'black',
            "font_size": 10,
            })
        no_border_10_center = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "font_size": 10,
            "border":False
            })
        cell_nto_bold_10 = workbook.add_format({
            'align': 'left',
            'valign': 'vleft',
            'top': 1,
            'left': 1,
            'right': 1,
            'bottom': 1,
            'right_color': 'black',
            'bottom_color': 'black',
            'top_color': 'black',
            'left_color': 'black',
            "font_size": 10,
            })
        cell_7 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'top': 1,
            'left': 1,
            'right': 1,
            'bottom': 1,
            'right_color': 'black',
            'bottom_color': 'black',
            'top_color': 'black',
            'left_color': 'black',
            "font_size": 7,
            })

        no_border_8 = workbook.add_format({
            'font_size':8,
        })
        no_border_7 = workbook.add_format({
            'font_size':7,
        })
        if int(trim) == 1:
            val_trim = '1è'
        elif int(trim) == 2:
            val_trim = '2ème'
        elif int(trim) == 3:
            val_trim = '3ème'
        else:
            val_trim = '4ème'


        worksheet_ost.merge_range('A1:E1','0rganisation Sanitaire Inter-Entreprises de Fianarantsoa' ,center_bol_12)
        worksheet_ost.merge_range('A2:E2','O.S.I.E.F' ,center_bol_12)
        worksheet_ost.merge_range('F1:J1','DECLARATION DES SALAIRES VERSES AU TITRE DE' ,center_15)
        worksheet_ost.merge_range('F2:J2',val_trim+' Trimestre '+y ,no_border_10_center)

        info_line = 'E-mail : osief.fianar@gmail.com                                                                                                             Tél 75 915 08 –75 511 31 Antarandolo Fianarantsoa'   
        worksheet_ost.write('A4',info_line ,left_12_bold) 

        n_bank = 'BFV : 340 21000 133138 32  _ BNI : 52 465 485 70 20 00'       
        worksheet_ost.write('A6',n_bank ,left_12_bold) 

        
        worksheet_ost.merge_range('A11:A27', 'Noms et Prénoms', cust_12)
        worksheet_ost.write('B11', 'Matricule', left_rigth_top_7)
        worksheet_ost.write('B12', 'CNaPS', left_rigth_7)
        worksheet_ost.write('B13', '', left_rigth_7)
        worksheet_ost.write('B14', '', left_rigth_7)
        worksheet_ost.write('B15', '', left_rigth_7)
        worksheet_ost.write('B16', '', left_rigth_7)
        worksheet_ost.write('B17', '', left_rigth_7)
        worksheet_ost.write('B18', '', left_rigth_7)
        worksheet_ost.write('B19', '', left_rigth_7)
        worksheet_ost.write('B20', '', left_rigth_7)
        worksheet_ost.write('B21', '', left_rigth_7)
        worksheet_ost.write('B22', '', left_rigth_7)
        worksheet_ost.write('B23', '', left_rigth_7)
        worksheet_ost.write('B24', '', left_rigth_7)
        worksheet_ost.write('B25', '', left_rigth_7)
        worksheet_ost.write('B26', '', left_rigth_7)
        worksheet_ost.write('B27', '', left_rigth_bottom_7)
        worksheet_ost.merge_range('C11:D21', 'DATE', cell_10_center)
        worksheet_ost.write('C22', 'E  E', left_rigth_7)
        worksheet_ost.write('C23', 'N  N', left_rigth_7)
        worksheet_ost.write('C24', 'T   ', left_rigth_7)
        worksheet_ost.write('C25', 'R  C', left_rigth_7)
        worksheet_ost.write('C26', 'E  O', left_rigth_7)
        worksheet_ost.write('C27', 'E  U', left_rigth_bottom_7)
        worksheet_ost.write('D22', 'D  E', left_rigth_7)
        worksheet_ost.write('D23', 'E  N', left_rigth_7)
        worksheet_ost.write('D24', 'P   ', left_rigth_7)
        worksheet_ost.write('D25', 'A  C', left_rigth_7)
        worksheet_ost.write('D26', 'R  O', left_rigth_7)
        worksheet_ost.write('D27', 'T  U', left_rigth_bottom_7)

        # 1er Mois
        worksheet_ost.merge_range('E11:F21', '1er MOIS', cell_10_center)
        worksheet_ost.merge_range('E22:E27', 'Salaire', cell_10_center)
        worksheet_ost.merge_range('F22:F27', 'Avantages', cell_10_center)

        # Temps Travail 1
        worksheet_ost.write('G11', 'T', left_rigth_top_7)
        worksheet_ost.write('G12', 'e', left_rigth_7)
        worksheet_ost.write('G13', 'm', left_rigth_7)
        worksheet_ost.write('G14', 'p', left_rigth_7)
        worksheet_ost.write('G15', 's', left_rigth_7)
        worksheet_ost.write('G16', ' ', left_rigth_7)
        worksheet_ost.write('G17', 't', left_rigth_7)
        worksheet_ost.write('G18', 'r', left_rigth_7)
        worksheet_ost.write('G19', 'a', left_rigth_7)
        worksheet_ost.write('G20', 'v', left_rigth_7)
        worksheet_ost.write('G21', 'a', left_rigth_7)
        worksheet_ost.write('G22', 'i', left_rigth_7)
        worksheet_ost.write('G23', 'l', left_rigth_7)
        worksheet_ost.write('G24', '', left_rigth_7)
        worksheet_ost.write('G25', '', left_rigth_7)
        worksheet_ost.write('G26', '', left_rigth_7)
        worksheet_ost.write('G27', '', left_rigth_bottom_7)

        # 2er Mois
        worksheet_ost.merge_range('H11:I21', '2er MOIS', cell_10_center)
        worksheet_ost.merge_range('H22:H27', 'Salaire', cell_10_center)
        worksheet_ost.merge_range('I22:I27', 'Avantages', cell_10_center)

        # Temps Travail 2
        worksheet_ost.write('J11', 'T', left_rigth_top_7)
        worksheet_ost.write('J12', 'e', left_rigth_7)
        worksheet_ost.write('J13', 'm', left_rigth_7)
        worksheet_ost.write('J14', 'p', left_rigth_7)
        worksheet_ost.write('J15', 's', left_rigth_7)
        worksheet_ost.write('J16', ' ', left_rigth_7)
        worksheet_ost.write('J17', 't', left_rigth_7)
        worksheet_ost.write('J18', 'r', left_rigth_7)
        worksheet_ost.write('J19', 'a', left_rigth_7)
        worksheet_ost.write('J20', 'v', left_rigth_7)
        worksheet_ost.write('J21', 'a', left_rigth_7)
        worksheet_ost.write('J22', 'i', left_rigth_7)
        worksheet_ost.write('J23', 'l', left_rigth_7)
        worksheet_ost.write('J24', '', left_rigth_7)
        worksheet_ost.write('J25', '', left_rigth_7)
        worksheet_ost.write('J26', '', left_rigth_7)
        worksheet_ost.write('J27', '', left_rigth_bottom_7)
        
        # 3er Mois
        worksheet_ost.merge_range('K11:L21', '1er MOIS', cell_10_center)
        worksheet_ost.merge_range('K22:K27', 'Salaire', cell_10_center)
        worksheet_ost.merge_range('L22:L27', 'Avantages', cell_10_center)

        # Temps Travail 3
        worksheet_ost.write('M11', 'T', left_rigth_top_7)
        worksheet_ost.write('M12', 'e', left_rigth_7)
        worksheet_ost.write('M13', 'm', left_rigth_7)
        worksheet_ost.write('M14', 'p', left_rigth_7)
        worksheet_ost.write('M15', 's', left_rigth_7)
        worksheet_ost.write('M16', ' ', left_rigth_7)
        worksheet_ost.write('M17', 't', left_rigth_7)
        worksheet_ost.write('M18', 'r', left_rigth_7)
        worksheet_ost.write('M19', 'a', left_rigth_7)
        worksheet_ost.write('M20', 'v', left_rigth_7)
        worksheet_ost.write('M21', 'a', left_rigth_7)
        worksheet_ost.write('M22', 'i', left_rigth_7)
        worksheet_ost.write('M23', 'l', left_rigth_7)
        worksheet_ost.write('M24', '', left_rigth_7)
        worksheet_ost.write('M25', '', left_rigth_7)
        worksheet_ost.write('M26', '', left_rigth_7)
        worksheet_ost.write('M27', '', left_rigth_bottom_7)
        # Observation
        worksheet_ost.write('N11', 'O', left_rigth_top_7)
        worksheet_ost.write('N12', 'B', left_rigth_7)
        worksheet_ost.write('N13', 'S', left_rigth_7)
        worksheet_ost.write('N14', 'E', left_rigth_7)
        worksheet_ost.write('N15', 'R', left_rigth_7)
        worksheet_ost.write('N16', 'V', left_rigth_7)
        worksheet_ost.write('N17', 'A', left_rigth_7)
        worksheet_ost.write('N18', 'T', left_rigth_7)
        worksheet_ost.write('N19', 'I', left_rigth_7)
        worksheet_ost.write('N20', 'O', left_rigth_7)
        worksheet_ost.write('N21', 'N', left_rigth_7)
        worksheet_ost.write('N22', 'S', left_rigth_7)
        worksheet_ost.write('N23', '', left_rigth_7)
        worksheet_ost.write('N24', '', left_rigth_7)
        worksheet_ost.write('N25', '', left_rigth_7)
        worksheet_ost.write('N26', '', left_rigth_7)
        worksheet_ost.write('N27', '', left_rigth_bottom_7)

        # Fiche de paie correspondant au choix
        if int(trim) == 1:
            d1 = date(int(y), 1, 1)
            d2 = date(int(y), 3, 31)
            date_paiement = '30 Avril'
        elif int(trim) == 2:
            d1 = date(int(y), 4, 1)
            d2 = date(int(y), 6, 30)
            date_paiement = '31 Juillet'
        elif int(trim) == 3:
            d1 = date(int(y), 7, 1)
            d2 = date(int(y), 9, 30)
            date_paiement = '31 Octobre'
        elif int(trim) == 4:
            d1 = date(int(y), 10, 1)
            d2 = date(int(y), 12, 31)
            date_paiement = '31 Janvier'

        payslips = request.env['hr.payslip'].sudo().search([('date_from', '>=', d1),('date_to', '<=', d2),('state', 'in', ['done', 'paid', 'verify']), ('contract_id.hr_health_id.code','in', ['OSIEF', 'osief'])], order="employee_id ASC")

        line = 28
        sal_1 = 0
        sal_2 = 0
        sal_3 = 0

        for employee in payslips.mapped('employee_id'):
            month_trim = 1
            sum_sbr = 0
            pslips = payslips.filtered(lambda p:p.employee_id.id == employee.id)
            for payslip in pslips:
                try:
                    sbr = payslip.line_ids.filtered(lambda l:l.code == 'SBR')[0].total
                except:
                    sbr = 0
                if month_trim == 1:
                    sal_1 +=sbr
                    cell = 'A'+str(line)
                    # Nom
                    emp_name = (payslip.employee_id.name or '') +' '+(payslip.employee_id.firstname or '')
                    worksheet_ost.write(cell, emp_name, cust_12)
                    # Matricule
                    cell = 'B'+str(line)
                    worksheet_ost.write(cell, '', cust_12)
                    # Dates entrée et Depart 1e Trim
                    cell = 'C'+str(line)
                    worksheet_ost.write(cell, str(d1), cell_10_center)
                    cell = 'D'+str(line)
                    worksheet_ost.write(cell, str(d2), cell_10_center)

                    worksheet_ost.write('E'+str(line), '{:,}' .format(sbr), cust_12)

                    # Vide
                    cell = 'F'+str(line)
                    worksheet_ost.write(cell, '', cust_12)
                    cell = 'G'+str(line)
                    worksheet_ost.write(cell, '', cust_12)
                    cell = 'I'+str(line)
                    worksheet_ost.write(cell, '', cust_12)
                    cell = 'J'+str(line)
                    worksheet_ost.write(cell, '', cust_12)
                    cell = 'L'+str(line)
                    worksheet_ost.write(cell, '', cust_12)
                    cell = 'M'+str(line)
                    worksheet_ost.write(cell, '', cust_12)
                    cell = 'N'+str(line)
                    worksheet_ost.write(cell, '', cust_12)

                else:
                    if month_trim == 2:
                        sal_2 += sbr
                        worksheet_ost.write('H'+str(line), '{:,}' .format(sbr), cust_12)
                    elif month_trim == 3:
                        sal_3 += sbr
                        worksheet_ost.write('K'+str(line), '{:,}' .format(sbr), cust_12)



                month_trim += 1

            line +=1

        # Ligne vide
        cell = 'A'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'B'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'C'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'D'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'F'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'G'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'H'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'I'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'J'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'K'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'L'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'M'+str(line)
        worksheet_ost.write(cell, '', cell_10)
        cell = 'N'+str(line)
        worksheet_ost.write(cell, '', cell_10)

        # Total
        line += 1
        cell = 'A'+str(line)+':A'+str(line+2)
        worksheet_ost.merge_range(cell, '', cell_10)

        cell = 'B'+str(line)+':D'+str(line)
        worksheet_ost.merge_range(cell, 'TOTAL', cell_left_12)
        cell = 'B'+str(line+1)+':D'+str(line+1)
        worksheet_ost.merge_range(cell, 'REPORT', cell_left_12)
        cell = 'B'+str(line+2)+':D'+str(line+2)
        worksheet_ost.merge_range(cell, 'TOTAUX', cell_left_12)

        # Sal_1
        cell = 'E'+str(line)
        worksheet_ost.write(cell, '{:,}' .format(sal_1), cell_right_12)
        cell = 'E'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'E'+str(line+2)
        worksheet_ost.write(cell, '{:,}' .format(sal_1), cell_right_12)

        # Avantage
        cell = 'F'+str(line)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'F'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'F'+str(line+2)
        worksheet_ost.write(cell, '', cell_right_12)

        # Tps Travail
        cell = 'G'+str(line)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'G'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'G'+str(line+2)
        worksheet_ost.write(cell, '', cell_right_12)

        # Sal_2
        cell = 'H'+str(line)
        worksheet_ost.write(cell, '{:,}' .format(sal_2), cell_right_12)
        cell = 'H'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'H'+str(line+2)
        worksheet_ost.write(cell, '{:,}' .format(sal_2), cell_right_12)

        # Avantage
        cell = 'I'+str(line)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'I'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'I'+str(line+2)
        worksheet_ost.write(cell, '', cell_right_12)

        # Tps Travail
        cell = 'J'+str(line)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'J'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'J'+str(line+2)
        worksheet_ost.write(cell, '', cell_right_12)

        # Sal_3
        cell = 'K'+str(line)
        worksheet_ost.write(cell, '{:,}' .format(sal_3), cell_right_12)
        cell = 'K'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'K'+str(line+2)
        worksheet_ost.write(cell, '{:,}' .format(sal_3), cell_right_12)

        # Avantage
        cell = 'L'+str(line)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'L'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'L'+str(line+2)
        worksheet_ost.write(cell, '', cell_right_12)

        # Tps Travail
        cell = 'M'+str(line)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'M'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'M'+str(line+2)
        worksheet_ost.write(cell, '', cell_right_12)

        # Observation
        cell = 'N'+str(line)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'N'+str(line+1)
        worksheet_ost.write(cell, '', cell_right_12)
        cell = 'N'+str(line+2)
        worksheet_ost.write(cell, '', cell_right_12)

        line+=3
        cell = 'A'+str(line)+':M'+str(line)
        total_sal = sal_1 + sal_2 + sal_3
        cotisation = total_sal * 8/100
        val = 'Cotisation :……'+'{:,}' .format(cotisation)+'  Ariary                        Total Salaire……'+'{:,}' .format(total_sal)+' Ariary'
        worksheet_ost.merge_range(cell, val,left_rigth_top_12)
        worksheet_ost.write('N'+str(line), '',cell_10)

        line += 1
        cell = 'A'+str(line)+':M'+str(line)
        val = 'Majoration de retard 10% :…………………………………………………                                             Cotisation 8% (Employeur 6% + Travailleurs 2%)….'
        worksheet_ost.merge_range(cell, val,left_rigth_bottom_12)
        worksheet_ost.write('N'+str(line), '',cell_10)

        line += 1
        cell = 'A'+str(line)
        val = 'NET A PAYER : (chiffres)…'+'{:,}' .format(cotisation)+' Ariary…… ; '
        worksheet_ost.write(cell, val, left_12_bold)

        line +=1
        cell = 'A'+str(line)+':F'+str(line)
        val = '   N.B. : * DATE IMPERATIVE DE PAIEMENT AVANT LE :'+date_paiement
        worksheet_ost.merge_range(cell, val, center_7_bold)

        cell = 'G'+str(line)+':H'+str(line)
        worksheet_ost.merge_range(cell, 'Fianarantsoa, le '+self.today_format(), center_bol_12_not_bol)

        line +=1
        cell = 'A'+str(line)+':F'+str(line)
        worksheet_ost.merge_range(cell, '* PASSE CE DELAI, UNE MAJORATION DE RETARD DE 10%  SERA APPLIQUEE.', center_7_bold)


        cell = 'G'+str(line)+':H'+str(line)
        worksheet_ost.merge_range(cell, 'Certifié sincère et conforme', center_bol_12_not_bol)

        val = '  *  LE NON OU LE REFUS DE PAIEMENT ENTRAINERA L’ANNULATION TEMPORAIRE DE SOINS SANS RESILIATION DE CONTRAT'
        line += 1
        cell = 'A'+str(line)+':F'+str(line)
        worksheet_ost.merge_range(cell,val, center_7_bold)

        line += 1
        cell = 'H'+str(line)+':K'+str(line)
        worksheet_ost.merge_range(cell, ' (c.à.d. L’adhérent est toujours redevable)   ', center_bol_12)

        line += 1
        cell = 'A'+str(line)
        worksheet_ost.write(cell, 'MODE DE PAIEMENT: ', left_12)

    def style(self, worksheet):
        worksheet.set_column('A:A', 16)
        worksheet.set_column('B:B', 7)
        worksheet.set_column('C:L', 13)

    def today_format(self):
        d = date.today()
        str_month = ['', 'Janvier', 'Février', 'Mars', 'Avril', 'Mei', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
        m = d.month

        str_date = str(d.day) +' '+str_month[m]+' '+str(d.year)
        return str_date


