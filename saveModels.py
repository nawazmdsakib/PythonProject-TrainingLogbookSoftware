# -*- coding: utf-8 -*-
'''
Created on Wed Mar 22 00:59:29 2023

@author: Md Sakib Nawaz
'''

# Class code.

# os, and pandas libraries are imported. 
import os
import pandas as pd

# Keras module from the TensorFlow library is imported. 
from tensorflow import keras

'''
A class definition with 2 functions where first one is init
function and second one will save all trained model details 
in csv format.
'''
class SaveModelsClass:
    
    # Define the class constructor.
    def __init__(self, trained_models, csv_filename):
        self.trained_models = trained_models
        self.csv_filename = csv_filename
        self.error_occurred = False
        self.save_models_to_csv()
   
    '''
    A function to save the trained models as .h5 files and 
    the model details as a .csv fil
    '''
    def save_models_to_csv(self):
        
        # Create a 'saved_models' directory if it doesn't exist.
        if not os.path.exists('saved_models'):
            os.makedirs('saved_models')

        model_data = []
        
        # Iterate through the trained models and save them as .h5 files.
        for i, (model, history) in enumerate(self.trained_models):
            
            # Get the current csv_filename and Remove the '.csv' extension.
            csv_filename_without_ext = self.csv_filename.split(".csv")[0]

            # Save the model using the csv_filename as a prefix.
            model_file_name = f'saved_models/{csv_filename_without_ext}_model_{i + 1}.h5'
            model.save(model_file_name)
  
            # Extract and store model information for the .csv file.
            model_name = f"model_{i + 1}"
            architecture = ", ".join([f"{layer.__class__.__name__}_{layer.units}" if isinstance(layer, keras.layers.Dense) else f"{layer.__class__.__name__}" for layer in model.layers[1:-1]])
            epochs = len(history.epoch)
            train_accuracy = history.history['accuracy'][-1]
            val_accuracy = history.history['val_accuracy'][-1]
            train_loss = history.history['loss'][-1]
            val_loss = history.history['val_loss'][-1]

            model_data.append([model_name, architecture, epochs, train_accuracy, val_accuracy, train_loss, val_loss])
        
        # Create a DataFrame to store the model data.
        df = pd.DataFrame(model_data, columns=["Model Name", "Architecture", "Number of Epochs", "Training Accuracy", "Validation Accuracy", "Training Loss", "Validation Loss"])

        # Save the DataFrame as a .csv file.
        try:
            model_name = f"{csv_filename_without_ext}model_{i + 1}"
            
            # Add '.csv' extension back.
            df.to_csv(f"{csv_filename_without_ext}.csv", index=False)  
            csv_file_location = os.path.abspath(f"{csv_filename_without_ext}.csv")
            
            # Print the model name and location.
            print("\n\nAll model details have been saved successfully")
            print(f"\nCSV file name: {csv_filename_without_ext}.csv")
            print(f"CSV file location: {csv_file_location}")
            print(f"\nModels file location: {os.path.abspath(model_file_name)}")
            self.error_occurred = False
        
        # If any OSerror occurs then it send 'True' value for error_occurred variable to the main code.
        except OSError as e:
            print(f"\n\nAn error occurred: {e}\n\nPlease try again!\n")
            self.error_occurred = True