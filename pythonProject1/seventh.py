

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1.1
randomIntegerNums_list = (np.random.randint(-3, 21, 10000)).tolist()
print(randomIntegerNums_list)

print("avg: " + str(np.average(randomIntegerNums_list)) + "\n" +
      "median: " + str(np.median(randomIntegerNums_list)) + "\n" +
      "max: " + str(np.max(randomIntegerNums_list)) + "\n" +
      "min: " + str(np.min(randomIntegerNums_list)) + "\n" +
      "The percent of nums < 3*standartDeviation " + str(
    np.sum(randomIntegerNums_list < 3 * np.std(randomIntegerNums_list)) / len(
        randomIntegerNums_list) * 100) + "%" + "\n" +
      "The percent of nums < median " + str(
    sum(randomIntegerNums_list < np.median(randomIntegerNums_list)) / len(randomIntegerNums_list) * 100) + "%")

uniqueNums_array, occurences_array = np.unique(randomIntegerNums_list, return_counts=True)
df_rows = []
for i in range(len(uniqueNums_array)):
    isNegative = uniqueNums_array[i] < 0
    a = [uniqueNums_array[i], occurences_array[i], isNegative]
    df_rows.append(a)
df = pd.DataFrame(df_rows)
df.columns = ['liczba', 'występowanie', 'czy_ujemna']
print(df)

df_withoutNegatives = df[df['czy_ujemna'] == 0]
print(df_withoutNegatives)

plt.bar(df['liczba'], df['występowanie'])
plt.xlabel('Liczba')
plt.ylabel('Częstotliwość')
plt.title('Histogram częstości występowania')
plt.show()

with open(f"Dane_{np.mean(df_withoutNegatives['liczba'])}_{np.std(df_withoutNegatives['liczba']):.4f}.csv",
          "w") as file:
    df_withoutNegatives.to_csv(file, index=False)
