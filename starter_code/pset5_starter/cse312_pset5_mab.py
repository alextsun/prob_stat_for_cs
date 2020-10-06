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

class MultiArmedBandit:
    """
    An instance of the MultiArmedBandit class contains K arms, where
    each arm is assumed to have a Bernoulli reward distribution. 
    Arm i's reward distribution is ~Ber(p_i).
    """

    def __init__(self, ps):
        """
        :param ps: An list/numpy array of K probabilties, where ps[i]
        is the underlying TRUE probability that arm i returns a 1, and
        (1 - ps[i]) is the underlying TRUE probability that arm i 
        returns a 0). We don't know these probabilities in real life 
        though!
        """
        assert np.all(0 <= ps) and np.all(ps <= 1)
        self.ps = ps
        self.K = len(ps)
        self.reset_history()

    def reset_history(self):
        """
        Creates/resets two empty lists to track the pulls and rewards.

        self.pull_history[t]:
            contains the index of the arm {0,1,...,self.K-1} that was pulled 
            at time t.

        self.reward_history[t]:
            contains the reward (either 0 or 1) that the arm pulled at time 
            t (self.pull_history[t]) gave.
        """
        self.pull_history = []
        self.reward_history = []

    def pull_arm(self, arm):
        """
        :param arm: Which arm to pull. Must be in the set {0,1,...,self.K-1}
        :return: Either a 1 or a 0: the random reward determined by pulling
        `arm` once.

        This function updates the pull history and reward history, and returns
        the reward observed by pulling `arm`. It's the only place we use self.ps.
        """
        assert 0 <= arm <= self.K - 1
        assert len(self.pull_history) == len(self.reward_history)
        reward = np.random.binomial(1, self.ps[arm])
        self.pull_history.append(arm)
        self.reward_history.append(reward)
        return reward

    def make_all_plots(self, algo):
        assert algo in ['ucb', 'thompson']
        self.plot_arm_selection(algo)
        self.plot_avg_cum_regret(algo)

    def plot_arm_selection(self, algo):
        """
        :param algo: Either the string 'ucb' or 'thompson'.

        Makes a plot with the x-axis being time, and the y-axis being
        cumulative proportion of time each arm was pulled. This plot 
        will have self.K different lines plotted: one per arm.
        """
        assert algo in ['ucb', 'thompson']
        assert len(self.pull_history) == len(self.reward_history)

        pull_history = np.array(self.pull_history)
        T = len(pull_history)
        x = np.arange(1, T + 1)
        for arm in range(self.K):
            indicators = (pull_history == arm)
            cumulative_prop = np.cumsum(indicators) / np.cumsum(np.ones(T))
            plt.plot(x, cumulative_prop, label='arm {0:d}, p={1:.2f}'.format(arm, self.ps[arm]))
        plt.legend()
        plt.xlabel("Time")
        plt.ylabel("Proportion of Times Pulled")
        plt.title("({}) Proportion of Times Pulled vs Time".format(algo))
        plt.savefig('prop_times_pulled_{}.png'.format(algo))
        plt.close()

    def plot_avg_cum_regret(self, algo):
        """
        :param algo: Either the string 'ucb' or 'thompson'.

        Makes a plot with the x-axis being time, and the y-axis being
        cumulative regret. 
        """
        assert algo in ['ucb', 'thompson']
        assert len(self.pull_history) == len(self.reward_history)

        reward_history = self.reward_history
        T = len(reward_history)
        x = np.arange(1, T + 1)
        cum_reward = np.cumsum(reward_history)
        best_exp_reward = np.max(ps) * np.arange(1, T + 1)
        y = (best_exp_reward - cum_reward) / np.cumsum(np.ones(T))
        plt.plot(x, y)
        plt.xlabel("Time")
        plt.ylabel("Avg Cumulative Regret")
        plt.title("({}) Avg Cumulative Regret vs Time".format(algo))
        plt.savefig('cum_regret_{}.png'.format(algo))
        plt.close()

    def upper_conf_bound(self, T=100000):
        """
        :param T: The number of time steps to run this UCB algorithm.
        :return: The total reward accumulated during T time steps.
        
        Implements the Upper Confidence Bound (UCB) algorithm
        for the Bernoulli Bandit Problem.

        Hint(s):
        1. Use np.zeros(m) to create an m-dimensional numpy array of 0's.
        2. Numpy arithmetic happens pointwise. That is, if
            x = [9, 35, 26] (numpy array)
            y = [3, 7, 13] (numpy array)
        Then,
            x / y = [3.0, 5.0, 2.0]
        3. You MUST use self.pull_arm(...) to get a 0/1 reward. This will also
        update some "history" so that the plots can be generated. You are not 
        allowed to, and will not get full credit if you modify/use self.ps. 
        You must follow the algorithm pseudocode provided.
        4. Be careful witht the ranges in the loops (for example: use range(1, T+1) 
        to go from 1,...,T).
        5. Use the functions np.log(...) and np.argmax(...).
        """
        self.reset_history()

        # TODO: Your code here (~15-20 lines)
        # Do NOT delete/modify the line above and below this comment.

        return np.sum(self.reward_history)

    def thompson_sampling(self, T=100000):
        """
        :param T: The number of time steps to run this UCB algorithm.
        :return: The total reward accumulated during T time steps.
        
        Implements the Thompson Sampling (TS) algorithm
        for the Beta-Bernoulli Bandit Problem.

        Hint(s):
        1. Use np.ones(m) to create an m-dimensional numpy array of 1's.
        2. Use np.random.beta(a, b) to generate a random float in [0,1]
        according to a Beta(a, b) distribution.
        3. You MUST use self.pull_arm(...) to get a 0/1 reward. This will also
        update some "history" so that the plots can be generated. You are not 
        allowed to, and will not get full credit if you modify/use self.ps. 
        You must follow the algorithm pseudocode provided.
        4. Be careful witht the ranges in the loops (for example: use range(1, T+1) 
        to go from 1,...,T).
        5. Use the function np.argmax(...).
        """
        self.reset_history()
        
        # TODO: Your code here (~10-15 lines)
        # Do NOT delete/modify the line above and below this comment.

        return np.sum(self.reward_history)

if __name__ == '__main__':
    """
    Creates an instance of the Bernoulli MAB problem with the true reward
    probabilities in ps, and runs UCB and Thompson Sampling for T iterations.
    Then, it makes some nice plots.
    """
    ps = np.array([0.36, 0.77, 0.89, 0.74, 0.11])
    T = 10000
    mab = MultiArmedBandit(ps=ps)
    ucb_reward = mab.upper_conf_bound(T=T)
    mab.make_all_plots('ucb')
    ts_reward = mab.thompson_sampling(T=T)
    mab.make_all_plots('thompson')
    print("Upper Conf Bound  Reward: {} after {} Steps".format(ucb_reward, T))
    print("Thompson Sampling Reward: {} after {} Steps".format(ts_reward, T))