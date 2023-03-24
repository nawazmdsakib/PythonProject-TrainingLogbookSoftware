# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:43:06 2023

@author: Sakib
"""

import sys

from getDataset import GetDatasetClass
from getArchitecture import GetArchitectureClass
from buildTrain import BuildTrainModelsClass
from saveModels import SaveModelsClass

print("\n      Welcome to the Training Logbook Software\n\nThis software can train deep learning models for image\nclassification using the popular MNIST dataset. You can\nchoose the number of models you want to train including\ncustomization of different types of architecture.\n\nWhich function would you like to perform?\n")

train_images, train_labels = None, None
eval_images, eval_labels = None, None
class_names = None


while True:

   
    choice = input(" 1. Load Dataset\n 2. Start Training\n 3. Remove Loaded Data\n 4. Exit\n\nPlease choose a function between 1 to 4: ")

    if choice == '1': 
                
        while True:
     
            load_choice = input("\nLoad a training dataset from below functions \n\n 1. Load default dataset\n 2. Load data from url\n 3. Exit to main menu\n 4. Exit\n\nEnter your choice between 1 to 4: ")

            if load_choice == '1':
                
                get_dataset_obj = GetDatasetClass()             
                train_images, train_labels = get_dataset_obj.train_images, get_dataset_obj.train_labels
                eval_images, eval_labels = get_dataset_obj.eval_images, get_dataset_obj.eval_labels
                class_names = get_dataset_obj.class_names
                
                
                if any(x is None for x in (train_images, train_labels, eval_images, eval_labels, class_names)):
                        print("\nReturning to the loading menu . . .")
                        continue
                                                
                elif (train_images, train_labels, eval_images, eval_labels, class_names) is not None:
                    print('\nData loading successfull')
                    print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                    break
                
              
            elif load_choice == '2': 
                print("\n!!! SORRY !!!\n\nThis option is not available for this software version!\n\nPlease load default dataset instead")
                continue    
                     
         
            elif load_choice == '3':
                print('\nWhich function would you like to perform?\n')
                break
                        
            elif load_choice == '4':
                print('\n\nExiting the software . . .\n\n***Thank you***')
                sys.exit()
                                      
            else:
                print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                continue   
 
    elif choice == '2':
    
        if any(x is None for x in (train_images, train_labels, eval_images, eval_labels, class_names)):
            print('\nData is not loaded!!!\n\nPlease load a dataset first to start training\n\nWhich function would you like to perform?\n')
            continue
    
        else:
    
            while True:
                num_models_input = input("\nPlease enter the number of the models to be trained (1-5)\nPress 'b' to go back to main menu or 'e' to exit the software\n\nPlease enter: ")
    
                if num_models_input.lower() == 'b':
                    print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                    break
                
                if num_models_input.lower() == 'e':
                   print('\n\nExiting the software . . .\n\n***Thank you***')
                   sys.exit()
                
                try:
                    num_models = int(num_models_input)
                    if 1 <= num_models <= 5:
                                            
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
                            print("\n\nTraining started\n\nDon't worry, the software will automatically\ncheck the overfitting and end the training.\n\nIt might take some time to finish the training.\n\nPlease wait while we finish the training . . .\n\n")
                            
                            build_train_models_obj = BuildTrainModelsClass(architectures, pooling_sizes, padding, num_epochs, train_images, train_labels, eval_images, eval_labels)
                            trained_models = build_train_models_obj.trained_models
                        
                            if trained_models is False:
                                print("\nReturning to the main menu . . .\n\nWhich function would you like to perform?\n")
                                break
                            
                            elif trained_models is not False:
                                                      
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
                    
                  
                   
    elif choice == '3':
        
        if any(x is None for x in (train_images, train_labels, eval_images, eval_labels, class_names)):
            print('\nNo loaded data found to remove!!!\n\nReturning to the main menu . . .\n\n\nWhich function would you like to perform?\n')
            continue
        
        else:
            
            train_images, train_labels = None, None
            eval_images, eval_labels = None, None
            class_names = None
            print("\nLoaded data has been removed\n\nReturning to the main menu . . .\n")
    
        
    elif choice == '4':
        print('\n\nExiting the software . . .\n\n***Thank you***')
        sys.exit() 
    
           
    else: 
        print('\nWrong Input!!!\n\nPlease enter numerical value 1-4\n\nThis software can only perform the functions below\n')
        continue
