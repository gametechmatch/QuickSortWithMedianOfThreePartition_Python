#################################################################
# QuickSortClientOne.py
#################################################################
# Author: gametechmatch
# Course: Data Structures
# CH7 - Advanced Sorting
# HW4 - WK4
# Programming Project 7.2
#################################################################
# This program modifies the quicksort() and helper methods listed
# in 7-7 and 7-8 to count the number of item copies they make
# during a sort and the number of key comparisons they make during
# a sort and returns the counts to the caller
#################################################################
# Note:
# (1) a swap counts as 3 copies
# (2) only comparisons of key values (not array indices) are counted
#################################################################

from ForwardQuickSort import *
import random

# This function is the main program
############################################################################################
def main():
   hwPartA()
   hwPartB()
   hwPartC()
   hwPartD()

# This function looks at the total key comparisons and copies for a forward-sorted array
############################################################################################
def hwPartA():
   print("\n############################################################################")
   print("(A) A Forward Sorted Array of 50 items: ")
   # Create and fill array
   myForwardArr = randomArray(50, 100, 1.346)

   # Sort array and print the total key comparisons and copies
   myForwardArr.quicksort()
   SortArrayOne.Array.printCopiesAndCounters(myForwardArr)

# This function looks at the total key comparisons and copies for a backward-sorted array
############################################################################################
def hwPartB():
   print("\n############################################################################")
   print("(B) A Backward Sorted Array of 50 items: ")
   # Create and fill array
   myBackwardArr = randomArray(50, 100, 83.456)

   # Sort array and print the total key comparisons and copies
   myBackwardArr.backwardQuicksort()
   SortArrayOne.Array.printCopiesAndCounters(myBackwardArr)

# This function looks at the total key comparisons and copies for an array with 50 of the same
# valued elements
############################################################################################
def hwPartC():
   print("\n############################################################################")
   print("(C) A Constant Value for all 50 items: ")
   # Create and fill array
   constantValueArr = fillConstantArray(50, 4)

   # Sort array and print the total key comparisons and copies
   constantValueArr.quicksort()
   SortArrayOne.Array.printCopiesAndCounters(constantValueArr)

# This function creates an array with 50 random items and then looks at the total copies
# and key comparisons when the cutoff value for the median-of-three pivot calculation
# is set at different values
############################################################################################
def hwPartD():
   print("\n############################################################################")
   print("(D) An Array of 50 Random Items: ")

# Creating the arrays with random values
   # Create and fill array
   myRandomArr3 = randomArray(50, 100, 3.14159)

   # Create a duplicate array to sort with a 'short' cutoff for the median-of-three
   # paritioning cutoff at 'short' = 7
   myRandomArr7 = randomArray(50, 100, 3.14159)

   # Create a duplicate array to sort with a 'short' cutoff for the median-of-three
   # paritioning cutoff at 'short' = 11
   myRandomArr11 = randomArray(50, 100, 3.14159)

# Sorting the arrays with different 'short' values for the median-of-three pivot cutoff
   # Sort array and print the total key comparisons and copies when 'short' = 3
   myRandomArr3.quicksort()
   print("\nSORTING RANDOM VALUES WHEN SHORT = 3")
   SortArrayOne.Array.printCopiesAndCounters(myRandomArr3)

   # Sort array and print the total key comparisons and copies when 'short' = 7
   myRandomArr7.quicksort(short=7)
   print("\nSORTING RANDOM VALUES WHEN SHORT = 7")
   SortArrayOne.Array.printCopiesAndCounters(myRandomArr7)

   # Sort array and print the total key comparisons and copies when 'short' = 11
   myRandomArr11.quicksort(short=11)
   print("\nSORTING RANDOM VALUES WHEN SHORT = 11")
   SortArrayOne.Array.printCopiesAndCounters(myRandomArr11)

# This function creates arrays with random values
#################################################################
def randomArray(size, maxValue, seed):

   # Create an array
   arr = Array(size)

   # Set random number generator to know state, then loop insert
   # random numbers
   random.seed(seed)
   for i in range(size):
      arr.insert(random.randrange(maxValue))

   # Return filled array
   return arr

# This function creates an array with only one value
#################################################################
def fillConstantArray(size, value):
   # Create array
   arr = Array(size)

   # Fill array
   i = 0
   while (i < 49):
      arr.insert(value)
      i += 1

   # return array
   return arr

#Execute main program
if __name__ == '__main__':
    main()
