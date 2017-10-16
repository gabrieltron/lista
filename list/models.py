
from django.db import models

# Create your models here.
class List(models.Model):
	size = models.IntegerField(default=0)
	first_element = models.IntegerField(default=0)
	class Meta:
		abstract = True

	def retrieve(self, set, exception):
		x = []
		try:
			elements = set()
			print elements
			current = elements.get(id=self.first_element)
			for i in range(0, self.size):
				x.append(current)
				current = elements.get(id=current.front)
				print self.size
				print current
		except exception:
			pass
		return x

	def sort(self, element, position, new, set):
		if self.size != 0:
			current = set.get(id=self.first_element)
			if position != 0:
				for i in range(0, (position - 1)):
					if current.front == 0:
						break
					current = set.get(id=current.front)
				element.front = current.front
				current.front = element.id
				element.back = current.id
				if element.front != 0:
					f = set.get(id=element.front)
					f.back = element.id
					f.save()
				element.save()
				current.save()
			else:
				element.back = 0
				current.back = element.id
				element.front = current.id
				self.first_element = element.id
				element.save()
				current.save()
		else:
			self.first_element = element.id
			element.front = 0
			element.back = 0
			element.save()
		if new:
			self.size+=1
		self.save()

class Board(List):
	username = models.CharField(max_length=50)
	def __str__(self):
		return self.username

	def sort(self, row, position, new):
		return List.sort(self, row, position, new, self.row_set)

	def remove(self, row, delete):
		current = self.row_set.get(id=self.first_element)
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
			self.first_element = current.front
		if current.front != 0:
			front = self.row_set.get(id=current.front)
			front.back = current.back
			front.save()
		if delete:
			current.delete()
		self.size-=1
		self.save()

	def retrieve(self):
		return List.retrieve(self, self.row_set.all, Row.DoesNotExist)

class Element(models.Model):
	back = models.IntegerField(default=0)
	front = models.IntegerField(default=0)
	name = models.TextField()

	class Meta:
		abstract = True

class Row(Element, List):
	board = models.ForeignKey(Board, on_delete=models.CASCADE)

	def sort(self, item, position, new):
		return List.sort(self, item, position, new, self.item_set)

	def remove(self, item, delete):
		current = self.item_set.get(id=self.first_element)
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
			self.first_element = current.front
		if current.front != 0:
			front = self.item_set.get(id=current.front)
			front.back = current.back
			front.save()
		if delete:
			current.delete()
		self.size-=1
		self.save()

	def retrieve(self):
		return List.retrieve(self, self.item_set.all, Item.DoesNotExist)

	def __str__(self):
		return self.name

class Item(Element):
	row = models.ForeignKey(Row, on_delete=models.CASCADE)
	def __str__(self):
		return self.text