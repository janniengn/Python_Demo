import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Create a more complex dataset
data = {
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=500),
    'Age': np.random.randint(18, 60, size=500),
    'Income': np.random.randint(30000, 120000, size=500),
    'Score': np.random.randn(500) * 15 + 75,  # Normally distributed scores
    'Height': np.random.uniform(150, 190, size=500),  # Height in cm
    'Weight': np.random.uniform(45, 100, size=500),  # Weight in kg
}

# Create DataFrame
df = pd.DataFrame(data)

# Add an artificial correlation between Income and Age
df['Income'] = df['Income'] + (df['Age'] - 30) * 200

# Plotting setup
plt.figure(figsize=(16, 12))

# Create a pairplot to visualize relationships between multiple continuous variables
sns.pairplot(df, hue='Category', palette='Set2', plot_kws={'alpha': 0.7})
plt.suptitle('Pairplot of Numerical Features', y=1.02)
plt.show()

# Create a correlation heatmap of the numerical variables
plt.figure
