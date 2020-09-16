import pandas as pd
# import numpy as np

class Pred:
    def __init__(self):
        self.df = pd.read_csv('/home/superadmin/DBDA/project/My_Project/Prediction.csv')
        
        
    def clean(self):
        
        x = self.df.iloc[:, 2:8].values
        y = self.df.iloc[:, 1].values
        from sklearn.preprocessing import LabelEncoder  
        encoder = LabelEncoder()
        x[:,0] = encoder.fit_transform(x[:,0])
        y = encoder.fit_transform(y)
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.8,random_state=123)
        return x_train,x_test,y_train,y_test
    def accuracy(self,predictions,y_test):
        # create the confusion matrix
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test, predictions)

        accuracy = (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])
        print(round((accuracy*100),2),"%")

    def decis(self,x_train,x_test,y_train):
        # x_train,x_test,y_train,y_test = clean()
        from sklearn.tree import DecisionTreeClassifier
        classifier = DecisionTreeClassifier()
        classifier = classifier.fit(x_train, y_train)
        predictions = classifier.predict(x_test)
        print(predictions)
        # return predictions
        return predictions
    
pred=Pred()
x_train,x_test,y_train,y_test = pred.clean()
x,y = pred.decis(x_train,x_test,y_train)
pred.accuracy(x,y_test)




import pandas as pd
from sklearn import  tree   

xtrain = pd.read_csv("/data/training/wine_train.csv", header = 0)
xtest = pd.read_csv("/data/test/wine_test.csv", header = 0)
x = xtrain.iloc[:,:11]
y = xtrain.iloc[:,11:]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.8,random_state=123)
#Write your code here
predictn = tree.DecisionTreeClassifier()
predictn = predictn.fit(x_train,y_train)
# print(xtest)
x = xtest.iloc[:,:11]
# print(x)
y = xtest.iloc[:,11:12]
# print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.8,random_state=123)
predictions =predictn.predict(x_test)
finalOutput =[] #

for i in predictions:
    if i< 6 :
        finalOutput.append('bad')
    elif i == 6 :
        finalOutput.append('normal')
    else:
        finalOutput.append('good')

    print(finalOutput)
f_out = pd.DataFrame(finalOutput,columns=['taste'])
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)

accuracy = (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])
print(round((accuracy*100),2),"%")

f_out.columns = ['id', 'taste']
f_out.to_csv("/code/wine_prediction.csv", index = False)
result = pd.read_csv("/code/wine_prediction.csv")
print(result)
