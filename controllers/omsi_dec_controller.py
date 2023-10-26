# -*- coding: utf-8 -*-

import io
from ast import literal_eval

import xlsxwriter as xlsxwriter

from odoo import http
from odoo.http import request

from datetime import date


class ExportReportOmsiController(http.Controller):

    @http.route('/web/binary/download_report_omsi_file', type='http', auth="public")
    def download_report_omsi_file(self, sante, plf, y, eff, mc, plf32, trim, eft):  #
        plf = literal_eval(plf)

        filename = "OMSI.xlsx"
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
            "left": 1,
            "right": 1,
            "font_size": 12,
            "left_color": "black",
            "right_color": "black",
            "align": "center"
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
        cust_2 = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            "left": 1,
            "right": 1,
            "left_color": "black",
            "right_color": "black",
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
            "bold": True,
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
            val_trim = 'Première'
        elif int(trim) == 2:
            val_trim = 'Deuxième'
        elif int(trim) == 3:
            val_trim = 'Troisième'
        else:
            val_trim = 'Quatrième'


        worksheet_ost.merge_range('A2:K2', 'ETAT DES COTISATIONS VERSEES A L\'OMSI AU TITRE DU '+val_trim+' Trimestre '+y,
                                  self.bold(workbook, 'center', 14, 1, True))

        worksheet_ost.merge_range('A4:E4', 'Nom et Adresse de l\'adhérent', cust_1)
        worksheet_ost.merge_range('A5:E5', 'CNAM Madagascar', cust_2)
        worksheet_ost.merge_range('A6:E6', '(Conservatoire National des Arts et Metiers)', cust_3)
        worksheet_ost.merge_range('A7:E7', '67 Ha Maison des produits 6ème étage 101-Antananarivo', cust_4)
        worksheet_ost.merge_range('A8:E8', '', left_rigth_bottom)

        worksheet_ost.write("I3", "Destinataire", center_bol_12)
        worksheet_ost.write("G4", "", topleft_border)
        worksheet_ost.write("H4", "", top_border)
        worksheet_ost.write("I4", "O.M.S.I", center_bol_14)
        worksheet_ost.write("J4", "", top_border)
        worksheet_ost.write("K4", "", toprigth_border)

        worksheet_ost.merge_range("G5:K5", "Organisation Médico-Sociale Interprofessionnelle", left_rigth_12)
        worksheet_ost.merge_range("G6:K6", "B.P. 424 Boulevard de la Fidelité 501-TOAMASINA", left_rigth_12)
        worksheet_ost.merge_range("G7:K7", "Compte bancaire: 00008 00490 21010002372-09", left_rigth_12)
        worksheet_ost.merge_range('G8:K8', 'Tél. 020 53 323 37 - E-mail: omsitmm@moov.mg', left_rigth_bottom)

        # Sheet header
        worksheet_ost.merge_range('A10:B10', 'N°d\'Inscription à l\'OMSI : ', left_12)
        worksheet_ost.merge_range('C10:K10', 'Déclaration nominative des salaires vérsés au cours du '+val_trim+' Trimestre '+y, left_12)
        worksheet_ost.merge_range('A11:A13', 'N°', cell_8)
        worksheet_ost.merge_range('B11:B13', 'NOM ET PRENOMS DU TRAVAILLEUR', cell_8)
        worksheet_ost.merge_range('C11:D11', 'DATE', cell_7)
        worksheet_ost.write('E11', '1er Mois', cell_7)
        worksheet_ost.write('F11', '2ème Mois', cell_7)
        worksheet_ost.write('G11', '3ème Mois', cell_7)
        worksheet_ost.write('H11', 'Total trimestriel', left_rigth_top_7)
        worksheet_ost.merge_range('I11:K11', '', cell_7)
        worksheet_ost.write('C12', 'Entrée en cours', left_rigth_top_7)
        worksheet_ost.write('D12', 'Départ en cours', left_rigth_top_7)
        worksheet_ost.write('C13', 'Du trimestre', left_rigth_bottom_7)
        worksheet_ost.write('D13', 'Du trimestre', left_rigth_bottom_7)

        worksheet_ost.write('E12', 'Salaire Brut Payé', left_rigth_7)
        worksheet_ost.write('F12', 'Salaire Brut Payé', left_rigth_7)
        worksheet_ost.write('G12', 'Salaire Brut Payé', left_rigth_7)
        worksheet_ost.write('H12', 'Salaire Brut Payé', left_rigth_7)

        worksheet_ost.write('E13', '', left_rigth_bottom_7)
        worksheet_ost.write('F13', '', left_rigth_bottom_7)
        worksheet_ost.write('G13', '', left_rigth_bottom_7)
        worksheet_ost.write('H13', '', left_rigth_bottom_7)

        worksheet_ost.write('I12', 'Quote-part', left_rigth_top_7)
        worksheet_ost.write('I13', 'Patronale 5,5 % ', left_rigth_bottom_7)
        
        worksheet_ost.write('J12', 'Quote-part', left_rigth_top_7)    
        worksheet_ost.write('J13', 'Salariale 1,5 %', left_rigth_bottom_7)    
        worksheet_ost.write('K12', 'TOTAL', left_rigth_top_7)
        worksheet_ost.write('K13', '(2)', left_rigth_bottom_7)   

        # Fiche de paie correspondant au choix
        if int(trim) == 1:
            d1 = date(int(y), 1, 1)
            d2 = date(int(y), 3, 31)
        elif int(trim) == 2:
            d1 = date(int(y), 4, 1)
            d2 = date(int(y), 6, 30)
        elif int(trim) == 3:
            d1 = date(int(y), 7, 1)
            d2 = date(int(y), 9, 30)
        elif int(trim) == 4:
            d1 = date(int(y), 10, 1)
            d2 = date(int(y), 12, 31)

        payslips = request.env['hr.payslip'].sudo().search([('date_from', '>=', d1),('date_to', '<=', d2),('state', 'in', ['done', 'paid', 'verify']), ('contract_id.hr_health_id.code','in', ['OMSI','omsi'])], order="employee_id ASC")

        nb = 1
        line = 14
        sum_cotisation = 0
        for employee in payslips.mapped('employee_id'):
            month_trim = 1
            sum_sbr = 0
            pslips = payslips.filtered(lambda p:p.employee_id.id == employee.id)
            cotisation = 0
            for payslip in pslips:
                try:
                    sbr = payslip.line_ids.filtered(lambda l:l.code == 'SBR')[0].total
                except:
                    sbr = 0
                if month_trim == 1:
                    sum_sbr += sbr
                    cell = 'A'+str(line)
                    worksheet_ost.write(cell, str(nb), cell_8)

                    cell = 'B'+str(line)
                    emp_name = (payslip.employee_id.name or '') +' '+(payslip.employee_id.firstname or '')
                    worksheet_ost.write(cell, emp_name, cell_8)

                    cell = 'C'+str(line)
                    worksheet_ost.write(cell, d1.strftime('%d/%m/%Y'), cell_8)

                    cell = 'D'+str(line)
                    worksheet_ost.write(cell, d2.strftime('%d/%m/%Y'), cell_8)

                    cell = 'E'+str(line)
                    worksheet_ost.write(cell, '{:,}' .format(sbr), cell_8)
                else:
                    if month_trim == 2:
                        sum_sbr += sbr
                        cell = 'F'+str(line)
                        worksheet_ost.write(cell, '{:,}' .format(sbr), cell_8)
                    elif month_trim == 3:
                        sum_sbr += sbr
                        cell = 'G'+str(line)
                        worksheet_ost.write(cell, '{:,}' .format(sbr), cell_8)

                cell = 'H'+str(line)
                worksheet_ost.write(cell, '{:,}' .format(sum_sbr), cell_8)

                cell = 'I'+str(line)
                patronal = sum_sbr * 5.5 /100
                worksheet_ost.write(cell, '{:,}' .format(patronal), cell_8)

                cell = 'J'+str(line)
                salarial = sum_sbr * 1.5 /100
                worksheet_ost.write(cell, '{:,}' .format(salarial), cell_8)
                cell = 'K'+str(line)
                cotisation = patronal + salarial
                worksheet_ost.write(cell, '{:,}' .format(cotisation), cell_8)



                month_trim += 1

            sum_cotisation += cotisation
            nb +=1
            line +=1

        line += 2
        cell = 'A'+str(line)
        worksheet_ost.write(cell, 'NB:', no_border_8)

        cell = 'B'+str(line)
        worksheet_ost.write(cell, '( 1 ) Sont condidérés comme travailleurs tous les ouvriers employés, cadres ', no_border_7)
        
        cell = 'B'+str(line+1)
        worksheet_ost.write(cell, ' y compris les expatriés ainsi que les gens de maison de l\'Etablissement.', no_border_7)        
        
        cell = 'B'+str(line+2)
        worksheet_ost.write(cell, '( 2 ) Les cotisations sont payables au 1er mois de chaque trimestre civil.', no_border_7)

        cell = 'B'+str(line+3)
        worksheet_ost.write(cell, '( 3 ) Tout paiement postérieur au délai consenti entraînera une majoration de 10%', no_border_7)
        
        cell = 'D'+str(line)+':E'+str(line)
        worksheet_ost.merge_range(cell, 'Montant de cotisations', cell_10)
        cell = 'F'+str(line)+':G'+str(line)
        worksheet_ost.merge_range(cell, '{:,}' .format(sum_cotisation), cell_10)

        cell = 'D'+str(line+1)+':E'+str(line+1)
        worksheet_ost.merge_range(cell, 'Majoration de retard 10%', cell_10)
        cell = 'F'+str(line+1)+':G'+str(line+1)
        worksheet_ost.merge_range(cell, '0', cell_10)

        cell = 'D'+str(line+2)+':E'+str(line+2)
        worksheet_ost.merge_range(cell, 'Total à payer', cell_10)
        cell = 'F'+str(line+2)+':G'+str(line+2)
        worksheet_ost.merge_range(cell, '0', cell_10)


        # Mode de versement
        cell = 'I'+str(line)+':K'+str(line)
        worksheet_ost.merge_range(cell, 'Mode de versement', cell_10_center)

        cell = 'I'+str(line+1)
        worksheet_ost.write(cell, 'Espece', cell_nto_bold_10)  
        cell = 'I'+str(line+2)
        worksheet_ost.write(cell, '', cell_nto_bold_10)  

        cell = 'J'+str(line+1)
        worksheet_ost.write(cell, 'Chèque', cell_nto_bold_10)
        cell = 'J'+str(line+2)
        worksheet_ost.write(cell, '', cell_nto_bold_10)  

        cell = 'K'+str(line+1)
        worksheet_ost.write(cell, 'Virement', cell_nto_bold_10)    
        cell = 'K'+str(line+2)
        worksheet_ost.write(cell, '', cell_nto_bold_10)   


        line += 4
        cell = 'E'+str(line)+':I'+str(line)
        worksheet_ost.write(cell, 'DECLARATION CERTIFIEE SINCERE ET VERITABLE', center_bol_12)   

        line += 2
        cell = 'E'+str(line)+':I'+str(line)
        worksheet_ost.write(cell, 'Toamasina, le '+self.today_format(), center_bol_12_not_bol) 

        line += 2
        cell = 'E'+str(line)+':I'+str(line)
        worksheet_ost.write(cell, '(Signature)', center_bol_12_not_bol) 

    def style(self, worksheet):
        worksheet.set_column('A:A', 6)
        worksheet.set_column('B:B', 38)
        worksheet.set_column('C:L', 11)

    def today_format(self):
        d = date.today()
        str_month = ['', 'Janvier', 'Février', 'Mars', 'Avril', 'Mei', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
        m = d.month

        str_date = str(d.day) +' '+str_month[m]+' '+str(d.year)
        return str_date


