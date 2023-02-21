#################################################################
# QuickSort.py
#################################################################
# Author: gametechmatch
# Course: Data Structures
# CH7 - Advanced Sorting
# HW4 - WK4
# Programming Project 7.2
#################################################################
# Source Title: QuickSort.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# This program implements a Quicksort for Arrays using previous Array class
#################################################################
totalCopies = 0
totalKeyComparisons = 0


import SortArrayOne

class Array(SortArrayOne.Array):

##########################################################################################
# This method executes the median-of-three partitioning technique by finding the median
# of lo, middle, and hi keys in a subarray and placing the median of the three values in
# the highest index for the partitioning code that comes later
##########################################################################################
	def medianOfThree(self, lowestIndexOfSubArray, highestIndexOfSubArray):
		# Calculate the middle index
		midIndex = (lowestIndexOfSubArray + highestIndexOfSubArray) // 2

		# Swap values in low and mid indicies if value in low > value in mid
		self.__totalKeyComparisons += 1
		if (self.get(lowestIndexOfSubArray)) > (self.get(midIndex)):
			self.__totalCopies += 3
			self.swap(lowestIndexOfSubArray, midIndex)

		# Swap values in low and high indicies if value in low > value in high
		self.__totalKeyComparisons += 1
		if (self.get(lowestIndexOfSubArray)) > (self.get(highestIndexOfSubArray)):
			self.__totalCopies += 3
			self.swap(lowestIndexOfSubArray, highestIndexOfSubArray)

		# Swap values in high and mid indicies if value in high > value in mid
		self.__totalKeyComparisons += 1
		if (self.get(highestIndexOfSubArray)) > (self.get(midIndex)):
			self.__totalCopies += 3
			self.swap(highestIndexOfSubArray, midIndex)

		# Return the highest index of the sub-array which is now pointing to
		# the median of the three values found
		return self.get(highestIndexOfSubArray)

##########################################################################################
# This method executes an insertion sort on small sub-arrays received specifically
# from the quicksort method
# It moves forward through the array pushing back lower values and shifting the higher
# values forward to make room for the lower values being inserted in the lower indicies
##########################################################################################
	def insertionSort(self, lowestIndexOfSubArray=0, highestIndexOfSubArray=None):
		# Set the high index pointer to the last item in the array if not already specified
		if highestIndexOfSubArray is None:
			highestIndexOfSubArray = len(self) - 1

		# Mark one item & store the marked item in temp
		for unsortedSectionPointer in range(lowestIndexOfSubArray + 1, highestIndexOfSubArray + 1):
			self.__totalCopies += 1
			temp = self.get(unsortedSectionPointer) # temp holds the value of the item we are checking

			# Move the sorting pointer to catch up to the pointer keeping track of segment that we
			# have sorted so far
			sortingPointer = unsortedSectionPointer

			# If the sorting pointer has not reached the beginning of the array (side that holds the
			# lowest values) and if the current value we are looking at (held in temp) is smaller than the
			# value before it, then move the sorting pointer one more towards the lower indicies to
			# compare the 'temp' value to the value in the data structure before it. Repeat this until
			# finding where the temp value can be inserted in the array
			checking = True
			while checking == True:

				# This 'if' statement checks if we have found where the value held in 'temp' can be
				# inserted into the array. If the value before the current index is greater than
				# the value held in 'temp', then the code under the if statement decrements the sorting
				# pointer and moves the higher value element forward one with each iteration of the while loop
				if ((sortingPointer > lowestIndexOfSubArray) and (temp < self.get(sortingPointer - 1))):
					self.__totalKeyComparisons += 1
					self.__totalCopies += 1

					# set prior value in array (that is greater than 'temp') forward by 1 index
					self.set(sortingPointer, self.get(sortingPointer - 1)) #.set(index, value)

					# move the sorting pointer down one
					sortingPointer -= 1

				# This else statement just counts a key comparison if we have either arrived at the beginning
				# of the array or if the temp value did not have to be moved on this iteration of the while loop
				else:
					self.__totalKeyComparisons += 1
					checking = False

			# Save the value held in 'temp' to its proper location in the array
			self.__totalCopies += 1
			self.set(sortingPointer, temp)

