from sklearn import tree
import matplotlib.pyplot as plt
from scipy import rand
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

dataset = pd.read_csv("dataset/box_noguantes_norma.csv")

x = dataset.drop('out',axis=1)
y = dataset['out']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10)

classifier = DecisionTreeClassifier(random_state=666)
classifier.fit(x_train, y_train)

y_predict = classifier.predict(x_test)



print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))

fig = plt.figure(figsize=(10,5))
_ = tree.plot_tree(classifier, 
                   feature_names=['x0','x1','y0','y1'],  
                   class_names=['0','1'],
                   filled=True)

plt.show()