#!/usr/bin/python3
"""
handles prediction routes
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.metrics import mean_squared_error
from keras.metrics import mean_absolute_error
from keras.metrics import RootMeanSquaredError
import requests
from io import StringIO
from math import sqrt

# In[2]:


#Reading the data 
url="https://raw.githubusercontent.com/NamasakaLennox/Msimu/main/ml_model/GHCN_Kenya.csv"
response = requests.get(url)
ghcn_file = StringIO(response.text)
climate_data=pd.read_csv(ghcn_file)

#Reading data observed from kitale and eldoret
kitale_eldoret=climate_data[(climate_data.NAME=='KITALE, KE')| (climate_data.NAME=='ELDORET INTERNATIONAL, KE')]
kitale_eldoret.reindex()


# In[3]:


#Formatting the date feature to a datetime datatype and setting it as the new index
kitale_eldoret['DATE']=pd.to_datetime(kitale_eldoret['DATE'])
kitale_eldoret.set_index('DATE',inplace=True)

#Splitting the data to have distinct forecasts for kitale and eldoret
kitale=kitale_eldoret[kitale_eldoret.NAME=='KITALE, KE']
eldoret=kitale_eldoret[kitale_eldoret.NAME=='ELDORET INTERNATIONAL, KE']
#After this split, the features only describing the specific location become redundant thus they should be dropped
kitale=kitale.drop(['STATION','NAME'],axis=1)
eldoret=eldoret.drop(['STATION','NAME'],axis=1)


# In[4]:


#Imputation of null values
train_size=int(len(eldoret)*0.67)
eldoret_train=eldoret[:train_size]
eldoret_test=eldoret[train_size:]

median_train_prcp=eldoret_train.PRCP.median()
eldoret_train.PRCP.fillna(median_train_prcp, inplace=True)

median_train_tavg=eldoret_train.TAVG.median()
eldoret_train.TAVG.fillna(median_train_tavg, inplace=True)

median_train_tmax=eldoret_train.TMAX.median()
eldoret_train.TMAX.fillna(median_train_tmax, inplace=True)

median_train_tmin=eldoret_train.TMIN.median()
eldoret_train.TMIN.fillna(median_train_tmin,inplace=True)

median_test_prcp=eldoret_test.PRCP.median()
eldoret_test.PRCP.fillna(median_test_prcp,inplace=True)

median_test_tavg=eldoret_test.TAVG.median()
eldoret_test.TAVG.fillna(median_test_tavg,inplace=True)

median_test_tmax=eldoret_test.TMAX.median()
eldoret_test.TMAX.fillna(median_test_tmax,inplace=True)

median_test_tmin=eldoret_test.TMIN.median()
eldoret_test.TMIN.fillna(median_test_tmin,inplace=True)

eldoret_actual=pd.concat([eldoret_train,eldoret_test])


# In[5]:


#Scaling the data
scaler=MinMaxScaler()
data=eldoret_actual[['PRCP']]
scaled_eldoret_prcp=scaler.fit_transform(data)


# Preparing the data for the LSTM model by creating a data structure with a look back period of 14 months to get the next 30 future values

# In[6]:


# Function to create sequences for LSTM
def create_sequences(data, lookback, forecast):
    X, y = [], []
    for i in range(len(data) - lookback - forecast + 1):
        X.append(data[i:(i + lookback), 0])
        y.append(data[(i + lookback):(i + lookback + forecast), 0])
    return np.array(X), np.array(y)

# Define lookback and forecast periods
lookback_period = 60
forecast_period = 30

X, y = create_sequences(scaled_eldoret_prcp, lookback_period, forecast_period)


# In[7]:


#Train-validation-test split of the data and data preparation for the LSTM model

# Train-Validation-Test split
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, shuffle=False)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, shuffle=False)

# Reshape data for LSTM input
X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_val = np.reshape(X_val, (X_val.shape[0], 1, X_val.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1] ))


# In[8]:


def build():
    #Building and training the LSTM model
    model=Sequential()
    model.add(LSTM(50,activation='relu',input_shape=(1,X_train.shape[2]),return_sequences=True))
    model.add(LSTM(50,activation='relu'))
    model.add(Dense(units=forecast_period, activation='relu'))


    model.compile(loss='mean_squared_error',optimizer='adam')
    model.fit(X_train,y_train,epochs=100,batch_size=50,validation_data=(X_val,y_val),verbose=2, shuffle=False)


    # In[9]:


    # Predictions and accuracy evaluation
    predictions = model.predict(X_test)

    # Inverse transform the predictions
    predictions = scaler.inverse_transform(predictions)
    y_test=scaler.inverse_transform(y_test)
    mse = np.mean(mean_squared_error(y_test, predictions))
    mae=np.mean(mean_absolute_error(y_test,predictions))
    #print(f'Mean Squared Error: {mse}')
    #print(f'RMSE: {sqrt(mse)}')
    #print(f'Mean Absolute Error: {mae}')


    # In[10]:



    # Use the trained model to predict future precipitation values
    last_lookback_data = scaled_eldoret_prcp[-lookback_period:]
    future_timesteps=30

    # Reshape the data for LSTM input
    X_future=np.array([last_lookback_data])
    X_future = np.reshape(X_future, (X_future.shape[0], 1, X_future.shape[1]))

    # Use the trained model to predict future precipitation values
    future_predictions = model.predict(X_future)

    return future_predictions

# Create future date index
future_date_index = pd.date_range(start='2023-11-26', periods=30, freq='D')

@app_views.route('/model_eldoret/', strict_slashes=False)
def model_eldoret():
    """
    returns data for prediction
    """
    out = {}
    future_predictions = build()
    future_predictions = scaler.inverse_transform(future_predictions)
    try:
        expected = pd.DataFrame(data={'Date': future_date_index, 'Predicted precipitation(mm)': future_predictions[0,:]})

        for i in range(len(expected)):
            out.update({expected.iloc[i,0]: expected.iloc[i, 1]})

    except Exception:
        return (jsonify([]))

    if out == {}:
        return (jsonify([]))

    return (jsonify(out))
