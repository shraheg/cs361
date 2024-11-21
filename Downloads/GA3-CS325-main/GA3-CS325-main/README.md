# GA3-CS325
CS325: Analysis of Algorithms, Fall 2024 Group Assignment 3 Due: Thr, 11/21/24

Homework Policy:
Students should work on group assignments in groups of preferably three people. Each group submits to CANVAS a zip ﬁle that includes their source code and their typeset report. The report must include the name of all group members. Speciﬁcally, for this assignment your zipped folder should contain two ﬁles named assignment3.pdf, and assignment3.py. One submission from each group is suﬃcient.
The goal of the homework assignments is for you to learn solving algorithmic problems. So, I recommend spending suﬃcient time thinking about problems individually before discussing them with your friends.
You are allowed to discuss the problems with other groups, and you are allowed to use other resources, but you must cite them. Also, you must write everything in your own words, copying verbatim is plagiarism.
I don’t know policy: you may write “I don’t know” and nothing else to answer a question and receive 25 percent of the total points for that problem whereas a completely wrong answer will receive zero.
Algorithms should be explained in plain english. You can use pseudocodes if it helps your explanation, but the grader will not try to understand a complicated pseudocode.
More items might be added to this list. ©
In this assignment, you will design algorithms to compute the weights of the ﬁrst, second, and third minimum spanning trees of a given graph. Speciﬁcally, given an undirected graph G with non-negative edge weights, your algorithm must output the weights of the ﬁrst, second, and third minimum spanning trees.

For example, the ﬁgure below illustrates a graph and its three smallest spanning trees, with weights 21, 22, and 23, from left to right.


Report (60%). In your report, include the description of your algorithms, running time analysis, and proof of correctness. Algorithms should be explained in plain english. You can use pseudocode if it helps your explanation, but the grader will not try to understand complicated pseudocode. For full credit, the algorithm must run in O(V 2E log V ). However, obtaining an O(V E) time algorithm is not too hard.

Code (40%). Submit a python that computes ﬁrst, second, and third minimum spanning trees of a given graph G. Your program will be tested against several test cases, for correctness and eﬃciency. For each test case, the program will be automatically stopped after 30 seconds if it is not done in that time. In this case, the group will miss the points of that test case.

Note: it is important that your output is formatted as described below, since your codes will be tested automatically. Speciﬁcally, you must implement the function “three min spanning trees” in the following code. The code you submit will be an implementation of this procedure in a ﬁle named “assignment3.py”.


Input/Output The ﬁrst line of the input ﬁle is one integer 1 ≤ n ≤ 30. The following n lines each is a row of the adjacency matrix of G, that is the ith number of the jth row is the weight of the the (i, j) edge (You can assume that the graph is complete, and all weights are non-negative integers).

The output should include three numbers, each written in a separate line: the weights of the ﬁrst, second, and third minimum spanning trees in order.



