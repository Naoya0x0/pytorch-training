import torchfrom torch
import number_of_students

class MyModel(nn.Module):

def __init__(self,arg1: int,arg2: float):
    super().__init__()
    self.arg1 = arg1self.arg2 = arg2
    def forward(self,x):
        x = x + self.arg1
        x = x / self.arg2

        return x 

if __name__ == "__main__":

    MyModel = MyModel(3, 2.0)

    _input = torch.ones([2,3])

    out1 = MyModel(_input)
    out2 = MyModel.forward(_input)


    print(out1)

    print(out2)