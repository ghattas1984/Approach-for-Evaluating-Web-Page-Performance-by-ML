
from IPython.display import Image
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import pandas as pd
import numpy as np

from sklearn.preprocessing import Normalizer, normalize, RobustScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import make_scorer, mean_squared_error

from sklearn.feature_selection import mutual_info_regression, RFECV,SelectFromModel,RFE,VarianceThreshold
from functools import partial
from pathlib import Path
from joblib import load, dump

from scipy import stats
from scipy.stats import norm
from statsmodels.graphics.gofplots import qqplot

data = pd.read_csv('Final_Dataset_with_featureselection.csv')

data.head()

data.describe().round(2)

data.shape

# Features data-type
data.info()

# Statistical summary
data.describe().T

data.groupby('class').size()

# Count of null values
data.isnull().sum()

# performance countplot
sns.countplot(x = 'class',data = data)

descriptors = ['Response_time', 'Load_time', 'page_size', 'broken_link',
       'no_of_request','start_render_time','time_to_interactive', 'markup_validation',
       'compression', 'document_complete_time']

var =  ['class']+ descriptors

print(len(descriptors))

nr_rows = 6
nr_cols = 3
target = 'class'

df = data
from sklearn.preprocessing import LabelEncoder

lb_make = LabelEncoder()
df["type_code"] = lb_make.fit_transform(df["class"])
df["type_code"].value_counts()

#Predictor Variables
# filtering out google_index as it has only 1 value
X = df[['Response_time', 'Load_time', 'page_size', 'broken_link',
       'no_of_request','start_render_time','time_to_interactive', 'markup_validation',
       'compression', 'document_complete_time']]

#Target Variable
y = df['type_code']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3,shuffle=True, random_state=5)

from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Create a RandomForestClassifier instance
rf = RandomForestClassifier(n_estimators=100, max_features='sqrt')

# Fit the model on the training data
rf.fit(X_train, y_train)

# Predict on the test data
y_pred_rf = rf.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_rf, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_rf)
print("accuracy:   %0.3f" % score)

# Support Vector Machines (SVMs)

from sklearn.svm import SVC

# Create an SVC instance
svm = SVC(kernel='linear')

# Fit the model on the training data
svm.fit(X_train, y_train)

# Predict on the test data
y_pred_svm = svm.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_svm, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_svm)
print("accuracy:   %0.3f" % score)

!pip install scikit-learn

import sklearn
from sklearn.neighbors import KNeighborsClassifier

# Create a KNeighborsClassifier instance
knn = KNeighborsClassifier(n_neighbors=5)

# Fit the model on the training data
knn.fit(X_train, y_train)

# Predict on the test data
y_pred_knn = knn.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_knn, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_knn)
print("accuracy:   %0.3f" % score)

#Naive Bayes

from sklearn.naive_bayes import GaussianNB

# Create a Gaussian Naive Bayes instance
nb = GaussianNB()

# Fit the model on the training data
nb.fit(X_train, y_train)

# Predict on the test data
y_pred_nb = nb.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_nb, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_nb)
print("accuracy:   %0.3f" % score)

# Naive Bayes multinomial

from sklearn.naive_bayes import MultinomialNB

# Create a MultinomialNB instance
mnb = MultinomialNB()

# Fit the model on the training data
mnb.fit(X_train, y_train)

# Predict on the test data
y_pred_mnb = mnb.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_mnb, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_mnb)
print("accuracy:   %0.3f" % score)

# Bayesian network

from sklearn.naive_bayes import GaussianNB

# Create an instance of the GaussianNB classifier
gnb = GaussianNB()

# Fit the model on the training data
gnb.fit(X_train, y_train)

# Predict the labels of the test data
y_pred_gnb = gnb.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_gnb, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_gnb)
print("accuracy:   %0.3f" % score)

from sklearn.tree import DecisionTreeClassifier
# Create a DecisionTreeClassifier instance
decision_tree = DecisionTreeClassifier()

# Fit the model on the training data
decision_tree.fit(X_train, y_train)

