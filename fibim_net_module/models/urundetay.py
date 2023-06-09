# -*- coding: utf-8 -*-

from odoo import models, fields


class FibimUrundetay(models.Model):
     _name = 'fibim.urundetay'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Ürün Detay'
     _rec_name = 'urun_detayi'

     urun_detayi = fields.Char(string='Detay', required=True)
     urun_marka = fields.Char(string='Marka')
     urun_model = fields.Char(string='Model')
     urun_ozellik = fields.Text(string='Özellik')



