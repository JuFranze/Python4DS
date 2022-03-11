import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Variables
area = ['East', 'West', 'North', 'East']
candidates= [100, 200, 300, 400]
matrix_1 = [[1, 2], [2, 4]]


# find out what type your variables are
print(type(area))
print(type(candidates))



#Find the max and min of the candidates list 
max_list_1 =np.max(candidates)
mix_list_1 = np.min(candidates)
print("The max of List_1 is :", max_list_1, " & the min :", mix_list_1)


#Create the sum of candidates with initial value of 50 to the sum
sum_list_1 = np.sum(candidates, initial=50)
print('Sum with initial value: ',sum_list_1)


#STD of list 1 & Matrix 1
# Standard Deviation (STD) is the measure by which the elements of a set are deviated or dispersed from the mean.
std_list_1 = np.std(candidates)
print( "Standard Deviation of list_1: ", std_list_1)

a= np.array(matrix_1)
std_matrix_1 = np.std(a)
print( "Standard Deviation of list_1: ", std_matrix_1)


# create graph with pandas for canditiakes & areas

# define dictionary
inter_dict = dict(area=area, qty=candidates)
print("Dictionary: ", inter_dict)

#create DataFrame from dictionary
interviews = pd.DataFrame(inter_dict)
print("Dataframe: ", interviews)

# render graph
interviews.plot(kind='barh', y = 'qty', x='area')
plt.show()
