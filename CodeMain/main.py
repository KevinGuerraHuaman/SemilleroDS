import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
#------------------------visualizacion

dataset = pd.read_csv('dataset/Stress-Lysis.csv',encoding='utf-8')
#etiquetas
print(dataset.columns.values.tolist())
#descripcion de datos
print(dataset.describe())
#verificamos valores nulos
print(dataset.isnull().sum(axis=0))

fig1, axs1 = plt.subplots(2,2)
axs1[0,0].hist(dataset['Humidity'].values)
axs1[0,0].set_title('Humidity(Sudoracion)')
axs1[0,1].hist(dataset['Temperature'].values)
axs1[0,1].set_title('Temperature')
axs1[1,0].hist(dataset['Step count'].values)
axs1[1,0].set_title('Step count')
axs1[1,1].hist(dataset['Stress Level'].values)
axs1[1,1].set_title('Stress Level')


fig2, axs2 = plt.subplots(2,2)
axs2[0,0].boxplot(dataset['Humidity'].values)
axs2[0,0].set_title('Humidity(Sudoracion)')
axs2[0,1].boxplot(dataset['Temperature'].values)
axs2[0,1].set_title('Temperature')
axs2[1,0].boxplot(dataset['Step count'].values)
axs2[1,0].set_title('Step count')
axs2[1,1].boxplot(dataset['Stress Level'].values)
axs2[1,1].set_title('Stress Level')

corr_df = dataset.corr(method='pearson')

fig = plt.figure()
axes = fig.add_subplot(111)
correlacion = axes.matshow(corr_df)
fig.colorbar(correlacion)

plt.show()



#----------------------------preprocesameinto
#revisar overlayer

# re-escalamiento de atributos
#(sirve cuando atributos tienen min y max muy diferentes)
"""
scaler = MinMaxScaler(feacture_range=(0,1))
rescaledX = scaler.fit_transform(X)

data_rescaled = pd.DataFrame(rescaledX, columns=['Humidity', 'Temperature', 'Step count', 'Stress Level'])
"""
# revisar balanceo

