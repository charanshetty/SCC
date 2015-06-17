# SCC
Finding total number of strongly connected components

This uses iterative DFS algorithm using stacks to overcome recursion limit of python
The reverse graph is created at the same instance where the orginal graph created, 
by this we don't need to create the reverse graph separately.

to run the program:
$python SCC.py SCC_1.txt

Assuming the text file is in the same folder as of the code
The output will be total number of SCCs in the graph which also includes includes 
individual nodes which are not part of any other SCCS (size(SCC) = 1)
For sample input the SCC is 23 , since it includes on SCC with size of 5 , and rest of 
them 1. So total number of SCCs = 27-5+1
