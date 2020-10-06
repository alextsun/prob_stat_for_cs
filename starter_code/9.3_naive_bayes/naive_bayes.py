# This starter code was written by Alex Tsun for CSE 312 Summer 2020.

# Student Name: ____
# UW Email    : ____@uw.edu

# =============================================================
# You may define helper functions, but DO NOT MODIFY
# the parameters or names of the provided functions.
# The autograder will expect that these functions exist
# and attempt to call them to grade you.

# Do NOT add any import statements.
# =============================================================

import numpy as np
import os

# ===================== ABOUT THE DATA ========================
# Inside the 'data' folder, the emails are separated into 'train' 
# and 'test' data. Each of these folders has nested 'spam' and 'ham'
# folders, each of which has a collection of emails as txt files.
# You will only use the emails in the 'train' folder to train your 
# classifier, and will evaluate on the 'test' folder.
        
# The emails we are using are a subset of the Enron Corpus,
# which is a set of real emails from employees at an energy
# company. The emails have a subject line and a body, both of
# which are 'tokenized' so that each unique word or bit of
# punctuation is separated by a space or newline. The starter
# code provides a function that takes a filename and returns a
# set of all of the distinct tokens in the file.
# =============================================================

class NaiveBayes():
    """
    This is a Naive Bayes spam filter, that learns word spam probabilities 
    from our pre-labeled training data and then predicts the label (ham or spam) 
    of a set of emails that it hasn't seen before. See the handout from section 2
    for details on implementation!
    """
    def __init__(self):
        """
        These variables are described in the 'fit' function below. 
        You will also need to access them in the 'predict' function.
        """
        self.num_train_hams = 0
        self.num_train_spams = 0
        self.word_counts_spam = {}
        self.word_counts_ham = {}
        self.HAM_LABEL = 'ham'
        self.SPAM_LABEL = 'spam'

    def load_data(self, path:str='data/'):
        """
        This function loads all the train and test data and returns
        the filenames as lists. You do not need to worry about how this
        function works unless you're curious.

        :param path: Expects a path such that inside are two folders:
        'train' and 'test'. Each of these two folders should have a 'spam' and
        'ham' folder inside. These four folders now all should just contain
        several txt files.
        :return: Inside a tuple, 
            1. A list with the ham training data filenames.
            2. A list with the spam training data filenames.
            3. A list with the ham test data filenames.
            4. A list with the spam test data filenames.
        """
        assert set(os.listdir(path)) == set(['test', 'train'])
        assert set(os.listdir(os.path.join(path, 'test'))) == set(['ham', 'spam'])
        assert set(os.listdir(os.path.join(path, 'train'))) == set(['ham', 'spam'])

        train_hams, train_spams, test_hams, test_spams = [], [], [], []
        for filename in os.listdir(os.path.join(path, 'train', 'ham')):
            train_hams.append(os.path.join(path, 'train', 'ham', filename))
        for filename in os.listdir(os.path.join(path, 'train', 'spam')):
            train_spams.append(os.path.join(path, 'train', 'spam', filename))
        for filename in os.listdir(os.path.join(path, 'test', 'ham')):
            test_hams.append(os.path.join(path, 'test', 'ham', filename))
        for filename in os.listdir(os.path.join(path, 'test', 'spam')):
            test_spams.append(os.path.join(path, 'test', 'spam', filename))

        return train_hams, train_spams, test_hams, test_spams

    def word_set(self, filename:list):
        """ 
        This function reads in a file and returns a set of all 
        the words. It ignores the subject line.

        :param path: The filename of the email to process.
        :return: A set of all the unique word in that file.

        For example, if the email had the following content:

        Subject: Get rid of your student loans
        Hi there,
        If you work for us, we will give you money
        to repay your student loans. You will be
        debt free!
        FakePerson_22393

        This function would return to you the set:
        {'', 'work', 'give', 'money', 'rid', 'your', 'there,',
            'for', 'Get', 'to', 'Hi', 'you', 'be', 'we', 'student',
            'debt', 'loans', 'loans.', 'of', 'us,', 'will', 'repay',
            'FakePerson_22393', 'free!', 'You', 'If'}
        """
        with open(filename, 'r') as f:
            text = f.read()[9:] # Ignoring 'Subject:'
            text = text.replace('\r', '')
            text = text.replace('\n', ' ')
            words = text.split(' ')
            return set(words)

    def fit(self, train_hams:list, train_spams:list):
        """
        :param train_hams: A list of train email filenames which are ham.
        :param train_spams: A list of train email filenames which are spam.
        :return: Nothing.

        At the end of this function, the following should be true:
        1. self.num_train_hams is set to the number of ham emails given.
        2. self.num_train_spams is set to the number of spam emails given.
        3. self.word_counts_spam is a DICTIONARY where word_counts_spam[word]
        is the number of spam emails which contained this word. 
        4. self.word_counts_ham is a DICTIONARY where word_counts_ham[word]
        is the number of ham emails which contained this word. 

        Hint(s):
        1. You may want to use the self.word_set function provided.
        2. You should not worry about Laplace smoothing or anything here:
        simply make sure your counts are correct from the data you're given.
        """
        def get_counts(filenames:list):
            """
            This is a nested function only accessible by parent 'fit',
            which we're in now. You may want to implement this function
            to avoid writing the same code for self.word_counts_spam and
            self.word_counts_ham!
            """
            pass

        pass # TODO: Your code here (10-20 lines)

    def predict(self, filename:str):
        """
        :param filename: The filename of an email to classify.
        :return: The prediction of our Naive Bayes classifier. This
        should either return self.HAM_LABEL or self.SPAM_LABEL.

        Guidelines:
        1. Make sure to use the log-trick to avoid underflow.
        2. Make sure for Laplace smoothing you use +1 in numerator 
        and +2 in denominator. This is even for words you haven't seen before
        in the training data, which would otherwise have 0 probability.
        3. Do not 'cheat' - meaning looking up the true label. We will
        test your code on a dataset you don't have access to. Remember,
        the goal is not 100% accuracy - a correct implementation will get
        exactly a certain accuracy.
        4. In case of a tie, predict 'self.HAM_LABEL'.
        5. Do NOT apply Laplace smoothing to P(ham) and P(spam).

        Hint(s):
        1. You may want to use the self.word_set function provided.
        2. Use np.log(...) to take logs.
        3. For a dictionary d, d[key] returns the value if the key exists.
        But if it doesn't, you get an error. To simplify your code,
        d.get(key, 0) will return d[key] if it exists, otherwise 0. 
        4. You'll want to use the values you set during the fit function.
        Access those variables with a 'self' prefix, like self.num_train_hams.
        """
        pass # TODO: Your code here (10-20 lines)
            

    def accuracy(self, hams:list, spams:list):
        """
        :param hams: A list of ham email filenames.
        :param spams: A list of spam email filenames.
        :return: The accuracy of our Naive Bayes model.
        """
        total_correct = 0
        total_datapoints = len(hams) + len(spams)
        for filename in hams:
            if self.predict(filename) == self.HAM_LABEL:
                total_correct += 1
        for filename in spams:
            if self.predict(filename) == self.SPAM_LABEL:
                total_correct += 1
        return total_correct / total_datapoints

if __name__ == '__main__':
    # Create a Naive Bayes classifier.
    nbc = NaiveBayes()

    # Load all the train/test ham/spam data.
    train_hams, train_spams, test_hams, test_spams = nbc.load_data()

    # Fit the model to the training data.
    nbc.fit(train_hams, train_spams)

    # Print out the accuracy on the train and test sets.
    print("Train Accuracy: {}".format(nbc.accuracy(train_hams, train_spams)))
    print("Test  Accuracy: {}".format(nbc.accuracy(test_hams, test_spams)))
