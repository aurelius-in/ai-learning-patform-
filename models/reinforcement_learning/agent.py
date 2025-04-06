import torch
import torch.nn as nn
import torch.optim as optim

class SimpleRLAgent(nn.Module):
    def __init__(self, state_size, action_size):
        super(SimpleRLAgent, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_size, 64),
            nn.ReLU(),
            nn.Linear(64, action_size)
        )

    def forward(self, x):
        return self.fc(x)