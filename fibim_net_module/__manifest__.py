# -*- coding: utf-8 -*-
{
    'name': "FibimNET",
    'summary': "FibimNET Modülü",
    'author': "FibimNET",
    'website': "https://www.fibim.com.tr",
    'sequence': "10",
    'license': "AGPL-3",
    'category': 'Extra Tools',
    'maintainer': "FibimNET",
    'version': '0.1',
    'depends': ['mail', 'product', 'stock', 'board', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'reports/report.xml',
        'reports/musteri_card.xml',
        'views/musteri.xml',
        'views/arizasikayet.xml',
        'views/talepbilgilendirme.xml',
        'views/onaylanantalep.xml',
        'views/oturmaizni.xml',
        'views/tarifeler.xml',
        'views/urundetay.xml',
        'views/ililce.xml',
        'views/mikrotikislemleri.xml',
        'views/istasyonbilgileri.xml',
        'views/bayiislemleri/bolgebayileri.xml',
        'views/bayiislemleri/ilbayileri.xml',
        'views/bayiislemleri/ilcebayileri.xml',
        'views/devrebilgileri/aldigimizdevreler.xml',
        'views/devrebilgileri/sattigimizdevreler.xml',
        'views/uzanti/urunuzanti.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
