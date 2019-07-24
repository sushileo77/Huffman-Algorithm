# Huffman-Algorithm
Implementation of a Huffman Compression Decompression Algorithm in Python
Implementation Description :-
	- Sort the Array in Descending Order
	- Use a Quick Sort Algorithm to Implement that Descending Order Sorting
	- Then Start from the First Index and Increment loop index by 2, so accumulate the digits at even places
	- Store, the above accumulated value in a variable
	- Start a new loop to accumulate the digits at odd places 
	- Return the accumulated digits in a list
	
Time Complexity:-
    - Here QuickSort Algorithm is used to Sort the Array in Descending Order
    - The Worst Case Complexity for QuickSort is O(logn)
	- Here we have two different For Loops running over a range of input list
	- Each For Loop's Time Complexity is O(n) as it executes for the length of input list
	- Thus we have two different For Loops, which become O(n) + O(n) = O(2n)
	- Thus we can normalize this is O(n)
	- However the worst timing complexity is O(n)
	
Space Complexity:-
	-  Require Space to Store for Variable i and j and pivot , which are the loop variables
	-  They are not dependent on the size of the Input Length
	-  Hence, the Space Complexity is O(1)
	-  The space for loop variable isn't needed anymore and can be reused in the next iteration. 
