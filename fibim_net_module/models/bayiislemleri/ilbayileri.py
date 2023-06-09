# -*- coding: utf-8 -*-

from odoo import models, fields


class Fibimilbayileri(models.Model):
     _name = 'fibim.ilbayileri'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'İl Bayileri'
     _rec_name = 'il_bayi_ili'

     il_bayi_yetkilisi = fields.Many2one('hr.employee', string='Bayi Yetkilisi', required=True)
     il_bayi_adres = fields.Text(string='Adres', required=True, track_visibility="always")
     il_bayi_ililce = fields.Many2one('fibim.ililce', string='İlçe', required=True, track_visibility="always")
     il_bayi_ili = fields.Char(related='il_bayi_ililce.turkiye_il', string='İl', track_visibility="always")
     il_bayi_sirket = fields.Many2one('res.company', string='Şirket', track_visibility="always")
     il_bayi_sssec = fields.Selection([
          ('il_bayi_sahissec', 'Şahıs'),
          ('il_bayi_sirketsec', 'Şirket'),
     ], default='il_bayi_sahissec', required=True, track_visibility="always")
     il_bayi_baglibolge = fields.Many2one('fibim.bolgebayileri', string='Bölge Bayisi')



