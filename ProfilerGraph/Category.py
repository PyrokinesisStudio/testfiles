import pickle
import sys

class InvalidCategoryName(Exception):
    pass

class Category:
	def __init__(self, name, data):
		self.name = name
		if not name + ":" in data[0][1]:
			raise InvalidCategoryName

		self.data = [(item[0], item[1][self.name + ":"]) for item in data]

	def compare(self, other):
		results = self.info()
		othresults = other.info()
		diffresults = [results[i] - othresults[i] for i in range(len(results))]
		self.display(diffresults)

	def info(self):
		maxtime = 0.0
		mintime = 100000000.0
		averagetime = 0.0
		averageinfluence = 0.0
		for item in self.data:
			pair = item[1]
			time = pair[0]
			influence = pair[1]

			if time < mintime:
				mintime = time
			if time > maxtime:
				maxtime = time

			averagetime += time
			averageinfluence += influence

		return (averagetime / len(self.data), averageinfluence / len(self.data), mintime, maxtime)

	def read(self):
		results = self.info()
		self.display(results)

	def display(self, results):
		print("Category:", self.name)
		print("\t Average time:\t\t", results[0], " ms")
		print("\t Average influence:\t", results[1], " %")
		print("\t Min time:\t\t", results[2], " ms")
		print("\t Max time:\t\t", results[3], " ms")
