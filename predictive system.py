# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open("C:/Users/admin/Desktop/MachineLearning/trained_model.sav",'rb'))


input_data = (0,137,40,35,168,43.1,2.288,33)

#changing the input_data to numpy array
input_array=np.asarray(input_data)
print(input_array)

# reshape the array as we are predecting for one instance 
input_resshaped = input_array.reshape(1,-1)
print(input_resshaped)

y_prediction = loaded_model.predict(input_resshaped)
print(y_prediction)

if (y_prediction[0]==0):
    print('the person is not diabetic')
else:
    print('the person is  diabetic')