# Predict on the test data
y_pred_dt = decision_tree.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_dt, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_dt)
print("accuracy:   %0.3f" % score)

# Logistic regression
from sklearn.linear_model import LogisticRegression
# Create a LogisticRegression instance
log_reg = LogisticRegression()

# Fit the model on the training data
log_reg.fit(X_train, y_train)

# Predict on the test data
y_pred_log_reg = log_reg.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_log_reg, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_log_reg)
print("accuracy:   %0.3f" % score)

# AdaBoost
from sklearn.ensemble import AdaBoostClassifier
# Create an AdaBoostClassifier instance
ada = AdaBoostClassifier()

# Fit the model on the training data
ada.fit(X_train, y_train)

# Predict on the test data
y_pred_ada = ada.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred_ada, target_names=['Excellent', 'Good', 'Unacceptable']))

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_pred_ada)
print("accuracy:   %0.3f" % score)


# time Complexity for all algorithms and run it

from IPython.display import Image
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer, normalize, RobustScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.feature_selection import mutual_info_regression, RFECV,SelectFromModel,RFE,VarianceThreshold
from functools import partial
from pathlib import Path
from joblib import load, dump
from scipy import stats
from scipy.stats import norm
from statsmodels.graphics.gofplots import qqplot
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier



# Time Complexity Analysis and Execution
# Note:  Time complexities are theoretical. Actual runtime depends on hardware and data.


# RandomForestClassifier
# Time Complexity: Training - O(n_estimators * m log m) , Prediction - O(m log n_estimators)
# Where n is the number of samples and m is the number of features.
print("Random Forest Classifier:")
# %timeit rf.fit(X_train, y_train) # Time the fitting process
# %timeit rf.predict(X_test) # Time the prediction process
print("---")

# SVC (Support Vector Classifier)
# Time complexity: Depends on the kernel. For linear kernel, it's roughly O(n*m), for others it can be higher (non-linear).
print("SVC:")
# %timeit svm.fit(X_train, y_train)
# %timeit svm.predict(X_test)
print("---")

# KNeighborsClassifier
# Time Complexity: Training - O(1), Prediction - O(n*m)
print("KNN:")
# %timeit knn.fit(X_train, y_train)
# %timeit knn.predict(X_test)
print("---")

# Gaussian Naive Bayes
# Time Complexity: Training - O(n*m), Prediction - O(m)
print("Gaussian Naive Bayes:")
# %timeit nb.fit(X_train, y_train)
# %timeit nb.predict(X_test)
print("---")

# Multinomial Naive Bayes
# Time Complexity: Training - O(n*m), Prediction - O(m)
print("Multinomial Naive Bayes:")
# %timeit mnb.fit(X_train, y_train)
# %timeit mnb.predict(X_test)
print("---")


# Decision Tree Classifier
# Time Complexity: Training - O(n*m*log n), Prediction - O(log n)
print("Decision Tree Classifier:")
# %timeit decision_tree.fit(X_train, y_train)
# %timeit decision_tree.predict(X_test)
print("---")

# Logistic Regression
# Time Complexity: Training - O(n*m^2) , Prediction - O(m)
print("Logistic Regression:")
# %timeit log_reg.fit(X_train, y_train)
# %timeit log_reg.predict(X_test)
print("---")

# AdaBoost Classifier
# Time Complexity: Training - O(n_estimators * T), where T is the training time of the base estimator
print("AdaBoost Classifier:")
# %timeit ada.fit(X_train, y_train)
# %timeit ada.predict(X_test)
print("---")

#result Time Complexity Analysis and Execution in table 

from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pd


# Time Complexity Analysis and Execution


algorithms = {
    "Random Forest Classifier": rf,
    "SVC": svm,
    "KNN": knn,
    "Gaussian Naive Bayes": nb,
    "Multinomial Naive Bayes": mnb,
    "Decision Tree Classifier": decision_tree,
    "Logistic Regression": log_reg,
    "AdaBoost Classifier": ada
}

results = []

