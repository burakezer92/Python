# -*- coding: utf-8 -*-

from odoo import models, fields


class FibimSattigimizdevreler(models.Model):
     _name = 'fibim.sattigimizdevreler'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Sattığımız Devreler'

     satilan_sirket = fields.Many2one('res.company', string='Şirket', required=True)
     satilan_devre_no = fields.Char(string='Devre No', required=True)
     satilan_devre_ip_adresi = fields.Char(string='Ip Adresi', required=True)
     satilan_devre_download = fields.Char(string='Download Hızı', required=True)
     satilan_devre_upload = fields.Char(string='Upload Hızı', required=True)
     satilan_sirket_yetkilisi = fields.Many2one('hr.employee', string='Şirket Yetkilisi', required=True)
     satilan_fibim_yetkilisi = fields.Many2one('hr.employee', string='Fibim Yetkilisi', required=True)



