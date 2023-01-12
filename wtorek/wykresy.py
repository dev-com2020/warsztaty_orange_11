import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv(r"../data.csv")
print(df)
df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
x = df['date']
y = df['Close']

lista = [100, 1999]

figura, ax = plt.subplots(2, figsize=(10, 4))
ax[0].scatter(x, y, marker='+', alpha=.5)
_ = ax[1].pie(lista, labels=['wpłata', 'wypłata'])
# _ = ax.legend()
plt.show()
