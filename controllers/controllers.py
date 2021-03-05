# -*- coding: utf-8 -*-
# from odoo import http


# class RshAccount(http.Controller):
#     @http.route('/rsh_account/rsh_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rsh_account/rsh_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rsh_account.listing', {
#             'root': '/rsh_account/rsh_account',
#             'objects': http.request.env['rsh_account.rsh_account'].search([]),
#         })

#     @http.route('/rsh_account/rsh_account/objects/<model("rsh_account.rsh_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rsh_account.object', {
#             'object': obj
#         })
