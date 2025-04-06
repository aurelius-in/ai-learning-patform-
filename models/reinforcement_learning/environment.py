import numpy as np

class LearningEnvironment:
    def __init__(self):
        self.state_space = 4
        self.action_space = 2
        self.state = np.random.rand(self.state_space)

    def step(self, action):
        reward = np.random.rand() if action == 1 else -np.random.rand()
        self.state = np.random.rand(self.state_space)
        done = np.random.rand() > 0.95
        return self.state, reward, done

    def reset(self):
        self.state = np.random.rand(self.state_space)
        return self.state