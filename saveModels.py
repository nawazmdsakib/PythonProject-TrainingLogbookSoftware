# -*- coding: utf-8 -*-
'''
Created on Wed Mar 22 00:59:29 2023

@author: Md Sakib Nawaz
'''

# Class code.

# os, sys and pandas libraries are imported. 
import sys
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
    def __init__(self, trained_models):
        self.trained_models = trained_models
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
            model.save(f'saved_models/model_{i + 1}.h5')
            
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
        
        # Prompt the user for a file name to save the .csv file.
        while True:
            csv_filename = input("\nPlease enter a file name to save the model details (without extension)\nor 'b' to go back to main menu or 'e' to exit'\n\nPlease enter: ")

            if csv_filename.lower() == 'b':
                return False

            elif csv_filename.lower() == 'e':
                print("\n\nExiting the software . . .\n\n***Thank you***")
                sys.exit()

            csv_filename = f"{csv_filename}.csv"

            # Check if the file already exists and handle user input.
            if os.path.exists(csv_filename):
                print(f"\nThe file named '{csv_filename}' already exists.")
                overwrite = input("\nDo you want to overwrite the file? Enter (yes/no)\nPlease enter 'b' to go back to main menu 'e' to exit\n\nPlease enter: ").lower()
                if overwrite == 'yes':
                    pass
                elif overwrite == 'b':
                    return False

                elif overwrite == 'e':
                    print("\n\nExiting the software . . .\n\n***Thank you***")
                    sys.exit()

                elif overwrite == 'no':
                    continue

                else:
                    
                    print("\n\nYou didn't enter any of these ('yes' or 'no' or 'b' or 'e')\n\nGoing back to the name input . . .\n")
                    continue

            else:
                pass

            # Save the DataFrame as a .csv file.
            try:
                df.to_csv(csv_filename, index=False)
                file_location = os.path.abspath(csv_filename)
                print("\n\nAll model details have been saved successfully")
                print(f"\nFile name: {csv_filename}")
                print(f"File location: {file_location}")
                break
            except OSError as e:
                print(f"\n\nAn error occured: {e}\n\nPlease try again!\n\n")
        