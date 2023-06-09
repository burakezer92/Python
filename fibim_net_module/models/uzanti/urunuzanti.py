# -*- coding: utf-8 -*-

from odoo import models, fields


class UrunUzanti(models.Model):
     _inherit = 'product.template'

     urun_uzanti_detay = fields.Many2one('fibim.urundetay', string='Ürün Detay', required=True)
     urun_uzanti_marka = fields.Char(related = 'urun_uzanti_detay.urun_marka', string='Marka')
     urun_uzanti_model = fields.Char(related = 'urun_uzanti_detay.urun_model', string='Model')
     urun_uzanti_ozellik = fields.Text(related='urun_uzanti_detay.urun_ozellik', string='Özellik')



