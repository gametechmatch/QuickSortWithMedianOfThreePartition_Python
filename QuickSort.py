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
# of lo, middle, and hi keys in a subarray and placing the median in the hi position for
# the partition
##########################################################################################
	def medianOfThree(self, lowestIndexOfSubArray, highestIndexOfSubArray):
		# Calculate the middle index
		midIndex = (lowestIndexOfSubArray + highestIndexOfSubArray) // 2

		# Swap values in low and mid indicies if value in low > value in mid
		self.__totalKeyComparisons += 1 # FOR HW
		if (self.get(lowestIndexOfSubArray)) > (self.get(midIndex)):
			self.__totalCopies += 3 # FOR HW
			self.swap(lowestIndexOfSubArray, midIndex)

		# Swap values in low and high indicies if value in low > value in high
		self.__totalKeyComparisons += 1 # FOR HW
		if (self.get(lowestIndexOfSubArray)) > (self.get(highestIndexOfSubArray)):
			self.__totalCopies += 3 # FOR HW
			self.swap(lowestIndexOfSubArray, highestIndexOfSubArray)

		# Swap values in high and mid indicies if value in high > value in mid
		self.__totalKeyComparisons += 1 # FOR HW
		if (self.get(highestIndexOfSubArray)) > (self.get(midIndex)):
			self.__totalCopies += 3 # FOR HW
			self.swap(highestIndexOfSubArray, midIndex)

		# Return item with the median key (now set to 'hi')
		return self.get(highestIndexOfSubArray)

##########################################################################################
# This method executes an insertion sort on small subarrays received specifically
# from the quicksort method
# It moves forward through the array pushing back lower values and leaving higher values
# in their place
##########################################################################################
	def insertionSort(self, lowestIndexOfSubArray=0, highestIndexOfSubArray=None):
		# Set the 'hi' index pointer to the last item in the array if not already specified
		if highestIndexOfSubArray is None:
			highestIndexOfSubArray = len(self) - 1

		# Mark one item & store the marked item in temp
		for unsortedSectionPointer in range(lowestIndexOfSubArray + 1, highestIndexOfSubArray + 1):
			self.__totalCopies += 1 # FOR HW
			temp = self.get(unsortedSectionPointer) # temp holds the value of the item we are checking

			# Move the 'inner' pointer to catch up to the 'outer' pointer
			sortingPointer = unsortedSectionPointer

			# If the 'inner' pointer has not reached the beginning of the array (side
			# that holds the lowest values) and
			# If the current value we are looking at (temp) is smaller than the value before it
			# then keep moving the 'inner' pointer towards the beginning of the array
			# (where the lowest values are held), descending the 'inner' pointer down and
			# comparing the 'temp' value to each value in the data structure until the
			# temp value can be inserted into its proper place
			checking = True
			while checking == True:

				# This if statement decrements the inner pointer with each loop
				if ((sortingPointer > lowestIndexOfSubArray) and (temp < self.get(sortingPointer - 1))):
					self.__totalKeyComparisons += 1  # FOR HW
					self.__totalCopies += 1 # FOR HW

					# set prior value in array one value forward
					self.set(sortingPointer, self.get(sortingPointer - 1)) #.set(index, value)

					# move the inner pointer down one. It will keep moving down
					# until we have found where the value in temp needs to be placed
					sortingPointer -= 1

				# This else statement just counts a key comparison if we have
				# either arrived at the beginning of the array or if the temp
				# value did not have to be moved in the first place
				else:
					self.__totalKeyComparisons += 1 # FOR HW
					checking = False

			# move marked the temp value to the sorted side of the array
			self.__totalCopies += 1 # FOR HW
			self.set(sortingPointer, temp)

##########################################################################################
# This private method partitions an array based on the items whose keys are below or equal
# to a pivot value to the left/low side compared to the rest (to the right/high side) within
# [lo, hi] knowing there is 1 key below the pivot & the pivot at (hi +1)
##########################################################################################
	def __part(self, pivot, lowestIndexOfSubArray, highestIndexOfSubArray):
		# Loop until there are not any more items to inspect
		while lowestIndexOfSubArray <= highestIndexOfSubArray:

			# Increment the lowestIndexOfSubArray until we find a value equal to or greater
			# than the pivot value.
			while (self.get(lowestIndexOfSubArray)) < (pivot):
				lowestIndexOfSubArray += 1
				self.__totalKeyComparisons += 1 # FOR HW

			# Decrement the highestIndexOfSubArray until we find a value less than or equal to
			# the pivot value
			while (pivot) < (self.get(highestIndexOfSubArray)):
				# make sure the key (coordinates with hi index now) is not in the upper partition
				highestIndexOfSubArray -= 1
				self.__totalKeyComparisons += 1 # FOR HW

			# If the lowest index is greater than or equal to the highest part of the subarray,
			# return the lowest index of the subarray
			if lowestIndexOfSubArray >= highestIndexOfSubArray:
				return lowestIndexOfSubArray

			# otherwise, swap the values where the lowestIndexOfSubArray is currently pointing
			# with the value where the highestIndexOfSubArray is currently pointing
			self.__totalCopies += 3 # FOR HW
			self.swap(lowestIndexOfSubArray, highestIndexOfSubArray)

			# Continue partitioning in between by then incrementing the lower index by one
			# and decreasing the high index by one
			lowestIndexOfSubArray, highestIndexOfSubArray = lowestIndexOfSubArray + 1, highestIndexOfSubArray - 1

		# Range to partition is now empty so return where the low index is currently pointing
		return lowestIndexOfSubArray

