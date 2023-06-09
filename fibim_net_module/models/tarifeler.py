# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class FibimTarifeler(models.Model):
    _name = 'fibim.tarife'
    _description = 'Tarifeler'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'tarife_adi'

    def tarifeyi_kullanan_musteriler(self):
        return {
            'name': _('Müşteriler'),
            'domain': [],
            'res_model': 'fibim.musteri',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
        }

    tarife_adi = fields.Char(string='Tarife Adı', required=True, track_visibility="always")
    tarife_tipi = fields.Selection([
        ('tarife_bireysel', 'Bireysel'),
        ('tarife_kurumsal', 'Kurumsal'),
        ('tarife_gorevli', 'Görevli'),
    ], default='tarife_bireysel', string="Tarife Tipi", required=True)
    tarife_fiyat = fields.Integer(string='Fiyat', required=True, track_visibility="always")
    tarife_up = fields.Integer(string='Upload Hızı', required=True, track_visibility="always")
    tarife_down = fields.Integer(string='Download Hızı', required=True, track_visibility="always")
    tarife_bitis_tarihi = fields.Date(string='Tarife Bitiş Tarihi')
    tarife_deneme = fields.Boolean(string='Deneme Tarifesi', track_visibility="always")
    tarife_taahhut = fields.Selection([
        ('tarife_taahhutsuz', 'Taahhütsüz'),
        ('tarife_12taahhut', '12 Ay Taahhütlü'),
        ('tarife_24taahhut', '24 Ay Taahhütlü'),
    ], default='tarife_taahhutsuz', string="Taahhüt", required=True)


