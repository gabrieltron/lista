
from django.db import models

# Create your models here.
class Board(models.Model):
	username = models.CharField(max_length=50)
	first_row = models.IntegerField(default=0)
	size = models.IntegerField(default=0)
	def __str__(self):
		return self.username

	def sort(self, row, position, new):
		if self.size != 0:
			cur = self.row_set.get(id=self.first_row)
			for i in range(0, (position - 1)):
				cur = self.row_set.get(id=cur.front)
			row.front = cur.front
			cur.front = row.id
			row.back = cur.id
			if row.front != 0:
				f = self.row_set.get(id=row.front)
				f.back = row.id
				f.save()
			row.save()
			cur.save()
		else:
			self.first_row = row.id
			row.front = 0
			row.back = 0
			row.save()
		self.size+=1
		self.save()

	def remove(self, row, delete):
		cur = self.row_set.get(id=self.first_row)
		for i in range(0, self.size):
			if cur.name == row.name:
				break;
			else:
				cur = self.row_set.get(id=cur.front)
		if cur.back != 0:
			back = self.row_set.get(id=cur.back)
			back.front = cur.front
			back.save()
		else:
			self.first_row = cur.front
		if cur.front != 0:
			front = self.row_set.get(id=cur.front)
			front.back = cur.back
			front.save()
		if delete:
			cur.delete()
		self.size-=1
		self.save()

	def retrieve(self):
		x = []
		try:
			cur = self.row_set.get(id=self.first_row)
			while cur.front != 0:
				x.append(cur)
				cur = self.row_set.get(id=cur.front)
			x.append(cur)
		except Row.DoesNotExist:
			pass
		return x

class Row(models.Model):
	back = models.IntegerField(default=0)
	front = models.IntegerField(default=0)
	name = models.TextField()
	board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Item(models.Model):
	text = models.TextField()
	row = models.ForeignKey(Row, on_delete=models.CASCADE)