##########################################################################################
# This method executes a quick sort by sorting items in an array between lo and hi indices.
# For short subarrays, it uses insertion sort. The short subarrays must be 3 or more to
# enable the median of three approach to choosing a pivot value
##########################################################################################
	def quicksort(self, lowestIndexOfSubArray=0, highestIndexOfSubArray=None, short=3):

		# If the hi index is not specified, set it equal to the highest index in the
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

		# Else, find the middle index (pivotItem) that will be included in the high part of the
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
		self.__totalCopies += 3 # FOR HW
		self.swap(partitionIndex, highestIndexOfSubArray) # both values sent to .swap() are indicies

		# sort the two subarrays.
		# The partitionIndex will be excluded because it can stay where
		# it is in the full array. (all values in lower part are already less than
		# partitionIndex and all values in higher part are already higher than partitionIndex)
		self.quicksort(lowestIndexOfSubArray, partitionIndex - 1, short) # lower part
		self.quicksort(partitionIndex + 1, highestIndexOfSubArray, short) # higher par

##########################################################################################
# This method executes the median-of-three partitioning technique by finding the median
# of lo, middle, and hi keys in a subarray and placing the median in the hi position for
# the partition
##########################################################################################
	def backwardMedianOfThree(self, lowestIndexOfSubArray, highestIndexOfSubArray):
		# Calculate the middle index
		midIndex = (lowestIndexOfSubArray + highestIndexOfSubArray) // 2

# Sorting and comparing 3 values at 3 indicies (lowest, middle, and highest indicies)
		# Swap values in low and mid indicies if value in low > value in mid
		self.__totalKeyComparisons += 1 # FOR HW
		if (self.get(lowestIndexOfSubArray)) < (self.get(midIndex)):
			self.__totalCopies += 3 # FOR HW
			self.swap(lowestIndexOfSubArray, midIndex)

		# Swap values in low and high indicies if value in low > value in high
		self.__totalKeyComparisons += 1 # FOR HW
		if (self.get(lowestIndexOfSubArray)) < (self.get(highestIndexOfSubArray)):
			self.__totalCopies += 3 # FOR HW
			self.swap(lowestIndexOfSubArray, highestIndexOfSubArray)

# Swapping values at midIndex and highest index to have a trigger point for a future sort to stop
# (in the middle index which will hold the lowest value of the 3 values checked after this if statement)
		# Swap values in high and mid indicies if value in high > value in mid
		self.__totalKeyComparisons += 1 # FOR HW
		if (self.get(highestIndexOfSubArray)) < (self.get(midIndex)):
			self.__totalCopies += 3 # FOR HW
			self.swap(highestIndexOfSubArray, midIndex)

		# Return item with the median key (now with the lowest of the three values)
		return self.get(highestIndexOfSubArray)

##########################################################################################
# This method executes an insertion sort on small subarrays received specifically
# from the quicksort method
# It moves forward through the array pushing back lower values and leaving higher values
# in their place
##########################################################################################
	def backwardInsertionSort(self, lowestIndexOfSubArray=0, highestIndexOfSubArray=None):
		# Set the 'hi' index pointer to the last item in the array if not already specified
		if highestIndexOfSubArray is None:
			highestIndexOfSubArray = len(self) - 1

		# Mark one item & store the marked item in temp
		for unsortedSectionPointer in range(lowestIndexOfSubArray + 1, highestIndexOfSubArray + 1):
			self.__totalCopies += 1 # FOR HW
			temp = self.get(unsortedSectionPointer) # temp holds the value of the item we are checking

			# Move the 'inner' pointer to catch up to the 'outer' pointer
			sortingPointer = unsortedSectionPointer

			# If the 'inner' pointer has not reached the beginning of the array (side
			# that holds the lowest values) and
			# If the current value we are looking at (temp) is smaller than the value before it
			# then keep moving the 'inner' pointer towards the beginning of the array
			# (where the lowest values are held), descending the 'inner' pointer down and
			# comparing the 'temp' value to each value in the data structure until the
			# temp value can be inserted into its proper place
			checking = True
			while checking == True:

				# This if statement decrements the inner pointer with each loop
				if ((sortingPointer > lowestIndexOfSubArray) and (temp > self.get(sortingPointer - 1))):
					self.__totalKeyComparisons += 1  # FOR HW
					self.__totalCopies += 1 # FOR HW

					# set prior value in array one value forward
					self.set(sortingPointer, self.get(sortingPointer - 1)) #.set(index, value)
					# move the inner pointer down one. It will keep moving down
					# until we have found where the value in temp needs to be placed
					sortingPointer -= 1

				# This else statement just counts a key comparison if we have
				# either arrived at the beginning of the array or if the temp
				# value did not have to be moved in the first place
				else:
					self.__totalKeyComparisons += 1 # FOR HW
					checking = False

			# move marked the temp value to the sorted side of the array
			self.__totalCopies += 1 # FOR HW
			self.set(sortingPointer, temp)

