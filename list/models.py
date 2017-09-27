
from django.db import models

# Create your models here.
class Board(models.Model):
	username = models.CharField(max_length=50)
	first_row = 0
	def __str__(self):
		return self.username

	def sort(row, position):
		cur = Row.objects.get(id=first_row)
		i = 1
		for cur in range(1, position):
			if (i == position) | (cur.front == 0):
				break
			else:
				cur = Row.objects.get(id=cur.front)
				i+=1
		previous = Row.objects.get(id=cur.back)
		row.front = cur.id
		cur.back = row.id
		previos.front = row.id

	def rows(self):
		cur = Row.objects.get(id=self.first_row)
		x = []
		while cur.front != 0:
			x.append(cur)
			cur = Row.objects.get(id=cur.front)
		x.append(cur)
		return x

class Row(models.Model):
	back = 0;
	front = 0;
	name = models.TextField()
	board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Item(models.Model):
	text = models.TextField()
	row = models.ForeignKey(Row, on_delete=models.CASCADE)
