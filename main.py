# -*- coding: utf-8 -*-
'''
Created on Tue Mar 21 20:43:06 2023

@author: Md Sakib Nawaz
'''

# Main code.

# sys library is imported.
import sys

# Classes are imported from the classes code files.
from getDataset import GetDatasetClass
from getArchitecture import GetArchitectureClass
from buildTrain import BuildTrainModelsClass
from saveModels import SaveModelsClass

# Print a welcome message and brief introduction.
print("\n      Welcome to the Training Logbook Software\n\nThis software can train deep learning models for image\nclassification using the popular MNIST dataset. You can\nchoose the number of models you want to train including\ncustomization of different types of architecture.\n\nWhich function would you like to perform?\n")

# Initialize data variables.
train_images, train_labels = None, None
eval_images, eval_labels = None, None
class_names = None

# Main menu loop for the program.
while True:

    # Prompt user to choose an option from main menu.
    choice = input(" 1. Load Dataset\n 2. Start Training\n 3. Remove Loaded Data\n 4. Exit\n\nPlease choose a function between 1 to 4: ")
    
    # Option 1: Load dataset.
    if choice == '1': 
        
        # Load menu loop for the program.       
        while True:
            
            # Prompt user to choose a dataset loading option.
            load_choice = input("\nLoad a training dataset from below functions \n\n 1. Load default dataset\n 2. Load data from url\n 3. Exit to main menu\n 4. Exit\n\nEnter your choice between 1 to 4: ")
            
            if load_choice == '1':
                
                # Create an object of GetDatasetClass and load the dataset.
                get_dataset_obj = GetDatasetClass()             
                train_images, train_labels = get_dataset_obj.train_images, get_dataset_obj.train_labels
                eval_images, eval_labels = get_dataset_obj.eval_images, get_dataset_obj.eval_labels
                class_names = get_dataset_obj.class_names
                
                # Check if data is loaded successfully and return to the main menu.          
                if any(x is None for x in (train_images, train_labels, eval_images, eval_labels, class_names)):
                        print("\nReturning to the loading menu . . .")
                        continue                               
                elif (train_images, train_labels, eval_images, eval_labels, class_names) is not None:
                    print('\nData loading successfull')
                    print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                    break
                
            # Loading dataset from ural.
            elif load_choice == '2': 
                
                '''
                THIS IS CURRENTLY NOT PROGRAMMED. SO A SORRY MESSAGE SHOWS. 
                WILL NEED TO PROGRAM FOR FUTURE VERSION OF THIS SOFTWARE.
                '''
                print("\n!!! SORRY !!!\n\nThis option is not available for this software version!\n\nPlease load default dataset instead")
                continue    
                     
            # Exit to main menu.
            elif load_choice == '3':
                print('\nWhich function would you like to perform?\n')
                break
            
            # Exit the program.            
            elif load_choice == '4':
                print('\n\nExiting the software . . .\n\n***Thank you***')
                sys.exit()
                                      
            else:
                print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                continue   
 
    # Start training option.
    elif choice == '2':
        
        # Check if data is loaded.
        if any(x is None for x in (train_images, train_labels, eval_images, eval_labels, class_names)):
            print('\nData is not loaded!!!\n\nPlease load a dataset first to start training\n\nWhich function would you like to perform?\n')
            continue
    
        else:
            
            # Prompt user to enter the number of models to be trained.
            while True:
                num_models_input = input("\nPlease enter the number of the models to be trained (1-5)\nPress 'b' to go back to main menu or 'e' to exit the software\n\nPlease enter: ")
                
                # Go back to the main menu.
                if num_models_input.lower() == 'b':
                    print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                    break
                
                # Exit the program.
                if num_models_input.lower() == 'e':
                   print('\n\nExiting the software . . .\n\n***Thank you***')
                   sys.exit()
                
                try:
                    num_models = int(num_models_input)
                    
                    # Limit the user to input model numbers to train from 1 to 5.
                    if 1 <= num_models <= 5:
                        
                        '''
                        Create an object of GetArchitectureClass and
                        Getting architecture, pooling sizes, padding and number of epochs.
                        '''
                        get_architecture_obj = GetArchitectureClass(num_models)
                        architectures = get_architecture_obj.architectures
                        pooling_sizes = get_architecture_obj.pooling_sizes
                        padding = get_architecture_obj.padding
                        num_epochs = get_architecture_obj.num_epochs
                        
                        if architectures is False or pooling_sizes is False or padding is False or num_epochs is False:
                            print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                            break
                          
                        if architectures is None or pooling_sizes is None or padding is None or num_epochs is None:
                            print('\n\nExiting the software . . .\n\n***Thank you***')
                            sys.exit()
         
                        if architectures and pooling_sizes and padding and num_epochs is not None:
                            
                            # Start training the models.
                            print("\n\nTraining started\n\nDon't worry, the software will automatically\ncheck the overfitting and end the training.\n\nIt might take some time to finish the training.\n\nPlease wait while we finish the training . . .\n")
                            
                            # Create an object of BuildTrainModelsClass and get trained models.
                            build_train_models_obj = BuildTrainModelsClass(architectures, pooling_sizes, padding, num_epochs, train_images, train_labels, eval_images, eval_labels)
                            trained_models = build_train_models_obj.trained_models
                        
                            if trained_models is False:
                                print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                                break
                            
                            elif trained_models is not False:
                                
                                # Save the trained models.                    
                                save_models_obj = SaveModelsClass(trained_models)
                                print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                                break                                                    
                            
                            else:
                                print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                                break
                      
                    else:
                        print("\n\nWrong Input!!!\n\nPlease enter an integer between (1-5) or 'b' or 'e'\n")
                        
                except ValueError:
                    print("\n\nWrong Input!!!\n\nPlease enter an integer between (1-5) or 'b' or 'e'\n")
                    
                  
    # Remove loaded data option.             
    elif choice == '3':
        
        # Check if loaded data exists.
        if any(x is None for x in (train_images, train_labels, eval_images, eval_labels, class_names)):
            print('\nNo loaded data found to remove!!!\n\nReturning to the main menu . . .\n\n\nWhich function would you like to perform?\n')
            continue
        
        else:
            
            # Remove loaded data
            train_images, train_labels = None, None
            eval_images, eval_labels = None, None
            class_names = None
            print("\nLoaded data has been removed\n\nReturning to the main menu . . .\n")
    
    # Exit the program.   
    elif choice == '4':
        print('\n\nExiting the software . . .\n\n***Thank you***')
        sys.exit() 
    
    # Keep the main menu loop running if in the main menu user don't enter 1-4.       
    else: 
        print('\nWrong Input!!!\n\nPlease enter numerical value 1-4\n\nThis software can only perform the functions below\n')
        continue

'''
This code is written with many helps from machinelearningmastery.com, youtube, class lectures, w3schools.com, 
programiz.com, numpy.org, learnpython.org, geeksforgeeks.org and other sites.

This code is written as a final project work for the Python Course at the University of Siegen.

Feel free to use this code.

'''