for name, algo in algorithms.items():
    fit_time = %timeit -o algo.fit(X_train, y_train)
    predict_time = %timeit -o algo.predict(X_test)
    results.append([name, fit_time.best, predict_time.best])


df_results = pd.DataFrame(results, columns=["Algorithm", "Fit Time", "Predict Time"])
df_results

# @title Algorithm

from matplotlib import pyplot as plt
import seaborn as sns
df_results.groupby('Algorithm').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)



#statistical significance tests to support my findings.

from scipy.stats import chi2_contingency

# Create contingency table
contingency_table = pd.crosstab(y_test, y_pred_rf)

# Perform chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Print results
print("Chi-squared statistic:", chi2)
print("P-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies:", expected)

# Interpret results
if p < 0.05:
    print("The results are statistically significant, suggesting a relationship between the predicted and actual classes.")
else:
    print("The results are not statistically significant, suggesting no relationship between the predicted and actual classes.")

#chart for these results

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have the following variables defined:
# y_test: True labels of the test data
# y_pred_rf: Predicted labels from the Random Forest model
# y_pred_svm: Predicted labels from the SVM model
# y_pred_knn: Predicted labels from the KNN model
# y_pred_nb: Predicted labels from the Naive Bayes model
# y_pred_mnb: Predicted labels from the Multinomial Naive Bayes model
# y_pred_gnb: Predicted labels from the Gaussian Naive Bayes model
# y_pred_dt: Predicted labels from the Decision Tree model
# y_pred_log_reg: Predicted labels from the Logistic Regression model
# y_pred_ada: Predicted labels from the AdaBoost model

# Create a dictionary to store the accuracy scores
accuracy_scores = {
    'Random Forest': accuracy_score(y_test, y_pred_rf),
    'SVM': accuracy_score(y_test, y_pred_svm),
    'KNN': accuracy_score(y_test, y_pred_knn),
    'Naive Bayes': accuracy_score(y_test, y_pred_nb),
    'Multinomial NB': accuracy_score(y_test, y_pred_mnb),
    'Gaussian NB': accuracy_score(y_test, y_pred_gnb),
    'Decision Tree': accuracy_score(y_test, y_pred_dt),
    'Logistic Regression': accuracy_score(y_test, y_pred_log_reg),
    'AdaBoost': accuracy_score(y_test, y_pred_ada)
}

# Create a bar plot of the accuracy scores
plt.figure(figsize=(10, 6))
sns.barplot(x=list(accuracy_scores.keys()), y=list(accuracy_scores.values()))
plt.title('Accuracy Scores of Different Models')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# chart for these results with accuracy, precision, Recall, f-score

from sklearn.metrics import precision_recall_fscore_support

# Assuming you have the following variables defined:
# y_test: True labels of the test data
# y_pred_rf: Predicted labels from the Random Forest model
# y_pred_svm: Predicted labels from the SVM model
# y_pred_knn: Predicted labels from the KNN model
# y_pred_nb: Predicted labels from the Naive Bayes model
# y_pred_mnb: Predicted labels from the Multinomial Naive Bayes model
# y_pred_gnb: Predicted labels from the Gaussian Naive Bayes model
# y_pred_dt: Predicted labels from the Decision Tree model
# y_pred_log_reg: Predicted labels from the Logistic Regression model
# y_pred_ada: Predicted labels from the AdaBoost model

# Create a dictionary to store the evaluation metrics
model_metrics = {}

# Calculate and store the metrics for each model
models = [
    ('Random Forest', y_pred_rf),
    ('SVM', y_pred_svm),
    ('KNN', y_pred_knn),
    ('Naive Bayes', y_pred_nb),
    ('Multinomial NB', y_pred_mnb),
    ('Gaussian NB', y_pred_gnb),
    ('Decision Tree', y_pred_dt),
    ('Logistic Regression', y_pred_log_reg),
    ('AdaBoost', y_pred_ada)
]

