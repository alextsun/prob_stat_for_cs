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

class TspMcmc:
    def __init__(self, filename='/data/us_capitals.txt'):
        self.locs = self.get_locs(filename)

    def get_locs(self, filename):
        """
        :param filename: The filename where each row has three columns
        separated by spaces: a location name, its latitude, and its 
        longitude.
        :return: A dictionary mapping the location name (str) to a 
        numpy array of length 2 (containing only latitude and longitude).
        """
        data = np.genfromtxt(filename, dtype=str)
        locs = {}
        for i in range(data.shape[0]):
            locs[data[i,0]] = data[i, 1:].astype(float)
        return locs

    def distance(self, route):
        """
        :param route: The current route (a list of strings) containing exactly 
        one of each location in some order.
        :return: The distance required to go from each location to the next
        (and returning to the start) in the order specified by the parameter `route`.

        Hint(s):
        1. np.linalg.norm(a - b) can be used to compute the distance between 
        a=(lat1, lon1) and b=(lat2, lon2). That is, a and b are each 2D vectors 
        (such as a numpy array of two elements) containing the latitude and 
        longitude of points.
        2. To access the value of a particular key in a dict, use the syntax:
        dict[key]. For our dictionary self.locs, self.locs[capital] would return a 2D
        numpy array containing the latitude and longitude of capital.
        3. You should sum a total of len(locs) quantities - don't forget to add 
        the last distance from the end point back to the beginning!
        """
        assert len(route) == len(self.locs.keys())
        pass # TODO: Your code here (<= 7 lines)

    def mcmc(self, T=0, num_iter=5000, succ_only=True):
        """
        :param T: The "temperature" parameter governing the tradeoff between
        exploration and exploitation.
        :param num_iter: The max number of iterations to perform.
        :param succ_only: 
            If True, must choose a single location, and swap with the location 
                immediately after (or wraparound if the last location was chosen).
                Use np.random.randint(...) to generate a random index i, and swap
                with index (i + 1) % len(route) in the current route.
            If False, during the transition phase, choose any two random locations in 
                the route and swap them (independently, meaning can swap with itself).
                Use np.random.randint(...) twice to generate random indices i and j, and 
                swap them. 
        :return: A tuple of three elements:
            1. The best route (a list).
            2. The distance of the best route (a float).
            3. A list of length num_iter, which has the distance of the 
            CURRENT route at the end of each iteration. This is NOT the current 
            best route NOR the new route (the CURRENT route is called "route" 
            in the pseudocode). (Hence, it is possible that it isn't monotone).

        Hint(s):
        1. Use the pseudocode provided in the spec!
        2. Use np.copy(route) to make a deep copy of route, so that you don't
        modify the current route when applying a random transition.
        3. Use your self.distance(...) function you implemented earlier.
        4. Use np.random.randint(...) to get a random integer — this should 
        be called once per iteration if succ_only is True and twice if succ_only
        is False.
        5. Use np.random.rand(...) to get a random float in [0, 1] — this 
        should be called once per iteration if delta is less than 0.
        6. Use np.exp(x) to compute e^x.
        7. Make sure you're using the parameter succ_only to determine what kind
        of random transitions are allowed.
        8. To return the variables a, b, and c in a tuple, do the following:
            return a, b, c
        """
        route = list(self.locs.keys())
        np.random.shuffle(route)

        pass # TODO: Your code here (~15-30 lines)

    def make_plot(self, T=0, num_iter=5000, succ_only=True, trials=10):
        """
        :param T: The "temperature" parameter governing the tradeoff between
        exploration and exploitation.
        :param num_iter: The max number of iterations to perform during each trial.
        :param succ_only: 
            If True, must choose a single location, and swap with the location 
                immediately after (or wraparound if the last location was chosen).
            If False, during the transition phase, choose any two random locations in 
                the route and swap them (independently, meaning can swap with itself). 
        :param trials: How many "random walks" to perform and plot.
        :return: A tuple of two elements:
            1. The best route (a list), over all "trials" number of trials.
            2. The distance of the best route (a float), over all "trials" number of trials.
        
        This function saves a SINGLE plot, with "trials" numbers of curves.
        On the x-axis, it plots the iteration number up to "num_iter".
        On the y-axis, it plots the current route distances for one run of MCMC. (And
        has "trials" separate curves on the same plot.)
        """
        np.random.seed(312)
        plt.figure()
        min_dist = float("inf")
        min_route = []
        for _ in range(trials):
            best_route, best_dist, lengths = self.mcmc(T, num_iter, succ_only)
            plt.plot(np.arange(len(lengths)), lengths)
            if best_dist < min_dist:
                min_dist = best_dist
                min_route = best_route
        print("Best Distance for T={}: {}".format(T, min_dist))
        file_name = "best_route_T=" + str(T) + "_succ_only=" + str(succ_only) + ".txt"
        print("Saving best route to the file: " + file_name)
        np.savetxt(file_name, np.array(min_route), "%s")
        plt.xlabel('Iteration')
        plt.ylabel('Length of Current Route')
        plt.suptitle('Distance vs. Iteration for Temperature {} with {} Transitions'.format(T, 'Successive' if succ_only else 'Any'))
        plt.title('Every trial is a different color.')
        mode = ('succ' if succ_only else 'any2')
        plt.savefig('mcmc_T={}_{}.png'.format(T, mode))
        return min_route, min_dist

if __name__ == '__main__':
    """
    Notes:
    1. In the below call to make_plot, the num_iter parameter is set to 500
    by default to run quickly. When you are ready to generate your final plots,
    you can change this parameter to 5000.
    2. To generate plots for part (e), you can change the succ_only parameter
    to False.
    """
    tsp_solver = TspMcmc()

    TEMPS = [0, 1, 5, 10]
    succ_only = True
    num_iter = 500
    for T in TEMPS:
        print("Making plot for T={} when succ_only={}".format(T, succ_only))
        tsp_solver.make_plot(T, num_iter=num_iter, succ_only=succ_only, trials=10)