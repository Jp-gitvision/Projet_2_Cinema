import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df_voiture = pd.read_csv(link)

plt.figure(figsize = (12,7))
sns.heatmap(df_voiture.corr(),
            annot=True,
            cmap ='vlag',
            center = 0)
plt.show()

# Nous pouvons remarquer qu'il y a de très forte corrélation positive entre ses trois ses 4 variables : cylinders, cubicinches, hp & weightlbs.
# Nous pouvons remarquer qu'il y a de très forte corrélation négative entre mpg et ses 4 variables : cylinders, cubicinches, hp & weightlbs
# nous pouvons aussi remarquer d'autres corrélations négatives un peu moins forte entre time-to-60 et ses 4 variables : cylinders, cubicinches, hp & weightlbs

plt.hist(df_voiture["mpg"])

# exemple d'un graphique en histogramme.

plt.figure(figsize=(12, 5))
sns.scatterplot(data = df_voiture, x = "mpg", y = "cubicinches", hue = "continent")

# Autre exemple avec un scatterplot sous matplotlib en prenant deux colonnes correlés négativement par continent.

sns.pairplot(
    df_voiture
)

# On peut remarquer le même constat que pour la correlation sous forme de heatmap