# -*- coding: utf-8 -*-
# from odoo import http


# class FibimNetModule(http.Controller):
#     @http.route('/fibim_net_module/fibim_net_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fibim_net_module/fibim_net_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fibim_net_module.listing', {
#             'root': '/fibim_net_module/fibim_net_module',
#             'objects': http.request.env['fibim_net_module.fibim_net_module'].search([]),
#         })

#     @http.route('/fibim_net_module/fibim_net_module/objects/<model("fibim_net_module.fibim_net_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fibim_net_module.object', {
#             'object': obj
#         })
