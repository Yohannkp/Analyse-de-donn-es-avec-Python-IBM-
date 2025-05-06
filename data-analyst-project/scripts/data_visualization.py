import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column, bins=30, title='Histogram', xlabel='Value', ylabel='Frequency'):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column], bins=bins, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def plot_scatter(data, x_column, y_column, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis'):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_column], data[y_column], alpha=0.6)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def plot_boxplot(data, column, title='Box Plot', xlabel='Category', ylabel='Value'):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x=column)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()