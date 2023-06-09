# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime


class FibimOnaylanantalep(models.Model):
     _name = 'fibim.onaylanantalep'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Onaylanan Talep'
     _rec_name = 'onaytalep_abone_isim'
     _order = "onaytalep_abone_tarih desc"

     def onaytalep_whatsapptus(self):
          return {
               'res_model': 'ir.actions.act_url',
               'type': 'ir.actions.act_url',
               'target': '_blank',
               'url': self.onaytalep_whatsappotomesaj
          }

     onaytalep_abone_isim = fields.Char(string='İsim')
     onaytalep_abone_soyisim = fields.Char(string='Soyisim')
     onaytalep_abone_tel = fields.Char(string='Telefon', track_visibility="always")
     onaytalep_abone_adres = fields.Char(string='Adres', track_visibility="always")
     onaytalep_abone_aciklama = fields.Char(string='Açıklama', track_visibility="always")
     onaytalep_abone_olusturan = fields.Many2one('res.users','Aboneliği Oluşturan', default=lambda self: self.env.user)
     onaytalep_abone_ililce = fields.Many2one('fibim.ililce', string='İlçe', track_visibility="always")
     onaytalep_abone_il = fields.Char(related='onaytalep_abone_ililce.turkiye_il', string='İl', track_visibility="always")
     onaytalep_abone_tarih = fields.Datetime(string='Tarih', track_visibility="always")
     onaytalep_abone_tarih_an = fields.Boolean()
     onaytalep_whatsappotomesaj = fields.Char()
     onaytalep_abone_durumu = fields.Boolean()
     onaytalep_abone_durumu_yazi = fields.Char(string='Durum', track_visibility="always")
     onaytalep_abone_hiz = fields.Selection([
          ('onaytalep_hiz5', '5 Mbps'),
          ('onaytalep_hiz10', '10 Mbps'),
          ('onaytalep_hiz15', '15 Mbps'),
          ('onaytalep_hiz20', '20 Mbps'),
          ('onaytalep_hiz25', '25 Mbps'),
          ('onaytalep_hiz35', '35 Mbps'),
          ('onaytalep_hiz50', '50 Mbps'),
          ('onaytalep_hiz100', '100 Mbps'),
     ], string="Hız Talebi", track_visibility="always")
     onaytalep_abone_tur = fields.Selection([
          ('onaytalep_abone_bireysel', 'Bireysel'),
          ('onaytalep_abone_kurumsal', 'Kurumsal'),
          ('onaytalep_abone_esnaf', 'Esnaf'),
     ], string="Tür")

     @api.onchange('onaytalep_abone_durumu_yazi', 'onaytalep_abone_durumu')
     def set_onaytalepabonedurumuyazi(self):
          if self.onaytalep_abone_durumu:
               self.onaytalep_abone_durumu_yazi = 'Kurulum Yapıldı'
          else:
               self.onaytalep_abone_durumu_yazi = 'Kurulum Yapılmadı'
          return

     @api.onchange('onaytalep_abone_isim', 'onaytalep_abone_soyisim', 'onaytalep_abone_tel', 'onaytalep_abone_adres',
                   'onaytalep_abone_aciklama')
     def set_onaytalepwhatsappotomesaj(self):
          self.onaytalep_whatsappotomesaj = "https://wa.me/905331346164?text=" + str(self.onaytalep_abone_isim) + " " + str(self.onaytalep_abone_soyisim) + " " + str(self.onaytalep_abone_tel) + " " + str(self.onaytalep_abone_adres) + " " + str(self.onaytalep_abone_aciklama)
          self.onaytalep_whatsappotomesaj = self.onaytalep_whatsappotomesaj.replace(" ", "%20")
          self.onaytalep_whatsappotomesaj = self.onaytalep_whatsappotomesaj.replace("False", "")
          return

     @api.onchange('onaytalep_abone_isim', 'onaytalep_abone_soyisim', 'onaytalep_abone_adres')
     def set_upperlower(self):
          if self.onaytalep_abone_isim:
               self.onaytalep_abone_isim = str(self.onaytalep_abone_isim).upper()
          if self.onaytalep_abone_soyisim:
               self.onaytalep_abone_soyisim = str(self.onaytalep_abone_soyisim).upper()
          if self.onaytalep_abone_adres:
               self.onaytalep_abone_adres = str(self.onaytalep_abone_adres).upper()
          return

     @api.onchange('onaytalep_abone_tarih_an', 'onaytalep_abone_tarih')
     def set_talepabonetarihan(self):
          if self.onaytalep_abone_tarih_an:
               self.onaytalep_abone_tarih = datetime.now()
               self.onaytalep_abone_tarih_an = False
          return



