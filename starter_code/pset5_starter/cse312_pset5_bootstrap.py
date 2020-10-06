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

def bootstrap_pval(group1, group2, ntrials=50000):
    """
    :param group1: A numpy array of values in one particular group.
    :param group2: A numpy array of values in another particular group.
    :param ntrials: The number of times to bootstrap.
    :return: Let mu1 be the TRUE mean of group1, and mu2 be the TRUE mean
    of group2 (we can only compute the sample means in this function, and don't
    have access to the true means). We have the null and alternative hypotheses:
        H0: mu1 = mu2
        H1: mu1 != mu2
    We use the bootstrapping method to compute and return the p-value for this
    particular hypothesis test.

    Hint(s):
    1. Use np.abs(...) to compute absolute values.
    2. Use np.mean(...) to compute the average of the values in a numpy array.
    3. Use np.concatenate(...) to concatenate two numpy arrays.
    4. You MUST use np.random.choice(...) with the parameter `replace=True`, to sample
    with replacement.
    5. Remember that when you resample, to make sure the number of resampled values is
    the same as that of the original. 
    """
    pass # TODO: Your code here (~10-15 lines)

if __name__ == '__main__':
    """
    Loads Coursera data in, and splits into two groups of students based on which of
    activity1 and activity2 they performed. Calls the boostrap_pval function to get a 
    p-value for the difference in means.
    """
    data = np.genfromtxt('data/coursera.txt', dtype=str)
    group1 = data[data[:, 0] == 'activity1', 1].astype(float)
    group2 = data[data[:, 0] == 'activity2', 1].astype(float)
    print("Activity 1 | n = {} | Sample Mean = {} | Sample Variance = {}".format(group1.shape, np.mean(group1), np.var(group1)))
    print("Activity 2 | n = {} | Sample Mean = {} | Sample Variance = {}".format(group2.shape, np.mean(group2), np.var(group2)))
    print("Testing H0: mu1 = mu2 vs H1: mu1 != mu2")
    p_val = bootstrap_pval(group1, group2)
    print("p-value: {}".format(p_val))
