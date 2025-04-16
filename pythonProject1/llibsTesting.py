

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array2d[1,0])
print(array2d[1,:])
print(array2d[:,1])

array1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array1d)
zeros_array = np.zeros((3,3))
print(zeros_array)

zeroslike_array = np.zeros(array1d.shape)
print(zeroslike_array)

oneslike_array = np.ones(array2d.shape)
print(oneslike_array)

random_array = np.random.rand(3,3)
print(random_array)

random_numbers = np.random.rand(5)
print(random_numbers)

random_integers = np.random.randint(low=1, high=100, size=5)
print(random_integers)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)

a= [['Ania',24],['Michał',9],['Darek',40],['Ania',24],['Michał',9],['Darek',40]]
df_a = pd.DataFrame(a)
print(df_a)

df_a.columns = ["Name", "Age"]
print(df_a)

df_a['Nowa kolumna'] = 1
print(df_a)

df_a = df_a.drop(columns=['Nowa kolumna'])
print(df_a)

print(df_a.head())
print(df_a.describe())

x = np.linspace(0, 10, 100) #Creates an array of evenly spaced numbers from start to stop (inclusive), with a total of num numbers.
y = np.sin(x)
plt.plot(x,y,label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x)')
plt.legend()
plt.show()

plt.scatter(x,y,label='scatter')