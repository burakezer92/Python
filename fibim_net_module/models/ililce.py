# -*- coding: utf-8 -*-

from odoo import models, fields


class Fibimililce(models.Model):
     _name = 'fibim.ililce'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'İl İlçe Bilgileri'
     _rec_name = 'turkiye_ilce'


     turkiye_il = fields.Char(string='İl', required=True)
     turkiye_ilce = fields.Char(string='İlçe', required=True)
     turkiye_il_kodu = fields.Char(string='İl Kodu', required=True)
     turkiye_ilce_kodu = fields.Char(string='İlçe Kodu', required=True)



