# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime


class FibimTalepbilgilendirme(models.Model):
     _name = 'fibim.talepbilgilendirme'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Talep Bilgilendirme'
     _rec_name = 'talep_abone_isim'
     _order = "talep_abone_tarih desc"

     def talepbilgilendirme_whatsapptus(self):
          return {
               'res_model': 'ir.actions.act_url',
               'type': 'ir.actions.act_url',
               'target': '_blank',
               'url': self.talep_whatsappotomesaj
          }

     talep_abone_isim = fields.Char(string='İsim')
     talep_abone_soyisim = fields.Char(string='Soyisim')
     talep_abone_tel = fields.Char(string='Telefon', track_visibility="always")
     talep_abone_adres = fields.Char(string='Adres', track_visibility="always")
     talep_abone_aciklama = fields.Char(string='Açıklama', track_visibility="always")
     talep_abone_ililce = fields.Many2one('fibim.ililce', string='İlçe', track_visibility="always")
     talep_abone_il = fields.Char(related='talep_abone_ililce.turkiye_il', string='İl', track_visibility="always")
     talep_abone_il_yazi = fields.Char()
     talep_abone_satispazarlama = fields.Many2one('hr.employee', string='Satış Pazarlama Bilgisi', track_visibility="always")
     talep_abone_tarih = fields.Datetime(string='Tarih', track_visibility="always")
     talep_abone_tarih_an = fields.Boolean()
     talep_abone_tip = fields.Selection([
         ('abone_talep', 'Talep'),
         ('abone_bilgilendirme', 'Bilgilendirme'),
     ], default='abone_talep', string="Tip")
     talep_abone_hiz = fields.Selection([
          ('talep_hiz5', '5 Mbps'),
          ('talep_hiz10', '10 Mbps'),
          ('talep_hiz15', '15 Mbps'),
          ('talep_hiz20', '20 Mbps'),
          ('talep_hiz25', '25 Mbps'),
          ('talep_hiz35', '35 Mbps'),
          ('talep_hiz50', '50 Mbps'),
          ('talep_hiz100', '100 Mbps'),
     ], string="Hız Talebi", track_visibility="always")
     talep_abone_tur = fields.Selection([
          ('talep_abone_bireysel', 'Bireysel'),
          ('talep_abone_kurumsal', 'Kurumsal'),
          ('talep_abone_esnaf', 'Esnaf'),
     ], string="Tür")
     talep_abone_durumu = fields.Boolean()
     talep_abone_durumu_yazi = fields.Char(string='Durum', track_visibility="always")
     talep_abone_olusturan = fields.Many2one('res.users', 'Aboneliği Oluşturan', default=lambda self: self.env.user)
     talep_abone_satispazarlamatel = fields.Char(related='talep_abone_satispazarlama.work_phone')
     talep_whatsappotomesaj = fields.Char()

     @api.onchange('talep_abone_il')
     def set_talepaboneilyazi(self):
          self.talep_abone_il_yazi = self.talep_abone_il
          return

     @api.onchange('talep_abone_isim', 'talep_abone_soyisim', 'talep_abone_tel', 'talep_abone_adres', 'talep_abone_aciklama', 'talep_abone_satispazarlama')
     def set_talepwhatsappotomesaj(self):
          self.talep_whatsappotomesaj = "https://wa.me/" + str(self.talep_abone_satispazarlamatel) + "?text=" + str(self.talep_abone_isim) + " " + str(self.talep_abone_soyisim) + " " + str(self.talep_abone_tel) + " " + str(self.talep_abone_adres) + " " + str(self.talep_abone_aciklama)
          self.talep_whatsappotomesaj = self.talep_whatsappotomesaj.replace(" ", "%20")
          self.talep_whatsappotomesaj = self.talep_whatsappotomesaj.replace("False", "")
          return

     @api.onchange('talep_abone_durumu_yazi', 'talep_abone_durumu')
     def set_talepabonedurumuyazi(self):
          if self.talep_abone_durumu:
               self.talep_abone_durumu_yazi = 'Abonelik Yapılacak'
          else:
               self.talep_abone_durumu_yazi = 'Abonelik Yapılmadı'
          return

     @api.onchange('talep_abone_isim', 'talep_abone_soyisim', 'talep_abone_adres')
     def set_upperlower(self):
          if self.talep_abone_isim:
               self.talep_abone_isim = str(self.talep_abone_isim).upper()
          if self.talep_abone_soyisim:
               self.talep_abone_soyisim = str(self.talep_abone_soyisim).upper()
          if self.talep_abone_adres:
               self.talep_abone_adres = str(self.talep_abone_adres).upper()
          return

     @api.onchange('talep_abone_tarih_an', 'talep_abone_tarih')
     def set_talepabonetarihan(self):
          if self.talep_abone_tarih_an:
               self.talep_abone_tarih = datetime.now()
               self.talep_abone_tarih_an = False
          return



