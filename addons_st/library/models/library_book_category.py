
from openerp import models, fields, api

class BookCategory(models.Model):
    _name = 'book.category'

    name = fields.Char('Category')
    number_of_books = fields.Integer('Total number of books')
    parent_id = fields.Many2one('book.category', string='Parent', ondelete='restrict', index=True)
    child_ids = fields.One2many('book.category', 'parent_id', string='Child')

    _parent_store = True
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive categories.')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'Book Title should be unique')]

