# -*- coding: utf-8 -*-
from odoo import http


class Meetup(http.Controller):
    @http.route('/meetup/meetup/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/meetup/meetup/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('meetup.listing', {
            'root': '/meetup/meetup',
            'objects': http.request.env['meetup.meetup'].search([]),
        })

    @http.route('/meetup/meetup/objects/<model("meetup.meetup"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('meetup.object', {
            'object': obj
        })
