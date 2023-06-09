# -*- coding: utf-8 -*-

from odoo import models, fields


class FibimAldigimizdevreler(models.Model):
     _name = 'fibim.aldigimizdevreler'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Aldığımız Devreler'

     alinan_sirket = fields.Many2one('res.company', string='Şirket', required=True)
     alinan_devre_no = fields.Char(string='Devre No', required=True)
     alinan_devre_ip_adresi = fields.Char(string='Ip Adresi', required=True)
     alinan_devre_download = fields.Char(string='Download Hızı', required=True)
     alinan_devre_upload = fields.Char(string='Upload Hızı', required=True)
     alinan_sirket_yetkilisi = fields.Many2one('hr.employee', string='Şirket Yetkilisi', required=True)
     alinan_fibim_yetkilisi = fields.Many2one('hr.employee', string='Fibim Yetkilisi', required=True)



