# -*- coding: utf-8 -*-

from odoo import models, fields


class Fibimistasyonbilgileri(models.Model):
     _name = 'fibim.istasyonbilgileri'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'İstasyon Bilgileri'
     _rec_name = 'istasyon_adi'

     istasyon_adi = fields.Char(string='İstasyon Adı', required=True)
     istasyon_mikrotik = fields.Many2one('fibim.mikrotikislemleri', string='Mikrotik', required=True)



