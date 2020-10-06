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
import mmh3

class DistElts:
    def __init__(self, seed_offset:int=0):
        """
        :param seed_offset: Allows for multiple instances of this
        class to provide different results.
        
        We only use one variable, self.val, in our entire
        implementation.
        """
        self.seed_offset = seed_offset
        self.val = float("inf")

    def hash(self, x:int) -> float:
        """
        :param x: The element x to be hashed.
        :return: A Unif(0,1) continuous random variable. However,
        if the same x is passed in, we will return the same exact
        Unif(0,1) rv. We do this by taking the modulus by a large
        number, and dividing by it so that we get "approximately" a
        random float between 0 and 1.
        """
        large_num = 2 ** 31
        h = mmh3.hash(x, self.seed_offset) % large_num + 1
        return h / large_num

    def update(self, x:int):
        """
        :param x: The new stream element x.
        
        In this function, you'll update self.val as you described
        in the previous part.

        Hint(s):
        1. You will want to use self.hash(...).
        """
        pass # TODO: Your code here (1 line)

    def estimate(self) -> int:
        """        
        :return: Your estimate so far for the number of distinct
        elements you've seen. Make sure you round to the nearest
        integer!

        Hint(s):
        1. You will want to use self.val here.
        """
        pass # TODO: Your code here (1 line)

class MultDistElts:
    def __init__(self, num_reps:int=1):
        """
        :param num_reps: How many copies of DistElts we have.

        Creates num_reps different DistElts objects, by passing in
        different seed_offsets.
        """
        self.num_reps = num_reps
        self.des = [DistElts(seed_offset=i) for i in range(num_reps)]

    def update(self, x:int):
        """
        :param x: The new stream element x.
        
        In this function, you'll call `update` for all the 
        DistElts objects in self.des.
        """
        pass # TODO: Your code here (2 lines)

    def estimate(self) -> int:
        """        
        :return: Your estimate so far for the number of distinct
        elements you've seen. You will take the AVERAGE of the mins
        from your DistElts objects in self.des to get a better estimate
        for the min, and THEN use the same approach as earlier to 
        make an estimate for the number of distinct elements. 

        Hint(s):
        1. Numpy is imported :).
        2. You can access fields of objects in Python 
           (similar to public fields in Java)
           Example:
           de = DistElts(seed_offset=0) # a DistElts Object
           val = de.val                 # the val field of de
        """
        pass # TODO: Your code here (1-5 lines)

if __name__ == '__main__':
    # You can test out things here. Feel free to write anything below.
    stream = np.genfromtxt('data/stream_small.txt', dtype='int')

    # 312 actual distinct Elements in the stream
    print("True Dist Elts: {}".format(312))

    # Create a DistElts object, and update for each element in the stream.
    # Finally, print out the estimate.
    de = DistElts()
    for x in stream:
        de.update(x)
    print("Dist Elts Estimate: {}".format(de.estimate()))

    # Create a MultDistElts object, and update for each element in the 
    # stream. Finally, print out the estimate.
    num_reps = 50
    mde = MultDistElts(num_reps=num_reps)
    for x in stream:
        mde.update(x)
    print("Mult Dist Elts Estimate with {} copies: {}".format(num_reps, mde.estimate()))