##########################################################################################
# This private method partitions an array based on the given pivot value and sends values
# lower than the pivot value in lower indicies than the pivot and vice versa for higher values
##########################################################################################
	def __part(self, pivot, lowestIndexOfSubArray, highestIndexOfSubArray):
		# Loop until there are not any more items to inspect
		while lowestIndexOfSubArray <= highestIndexOfSubArray:

			# Increment the lowestIndexOfSubArray until we find a value equal to or greater
			# than the pivot value.
			while (self.get(lowestIndexOfSubArray)) < (pivot):
				lowestIndexOfSubArray += 1
				self.__totalKeyComparisons += 1

			# Decrement the highestIndexOfSubArray until we find a value less than or equal to
			# the pivot value
			while (pivot) < (self.get(highestIndexOfSubArray)):
				highestIndexOfSubArray -= 1
				self.__totalKeyComparisons += 1

			# If the lowest index is greater than or equal to the highest index, then return
			# the lowest index of the subarray
			if lowestIndexOfSubArray >= highestIndexOfSubArray:
				return lowestIndexOfSubArray

			# otherwise, swap the values where the lowestIndexOfSubArray is currently pointing
			# with the value where the highestIndexOfSubArray is currently pointing
			self.__totalCopies += 3
			self.swap(lowestIndexOfSubArray, highestIndexOfSubArray)

			# Continue partitioning in between by then incrementing the lower index by one
			# and decreasing the high index by one
			lowestIndexOfSubArray, highestIndexOfSubArray = lowestIndexOfSubArray + 1, highestIndexOfSubArray - 1

		# Partitioning is now complete. Return the low index
		return lowestIndexOfSubArray

##########################################################################################
# This method executes a quicksort sorting algorithm.
# For subarrays at or below the cut-off point (default 3), it uses insertion sort. For
# larger arrays, it uses the median of three partitioning technique and recursive calls
# to itself to further partition and sort the rest of the array
##########################################################################################
	def quicksort(self, lowestIndexOfSubArray=0, highestIndexOfSubArray=None, short=3):

		# If the high index is not specified, set it equal to the highest index in the
		# array
		if highestIndexOfSubArray is None:
			highestIndexOfSubArray = len(self) - 1

		# Set a value where any subarrays with a total number of elements equal to or
		# less than that value get sorted by the insertion sort rather than getting
		# sent to the median of three partitioning function
		short = max(3, short)

# Find the right pivot value############################################################
		# If subarray is at or below our cutoff (short), then use insertion sort
		if highestIndexOfSubArray - lowestIndexOfSubArray + 1 <= short:
			return self.insertionSort(lowestIndexOfSubArray, highestIndexOfSubArray)

		# Else, find the middle index (nextPivotIndex) that will be included in the high part of the
		# next partition by doing a small sort that puts 3 values in known locations on the subarray
		# and returning the highest of the three values placed where the array will
		# be partitioned (highest of 3 values now held where 'nextPivotIndex' is pointing to
		nextPivotIndex = self.medianOfThree(lowestIndexOfSubArray, highestIndexOfSubArray)

# Partition the array###################################################################
		# Create an index (partitionIndex) to use in further partitioning the array
		# while doing a bit more sorting
		partitionIndex = self.__part(nextPivotIndex, lowestIndexOfSubArray + 1, highestIndexOfSubArray - 1)

		# swap the value at the partitionIndex with the value at the highestIndexOfSubArray so that
		# the middle value found in the medianOfThree function is now housed at the index(partitionIndex)
		# where the array will be parted
		self.__totalCopies += 3
		self.swap(partitionIndex, highestIndexOfSubArray)

		# sort the two subarrays.
		# The partitionIndex will be excluded because it can stay where it is in the full array.
		# (all values in lower part are already less than value held in partitionIndex and all
		# in higher part are already higher than value held in partitionIndex)
		self.quicksort(lowestIndexOfSubArray, partitionIndex - 1, short) # lower part
		self.quicksort(partitionIndex + 1, highestIndexOfSubArray, short) # higher par

