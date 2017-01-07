
[spmatrix, tokenlist, trainCategory] = readMatrix('MATRIX.TRAIN.50');

trainMatrix = full(spmatrix);
numTrainDocs = size(trainMatrix, 1);
numTokens = size(trainMatrix, 2);
disp (numTrainDocs);
%disp (numTokens); %(rows, cols) - > (m training samples, n tokens)

% trainMatrix is now a (numTrainDocs x numTokens) matrix.
% Each row represents a unique document (email).
% The j-th column of the row $i$ represents the number of times the j-th
% token appeared in email $i$. 

% tokenlist is a long string containing the list of all tokens (words).
% These tokens are easily known by position in the file TOKENS_LIST

% trainCategory is a (1 x numTrainDocs) vector containing the true 
% classifications for the documents just read in. The i-th entry gives the 
% correct class for the i-th email (which corresponds to the i-th row in 
% the document word matrix).

% Spam documents are indicated as class 1, and non-spam as class 0.
% Note that for the SVM, you would want to convert these to +1 and -1.
% YOUR CODE HERE
spam = 0.0; %calculate no of spam emails
for elm=1:numTrainDocs
    if trainCategory(1, elm)==1
        spam = spam + 1;
    end
end

y_1 = spam/numTrainDocs;
y_0 = 1.0 - y_1;
phi_0 = zeros(1, numTokens);%phi given email is not spam
phi_1 = zeros(1, numTokens);%phi given email is spam;
words_doc = zeros(1, numTrainDocs); %no of words in ith email
for rows=1:numTrainDocs
    count = 0.0;%no. of words in each e-mail
    for elem=1:numTokens
        count = count + trainMatrix(rows, elem);
    end
    words_doc(1, rows) = count;
end

for token=1:numTokens
    count_1 = 1.0;%spam, 1 for laplace smoothing
    denom_1 = numTokens; %|V| for laplace smoothing
    count_0 = 1.0;%not_spam
    denom_0 = numTokens;
    for row=1:numTrainDocs
        if trainCategory(1, row)==1
            count_1 = count_1 + trainMatrix(row, token);
            denom_1 = denom_1 + words_doc(row);
        else
            count_0 = count_0 + trainMatrix(row, token);
            denom_0 = denom_0 + words_doc(row);
        end
    end
    phi_0(1, token) = 1.0*count_0/denom_0;
    phi_1(1, token) = 1.0*count_1/denom_1;
end
disp ('Training Succesful!');
for elem=1:5
    disp (phi_0(1, elem));
end
