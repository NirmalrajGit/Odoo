# -*- coding: utf-8 -*-
from openerp import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _inherit = ['library.book', 'mail.thread']

    user_id = fields.Many2one('res.partner', string='Held by')
    date_issued = fields.Date('Issue Date')
    due_date = fields.Date('Due Date')
    books_taken_line = fields.One2many('user.history', 'history_id', string='History')


class UserHistory(models.Model):
    _name = 'user.history'

    history_id = fields.Many2one('library.book', string='History_ID')
    title = fields.Char('Book Title')
    date_taken = fields.Date('Date Taken')
    date_return = fields.Date('Date Returned')