##########################################################################################
# This private method partitions an array based on the items whose keys are below or equal
# to a pivot value to the left/low side compared to the rest (to the right/high side) within
# [lo, hi] knowing there is 1 key below the pivot & the pivot at (hi +1)
##########################################################################################
	def __backwardPart(self, pivot, lowestIndexOfSubArray, highestIndexOfSubArray):
		# Loop until there are not any more items to inspect
		while lowestIndexOfSubArray <= highestIndexOfSubArray:

			# Increment the lowestIndexOfSubArray until we find a value equal to or less
			# than the pivot value.
			while (self.get(lowestIndexOfSubArray)) > (pivot):
				lowestIndexOfSubArray += 1
				self.__totalKeyComparisons += 1 # FOR HW

			# Decrement the highestIndexOfSubArray until we find a value greater than or equal to
			# the pivot value
			while (pivot) > (self.get(highestIndexOfSubArray)):
				# make sure the key (coordinates with hi index now) is not in the upper partition
				highestIndexOfSubArray -= 1
				self.__totalKeyComparisons += 1 # FOR HW

			# If the lowest index is greater than or equal to the highest part of the subarray,
			# return the lowest index of the subarray
			if lowestIndexOfSubArray >= highestIndexOfSubArray:
				return lowestIndexOfSubArray

			# otherwise, swap the values where the lowestIndexOfSubArray is currently pointing
			# with the value where the highestIndexOfSubArray is currently pointing
			self.__totalCopies += 3 # FOR HW
			self.swap(lowestIndexOfSubArray, highestIndexOfSubArray)

			# Continue partitioning in between by then incrementing the lower index by one
			# and decreasing the high index by one
			lowestIndexOfSubArray, highestIndexOfSubArray = lowestIndexOfSubArray + 1, highestIndexOfSubArray - 1

		# Range to partition is now empty so return where the low index is currently pointing
		return lowestIndexOfSubArray

##########################################################################################
# This method executes a quick sort by sorting items in an array between lo and hi indices.
# For short subarrays, it uses insertion sort. The short subarrays must be 3 or more to
# enable the median of three approach to choosing a pivot value
##########################################################################################
	def backwardQuicksort(self, lowestIndexOfSubArray=0, highestIndexOfSubArray=None, short=3):

		# If the hi index is not specified, set it equal to the highest index in the
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

		# Else, find the middle index (pivotItem) that will be included in the high part of the
		# next partition by doing a small sort that puts 3 values in known locations on the subarray
		# and returning the lowest of the three values placed where the array will
		# be partitioned (lowest of 3 values now held where 'nextPivotIndex' is pointing to
		nextPivotIndex = self.backwardMedianOfThree(lowestIndexOfSubArray, highestIndexOfSubArray)

# Partition the array###################################################################
		# Create an index (partitionIndex) to use in further partitioning the array
		# while doing a bit more sorting. The partition index will be pointing at the
		# index of the median value found in the .medianOfThree() function
		partitionIndex = self.__backwardPart(nextPivotIndex, lowestIndexOfSubArray + 1, highestIndexOfSubArray - 1)

		# swap the value at the partitionIndex with the value at the highestIndexOfSubArray so that
		# the middle value found in the medianOfThree function is now housed at the index(partitionIndex)
		# where the array will be parted
		self.__totalCopies += 3 # FOR HW
		self.swap(partitionIndex, highestIndexOfSubArray) # both values sent to .swap() are indicies

		# sort the two subarrays.
		# The partitionIndex will be excluded because it can stay where
		# it is in the full array. (all values in lower part are already less than
		# partitionIndex and all values in higher part are already higher than partitionIndex)
		self.backwardQuicksort(lowestIndexOfSubArray, partitionIndex - 1, short) # lower part
		self.backwardQuicksort(partitionIndex + 1, highestIndexOfSubArray, short) # higher part
