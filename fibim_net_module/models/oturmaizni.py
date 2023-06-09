# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class FibimOturmaizni(models.Model):
     _name = 'fibim.oturmaizni'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Oturma İzni'
     _rec_name = 'yabanci_abone_no'
     _order = "yabanci_abone_bit_tarih"

     yabanci_abone_no = fields.Char(string='Abone No')
     yabanci_abone_uyelik_tar = fields.Date(string='Üyelik Tarihi')
     yabanci_abone_kimlikno = fields.Char(string='Yabancı Kimlik No')
     yabanci_abone_isim = fields.Char(string='İsim')
     yabanci_abone_soyisim = fields.Char(string='Soyisim')
     yabanci_abone_tel = fields.Char(string='Telefon', track_visibility="always")
     yabanci_abone_adres = fields.Char(string='Adres', track_visibility="always")
     yabanci_abone_aciklama = fields.Char(string='Açıklama', track_visibility="always")
     yabanci_abone_bas_tarih = fields.Date(string='Başlangıç Tarihi', track_visibility="always")
     yabanci_abone_bit_tarih = fields.Date(string='Bitiş Tarihi', track_visibility="always")
