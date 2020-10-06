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

"""
The data for this problem is provided in pokemon_small.txt and follows the
following format.

Col 1: pokemon_id: A unique identifier for the Pokemon.
Col 2: is_legendary: A 1 if the Pokemon is legendary, and 0 otherwise.
Col 3: height: The height of the Pokemon in meters.
Col 4: weight: The weight of the Pokemon in kilograms.
Col 5: encounter_prob: The probability of encountering this Pokemon 
in the wild grass. Note the sum of this entire column is 1, since when
you make an encounter, exactly one of these Pokemon appears.
Col 6: catch_prob: Once you have encountered a Pokemon, the probability 
you catch it. (Ignore any mechanics of the actual game if you’ve played 
a Pokemon game in the past.)
"""

def part_a(filename:str='data/pokemon_small.txt'):
    """
    Compute the proportion of Pokemon that are legendary, the average
    height, the average weight, the average encounter_prob, and average 
    catch_prob. 

    :param filename: The path to the csv as described in the pset.
    :return: A numpy array of length 5 with these 5 quantities.

    Hint(s):
    1. Use np.genfromtxt(...) to load the file. Do NOT hardcode 
    'data/pokemon_small.txt' as the parameter as we may use other hidden
    files to test your function.
    2. Use np.mean(...) with its axis parameter to compute means in one line.
    """
    pass # TODO: Your code here (<= 3 lines)

def part_b(filename:str='data/pokemon_small.txt'):
    """
    Compute the proportion of Pokemon that are legendary, the average
    height, the average weight, the average encounter_prob, and average 
    catch_prob OF ONLY those Pokemon STRICTLY heavier than the median weight. 

    :param filename: The path to the csv as described in the pset.
    :return: A numpy array of length 5 with these 5 quantities.

    Hint(s):
    1. Use np.median(...) to compute medians along an axis.
    2. Use np.where(...) to select only certain rows.
    """
    pass # TODO: Your code here (<= 5 lines)

def part_c(filename:str='data/pokemon_small.txt', ntrials:int=5000):
    """
    Suppose you are walking around the wild grass, and you wonder: how
    many encounters do you expect to make until you ENCOUNTER each Pokemon 
    (at least) once? 

    :param filename: The path to the csv as described in the pset.
    :param ntrials: How many simulations to run.
    :return: The (simulated) average number of ENCOUNTERS you expect to 
    make, until you ENCOUNTER each Pokemon (at least) once.

    Hint(s):
    1. You only need to use one of the columns for this part!
    2. You may want to use np.random.choice(...) with the parameter a
    being np.arange(...) and the parameter p being the data column!
    """

    def sim_one():
        """
        This is a nested function only accessible by parent 'part_c',
        which we're in now. You may want to implement this function!
        """
        pass

    pass # TODO: Your code here (10-20 lines)

def part_d(filename:str='data/pokemon_small.txt', ntrials:int=5000):
    """
    Suppose you are walking around the wild grass, and you wonder: how
    many encounters do you expect to make until you CATCH each Pokemon 
    (at least) once? 

    :param filename: The path to the csv as described in the pset.
    :param ntrials: How many simulations to run.
    :return: The (simulated) average number of ENCOUNTERS you expect to 
    make, until you CATCH each Pokemon (at least) once.

    Hint(s):
    1. You only need to use two of the columns for this part!
    2. You may want to use np.random.choice(...) with the parameter a
    being np.arange(...) and the parameter p being the data column!
    3. You may want to use np.random.rand(...).
    """
    data = np.genfromtxt(filename)[:, -2:]
    n_pokemon = data.shape[0]

    def sim_one():
        """
        This is a nested function only accessible by parent 'part_d',
        which we're in now. You may want to implement this function!
        """
        pass
    
    pass # TODO: Your code here (10-20 lines)

if __name__ == '__main__':
    # You can test out things here. Feel free to write anything below.
    print(part_a())
    print(part_b())
    print(part_c())
    print(part_d())