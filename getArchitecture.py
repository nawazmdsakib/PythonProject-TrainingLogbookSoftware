# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 00:57:07 2023

@author: Sakib
"""

# -*- coding: utf-8 -*-
'''
Created on Wed Mar 22 00:31:00 2023

@author: Md Sakib Nawaz
'''

# Class code.

'''
A class to get architecture configurations for multiple
models based on user choice from the options provided.
'''
class GetArchitectureClass:
    
    # Initialize the class with the number of models to configure.
    def __init__(self, num_models):
        self.allowed_activations = ['relu', 'sigmoid', 'tanh']    
        self.architectures, self.pooling_sizes, self.padding, self.num_epochs = self.get_architecture(num_models)
      
    # Method to get architecture configurations for a specified number of models.
    def get_architecture(self, num_models):
        allowed_activations = ['relu', 'sigmoid', 'tanh']
        architectures = []     
        pooling_sizes = []
        padding = []  
        num_epochs = [] 
        
        # Iterate through the number of models and get their configurations.
        for i in range(num_models):
            
            # Get the number of epochs for the model.
            while True:
                try:
                    user_input = input(f"\n\nEnter the number of Epochs for model {i + 1}\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                    if user_input.lower() == 'b':
                        return (False,False,False,False)
                    if user_input.lower() == 'e':
                        return (None,None,None,None)
                    input_num_epochs = int(user_input)  
                    break
                except ValueError:
                    print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
            num_epochs.append(input_num_epochs) 
            
            # Get the pooling size for the model.
            while True:
                try:
                    user_input = input(f"\n\nEnter the Pooling size for model {i + 1}\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                    if user_input.lower() == 'b':
                        return (False,False,False,False)
                    if user_input.lower() == 'e':
                        return (None,None,None,None)
                    pooling_size = int(user_input)
                    break
                except ValueError:
                    print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
            pooling_sizes.append(pooling_size)
            
            # Get the padding type for the model.
            while True:
                user_input = input(f"\n\nEnter the Padding for model {i + 1} (valid, same)\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                padding_type = user_input.lower()
                if padding_type == 'b':
                    return (False,False,False,False)
                if padding_type == 'e':
                    return (None,None,None,None)
                if padding_type == 'valid' or padding_type == 'same':
                    padding.append(padding_type)
                    break
                else:
                    print("\n\nWrong Input!!!\n\nPlease enter 'valid' or 'same' or 'b' or 'e'\n")
    
            # Get the number of layers and their configurations for the model.
            layers = []
            while True:
                try:
                    user_input = input(f"\n\nEnter the number of Layers for model {i + 1}\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                    if user_input.lower() == 'b':
                        return (False,False,False,False)
                    if user_input.lower() == 'e':
                        return (None,None,None,None)
                    num_layers = int(user_input)
                    break
                except ValueError:
                    print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
           
            # Get layer details for each layer in the model.
            for j in range(num_layers):
                while True:
                    user_input = input(f"\n\nEnter the Layer Type for layer {j + 1} of model {i + 1} (Conv2D or Dense)\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                    
                    if user_input.lower() == 'b':
                        return (False,False,False,False)
                    elif user_input.lower() == 'e':
                        return (None,None,None,None)
                    
                    layer_type = user_input.lower()
                    if layer_type == 'conv2d':
                        
                        # Get the number of filters, kernel size, and activation for the Conv2D layer.
                        while True:
                            try:
                                user_input = input(f"\n\nEnter the number of Filters for layer {j + 1} of model {i + 1}\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                                if user_input.lower() == 'b':
                                    return (False,False,False,False)
                                if user_input.lower() == 'e':
                                    return (None,None,None,None)
                                filters = int(user_input)
                                break
                            except ValueError:
                                print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
                        while True:
                            try:
                                user_input = input(f"\n\nEnter the Kernel size for layer {j + 1} of model {i + 1}\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                                if user_input.lower() == 'b':
                                    return (False,False,False,False)
                                if user_input.lower() == 'e':
                                    return (None,None,None,None)
                                kernel_size = int(user_input)
                                break
                            except ValueError:
                                print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
                        while True:
                            user_input = input(f"\n\nEnter the Activation function for layer {j + 1} of model {i + 1} (relu, sigmoid, tanh)\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                            if user_input.lower() == 'b':
                                return (False,False,False,False)
                            if user_input.lower() == 'e':
                                return (None,None,None,None)
                            
                            activation = user_input.lower()
                            if activation in allowed_activations:
                                layers.append(('Conv2D', filters, kernel_size, activation))
                                break
                            else:
                                print("\n\nWrong Input!!!\n\nPlease enter a valid activation function (relu, sigmoid, tanh) or 'b' or 'e'\n")

                    elif layer_type == 'dense':
                        
                        # Get the number of nodes and activation for the Dense layer.
                        while True:
                            try:
                                user_input = input(f"\n\nEnter the number of Nodes for layer {j + 1} of model {i + 1}\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                                if user_input.lower() == 'b':
                                    return (False,False,False,False)
                                if user_input.lower() == 'e':
                                    return (None,None,None,None)
                                nodes = int(user_input)
                                break
                            except ValueError:
                                print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")

                        while True:
                            user_input = input(f"\n\nEnter the Activation function for layer {j + 1} of model {i + 1} (relu, sigmoid, tanh)\n|'b' for main menu | 'e' to exit\n\nPlease enter: ")
                            if user_input.lower() == 'b':
                                return (False,False,False,False)
                            if user_input.lower() == 'e':
                                return (None,None,None,None)
                            
                            activation = user_input.lower()
                            if activation in allowed_activations:
                                layers.append(('Dense', nodes, activation))
                                break
                            else:
                                print("\n\nWrong Input!!!\n\nPlease enter a valid activation function (relu, sigmoid, tanh) or 'b' or 'e'\n")

                    else:
                        print("\n\nWrong Input!!!\n\nPlease enter a valid layer type (Conv2D or Dense) or 'b' or 'e'\n")
                    
                    # If a valid layer type is entered, break the loop.
                    if layer_type == 'conv2d' or layer_type == 'dense':
                        break
               
             # Add the configured layers for the model to the architectures list.
            architectures.append(layers)
        
        # Return the collected architectures, pooling_sizes, padding, and num_epochs.
        return architectures, pooling_sizes, padding, num_epochs