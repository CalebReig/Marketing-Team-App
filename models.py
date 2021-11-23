import pickle
import os
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def load_model():
    """
    This function loads the model used to predict customer response.
    Returns model
    """
    folder = 'items'
    filename = 'model.sav'
    path = os.path.join(folder, filename)
    model = pickle.load(open(path, 'rb'))
    return model


def load_data():
    """
    This function loads customer data
    Returns df
    """
    folder = 'items'
    filename = 'mc_fe.csv'
    path = os.path.join(folder, filename)
    df = pd.read_csv(path, index_col='ID')
    return df


def load_3d():
    """
    This function loads customer cluster data
    Returns df
    """
    folder = 'items'
    filename = '3d_cus.csv'
    path = os.path.join(folder, filename)
    df = pd.read_csv(path)
    return df


def load_pipeline():
    """
    This function loads the data preprocessing pipeline for the customer response model
    Returns pipeline
    """
    #loads the data and model for the pipeline
    df = load_data()
    model = load_model()

    #data to fit the ct
    X, y = df.drop('Response', axis=1).values, df['Response'].values

    # Creates a column transformer that sends 'Education' to be encoded and rest scaled
    ct = ColumnTransformer([
        ('catagoric', OneHotEncoder(), [0]),
        ('numeric', StandardScaler(), list(range(1, len(X.T))))
    ])

    #Creates a pipeline to transform data and predict value
    pipeline = Pipeline([
        ('column_trans', ct),
        ('model', model)
    ])
    pipeline.fit(X, y)
    return pipeline




