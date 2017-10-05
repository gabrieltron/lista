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
			board.sort(row, board.size)
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
		board.remove(old_rows[0])
		board.remove(old_rows[5])
		board.remove(old_rows[9])
		new_rows = board.retrieve()
		self.assertIs(board.size, 7)
		i = 1
		for row in new_rows:
			self.assertEqual(str(i).decode("utf-8"), row.name)
			if (i == 4):
				i+=1
			i+=1

	def test_delete_empty(self):
		board = self.create_ten_rows()
		rows = board.retrieve()
		for row in rows:
			board.remove(row)
		self.assertIs(board.size, 0)
		self.assertTrue(board.retrieve() == [])
		with self.assertRaises(Row.DoesNotExist):
			board.row_set.get(id=board.first_row)

	def test_destroy_then_create(self):
		board = self.create_ten_rows()
		rows = board.retrieve()
		for row in rows:
			board.remove(row)
		self.assertIs(board.size, 0)
		x = []
		for count in range(10):
			row = board.row_set.create(name=str(count))
			x.append(row)
		row.save()
		board.sort(x[3], 0)
		board.sort(x[9], 1)
		board.sort(x[2], 2)
		board.sort(x[0], 3)
		board.sort(x[1], 4)
		board.sort(x[7], 5)
		board.sort(x[4], 6)
		board.sort(x[6], 7)
		board.sort(x[5], 8)
		board.sort(x[8], 9)

		new_rows = board.retrieve()
		i = 0
		for row in new_rows:
			if i == 0:
				self.assertEqual(str(x[3].name).decode("utf-8"), row.name)
			if i == 1:
				self.assertEqual(str(x[9].name).decode("utf-8"), row.name)
			if i == 2:
				self.assertEqual(str(x[2].name).decode("utf-8"), row.name)
			if i == 3:
				self.assertEqual(str(x[0].name).decode("utf-8"), row.name)
			if i == 4:
				self.assertEqual(str(x[1].name).decode("utf-8"), row.name)
			if i == 5:
				self.assertEqual(str(x[7].name).decode("utf-8"), row.name)
			if i == 6:
				self.assertEqual(str(x[4].name).decode("utf-8"), row.name)
			if i == 7:
				self.assertEqual(str(x[6].name).decode("utf-8"), row.name)
			if i == 8:
				self.assertEqual(str(x[5].name).decode("utf-8"), row.name)
			if i == 9:
				self.assertEqual(str(x[8].name).decode("utf-8"), row.name)
			i+=1