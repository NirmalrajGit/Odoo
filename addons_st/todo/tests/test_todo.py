# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):

    def test_create(self):
        ' Create a simple ToDo '
        todo = self.env['todo.task']
        task = todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)
