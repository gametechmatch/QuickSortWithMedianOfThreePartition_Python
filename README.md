# QuickSortWithMedianOfThreePartition_Python
# Author: gametechmatch

____________WHAT THE MAIN PROGRAM DOES:____________
The main program (QuickSortClientOne.py) counts the number of value comparisons and copies (values being copied or swapped) done when sorting different arrays
with different approaches (ex: constant values vs random values, changes in the floor-limit for total elements permitted in a median-of-three partitioning)

____________SORTING & PARTITIONING ALGORITHMS USED:____________
This project uses Python to implement a Quicksort with a median-of-three partitioning algorithm and insertion sort for sections of the array
that are less than or equal to a given value (default 3)

____________COMPUTER PROGRAMMING MODEL(S):____________
Object Oriented Programming (primary model)
Procedural Programming (secondary model)

____________FILES:____________
QuickSortClientOne.py --- main program

SortArrayOne.py---parent class to create a list (sometimes called an array)

QuickSort.py---child class to add quicksort functionality



____________OTHER NOTES:____________
Python lists are the closest equivalent to an array in other coding languages, but some websites distinguish them on their functionality and imply that both are capable in Python with some extra code. Since this textbook used the word "array" for the original code that this was built off of, I kept using that terminology. Additionally, since this has been implemented through object oriented programming, it would most accurately be described as a linked list, but going back to the first point, I kept the verbiage used in the textbook's chapter.
