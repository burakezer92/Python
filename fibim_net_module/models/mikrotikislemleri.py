# -*- coding: utf-8 -*-

from odoo import models, fields


class FibimMikrotikislemleri(models.Model):
     _name = 'fibim.mikrotikislemleri'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Mikrotik İşlemleri'
     _rec_name = 'mikrotik_adi'

     mikrotik_adi = fields.Char(string='Mikrotik Adı', required=True)
     mikrotik_kullanici_adi = fields.Char(string='Mikrotik Kullanıcı Adı', required=True)
     mikrotik_sifre = fields.Char(string='Şifre', required=True, track_visibility="always")
     mikrotik_ip_adresi = fields.Char(string='Ip Adresi', required=True, track_visibility="always")
     mikrotik_secret = fields.Char(string='Mikrotik Secret', required=True)



