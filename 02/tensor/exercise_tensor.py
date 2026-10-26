import numpy as np 
import torch

data = np.array([[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

tensor = torch.tensor(data,dtype = float)
print("Problem1")
print(tensor)

subject_first = tensor.permute(2,0,1)
print("Problem2")
print(subject_first)

student_totals = subject_first.sum(dim=0)
print("Problem3")
print(student_totals)

class_means = student_totals.mean(dim = 1)
print("Problem4")
print(class_means)

number_of_students = student_totals.shape[1]
class_means_without_mean = (
    student_totals.sum(dim=1) / number_of_students    
)
print("Pronlem5")
print(class_means_without_mean)