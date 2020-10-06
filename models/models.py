# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class clinic(models.Model):
    _name = 'clinic.doctor'
    name = fields.Char()
    schedule = fields.One2many('clinic_doctor.schedule', 'schedule_id', string='schedule')


class clinic_line(models.Model):
    _name = 'clinic_doctor.schedule'

    schedule_id = fields.Many2one("clinic.doctor")
    day = fields.Selection([
        ('draft', 'saturday'),
        ('sun', 'sunday'),
        ('mon', 'monday'),
        ('tue', 'tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'thursday'),
        ('fri', 'friday'),
    ], string='day')
    start_date = fields.Float(string="start time")
    end_date = fields.Float(string="end time")
    reservation_status = fields.Boolean(string="reservation status")


class reservations(models.Model):
    _name = 'reservation.date'

    name = fields.Char(string="patient name")
    doctor_name = fields.Many2one("clinic.doctor")
    reservation_time = fields.Float(string="reservation time", digit=(6, 2), required=True)
    reservation_date = fields.Selection([
        ('draft', 'saturday'),
        ('sun', 'sunday'),
        ('mon', 'monday'),
        ('tue', 'tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'thursday'),
        ('fri', 'friday'),
    ], string='reservation date')

    reservation_status = fields.Boolean(string="reservation status")
    _sql_constraints = [
        ('reservation_unique',
         'UNIQUE(reservation_time)',
         "There is reservation in this time"),
    ]

    @api.constrains('reservation_time')
    def _check_something(self):
        for record in self:
            if record.reservation_time >= 23.76:
                raise ValidationError("there isn't booking in this time ")

    def confirm(self):
        for r in self.env['clinic_doctor.schedule'].search([]):
            if (r.day == self.reservation_date) & (r.start_date <= self.reservation_time <= r.end_date):
                self.reservation_status = True
