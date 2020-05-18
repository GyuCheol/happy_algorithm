import torch
import torch.nn as nn

# target output size of 5x7
m = nn.AdaptiveAvgPool2d((2,2))
input = torch.randn(1, 3, 4, 4)
print(input)

output = m(input)
print(output)

