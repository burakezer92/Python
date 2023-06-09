# -*- coding: utf-8 -*-

from odoo import models, fields


class Fibimilcebayileri(models.Model):
     _name = 'fibim.ilcebayileri'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'İlçe Bayileri'
     _rec_name = 'ilce_bayi_ililce'

     ilce_bayi_yetkilisi = fields.Many2one('hr.employee', string='Bayi Yetkilisi', required=True)
     ilce_bayi_adres = fields.Text(string='Adres', required=True, track_visibility="always")
     ilce_bayi_ililce = fields.Many2one('fibim.ililce', string='İlçe', required=True, track_visibility="always")
     ilce_bayi_il = fields.Char(related='ilce_bayi_ililce.turkiye_il', string='İl', track_visibility="always")
     ilce_bayi_sirket = fields.Many2one('res.company', string='Şirket', track_visibility="always")
     ilce_bayi_sssec = fields.Selection([
          ('ilce_bayi_sahissec', 'Şahıs'),
          ('ilce_bayi_sirketsec', 'Şirket'),
     ], default='ilce_bayi_sahissec', required=True, track_visibility="always")
     ilce_bayi_baglibolge = fields.Many2one('fibim.bolgebayileri', string='Bölge Bayisi')
     ilce_bayi_bagliil = fields.Many2one('fibim.ilbayileri', string='İl Bayisi')



