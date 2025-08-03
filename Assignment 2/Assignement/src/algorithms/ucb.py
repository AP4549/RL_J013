import numpy as np
from algorithms.base_algorithm import BaseMABAlgorithm

class UCB(BaseMABAlgorithm):
    """
    Upper Confidence Bound (UCB) algorithm
    Balances exploration and exploitation using confidence bounds
    """
    def __init__(self, n_arms: int, c: float = 2.0, **kwargs):
        super().__init__(n_arms, **kwargs)
        self.c = c  # Exploration parameter
        
    def select_arm(self) -> int:
        """
        ## IMPLEMENT UCB ALGORITHM HERE ##
        
        Input: None (uses self.estimates, self.pulls, self.c)
        Output: int - selected arm index
        
        Strategy: UCB balances exploration and exploitation using confidence bounds
        - If some arms haven't been pulled: pull one of them
        - Otherwise: select arm with highest UCB value
        - UCB formula: estimate + c * sqrt(log(total_pulls) / arm_pulls)
        """
        if np.any(self.pulls == 0):
            return int(np.argmin(self.pulls))
        ucb_values = self.estimates + self.c * np.sqrt(np.log(np.sum(self.pulls)) / self.pulls)
        return int(np.argmax(ucb_values))