##########################################################################################
# This method executes the backward median-of-three partitioning technique. This version
# is used for a descending quicksort
##########################################################################################
	def backwardMedianOfThree(self, lowestIndexOfSubArray, highestIndexOfSubArray):
		# Calculate the middle index
		midIndex = (lowestIndexOfSubArray + highestIndexOfSubArray) // 2

# Sorting and comparing 3 values at 3 indicies (lowest, middle, and highest indicies)
		# Swap values in low and mid indicies if value in low index < value in midIndex
		self.__totalKeyComparisons += 1
		if (self.get(lowestIndexOfSubArray)) < (self.get(midIndex)):
			self.__totalCopies += 3
			self.swap(lowestIndexOfSubArray, midIndex)

		# Swap values in low and high indicies if value in low index < value in high index
		self.__totalKeyComparisons += 1
		if (self.get(lowestIndexOfSubArray)) < (self.get(highestIndexOfSubArray)):
			self.__totalCopies += 3
			self.swap(lowestIndexOfSubArray, highestIndexOfSubArray)

# Swapping values at midIndex and highest index to have a trigger point for a future sort to stop
# (in the middle index which will hold the lowest value of the 3 values checked after this if statement)
		# Swap values in high and mid indicies if value in high < value in mid
		self.__totalKeyComparisons += 1
		if (self.get(highestIndexOfSubArray)) < (self.get(midIndex)):
			self.__totalCopies += 3
			self.swap(highestIndexOfSubArray, midIndex)

		# Return the highest index of the sub-array which is now pointing to
		# the median of the three values found
		return self.get(highestIndexOfSubArray)

##########################################################################################
# This method executes a backward insertion sort
##########################################################################################
	def backwardInsertionSort(self, lowestIndexOfSubArray=0, highestIndexOfSubArray=None):
		# Set the high index pointer to the last item in the array if not already specified
		if highestIndexOfSubArray is None:
			highestIndexOfSubArray = len(self) - 1

		# Mark one item & store the marked item in temp
		for unsortedSectionPointer in range(lowestIndexOfSubArray + 1, highestIndexOfSubArray + 1):
			self.__totalCopies += 1
			temp = self.get(unsortedSectionPointer) # temp holds the value of the item we are checking

			# Move the sorting pointer to catch up to the unsorted section pointer
			sortingPointer = unsortedSectionPointer

			# Sort the values
			checking = True
			while checking == True:

				# If the sorting pointer has not reached the beginning of the array (side
				# that holds the lowest indexes and eventually the highest values) and
				# if the current value we are looking at (temp) is greater than the value before it,
				# then move the sorting pointer one index towards the side of the array with the
				# index 0 and move the prior value forward. The while loop will repeat until we have
				# found the correct location for the value being held in temp
				if ((sortingPointer > lowestIndexOfSubArray) and (temp > self.get(sortingPointer - 1))):
					self.__totalKeyComparisons += 1
					self.__totalCopies += 1

					# set prior value in array one value forward
					self.set(sortingPointer, self.get(sortingPointer - 1)) #.set(index, value)
					# move the sorting pointer down by one index.
					sortingPointer -= 1

				# This else statement just counts a key comparison if the sorting pointer has reached index 0
				# of the array or if the temp value did not have to be moved down again on this iteration of
				# the while loop
				else:
					self.__totalKeyComparisons += 1
					checking = False

			# Save the value in temp to its proper place in the array
			self.__totalCopies += 1
			self.set(sortingPointer, temp)

