###############################################################################
# Mlflow Example @ Auckland Machine Learning Summit 
#
# Predict the onset of diabetes based on diagnostic measures
#
# Author: Vivek Katial
# Created 2019-02-14
###############################################################################

# Import relevant libraries
import os
import warnings
import sys
import pandas as pd
import mlflow
import mlflow.sklearn
import numpy as np

# Import SKlearn dependencies
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


# Import plotting dependencies
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


'''
Read data into environment
'''
def read_data(file_name):
    # Define column names
    col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
    pima = pd.read_csv(file_name, header=0, names=col_names)
    pima.astype(np.float64)

    return pima

'''
Process data into train/test splits
'''
def process_data(df):
    # Split dataset into input variables and our target variable
    feature_cols = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
    X = pima[feature_cols] # Inputs
    y = pima.label

    # Split X and y into the training and test set
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

    return X_train,X_test,y_train,y_test

'''
Building logistic regression model
'''
def build_model(X_train,X_test,y_train,y_test, solver, C):

    # instantiate the model (using the default parameters)
    logreg = LogisticRegression(
        solver=solver,
        C=C, 
        max_iter=1000
        )

    # fit the model with data
    logreg.fit(X_train,y_train)

    # compute predictions
    y_pred=logreg.predict(X_test)

    mlflow.sklearn.log_model(logreg, "sk_models")

    return y_pred

'''
Compute outputs
'''
def compute_outputs(y_test, y_pred):
    # Plot matrix
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)

    # name  of classes
    class_names=[0,1] 

    fig, ax = plt.subplots()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names)
    plt.yticks(tick_marks, class_names)

    # create heatmap
    conf_mat = sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
    ax.xaxis.set_label_position("top")
    plt.tight_layout()
    plt.title('Confusion matrix', y=1.1)
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')

    figure = conf_mat.get_figure()    
    figure.savefig('conf_mat.png', dpi=400)

    mlflow.log_artifact('conf_mat.png')

    # Output results
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("Precision:",metrics.precision_score(y_test, y_pred))
    print("Recall:",metrics.recall_score(y_test, y_pred))

    # Log metrics
    mlflow.log_metric("Accuracy",metrics.accuracy_score(y_test, y_pred))
    mlflow.log_metric("Precision",metrics.precision_score(y_test, y_pred))
    mlflow.log_metric("Recall",metrics.recall_score(y_test, y_pred))

if __name__ == '__main__':

    # Extract parameters argument variables
    C = float(sys.argv[1]) if len(sys.argv) > 1 else 1
    solver = sys.argv[2] if len(sys.argv) > 2 else "liblinear"

    mlflow.log_param("C", C)
    mlflow.log_param("solver", solver)

    pima = read_data("diabetes.csv")
    X_train,X_test,y_train,y_test = process_data(pima)

    y_pred = build_model(X_train,X_test,y_train,y_test, solver, C)
    compute_outputs(y_test, y_pred)
    print("Awesome your experiment is DONE!")