for model_name, y_pred in models:
    precision, recall, fscore, support = precision_recall_fscore_support(
        y_test, y_pred, average='weighted'
    )
    accuracy = accuracy_score(y_test, y_pred)
    model_metrics[model_name] = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1-score': fscore
    }

# Convert the metrics dictionary to a DataFrame
metrics_df = pd.DataFrame.from_dict(model_metrics, orient='index')

# Transpose the DataFrame for easier plotting
metrics_df = metrics_df.T

# Create a figure and axes
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the metrics for each model
width = 0.15
x = np.arange(len(metrics_df.columns))
for i, metric in enumerate(metrics_df.index):
    ax.bar(x + i * width, metrics_df.loc[metric], width, label=metric)

# Set the x-axis labels
ax.set_xticks(x + (len(metrics_df.index) / 2 - 0.5) * width)
ax.set_xticklabels(metrics_df.columns, rotation=45, ha='right')

# Set the y-axis label
ax.set_ylabel('Score')

# Set the title
ax.set_title('Comparison of Model Performance Metrics')

# Add a legend
ax.legend()

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()

# Friedman test

from scipy.stats import friedmanchisquare

# Assuming you have the predicted labels for each model stored in variables like y_pred_rf, y_pred_svm, etc.

# Combine the predicted labels into a single array
predictions = np.array([y_pred_rf, y_pred_svm, y_pred_knn, y_pred_nb, y_pred_mnb, y_pred_gnb, y_pred_dt, y_pred_log_reg, y_pred_ada])

# Perform Friedman test
statistic, p_value = friedmanchisquare(*predictions)

# Print results
print("Friedman statistic:", statistic)
print("P-value:", p_value)

# Interpret results
if p_value < 0.05:
    print("The results are statistically significant, suggesting a difference in performance among the models.")
else:
    print("The results are not statistically significant, suggesting no difference in performance among the models.")

#  post -hoc test

from scipy.stats import friedmanchisquare, rankdata
from scikit_posthocs import posthoc_nemenyi_friedman

# Combine the predicted labels into a single array
predictions = np.array([y_pred_rf, y_pred_svm, y_pred_knn, y_pred_nb,
                       y_pred_mnb, y_pred_gnb, y_pred_dt, y_pred_log_reg, y_pred_ada])

# Perform Friedman test
statistic, p_value = friedmanchisquare(*predictions)

# Print results
print("Friedman statistic:", statistic)
print("P-value:", p_value)

# Perform post-hoc Nemenyi test if Friedman test is significant
if p_value < 0.05:
    # Rank the predictions for each model
    ranked_predictions = rankdata(predictions, axis=1)

    # Perform Nemenyi post-hoc test
    posthoc_result = posthoc_nemenyi_friedman(ranked_predictions)

    # Print post-hoc results
    print("\nNemenyi Post-Hoc Test:")
    print(posthoc_result)

from scipy.stats import friedmanchisquare, rankdata
from scikit_posthocs import posthoc_nemenyi_friedman

# ... (Your existing code)

# Perform Friedman test
statistic, p_value = friedmanchisquare(*predictions)

# Print results
print("Friedman statistic:", statistic)
print("P-value:", p_value)

# Perform post-hoc Nemenyi test if Friedman test is significant
if p_value < 0.05:
    # Calculate mean ranks for each model
    mean_ranks = np.mean(rankdata(predictions, axis=1), axis=1)

    # Perform Nemenyi post-hoc test
    posthoc_result = posthoc_nemenyi_friedman(mean_ranks.reshape(1,-1)) # Reshape to a 2D array

    # Print post-hoc results with model names
    model_names = ['Random Forest', 'SVM', 'KNN', 'Naive Bayes',
                   'Multinomial NB', 'Gaussian NB', 'Decision Tree',
                   'Logistic Regression', 'AdaBoost']

    print("\nNemenyi Post-Hoc Test:")
    posthoc_result.columns = model_names
    posthoc_result.index = model_names
    print(posthoc_result)

# (Post-Hoc Test)

from scipy.stats import wilcoxon

