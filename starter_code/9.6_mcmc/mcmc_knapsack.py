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
import matplotlib.pyplot as plt
from os.path import join, dirname

class KnapsackMcmc:
    def __init__(self, filename=join(dirname(__file__), 'data', 'items.txt')):
        self.item_names, self.values, self.weights = self.get_items(filename)
        self.num_items = len(self.item_names)

    def get_items(self, filename):
        """
        :param filename: The filename where each row has three columns
        separated by spaces: an item name, its value, and its weight.
        :return: Three numpy arrays: an array of item names, item values, and item weights.
        These all should be of the same size.
        """
        data = np.genfromtxt(filename, dtype=str)
        return data[:, 0], data[:, 1].astype(float), data[:, 2].astype(float)
    
    def value(self, subset):
        """
        :param subset: The current subset represented by a numpy array of 0's and 1's.
        This is of the same length as self.items (and hence self.values and self.weights).
        :return: The total value of the subset (the sum of the values of the items in subset).

        Hint(s):
        1. np.dot(x, y) for two numpy arrays x and y of the same length returns their dot product
        sum(x[i]*y[i]). Given that `subset` is of vector of 0's and 1's, how can we efficiently compute
        the value of `subset`?
        """
        assert self.values.shape == subset.shape
        return 0 # TODO: Your code here (~1-4 lines)

    def weight(self, subset):
        """
        :param subset: The current subset represented by a numpy array of 0's and 1's.
        This is of the same length as self.items (and hence self.values and self.weights).
        :return: The total weight of the subset (the sum of the weights of the items in subset).
        """
        assert self.weights.shape == subset.shape
        return 0 # TODO: Your code here (~1-4 lines)

    def mcmc(self, W:float, T:float=0, num_iter:int=5000):
        """
        :param W: The maximum weight of the knapsack.
        :param T: The "temperature" parameter governing the tradeoff between
        exploration and exploitation. Must be nonnegative.
        :param num_iter: The max number of iterations to perform.
        :return: A tuple of three elements:
            1. The best subset (a list of 1's and 0's, indicating whether we took each item).
            2. The value of the best subset (a float).
            3. A list of length num_iter, which has the value of the 
            CURRENT subset at the end of each iteration. This is NOT the current 
            best subset NOR the new subset (the CURRENT route is called "subset" 
            in the pseudocode). (Hence, it is possible that it isn't monotone).

        Hint(s):
        1. Use the pseudocode provided in the spec!
        2. Use np.copy(subset) to make a deep copy of subset, so that you don't
        modify the current subset when applying a random transition.
        3. Use your self.value(...) and self.weight(...) functions you implemented earlier.
        4. Use np.random.randint(...) to get a random integer — this should be called 
        exactly once per iteration. Though the pseudocode says to get a random integer
        in {1, 2, ..., n}, since Python uses 0-indexing, get one in {0, 1, ..., n-1}.
        5. Use np.random.rand(...) to get a random float in [0, 1] — this 
        should be called 0-1 times per iteration (only if delta < 0 and T > 0).
        6. Use np.exp(x) to compute e^x.
        7. self.num_items stores the total number of items.
        8. To return the variables a, b, and c in a tuple, do the following:
            return a, b, c
        """
        assert W > 0
        assert T >= 0
        assert num_iter > 0

        # This line creates your initial empty subset (knapsack).
        subset = np.zeros(self.num_items)
        # TODO: Your code here (~10-20 lines)
        return None, None, None

    def make_plot(self, W:float, T:float=0, num_iter:int=5000, trials:int=10):
        """
        :param T: The "temperature" parameter governing the tradeoff between
        exploration and exploitation.
        :param num_iter: The max number of iterations to perform during each trial. 
        :param trials: How many "random walks" to perform and plot.
        :return: A tuple of two elements:
            1. The best subset (a list of 0/1's), over all "trials" number of trials.
            2. The value of the best subset (a float), over all "trials" number of trials.
        
        This function saves a SINGLE plot, with "trials" numbers of curves.
        On the x-axis, it plots the iteration number up to "num_iter".
        On the y-axis, it plots the current subset values for one run of MCMC. (And
        has "trials" separate curves on the same plot.)
        """
        np.random.seed(312)
        plt.figure()
        max_value = 0
        max_subset = []
        for _ in range(trials):
            best_subset, best_value, lengths = self.mcmc(W, T, num_iter)
            plt.plot(np.arange(len(lengths)), lengths)
            if best_value > max_value:
                max_value = best_value
                max_subset = best_subset
        print("Best Value for T={}: {}".format(T, best_value))
        file_name = "best_subset_T={}.txt".format(T)
        print("Saving best subset to the file: " + file_name)
        np.savetxt(file_name, max_subset, "%s")
        plt.xlabel('Iteration')
        plt.ylabel('Value of Current Subset')
        plt.suptitle('Value vs. Iteration for Temperature {}'.format(T))
        plt.title('Every trial is a different color.')
        plt.savefig('mcmc_T={}.png'.format(T))
        return max_subset, max_value

if __name__ == '__main__':
    knapsack_solver = KnapsackMcmc()

    TEMPS = [0,1,10,100]
    num_iter = 5000
    for T in TEMPS:
        print("Making plot for T={}".format(T))
        knapsack_solver.make_plot(W=400, T=T, num_iter=num_iter, trials=10)