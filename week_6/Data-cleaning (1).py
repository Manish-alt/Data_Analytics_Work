
################ Data cleaning the Iris dataset #################
from sklearn import datasets
import pandas as pd

# load iris dataset
iris = datasets.load_iris()
# Since this is a bunch, create a dataframe
iris_df=pd.DataFrame(iris.data)
iris_df['class']=iris.target

iris_df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
#### ===> TASK 1: here - add two more lines of the code to find the number and mean of missing data
# find the number of missing values in each column
missing_count = iris_df.isnull().sum()
print("Number of missing values:\n", missing_count)

# find the mean of missing values in each column
missing_mean = iris_df.isnull().mean()
print("Mean of missing values:\n", missing_mean)

cleaned_data = iris_df.dropna(how="all", inplace=True) # remove any empty lines


iris_X=iris_df.iloc[:5,[0,1,2,3]]
print(iris_X)

### TASK2: Here - Write a short readme to explain above code and how we can calculate the corrolation amoung featuers with description

# README: Iris Dataset Analysis
# Overview

# This script demonstrates how to analyze the Iris dataset using Python libraries such as pandas and scikit-learn. The code loads the Iris dataset, processes it into a pandas DataFrame, handles missing data, and extracts a subset of features for further analysis. Below, we explain the code functionality and how to compute the correlation among features.

# Code Explanation

# Loading the Iris Dataset:

# from sklearn import datasets
# import pandas as pd

# iris = datasets.load_iris()

# The Iris dataset is loaded using sklearn.datasets.load_iris(). This dataset includes features such as sepal length, sepal width, petal length, and petal width, along with the target classes.

# Creating a DataFrame:

# iris_df = pd.DataFrame(iris.data)
# iris_df['class'] = iris.target

# iris_df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']

# The dataset is converted into a pandas DataFrame for easier manipulation. Column names are assigned for clarity.

# Handling Missing Data:

# # Find the number of missing values per column
# missing_count = iris_df.isnull().sum()

# # Find the mean of missing values (proportion of missing data per column)
# missing_mean = iris_df.isnull().mean()

# print("Number of missing values:\n", missing_count)
# print("\nMean of missing values:", missing_mean)

# To ensure data integrity, the code checks for missing values using isnull().sum() and calculates the proportion of missing data using isnull().mean().

# Cleaning the Data:

# cleaned_data = iris_df.dropna(how="all", inplace=True)

# Rows with all values missing are removed using dropna().

# Extracting a Subset of Features:

# iris_X = iris_df.iloc[:5, [0, 1, 2, 3]]
# print(iris_X)

# A subset of features (sepal length, sepal width, petal length, petal width) for the first 5 rows is extracted for preview.

# Calculating Correlation Among Features

# To compute the correlation among the features in the Iris dataset, you can use the following:

# # Compute correlation matrix
# correlation_matrix = iris_df.iloc[:, :-1].corr()

# # Display correlation matrix
# print("Correlation matrix:\n", correlation_matrix)

# Description:

# The corr() function calculates the Pearson correlation coefficient for each pair of features.

# The output is a symmetric matrix where each cell represents the correlation between two features:

# Values close to 1 indicate a strong positive correlation.

# Values close to -1 indicate a strong negative correlation.

# Values near 0 indicate little or no correlation.

# By analyzing the correlation matrix, you can identify relationships between features, which can be helpful in feature selection or understanding the dataset's structure.