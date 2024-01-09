import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import export_graphviz

import graphviz
from IPython.display import display
from sklearn.tree import export_graphviz

# Load the data from Excel
df = pd.read_excel('data.xlsx')

# 'Abandono' is the target variable
selected_columns = ['maiores 23', 'cd_curso', 'sexo', 'trabalhadorEstudante', 'Abandono']
features = df[selected_columns].drop('Abandono', axis=1)
target = df['Abandono']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the Random Forest model
model = RandomForestClassifier()

# Hyperparameter tuning with GridSearchCV (if needed)
param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best model from the grid search
best_model = grid_search.best_estimator_

# Export and display the first three decision trees
for i in range(3):
    tree = best_model.estimators_[i]  # Access the ith decision tree
    dot_data = export_graphviz(tree,
                               feature_names=X_train.columns,
                               filled=True,
                               max_depth=2,
                               impurity=False,
                               proportion=True)
    graph = graphviz.Source(dot_data)
    display(graph)
