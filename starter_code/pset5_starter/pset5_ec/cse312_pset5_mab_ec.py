# This starter code was written by Cooper Chia for CSE 312 Summer 2020.

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


class BanditAlgo:
    def __init__(self, k):
        """
        :param k: The total number of arms.

        You may (and should) define more fields as you need!
        """
        self.k = k

    def choose_arm(self):
        """
        :return: A single int n (0 <= n < k) representing an
        arm to choose. This method will be called once per
        iteration to choose the next arm.
        """
        return 0

    def update(self, reward, arm):
        """
        :param reward: An int (either 1 or 0) representing
        your reward for a single arm pull.
        :param arm: An int (0 <= arm < k) corresponding to which
        arm the reward came from.

        You should use this function to update your bandit model!
        It will be called once per iteration after the arm has
        been chosen and reward received.
        """
        pass


if __name__ == '__main__':
    """
    This is a simplified example of what we will
    do to test your code. 'data.txt' contains some
    rewards for each arm for each time step. 
    We iterate over the timesteps giving you the 
    reward at the arms your implementation chooses.
    From this we calculate the total reward and regret.
    """

    rewards = np.genfromtxt('data.txt', dtype=int)
    bandit_length = len(rewards[0])
    mab = BanditAlgo(bandit_length)
    total_reward = 0

    # Each iteration represents a single arm pull
    # out of 1000 trials.
    for t in rewards:
        arm_chosen = mab.choose_arm()
        reward = t[arm_chosen]
        total_reward += reward
        mab.update(reward, arm_chosen)
    print("Your total reward is: " + str(total_reward))
    # Not given to you, but the best arm has p=0.8, so best
    # total expected reward possible is 800 (out of 1000).
    print("Your regret is: " + str(16278 - total_reward))
