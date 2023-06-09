# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from zeep import Client
client = Client(wsdl='https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?wsdl')

class FibimMusteri(models.Model):
    _name = 'fibim.musteri'
    _description = 'Müşteri Kayıt'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'abone_no'
    _order = "abone_uyelik_bas"


    @api.constrains('abone_sifre')
    def check_sifre(self):
        for rec in self:
            if rec.abone_sifre > 999999:
                raise ValidationError("Şifre En Fazla 6 Hane Olabilir")


    abone_no = fields.Char(string='Abone No')
    abone_kullanici_isim = fields.Char(string='Kullanıcı Adı')
    abone_isim = fields.Char(string='İsim')
    abone_anne_isim = fields.Char(string='Anne Adı')
    abone_baba_isim = fields.Char(string='Baba Adı')
    abone_soyisim = fields.Char(string='Soyisim')
    abone_tel = fields.Char(string='Telefon', track_visibility="always")
    abone_uyelik_bas = fields.Datetime(string='Üyelik Tarihi')
    abone_uyelik_bit = fields.Datetime(string='Üyelik Bitiş Tarihi', track_visibility="always")
    abone_adres = fields.Char(string='Adres', track_visibility="always")
    abone_tarife = fields.Many2one('fibim.tarife', string='Tarife', track_visibility="always")
    abone_durum = fields.Selection([
        ('abone_aktif', 'Aktif'),
        ('abone_pasif', 'Pasif'),
        ('abone_iptal', 'İptal Et'),
    ], default='abone_aktif', string="Durum", track_visibility="always")
    abone_modem_ucret = fields.Selection([
        ('abone_modem_kiralik', 'Kiralık (Tarifeye Ek +5 ₺)'),
        ('abone_modem_depozito', 'Depozitolu (200 ₺)'),
    ], default='abone_modem_kiralik', string="Modem Ücreti", track_visibility="always")
    abone_tc = fields.Char(string='TC No')
    abone_dogum_tarihi = fields.Date(string='Doğum Tarihi')
    abone_fatura_adres = fields.Text(string='Fatura Adresi', track_visibility="always")
    abone_mail = fields.Char(string='E-mail', track_visibility="always")
    abone_sifre = fields.Integer(string='Şifre', track_visibility="always")
    abone_urun = fields.Many2many('stock.production.lot', string='Ürün Bilgileri', track_visibility="always")
    abone_mikrotik = fields.Many2one('fibim.mikrotikislemleri', string='Mikrotik Bilgisi', track_visibility="always")
    abone_ililce = fields.Many2one('fibim.ililce', string='İlçe', track_visibility="always")
    abone_il = fields.Char(related='abone_ililce.turkiye_il', string='İl', track_visibility="always")
    abone_faturaililce = fields.Many2one('fibim.ililce', string='İlçe', track_visibility="always")
    abone_faturail = fields.Char(related='abone_faturaililce.turkiye_il', string='İl', track_visibility="always")
    abone_teknikservis = fields.Many2one('hr.employee', string='Teknik Servis Bilgisi', track_visibility="always")
    abone_tarife_fiyat = fields.Integer(related='abone_tarife.tarife_fiyat', string='Tarife Ücreti', track_visibility="always")
    abone_tarife_down = fields.Integer(related='abone_tarife.tarife_down', string='D', track_visibility="always")
    abone_tarife_up = fields.Integer(related='abone_tarife.tarife_up', string='U', track_visibility="always")
    abone_dogum_yeri = fields.Char(string='Doğum Yeri')
    abone_id = fields.Char(default=lambda self: self.env['ir.sequence'].next_by_code('fibim.musteri.id'))
    abone_il_kodu = fields.Char(related='abone_ililce.turkiye_il_kodu')
    abone_ilce_kodu = fields.Char(related='abone_ililce.turkiye_ilce_kodu')
    abone_bolge_bayi = fields.Many2one('fibim.bolgebayileri', string='Bölge Bayi Bilgisi',
                                         track_visibility="always")
    abone_il_bayi = fields.Many2one('fibim.ilbayileri', string='İl Bayi Bilgisi',
                                         track_visibility="always")
    abone_ilce_bayi = fields.Many2one('fibim.ilcebayileri', string='İlçe Bayi Bilgisi',
                                         track_visibility="always")
    abone_dogrulama = fields.Boolean(string='Abone Doğrulama')

    #@api.onchange('abone_no','abone_il_kodu','abone_ilce_kodu','abone_id')
    #def set_no(self):
    #    self.abone_no = str(self.abone_il_kodu) + str(self.abone_ilce_kodu) + self.abone_id
    #    return
    #
    #@api.model
    #def create(self, vals):
    #    if vals.get('abone_id', _('New')) == _('New'):
    #
    #            vals['abone_id'] = self.env['ir.sequence'].next_by_code('fibim.musteri.id') or _('New')
    #
    #
    #    result = super(FibimMusteri, self).create(vals)
    #    return result

    @api.onchange('abone_isim', 'abone_soyisim', 'abone_dogum_yeri', 'abone_mail','abone_anne_isim','abone_baba_isim','abone_adres','abone_fatura_adres','abone_kullanici_isim')
    def set_upperlower(self):
        if self.abone_isim:
            self.abone_isim = str(self.abone_isim).upper()
        if self.abone_soyisim:
            self.abone_soyisim = str(self.abone_soyisim).upper()
        if self.abone_dogum_yeri:
            self.abone_dogum_yeri = str(self.abone_dogum_yeri).upper()
        if self.abone_mail:
            self.abone_mail = str(self.abone_mail).upper()
        if self.abone_anne_isim:
            self.abone_anne_isim = str(self.abone_anne_isim).upper()
        if self.abone_baba_isim:
            self.abone_baba_isim = str(self.abone_baba_isim).upper()
        if self.abone_adres:
            self.abone_adres = str(self.abone_adres).upper()
        if self.abone_fatura_adres:
            self.abone_fatura_adres = str(self.abone_fatura_adres).upper()
        if self.abone_kullanici_isim:
            self.abone_kullanici_isim = str(self.abone_kullanici_isim).lower()
        return

    @api.onchange('abone_dogrulama', 'abone_tc', 'abone_isim', 'abone_soyisim', 'abone_dogum_tarihi')
    def set_dogrulama(self):
        if self.abone_tc and self.abone_dogum_tarihi:
            if self.abone_tc.isdigit():
                self.abone_dogrulama = client.service.TCKimlikNoDogrula(int(self.abone_tc), self.abone_isim, self.abone_soyisim, int(self.abone_dogum_tarihi.year))
                return
            else:
                self.abone_dogrulama = False
        else:
            self.abone_dogrulama = False