# Perform Wilcoxon signed-rank test for each pair of models
model_names = ['Random Forest', 'SVM', 'KNN', 'Naive Bayes', 'Multinomial NB', 'Gaussian NB', 'Decision Tree', 'Logistic Regression', 'AdaBoost']
for i in range(len(model_names)):
  for j in range(i + 1, len(model_names)):
    model1_predictions = predictions[i]
    model2_predictions = predictions[j]

    # Check if predictions are identical before performing Wilcoxon test
    if not (model1_predictions == model2_predictions).all():  # Check if all predictions are the same
        statistic, p_value = wilcoxon(model1_predictions, model2_predictions)
        print(f"Wilcoxon test for {model_names[i]} vs {model_names[j]}: statistic={statistic}, p-value={p_value}")

        # Interpret results
        if p_value < 0.05:
            print(f"  Significant difference in performance between {model_names[i]} and {model_names[j]}")
        else:
            print(f"  No significant difference in performance between {model_names[i]} and {model_names[j]}")
    else:
        print(f"Wilcoxon test for {model_names[i]} vs {model_names[j]}: Predictions are identical, cannot perform test.")





# Summarize the accuracy scores
print("Accuracy Scores:")
for model, score in accuracy_scores.items():
    print(f"{model}: {score:.3f}")

# Interpret the Friedman test results
print("\nFriedman Test:")
if p_value < 0.05:
    print("There is a significant difference in performance among the models.")
else:
    print("There is no significant difference in performance among the models.")

# Interpret the Wilcoxon signed-rank test results
print("\nWilcoxon Signed-Rank Tests:")
for i in range(len(model_names)):
    for j in range(i + 1, len(model_names)):
        model1_predictions = predictions[i]
        model2_predictions = predictions[j]
        if not (model1_predictions == model2_predictions).all():
            statistic, p_value = wilcoxon(model1_predictions, model2_predictions)
            if p_value < 0.05:
                print(f"There is a significant difference between {model_names[i]} and {model_names[j]}.")
            else:
                print(f"There is no significant difference between {model_names[i]} and {model_names[j]}.")
        else:
            print(f"Predictions for {model_names[i]} and {model_names[j]} are identical.")

# Identify the best-performing model(s) based on accuracy and statistical tests
best_models = [model for model, score in accuracy_scores.items() if score == max(accuracy_scores.values())]
print("\nBest Performing Model(s):", ", ".join(best_models))



# results in table

from tabulate import tabulate



# Create a list of lists for the table data
table_data = [['Model', 'Accuracy Score']]
for model, score in accuracy_scores.items():
    table_data.append([model, f"{score:.3f}"])

# Add a separator row
table_data.append(['---', '---'])

# Add Friedman test results
table_data.append(['Friedman Test', f"Statistic: {statistic:.3f}, P-value: {p_value:.3f}"])

# Add Wilcoxon test results
table_data.append(['Wilcoxon Tests', ''])
for i in range(len(model_names)):
    for j in range(i + 1, len(model_names)):
        model1_predictions = predictions[i]
        model2_predictions = predictions[j]
        if not (model1_predictions == model2_predictions).all():
            statistic, p_value = wilcoxon(model1_predictions, model2_predictions)
            table_data.append([f"{model_names[i]} vs {model_names[j]}", f"Statistic: {statistic:.3f}, P-value: {p_value:.3f}"])
        else:
            table_data.append([f"{model_names[i]} vs {model_names[j]}", "Predictions are identical"])

# Print the table
print(tabulate(table_data, headers='firstrow', tablefmt='grid'))

# Identify the best-performing model(s) based on accuracy and statistical tests
best_models = [model for model, score in accuracy_scores.items() if score == max(accuracy_scores.values())]
print("\nBest Performing Model(s):", ", ".join(best_models))



import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np



# Create a DataFrame from the accuracy scores
accuracy_scores = {'Random Forest': 0.85, 'SVM': 0.92, 'KNN': 0.88, 'Naive Bayes': 0.79,
                   'Multinomial NB': 0.82, 'Gaussian NB': 0.80, 'Decision Tree': 0.75,
                   'Logistic Regression': 0.87, 'AdaBoost': 0.90}  # Example scores
