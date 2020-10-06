# -*- coding: utf-8 -*-
# from odoo import http


# class Clinic(http.Controller):
#     @http.route('/clinic/clinic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinic/clinic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinic.listing', {
#             'root': '/clinic/clinic',
#             'objects': http.request.env['clinic.clinic'].search([]),
#         })

#     @http.route('/clinic/clinic/objects/<model("clinic.clinic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinic.object', {
#             'object': obj
#         })
