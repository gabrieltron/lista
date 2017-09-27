# -*- coding: utf-8 -*-

from django.test import TestCase

from .models import Board, Row

# Create your tests here.
class RowModelTests(TestCase):

	def test_ten_rows_created(self):
		board = Board(username='test')
		board.save()
		for count in range(10):
			row = board.row_set.create(name=str(count))
			row.save()
			board.sort(row, row.id, True)
			board.save()
		self.assertIs(board.size, 10)
		all_rows = board.rows()
		self.assertIs(len(all_rows), board.size)
		i = 0
		for row in all_rows:
			self.assertEqual(str(i).decode("utf-8"), row.name)
			i+=1