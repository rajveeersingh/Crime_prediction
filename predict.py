import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import math
import locale
from testmongo import *

class Predict:
    def clean(self):
        df = pd.read_csv('/home/superadmin/DBDA/project/My_Project/Predict.csv',usecols=['crime_type','year'])
        Nd = pd.DataFrame(df['crime_type'].groupby(df['year']).agg('count').reset_index(name="crime_count"))
        x = Nd.iloc[:, [0]].values
        y = Nd.iloc[:, [1]].values   
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1234)
        return x_train,y_train
    # prediction model
    def model(self,value):
        x_train,y_train = Predict().clean()
        regression = LinearRegression()
        regression.fit(x_train, y_train)
        prediction = regression.predict([[value]])
        print(prediction[0][0])
        z = prediction[0][0] % 1
        if z >= 0.5:  
            pred = math.ceil(prediction[0][0])
            print(f"prdiction1 is {pred}")
        else:
            pred = math.floor(prediction[0][0])
            print(f"prdiction 2is {pred}")
        return locale.format("%d", pred, grouping=True)

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
        return predictions