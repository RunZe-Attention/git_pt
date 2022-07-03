import torch


t = torch.tensor([[1,2],[3,4]])
#print(t)

b = torch.gather(input=t,dim=0,index=torch.tensor([[0,1],[1,0]]))

print(b)