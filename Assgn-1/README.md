##Notes and thoughts on Generalized Linear Models.
* Read Andrew Ng's notes for full explanation
* In Logistic Regreassion, the separation line is same for both, labels {0, 1} and {-1, 1}. Only the regression formula
is tweaked a little bit - Read [here](www.hongliangjie.com/wp-content/uploads/2011/10/logistic.pdf) for in-depth explanation.
* For Pset-1 problem on Logistic regression via Newton's Method, somehow initializing theta with all 1s only seems to work.
* For notes on Maximum Likelihood Estimation for Logistic Regression, an in-depth explanation is - [here](http://sites.stat.psu.edu/~jiali/course/stat597e/notes2/logit.pdf).
* Trick for solving Problem 3 on Gaussian Discrimant Analysis, think in terms of Indicator Random Variables. The labels here are {1, -1}. In this case formula is ![this] (https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-1/CodeCogsEqn.gif).
* The final likelihood equation for Problem 3 in terms of given paramters (when n=1) ![is] (https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-1/FinalLikelihoodEquation.png).
* Differentiating the likelihood wrt to the parameters gives the answer, pretty straightforward, no suprised or tricks required.
* The cost function J wrt theta for the quasar regression problem ![is] (https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-1/Normal_eqn_with_W.png)
* The wrong way to take the trace derivative ![is] (https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-1/wrong_trace_derivative.png) and
the right way to take the trace derivative ![is] (https://github.com/sudk1896/CS229-Notes/blob/master/Assgn-1/correct_trace_derivative.png).
