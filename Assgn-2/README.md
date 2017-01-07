##Notes and thoughts on Assignment-2.
* For SVMs read Notes. 
* Solutions for Problem 1 are ![here](https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-2/CodeCogsEqn.png).
* Most of them boil down to deriving the form ![here](https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-2/PSD.png), you express it as a square of sums, which will always be greater than equal to zero.
* Matlab code for Naive Bayes with Multinomial Event model is ![here](https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-2/nb_train.m), pretty straightforward. The results after training on datasets of sizes (no. of documents) 50, 100, 200, 400, 800, 1400, 2144 are, in percentages, 3.87,2.62, 2.62, 1.87, 1.75, 1.63, 1.63. Its the exact same answer as given in the key. The test data is weak, if you know what I mean!.
* To find the 5 most frequent keywords in spam mails as mentioned in the problem, I just calculated the heuristic (the log of the ratio) wrote them to a txt file, read it in python and sorted according the log of ratio. Don't ask, MATLAB is a huge pain. The output file and python file to read the results are ![here](https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-2/out.txt) and ![here](https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-2/red.py) and the answers are  ```httpaddr, spam, unsubscribe, ebai, valet``` which match exactly with the ones in the key. 

