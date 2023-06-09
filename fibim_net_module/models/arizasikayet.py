# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class FibimArizasikayet(models.Model):
     _name = 'fibim.arizasikayet'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Arıza Şikayet'
     _rec_name = 'ariza_abone_no'
     _order = "ariza_abone_tarihbas desc"

     def digeraboneariza(self):
          return {
               'name': _('Diğer Arızalar'),
               'domain': [('ariza_abone_no', '=', self.ariza_abone_no)],
               'res_model': 'fibim.arizasikayet',
               'view_id': False,
               'view_mode': 'tree,form',
               'type': 'ir.actions.act_window',
               'view_type': 'form',
          }

     def ariza_whatsapptus(self):
          return {
               'res_model': 'ir.actions.act_url',
               'type': 'ir.actions.act_url',
               'target': '_blank',
               'url': self.ariza_whatsappotomesaj
          }

     def ariza_digerarizalarsayacfonk(self):
          sayac = self.env['fibim.arizasikayet'].search_count([('ariza_abone_no', '=', self.ariza_abone_no)])
          self.ariza_digerarizalarsayac = sayac


     ariza_abone_no = fields.Char(string='Abone No')
     ariza_abone_isim = fields.Char(string='İsim')
     ariza_abone_soyisim = fields.Char(string='Soyisim')
     ariza_abone_tel = fields.Char(string='Telefon', track_visibility="always")
     ariza_abone_adres = fields.Char(string='Adres', track_visibility="always")
     ariza_abone_aciklama = fields.Char(string='Arıza Açıklaması', track_visibility="always")
     ariza_abone_cozumaciklama = fields.Char(string='Çözüm Açıklaması', track_visibility="always")
     ariza_abone_ililce = fields.Many2one('fibim.ililce', string='İlçe', track_visibility="always")
     ariza_abone_il = fields.Char(related='ariza_abone_ililce.turkiye_il', string='İl', track_visibility="always")
     ariza_abone_il_yazi = fields.Char()
     ariza_abone_teknikservis = fields.Many2one('hr.employee', string='Teknik Servis Bilgisi', track_visibility="always")
     ariza_abone_tarihbas = fields.Datetime(string=' Başlangıç Tarihi', track_visibility="always")
     ariza_abone_tarihbas_an = fields.Boolean()
     ariza_abone_tarihbit = fields.Datetime(string='Bitiş Tarihi', track_visibility="always")
     ariza_abone_tarihbit_an = fields.Boolean()
     ariza_abone_durumu = fields.Boolean()
     ariza_abone_durumu_yazi = fields.Char(string='Arıza Durumu', track_visibility="always")
     ariza_abone_tip = fields.Selection([
         ('abone_ariza', 'Arıza'),
         ('abone_sikayet', 'Şikayet'),
     ], default='abone_ariza', string="Tip")
     ariza_abone_tur = fields.Selection([
          ('ariza_abone_bireysel', 'Bireysel'),
          ('ariza_abone_kurumsal', 'Kurumsal'),
          ('ariza_abone_esnaf', 'Esnaf'),
     ], string="Tür")
     ariza_kayitli_abone_sec = fields.Many2one('fibim.musteri', string='Kayıtlı Müşteri')
     ariza_kayitli_abone_no = fields.Char(related='ariza_kayitli_abone_sec.abone_no')
     ariza_kayitli_abone_isim = fields.Char(related='ariza_kayitli_abone_sec.abone_isim')
     ariza_kayitli_abone_soyisim = fields.Char(related='ariza_kayitli_abone_sec.abone_soyisim')
     ariza_kayitli_abone_adres = fields.Char(related='ariza_kayitli_abone_sec.abone_adres')
     ariza_kayitli_abone_tel = fields.Char(related='ariza_kayitli_abone_sec.abone_tel')
     ariza_kayitli_abone_ililce = fields.Many2one(related='ariza_kayitli_abone_sec.abone_ililce')
     ariza_whatsappotomesaj = fields.Char()
     ariza_abone_teknikservistel = fields.Char(related='ariza_abone_teknikservis.work_phone')
     ariza_giderilmesuresi = fields.Char()
     ariza_giderilmesuresidak = fields.Integer(string='Arıza Giderilme Süresi (Dak)')
     ariza_digerarizalarsayac = fields.Integer(compute = 'ariza_digerarizalarsayacfonk')


     @api.onchange('ariza_abone_il')
     def set_arizaaboneilyazi(self):
          self.ariza_abone_il_yazi = self.ariza_abone_il
          return

     @api.onchange('ariza_abone_tarihbit', 'ariza_abone_tarihbas')
     def set_arizagiderilmesuresi(self):
          if self.ariza_abone_tarihbit and self.ariza_abone_tarihbas:
               arizagiderilmesuresi = self.ariza_abone_tarihbit - self.ariza_abone_tarihbas
               self.ariza_giderilmesuresidak = int(arizagiderilmesuresi.total_seconds()/60)
          return

     @api.onchange('ariza_abone_isim','ariza_abone_soyisim','ariza_abone_tel','ariza_abone_adres','ariza_abone_aciklama', 'ariza_abone_teknikservis')
     def set_arizawhatsappotomesaj(self):
          self.ariza_whatsappotomesaj = "https://wa.me/" + str(self.ariza_abone_teknikservistel) + "?text=" + str(self.ariza_abone_isim) + " " + str(self.ariza_abone_soyisim) + " " + str(self.ariza_abone_tel) + " " + str(self.ariza_abone_adres) + " " + str(self.ariza_abone_aciklama)
          self.ariza_whatsappotomesaj = self.ariza_whatsappotomesaj.replace(" ", "%20")
          self.ariza_whatsappotomesaj = self.ariza_whatsappotomesaj.replace("False", "")
          return

     @api.onchange('ariza_kayitli_abone_sec')
     def set_arizakayitliabonegetir(self):
          if self.ariza_kayitli_abone_sec:
               self.ariza_abone_no = self.ariza_kayitli_abone_no
               self.ariza_abone_isim = self.ariza_kayitli_abone_isim
               self.ariza_abone_soyisim = self.ariza_kayitli_abone_soyisim
               self.ariza_abone_adres = self.ariza_kayitli_abone_adres
               self.ariza_abone_ililce = self.ariza_kayitli_abone_ililce
               self.ariza_abone_tel = self.ariza_kayitli_abone_tel
          return

     @api.onchange('ariza_abone_tarihbas_an', 'ariza_abone_tarihbas')
     def set_arizaabonetarihbasan(self):
          if self.ariza_abone_tarihbas_an:
               self.ariza_abone_tarihbas = datetime.now()
               self.ariza_abone_tarihbas_an = False
          return

     @api.onchange('ariza_abone_durumu_yazi', 'ariza_abone_durumu')
     def set_arizaabonedurumuyazi(self):
          if self.ariza_abone_durumu:
               self.ariza_abone_durumu_yazi = 'Çözüldü'
          else:
               self.ariza_abone_durumu_yazi = 'Sorun Var'
          return

     @api.onchange('ariza_abone_tarihbit_an', 'ariza_abone_tarihbit')
     def set_arizaabonetarihbitan(self):
          if self.ariza_abone_tarihbit_an:
               self.ariza_abone_tarihbit = datetime.now()
               self.ariza_abone_tarihbit_an = False
          return

     @api.onchange('ariza_abone_durumu_yazi', 'ariza_abone_tarihbit')
     def set_arizaabonetarihbitcozulmean(self):
          if self.ariza_abone_durumu_yazi == "Çözüldü" and self.ariza_abone_tarihbit == False:
               self.ariza_abone_tarihbit = datetime.now()
          return

     @api.onchange('ariza_abone_isim', 'ariza_abone_soyisim', 'ariza_abone_adres')
     def set_upperlower(self):
          if self.ariza_abone_isim:
               self.ariza_abone_isim = str(self.ariza_abone_isim).upper()
          if self.ariza_abone_soyisim:
               self.ariza_abone_soyisim = str(self.ariza_abone_soyisim).upper()
          if self.ariza_abone_adres:
               self.ariza_abone_adres = str(self.ariza_abone_adres).upper()
          return

     @api.onchange('ariza_abone_tarihbit', 'ariza_abone_tarihbas')
     def set_tarihbasbitkarsilastirma(self):
          if str(self.ariza_abone_tarihbit) < str(self.ariza_abone_tarihbas):
               raise ValidationError("Bitiş Tarihi Başlangıç Tarihinden Önce Olamaz!")