#################################################################
# SortArrayOne.py
#################################################################
# Source Title: SortArray.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Course: Data Structures
# CH7 - Advanced Sorting
# HW4 - WK4
# Programming Project 7.2
#################################################################
# This program implement a sortable Array data structure
#################################################################

class Array(object):
	def __init__(self, initialSize):
		self.__a = [None] * initialSize
		self.__nItems = 0

		# counters for homework
		self.__totalCopies = 0
		self.__totalKeyComparisons = 0

# This method returns the total number of items in an array
##########################################################################################
	def __len__(self):
		return self.__nItems

# This method returns the value at a given index if the index is within bounds
##########################################################################################
	def get(self, n):
		if 0 <= n and n < self.__nItems: # checking if index is in bounds
			return self.__a[n]

# This method inserts an index and its coordinating value if the index  in bounds
##########################################################################################
	def set(self, n, value):
		if 0 <= n and n < self.__nItems: # checking if index in bounds
			self.__a[n] = value # setting the index & value

# This method swaps the values at two given indices if they are in bounds
##########################################################################################
	def swap(self, j, k):
		if ((0 <= j) & (j < self.__nItems) & (0 <= k) & (k < self.__nItems)): # checking bounds
			self.__a[j], self.__a[k] = self.__a[k], self.__a[j] # swapping values

# This method inserts an index/value pair if the array is not full
##########################################################################################
	def insert(self, item):
		if self.__nItems >= len(self.__a): # check if array full
			raise Exception("Array overflow")
		self.__a[self.__nItems] = item # insert index value pair if array not full
		self.__nItems += 1 # increment total values

# This method searches for a value in the array. The value is returned if it is found
# A -1 is returned if the value is not found
##########################################################################################
	def find(self, item):
		for j in range(self.__nItems): # search for value
			if self.__a[j] == item:
				return j # return value if found
		return -1 # return -1 if not found

# This method searches for a value and returns it if found
##########################################################################################
	def search(self, item):
		return self.get(self.find(item))

# This method deletes the first occurrence of a value by moving all the values to the left
# of it to the right by one. It returns true if the value was found and returns false if
# the value was not found
##########################################################################################
	def delete(self, item):
		for j in range(self.__nItems):
			if self.__a[j] == item: # if value found
				self.__nItems -= 1 # lower the count of the total number of items
				for k in range(j, self.__nItems): # range = index of value to end of array
					self.__a[k] = self.__a[k + 1] # move all values to right to delete value
				return True
		return False # return false if value not found

# This method deletes the last value in an array
##########################################################################################
	def deleteLast(self, n=1):
		for j in range(min(n, self.__nItems)):
			self.__nItems -= 1 # lower the count of total values by 1
			self.__a[self.__nItems] = None

# This method prints all values in an array by applying the print function to each value
##########################################################################################
	def traverse(self, function=print):
		for j in range(self.__nItems):
			function(self.__a[j])

# This method is a special method for the str() function to print all values
##########################################################################################
	def __str__(self):
		ans = "["
		for i in range(self.__nItems):
			if len(ans) > 1:
				ans += ", "
			ans += str(self.__a[i])
		ans += "]"
		return ans

# This method prints the total number of items copied and total number of key comparisons
##########################################################################################
	def printCopiesAndCounters(self):
		print(f"Total Copies: {self.__totalCopies}")
		print(f"Total Key Comparisons: {self.__totalKeyComparisons}")
