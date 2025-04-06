# save_checkpoint.py

import torch
import torch.nn as nn

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

# Initialize and save model
model = SimpleRLAgent(state_size=4, action_size=2)
torch.save(model.state_dict(), "checkpoint_rl.pt")
print("checkpoint_rl.pt saved successfully.")
