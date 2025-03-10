from flask import Flask, render_template, url_for
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


data=pd.read_csv('train.csv')

visualize=Flask(__name__)

@visualize.route("/")
def home():
    return "Welcome to the Home page of the Data Visualization of Home Loan Status Data set"

@visualize.route('/Numerical_data')
def Numerical_data(): 
    num_feat = data.select_dtypes('number') 
    for feature in num_feat: 
        plt.figure()
        sns.boxplot(data, x='Loan_Status', y=feature)
        plt.show()
    return "Numerical Data Visualization"
    

if __name__ == '__main__':
    visualize.run(debug=True, port=3000)