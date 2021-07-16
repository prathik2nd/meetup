# -*- coding: utf-8 -*-

from odoo import models, fields, api



class meetup(models.Model):
    _name = 'meetup.meetup'
    _description = 'meetup.meetup'

    name = fields.Char('Meetup Name')
    meetfdate = fields.Date('Meeting From Date')
    meettdate = fields.Date('Meeting To Date')    
    mob = fields.Integer('Mobile Number')
    cname = fields.Many2one('meetup.contacts','Contact Name')


class Contacts(models.Model):
    _name = 'meetup.contacts'
    _description = 'meetup.contacts'

    name = fields.Char('Name')
    address = fields.Text('Address')
    email = fields.Char('Email ID')
    phone = fields.Char('Phone No')
  