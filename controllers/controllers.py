# -*- coding: utf-8 -*-
from odoo import http

# class Parqueatracciones(http.Controller):
#     @http.route('/parqueatracciones/parqueatracciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parqueatracciones/parqueatracciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parqueatracciones.listing', {
#             'root': '/parqueatracciones/parqueatracciones',
#             'objects': http.request.env['parqueatracciones.parqueatracciones'].search([]),
#         })

#     @http.route('/parqueatracciones/parqueatracciones/objects/<model("parqueatracciones.parqueatracciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parqueatracciones.object', {
#             'object': obj
#         })