metrics_df = pd.DataFrame.from_dict(accuracy_scores, orient='index', columns=['Accuracy'])

# Create a heatmap of the metrics_df
plt.figure(figsize=(10, 6))
sns.heatmap(metrics_df, annot=True, fmt=".3f", cmap="YlGnBu")
plt.title('Heatmap of Model Performance Metrics')
plt.xlabel('Model')
plt.ylabel('Metric')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()




import matplotlib.pyplot as plt
import pandas as pd


data = {
    'Comparison': ['Random Forest vs SVM', 'Random Forest vs KNN', 'Random Forest vs Naive Bayes',
                   'Random Forest vs Multinomial NB', 'Random Forest vs Gaussian NB',
                   'Random Forest vs Decision Tree', 'Random Forest vs Logistic Regression',
                   'Random Forest vs AdaBoost', 'SVM vs KNN', 'SVM vs Naive Bayes',
                   'SVM vs Multinomial NB', 'SVM vs Gaussian NB', 'SVM vs Decision Tree',
                   'SVM vs Logistic Regression', 'SVM vs AdaBoost', 'KNN vs Naive Bayes',
                   'KNN vs Multinomial NB', 'KNN vs Gaussian NB'],
    'P-value': [0.639, 0.06, 0.013, 0.453, 0.013, 0.986, 0.793, 0.17, 0.087, 0.014,
                0.296, 0.014, 0.773, 0.879, 0.366, 0.819, 0.026, 0.819]
}
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(12, 6))
plt.bar(df['Comparison'], df['P-value'])
plt.xlabel('Comparison')
plt.ylabel('P-value')
plt.title('P-values for Model Comparisons')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



from IPython.display import Image
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer, normalize, RobustScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.feature_selection import mutual_info_regression, RFECV,SelectFromModel,RFE,VarianceThreshold
from functools import partial
from pathlib import Path
from joblib import load, dump
from scipy import stats
from scipy.stats import norm
from statsmodels.graphics.gofplots import qqplot
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from scipy.stats import friedmanchisquare, rankdata, wilcoxon
from scikit_posthocs import posthoc_nemenyi_friedman
from sklearn.metrics import precision_recall_fscore_support
from statsmodels.stats.contingency_tables import chi2_contingency
from tabulate import tabulate






# Additional comparisons data
additional_comparisons = {
    'Comparison': ['KNN vs Decision Tree', 'KNN vs Logistic Regression', 'KNN vs AdaBoost',
                   'Naive Bayes vs Multinomial NB', 'Naive Bayes vs Decision Tree',
                   'Naive Bayes vs Logistic Regression', 'Naive Bayes vs AdaBoost',
                   'Multinomial NB vs Gaussian NB', 'Multinomial NB vs Decision Tree',
                   'Multinomial NB vs Logistic Regression', 'Multinomial NB vs AdaBoost',
                   'Gaussian NB vs Decision Tree', 'Gaussian NB vs Logistic Regression',
                   'Gaussian NB vs AdaBoost', 'Decision Tree vs Logistic Regression',
                   'Decision Tree vs AdaBoost', 'Logistic Regression vs AdaBoost'],
    'P-value': [0.117, 0.123, 0.335, 0.026, 0.049, 0.027, 0.166, 0.026, 0.44,
                0.368, 0.156, 0.049, 0.027, 0.166, 0.859, 0.268, 0.34]
}
additional_comparisons_df = pd.DataFrame(additional_comparisons)

#Combine the predicted labels into a single array (assuming you have all your y_preds)
predictions = np.array([y_pred_rf, y_pred_svm, y_pred_knn, y_pred_nb, y_pred_mnb, y_pred_gnb, y_pred_dt, y_pred_log_reg, y_pred_ada])
model_names = ['Random Forest', 'SVM', 'KNN', 'Naive Bayes', 'Multinomial NB', 'Gaussian NB', 'Decision Tree', 'Logistic Regression', 'AdaBoost']
