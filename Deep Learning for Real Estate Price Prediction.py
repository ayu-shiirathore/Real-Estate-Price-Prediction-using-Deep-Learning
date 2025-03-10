#!/usr/bin/env python
# coding: utf-8

# # TASK #1: UNDERSTAND THE PROBLEM STATEMENT AND BUSINESS CASE

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# 

# # TASK #2: IMPORT LIBRARIES AND DATASETS

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False) 
# setting the style of the notebook to be monokai theme  
# this line of code is important to ensure that we are able to see the x and y axes clearly
# If you don't run this code line, you will notice that the xlabel and ylabel on any plot is black on black and it will be hard to see them. 


# In[2]:


house_df = pd.read_csv('realestate_prices.csv', encoding = 'ISO-8859-1')


# In[3]:


house_df


# In[4]:





# In[5]:





# In[6]:





# **PRACTICE OPPORTUNITY #1 [OPTIONAL]:**
# - **What is the average house price?**
# - **What is the price of the cheapest house?**
# - **What is the average number of bathrooms and bedrooms? round your answer to the lowest value**
# - **What is the maximum number of bedrooms?**

# In[ ]:





# # TASK #3: PERFORM DATA VISUALIZATION

# In[7]:





# In[8]:





# In[9]:


f, ax = plt.subplots(figsize = (20, 20))
sns.heatmap(house_df.corr(), annot = True)


# In[10]:


house_df_sample = house_df[ ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement', 'yr_built']   ]


# In[11]:


house_df_sample


# **PRACTICE OPPORTUNITY #2 [OPTIONAL]:**
# - **Using Seaborn, plot the pairplot for the features contained in "house_df_sample"**
# - **Explore the data and perform sanity check**

# In[ ]:





# # TASK #4: PERFORM DATA CLEANING AND FEATURE ENGINEERING

# In[4]:


selected_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'sqft_above', 'sqft_basement']


# In[5]:


X = house_df[selected_features]


# In[6]:


X


# In[15]:


y = house_df['price']


# In[16]:


y


# In[17]:


X.shape


# In[18]:


y.shape


# In[7]:


from sklearn.preprocessing import MinMaxScaler


# In[20]:


X_scaled


# In[21]:


X_scaled.shape


# In[22]:


scaler.data_max_


# In[23]:


scaler.data_min_


# In[24]:


y = y.values.reshape(-1,1)


# In[25]:


y_scaled = scaler.fit_transform(y)


# In[26]:


y_scaled


# # TASK #5: TRAIN A DEEP LEARNING MODEL WITH LIMITED NUMBER OF FEATURES

# In[8]:


from sklearn.model_selection import train_test_split


# In[28]:


X_train.shape


# In[29]:


X_test.shape


# In[9]:


import tensorflow.keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense

model = Sequential()


# In[31]:


model.summary()


# In[32]:


model.compile(optimizer = 'Adam', loss = 'mean_squared_error')


# In[33]:


epochs_hist = model.fit(X_train, y_train, epochs = 100, batch_size = 50, validation_split = 0.2)


# **PRACTICE OPPORTUNITY #3 [OPTIONAL]:**
# - **Change the architecture of the network by adding an additional dense layer with 200 neurons. Use "Relu" as an activation function**
# - **How many trainable parameters does the new network has?**

# In[ ]:





# # TASK #6: EVALUATE TRAINED DEEP LEARNING MODEL PERFORMANCE 

# In[34]:


epochs_hist.history.keys()


# In[35]:


plt.plot(epochs_hist.history['loss'])
plt.plot(epochs_hist.history['val_loss'])
plt.title('Model Loss Progress During Training')
plt.xlabel('Epoch')
plt.ylabel('Training and Validation Loss')
plt.legend(['Training Loss', 'Validation Loss'])


# In[36]:


# 'bedrooms','bathrooms','sqft_living','sqft_lot','floors', 'sqft_above', 'sqft_basement'
X_test_1 = np.array([[ 4, 3, 1960, 5000, 1, 2000, 3000 ]])

scaler_1 = MinMaxScaler()
X_test_scaled_1 = scaler_1.fit_transform(X_test_1)

y_predict_1 = model.predict(X_test_scaled_1)

y_predict_1 = scaler.inverse_transform(y_predict_1)
y_predict_1


# In[37]:


y_predict = model.predict(X_test)
plt.plot(y_test, y_predict, "^", color = 'r')
plt.xlabel('Model Predictions')
plt.ylabel('True Values')


# In[38]:


y_predict_orig = scaler.inverse_transform(y_predict)
y_test_orig = scaler.inverse_transform(y_test)


# In[39]:


