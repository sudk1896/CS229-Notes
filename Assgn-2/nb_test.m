
[spmatrix, tokenlist, category] = readMatrix('MATRIX.TEST');

testMatrix = full(spmatrix);
numTestDocs = size(testMatrix, 1);
numTokens = size(testMatrix, 2);

% Assume nb_train.m has just been executed, and all the parameters computed/needed
% by your classifier are in memory through that execution. You can also assume 
% that the columns in the test set are arranged in exactly the same way as for the
% training set (i.e., the j-th column represents the same token in the test data 
% matrix as in the original training data matrix).

% Write code below to classify each document in the test set (ie, each row
% in the current document word matrix) as 1 for SPAM and 0 for NON-SPAM.

% Construct the (numTestDocs x 1) vector 'output' such that the i-th entry 
% of this vector is the predicted class (1/0) for the i-th  email (i-th row 
% in testMatrix) in the test set.
output = zeros(numTestDocs, 1);

%---------------
% YOUR CODE HERE


%---------------
for row=1:numTestDocs
    ans_spam = log(y_1);
    ans_not_spam = log(y_0);
    for tokens=1:numTokens
        ans_spam = ans_spam + testMatrix(row, tokens)*log(phi_1(tokens));
        ans_not_spam = ans_not_spam + testMatrix(row, tokens)*log(phi_0(tokens));
    end
    disp(ans_spam);
    disp(ans_not_spam);
    if ans_spam > ans_not_spam
        output(row, 1)=1;
    else
        output(row, 1)=0;
    end
end
%Compute the error on the test set
y = full(category);
y = y(:);
error = sum(y ~= output) / numTestDocs;

%Print out the classification error on the test set
fprintf(1, 'Test error: %1.4f\n', error);