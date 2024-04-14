import torch
import torch.nn as nn
import torch.nn.functional as F

class ReturnsClassifier(nn.Module):

    def __init__(
            self,
            num_units_1st=10,
            num_units_2nd=30,
            nonlin=F.relu,
            dropout=0.0,
    ):

        # initialise model
        super().__init__()
        self.num_units_1st = num_units_1st
        self.num_units_2nd = num_units_2nd
        self.nonlin = nonlin
        self.dropout = dropout

        # first hidden layer
        self.dense0 = nn.Linear(41, num_units_1st)
        self.nonlin = nonlin
        self.dropout = nn.Dropout(dropout)

        # second hidden layer
        self.dense1 = nn.Linear(num_units_1st, num_units_2nd)
        self.output = nn.Linear(num_units_2nd, 2)

    def forward(self, X, **kwargs):
        X = self.nonlin(self.dense0(X))
        X = self.dropout(X)
        X = F.relu(self.dense1(X))
        X = F.softmax(self.output(X), dim=-1)
        return X
