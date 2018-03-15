# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp
from openerp.fields import Date as dt


class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char('Title', required=True)
    image = fields.Binary('Image')
    description = 'Library Book'
    cost_price = fields.Float('Book Cost', dp.get_precision('Book Price'))
    in_stock = fields.Boolean('In Stock', default=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary('Retail Price', currency_field='currency_id')
    date_release = fields.Date('Release date', default=fields.Date.today())
    author_ids = fields.Many2many('res.partner', string='Authors')
    issue_line = fields.One2many('issue.history', 'issue_id', string='Issue History',
                                     help='Dates of Issue/Return history of the book')

    @api.constrains('date_release')
    def _check_date_release(self):
        for r in self:
            if r.date_release > dt.today():
                raise models.ValidationError('Release date cannot be in future.')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'Book Title should be unique!')]


class IssueHistory(models.Model):
    _name = 'issue.history'

    issue_id = fields.Many2one('library.book', string='issue_ID')
    issue_date = fields.Date('Date Issued')
    return_date = fields.Date('Date Returned')
    lib_user = fields.Many2one('res.partner', string='User')