##########################################################################################
# This is the __part method used for the backward quicksort (descending values)
##########################################################################################
	def __backwardPart(self, pivot, lowestIndexOfSubArray, highestIndexOfSubArray):
		# Loop until there are not any more items to inspect
		while lowestIndexOfSubArray <= highestIndexOfSubArray:

			# Increment the lowestIndexOfSubArray until we find a value equal to or less
			# than the pivot value.
			while (self.get(lowestIndexOfSubArray)) > (pivot):
				lowestIndexOfSubArray += 1
				self.__totalKeyComparisons += 1

			# Decrement the highestIndexOfSubArray until we find a value greater than or equal to
			# the pivot value
			while (pivot) > (self.get(highestIndexOfSubArray)):
				highestIndexOfSubArray -= 1
				self.__totalKeyComparisons += 1

			# If the lowest index is greater than or equal to the highest index of the subarray,
			# return the lowest index of the subarray
			if lowestIndexOfSubArray >= highestIndexOfSubArray:
				return lowestIndexOfSubArray

			# otherwise, swap the value that the lowestIndexOfSubArray is currently pointing
			# to with the value that the highestIndexOfSubArray is currently pointing
			self.__totalCopies += 3
			self.swap(lowestIndexOfSubArray, highestIndexOfSubArray)

			# Continue partitioning in between by incrementing the lower index by one
			# and decrementing the high index by one
			lowestIndexOfSubArray, highestIndexOfSubArray = lowestIndexOfSubArray + 1, highestIndexOfSubArray - 1

		# Partitioning is now complete. Return the low index
		return lowestIndexOfSubArray

##########################################################################################
# This method executes a backward quick sort (array with descending values)
##########################################################################################
	def backwardQuicksort(self, lowestIndexOfSubArray=0, highestIndexOfSubArray=None, short=3):

		# If the high index is not specified, set it equal to the highest index in the
		# array
		if highestIndexOfSubArray is None:
			highestIndexOfSubArray = len(self) - 1

		# Set a value where any subarrays with a total number of elements equal to or
		# less than that value get sorted by the insertion sort rather than getting
		# sent to the median of three partitioning function
		short = max(3, short)

# Find the right pivot value############################################################
		# If subarray is at or below our cutoff (short), then use insertion sort
		if highestIndexOfSubArray - lowestIndexOfSubArray + 1 <= short:
			return self.backwardInsertionSort(lowestIndexOfSubArray, highestIndexOfSubArray)

		# Else, find the middle index (nextPivotIndex) that will be included in the high part of the
		# next partition by doing a small sort that puts 3 values in known locations on the subarray
		# and returning the highest of the three values placed where the array will
		# be partitioned (highest of 3 values now held where 'nextPivotIndex' is pointing to
		nextPivotIndex = self.backwardMedianOfThree(lowestIndexOfSubArray, highestIndexOfSubArray)

# Partition the array###################################################################
		# Create an index (partitionIndex) to use in further partitioning the array
		# while doing a bit more sorting
		partitionIndex = self.__backwardPart(nextPivotIndex, lowestIndexOfSubArray + 1, highestIndexOfSubArray - 1)

		# swap the value at the partitionIndex with the value at the highestIndexOfSubArray so that
		# the middle value found in the medianOfThree function is now housed at the index(partitionIndex)
		# where the array will be parted
		self.__totalCopies += 3
		self.swap(partitionIndex, highestIndexOfSubArray) # both values sent to .swap() are indicies

		# sort the two subarrays.
		# The partitionIndex will be excluded because it can stay where it is in the full array.
		# (all values in lower part are already less than value held in partitionIndex and all
		# in higher part are already higher than value held in partitionIndex)
		self.backwardQuicksort(lowestIndexOfSubArray, partitionIndex - 1, short) # lower part
		self.backwardQuicksort(partitionIndex + 1, highestIndexOfSubArray, short) # higher part
