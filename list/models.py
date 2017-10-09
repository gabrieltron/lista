
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
				if cur.front == 0:
					break
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
		if new:
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
			for i in range(0, self.size):
				x.append(cur)
				cur = self.row_set.get(id=cur.front)
			x.append(cur)
		except Row.DoesNotExist:
			pass
		return x

class Row(models.Model):
	back = models.IntegerField(default=0)
	front = models.IntegerField(default=0)
	size = models.IntegerField(default=0)
	first_item = models.IntegerField(default=0)
	name = models.TextField()
	board = models.ForeignKey(Board, on_delete=models.CASCADE)

	def sort(self, item, position, new):
		if self.size != 0:
			cur = self.item_set.get(id=self.first_item)
			if position != 0:
				for i in range(0, (position - 1)):
					if cur.front == 0:
						break
					cur = self.item_set.get(id=cur.front)
				item.front = cur.front
				cur.front = item.id
				item.back = cur.id
				if item.front != 0:
					f = self.item_set.get(id=item.front)
					f.back = item.id
					f.save()
				item.save()
				cur.save()
			else:
				item.back = cur.back
				cur.back = item.id
				item.front = cur.id
				self.first_item = item.id
				item.save()
				cur.save()
		else:
			self.first_item = item.id
			item.front = 0
			item.back = 0
			item.save()
		if new:
			self.size+=1
		self.save()

	def remove(self, item, delete):
		cur = self.item_set.get(id=self.first_item)
		for i in range(0, self.size):
			if cur.text == item.text:
				break;
			else:
				cur = self.item_set.get(id=cur.front)
		if cur.back != 0:
			back = self.item_set.get(id=cur.back)
			back.front = cur.front
			back.save()
		else:
			self.first_item = cur.front
		if cur.front != 0:
			front = self.item_set.get(id=cur.front)
			front.back = cur.back
			front.save()
		if delete:
			cur.delete()
		self.size-=1
		self.save()

	def retrieve(self):
		x = []
		print self.size
		try:
			cur = self.item_set.get(id=self.first_item)
			for i in range(0, self.size):
				x.append(cur)
				cur = self.item_set.get(id=cur.front)
		except Item.DoesNotExist:
			pass
		return x

class Item(models.Model):
	back = models.IntegerField(default=0)
	front = models.IntegerField(default=0)
	text = models.TextField()
	row = models.ForeignKey(Row, on_delete=models.CASCADE)
	def __str__(self):
		return self.text
