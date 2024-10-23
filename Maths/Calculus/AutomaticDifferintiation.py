import torch

x = torch.tensor(5.0)
x.requires_grad_()

y = x**2
y.backward()

print(x.grad)