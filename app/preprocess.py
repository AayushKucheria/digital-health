# import pickle
# import numpy as np
# import pandas as pd
# from lightgbm import LGBMClassifier
# from sklearn.preprocessing import OneHotEncoder
#
# # Load data and save indices of columns
# df = pd.read_csv("../notebooks/data.csv")
# features = df.drop('left', 1).columns
# pickle.dump(features, open('data/features.pickle', 'wb'))
#
# # Fit and save an OneHotEncoder
# columns_to_fit = ['sales', 'salary']
# enc = OneHotEncoder(sparse=False).fit(df.loc[:, columns_to_fit])
# pickle.dump(enc, open('data/encoder.pickle', 'wb'))
#
# # Transform variables, merge with existing df and keep column names
# column_names = enc.get_feature_names(columns_to_fit)
# encoded_variables = pd.DataFrame(enc.transform(df.loc[:, columns_to_fit]), columns=column_names)
# df = df.drop(columns_to_fit, 1)
# df = pd.concat([df, encoded_variables], axis=1)
#
# # Fit and save model
# X, y = df.drop('left', 1), df.loc[:, 'left']
# clf = LGBMClassifier().fit(X, y)
# pickle.dump(clf, open('data/model.pickle', 'wb'))