plt.plot(y_test_orig, y_predict_orig, "^", color = 'r')
plt.xlabel('Model Predictions')
plt.ylabel('True Values')
plt.xlim(0, 5000000)
plt.ylim(0, 3000000)


# In[40]:


k = X_test.shape[1]
n = len(X_test)
n


# In[41]:


k


# In[10]:


from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from math import sqrt

RMSE = float(format(np.sqrt(mean_squared_error(y_test_orig, y_predict_orig)),'.3f'))
MSE = mean_squared_error(y_test_orig, y_predict_orig)
MAE = mean_absolute_error(y_test_orig, y_predict_orig)
r2 = r2_score(y_test_orig, y_predict_orig)
adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)

print('RMSE =',RMSE, '\nMSE =',MSE, '\nMAE =',MAE, '\nR2 =', r2, '\nAdjusted R2 =', adj_r2) 


# # TASK #7. TRAIN AND EVALUATE A DEEP LEARNING MODEL WITH INCREASED NUMBER OF FEATURES (INDEPENDANT VARIABLES)

# In[68]:


selected_features = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors', 'sqft_above', 'sqft_basement', 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'yr_built', 
'yr_renovated', 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15']

X = house_df[selected_features]


# In[69]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


# In[70]:


y = house_df['price']


# In[71]:


y = y.values.reshape(-1,1)
y_scaled = scaler.fit_transform(y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size = 0.25)


# In[72]:


import tensorflow.keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(10, input_dim = 19, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(1, activation = 'linear'))


# In[73]:


model.compile(optimizer = 'adam', loss = 'mean_squared_error')


# In[74]:


epochs_hist = model.fit(X_train, y_train, epochs = 100, batch_size = 50, verbose = 1, validation_split = 0.2)


# In[75]:


plt.plot(epochs_hist.history['loss'])
plt.plot(epochs_hist.history['val_loss'])
plt.title('Model Loss Progress During Training')
plt.ylabel('Training and Validation Loss')
plt.xlabel('Epoch number')
plt.legend(['Training Loss', 'Validation Loss'])


# In[79]:


y_predict = model.predict(X_test)
plt.plot(y_test, y_predict, "^", color = 'r')
plt.xlabel("Model Predictions")
plt.ylabel("True Value (ground Truth)")
plt.title('Linear Regression Predictions')
plt.show()


# In[80]:


y_predict_orig = scaler.inverse_transform(y_predict)
y_test_orig = scaler.inverse_transform(y_test)


# In[81]:


from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from math import sqrt

RMSE = float(format(np.sqrt(mean_squared_error(y_test_orig, y_predict_orig)),'.3f'))
MSE = mean_squared_error(y_test_orig, y_predict_orig)
MAE = mean_absolute_error(y_test_orig, y_predict_orig)
r2 = r2_score(y_test_orig, y_predict_orig)
adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)

print('RMSE =',RMSE, '\nMSE =',MSE, '\nMAE =',MAE, '\nR2 =', r2, '\nAdjusted R2 =', adj_r2) 


# **PRACTICE OPPORTUNITY #4 [OPTIONAL]:**
# - **Change the architecture of the network to increase the coefficient of determination to at least 0.86.**  

# In[ ]:





# # GREAT JOB!

# # PRACTICE OPPORTUNITIES SOLUTIONS

# **PRACTICE OPPORTUNITY #1 SOLUTION:**
# - **What is the average house price?**
# - **What is the price of the cheapest house?**
# - **What is the average number of bathrooms and bedrooms? round your answer to the lowest value**
# - **What is the maximum number of bedrooms?**

# In[54]:


house_df.describe()


# **PRACTICE OPPORTUNITY #2 SOLUTION:**
# - **Using Seaborn, plot the pairplot for the features contained in "house_df_sample"**
# - **Explore the data and perform sanity check**

# In[55]:


sns.pairplot(house_df_sample)


# **PRACTICE OPPORTUNITY #3 SOLUTION:**
# - **Change the architecture of the network by adding an additional dense layer with 200 neurons. Use "Relu" as an activation function**
# - **How many trainable parameters does the new network has**

# In[56]:


import tensorflow.keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(100, input_dim = 7, activation = 'relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(1, activation = 'linear'))

model.summary()


# **PRACTICE OPPORTUNITY #4 SOLUTION:**
# - **Change the architecture of the network to increase the coefficient of determination to at least 0.86.**  

# In[57]:


import tensorflow.keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(10, input_dim = 19, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(200, activation = 'relu'))
model.add(Dense(200, activation = 'relu'))

model.add(Dense(1, activation = 'linear'))


# In[ ]:




