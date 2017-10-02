# -*- coding: utf-8 -*-

from django.test import TestCase

from .models import Board, Row

# Create your tests here.
class RowModelTests(TestCase):

	def create_ten_rows(self):
		board = Board(username='test')
		board.save()
		for count in range(10):
			row = board.row_set.create(name=str(count))
			row.save()
			board.sort(row, row.id, True)
		return board

	def test_ten_rows_created(self):
		board = self.create_ten_rows()
		self.assertIs(board.size, 10)
		all_rows = board.retrieve()
		self.assertIs(len(all_rows), board.size)
		i = 0
		for row in all_rows:
			self.assertEqual(str(i).decode("utf-8"), row.name)
			i+=1

	def test_destroy(self):
		board = self.create_ten_rows()
		old_rows = board.retrieve()
		board.remove(old_rows[0], True)
		board.remove(old_rows[5], True)
		board.remove(old_rows[9], True)
		new_rows = board.retrieve()
		self.assertIs(board.size, 7)
		i = 1
		for row in new_rows:
			self.assertEqual(str(i).decode("utf-"), row.name)
			if (i == 4):
				i+=1
			i+=1
