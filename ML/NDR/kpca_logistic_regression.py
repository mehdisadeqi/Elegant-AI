import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Classification
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA, KernelPCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Read sensor data
sensor_data = pd.read_csv('SensorsDataDividedByClass.csv')

# Split data to train and test sets
train_x, test_x, train_y, test_y = train_test_split(sensor_data.iloc[:, :10], sensor_data.iloc[:, 10], test_size=0.3)

# Create a pipeline of 'dimensionality reduction' using KPCA followed by a Logistic Regression classifier, 
# then fit it to the train data
pipeline = Pipeline([('kpca', KernelPCA(n_components=2, kernel='rbf')), 
                     ('classifier', LogisticRegression(solver='lbfgs', random_state=12345))])
model_kpca = pipeline.fit(train_x, train_y)

# transform test data using KPCA in the pipeline
transformed_test_x = pipeline['kpca'].transform(test_x)

# Visualize transformed test data along with the decision boundary of Logistic Regression classifier.
X1, X2 = np.meshgrid(np.arange(transformed_test_x[:, 0].min() - 0.1, transformed_test_x[:, 0].max() + 0.1, 0.001), 
                     np.arange(transformed_test_x[:, 1].min() - 0.1, transformed_test_x[:, 1].max() + 0.1, 0.001))

fig, axs = plt.subplots(1, 2, figsize=(15, 7))
# KPCA transformed test data
axs[0].scatter(transformed_test_x[:, 0], transformed_test_x[:, 1], 
               c=test_y, alpha=0.2, cmap=ListedColormap(['green', 'red']))
# KPCA transformed test data along with the decision boundary
axs[1].contourf(X1, X2, 
                model_kpca['classifier'].predict(np.array([X1.flatten(), X2.flatten()]).T).reshape(X1.shape), 
                alpha=0.6, cmap=ListedColormap(['red', 'green']))
axs[1].scatter(transformed_test_x[:, 0], transformed_test_x[:, 1], 
               c=test_y, alpha=0.3, cmap=ListedColormap(['green', 'red']))