# -*- coding: utf-8 -*-

from odoo import models, fields


class FibimBolgebayileri(models.Model):
     _name = 'fibim.bolgebayileri'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Bölge Bayileri'
     _rec_name = 'bolge_bayi_bolgesi'

     bolge_bayi_bolgesi = fields.Selection([
          ('bolge_bayi_marmarasec', 'Marmara Bölgesi'),
          ('bolge_bayi_icanadolusec', 'İç Anadolu Bölgesi'),
          ('bolge_bayi_egesec', 'Ege Bölgesi'),
          ('bolge_bayi_akdenizsec', 'Akdeniz Bölgesi'),
          ('bolge_bayi_guneydogusec', 'Güneydoğu Anadolu Bölgesi'),
          ('bolge_bayi_karadenizsec', 'Karadeniz Bölgesi'),
          ('bolge_bayi_doguanadolusec', 'Doğu Anadolu Bölgesi'),
     ], string='Bölge', required=True)
     bolge_bayi_yetkilisi = fields.Many2one('hr.employee', string='Bayi Yetkilisi', required=True)
     bolge_bayi_adres = fields.Text(string='Adres', required=True, track_visibility="always")
     bolge_bayi_ililce = fields.Many2one('fibim.ililce', string='İlçe', required=True, track_visibility="always")
     bolge_bayi_il = fields.Char(related='bolge_bayi_ililce.turkiye_il', string='İl', track_visibility="always")
     bolge_bayi_sirket = fields.Many2one('res.company', string='Şirket', track_visibility="always")
     bolge_bayi_sssec = fields.Selection([
          ('bolge_bayi_sahissec', 'Şahıs'),
          ('bolge_bayi_sirketsec', 'Şirket'),
     ], default='bolge_bayi_sahissec', required=True, track_visibility="always")



