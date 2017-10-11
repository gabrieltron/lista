
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
			current = self.row_set.get(id=self.first_row)
			for i in range(0, (position - 1)):
				if current.front == 0:
					break
				current = self.row_set.get(id=current.front)
			row.front = current.front
			current.front = row.id
			row.back = current.id
			if row.front != 0:
				f = self.row_set.get(id=row.front)
				f.back = row.id
				f.save()
			row.save()
			current.save()
		else:
			self.first_row = row.id
			row.front = 0
			row.back = 0
			row.save()
		if new:
			self.size+=1
		self.save()

	def remove(self, row, delete):
		current = self.row_set.get(id=self.first_row)
		for i in range(0, self.size):
			if current.name == row.name:
				break;
			else:
				current = self.row_set.get(id=current.front)
		if current.back != 0:
			back = self.row_set.get(id=current.back)
			back.front = current.front
			back.save()
		else:
			self.first_row = current.front
		if current.front != 0:
			front = self.row_set.get(id=current.front)
			front.back = current.back
			front.save()
		if delete:
			current.delete()
		self.size-=1
		self.save()

	def retrieve(self):
		x = []
		try:
			rows = self.row_set.all()
			current = rows.get(id=self.first_row)
			for i in range(0, self.size):
				x.append(current)
				current = rows.get(id=current.front)
			x.append(current)
		except Row.DoesNotExist:
			pass
		return x

class Element(models.Model):
	back = models.IntegerField(default=0)
	front = models.IntegerField(default=0)

	class Meta:
		abstract = True

class Row(Element):
#	back = models.IntegerField(default=0)
#	front = models.IntegerField(default=0)
	size = models.IntegerField(default=0)
	first_item = models.IntegerField(default=0)
	name = models.TextField()
	board = models.ForeignKey(Board, on_delete=models.CASCADE)

	def sort(self, item, position, new):
		if self.size != 0:
			current = self.item_set.get(id=self.first_item)
			if position != 0:
				for i in range(0, (position - 1)):
					if current.front == 0:
						break
					current = self.item_set.get(id=current.front)
				item.front = current.front
				current.front = item.id
				item.back = current.id
				if item.front != 0:
					f = self.item_set.get(id=item.front)
					f.back = item.id
					f.save()
				item.save()
				current.save()
			else:
				item.back = 0
				current.back = item.id
				item.front = current.id
				self.first_item = item.id
				item.save()
				current.save()
		else:
			self.first_item = item.id
			item.front = 0
			item.back = 0
			item.save()
		if new:
			self.size+=1
		self.save()

	def remove(self, item, delete):
		current = self.item_set.get(id=self.first_item)
		j = 0
		for i in range(0, self.size):
			if current.text == item.text:
				break;
			else:
				current = self.item_set.get(id=current.front)
				j+=1
		if j != 0:
			back = self.item_set.get(id=current.back)
			back.front = current.front
			back.save()
		else:
			self.first_item = current.front
		if current.front != 0:
			front = self.item_set.get(id=current.front)
			front.back = current.back
			front.save()
		if delete:
			current.delete()
		self.size-=1
		self.save()

	def retrieve(self):
		x = []
		try:
			rows = self.item_set.all()
			current = rows.get(id=self.first_item)
			for i in range(0, self.size):
				x.append(current)
				current = rows.get(id=current.front)
		except Item.DoesNotExist:
			pass
		return x

	def __str__(self):
		return self.name

class Item(Element):
#	back = models.IntegerField(default=0)
#	front = models.IntegerField(default=0)
	text = models.TextField()
	row = models.ForeignKey(Row, on_delete=models.CASCADE)
	def __str__(self):
		return self.text