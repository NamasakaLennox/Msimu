#!/usr/bin/env python3
# coding: utf-8

# In[9]:


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
train_size=int(len(kitale)*0.67)
kitale_train=kitale[:train_size]
kitale_test=kitale[train_size:]

median_train_prcp=kitale_train.PRCP.median()
kitale_train.PRCP.fillna(median_train_prcp, inplace=True)

median_train_tavg=kitale_train.TAVG.median()
kitale_train.TAVG.fillna(median_train_tavg, inplace=True)

median_train_tmax=kitale_train.TMAX.median()
kitale_train.TMAX.fillna(median_train_tmax, inplace=True)

median_train_tmin=kitale_train.TMIN.median()
kitale_train.TMIN.fillna(median_train_tmin,inplace=True)

median_test_prcp=kitale_test.PRCP.median()
kitale_test.PRCP.fillna(median_test_prcp,inplace=True)

median_test_tavg=kitale_test.TAVG.median()
kitale_test.TAVG.fillna(median_test_tavg,inplace=True)

median_test_tmax=kitale_test.TMAX.median()
kitale_test.TMAX.fillna(median_test_tmax,inplace=True)

median_test_tmin=kitale_test.TMIN.median()
kitale_test.TMIN.fillna(median_test_tmin,inplace=True)

kitale_actual=pd.concat([kitale_train,kitale_test])


# In[42]:


#Scaling the data
scaler=MinMaxScaler()
data=kitale_actual[['PRCP']]
scaled_kitale_prcp=scaler.fit_transform(data)


# Preparing the data for the LSTM model by creating a data structure with a look back period of 14 months to get the next 30 future values

# In[52]:


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

X, y = create_sequences(scaled_kitale_prcp, lookback_period, forecast_period)


# In[53]:


#Train-validation-test split of the data and data preparation for the LSTM model

# Train-Validation-Test split
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, shuffle=False)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, shuffle=False)

# Reshape data for LSTM input
X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_val = np.reshape(X_val, (X_val.shape[0], 1, X_val.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1] ))


# In[54]:


#Building and training the LSTM model
model=Sequential()
model.add(LSTM(50,activation='relu',input_shape=(1,X_train.shape[2]),return_sequences=True))
model.add(LSTM(50,activation='relu'))
model.add(Dense(units=forecast_period, activation='relu'))


model.compile(loss='mean_squared_error',optimizer='adam')
model.fit(X_train,y_train,epochs=100,batch_size=50,validation_data=(X_val,y_val),verbose=2, shuffle=False)


# In[55]:


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


# In[58]:


# Plot actual vs predicted values with date indexes

#plt.figure(figsize=(12, 6))
#plt.plot(kitale_actual.index[-len(y_test):], y_test[:, 0], label='Actual')
#plt.plot(kitale_actual.index[-len(predictions):], predictions[:, 0], label='Predicted')
#plt.title('Actual vs Predicted Precipitation(Kitale)')
#plt.xlabel('Date')
#plt.ylabel('PRCP')
#plt.legend()
#plt.show()


# In[57]:


# Use the trained model to predict future precipitation values
last_lookback_data = scaled_kitale_prcp[-lookback_period:]
future_timesteps=30

# Reshape the data for LSTM input
X_future=np.array([last_lookback_data])
X_future = np.reshape(X_future, (X_future.shape[0], 1, X_future.shape[1]))

# Use the trained model to predict future precipitation values
future_predictions = model.predict(X_future)

# Inverse transform the predicted values
future_predictions = scaler.inverse_transform(future_predictions)

# Create future date index
future_date_index = pd.date_range(start='2023-11-26', periods=future_timesteps, freq='D')

# Plot actual values and predicted values for future dates
plt.figure(figsize=(12, 6))
plt.plot(future_date_index, future_predictions[0,:], label='Predicted (Precipitation)', marker='o')
plt.title('Predicted Precipitation in Kitale for the next 30 days')
plt.xlabel('Date')
plt.ylabel('Precipitation(mm)')
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()


# In[29]:


# Use the trained model to predict future precipitation values
last_lookback_data = scaled_kitale_prcp[-lookback_period:]
future_timesteps=30

# Reshape the data for LSTM input
X_future=np.array([last_lookback_data])
X_future = np.reshape(X_future, (X_future.shape[0], X_future.shape[1], 1))

# Use the trained model to predict future precipitation values
future_predictions = model.predict(X_future)

# Inverse transform the predicted values
future_predictions = scaler.inverse_transform(future_predictions)
future_predictions.shape


# In[22]:


k=[1,2,3,4]
j=[k]
j


# In[ ]:




