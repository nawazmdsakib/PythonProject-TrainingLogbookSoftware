# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 00:31:00 2023

@author: Sakib
"""

class GetArchitectureClass:
    def __init__(self, num_models):
        self.allowed_activations = ['relu', 'sigmoid', 'tanh']    
        self.architectures, self.pooling_sizes, self.padding, self.num_epochs = self.get_architecture(num_models)
      

    def get_architecture(self, num_models):
        allowed_activations = ['relu', 'sigmoid', 'tanh']
        architectures = []     
        pooling_sizes = []
        padding = []  
        num_epochs = [] 
        
        
        for i in range(num_models):
            
            while True:
                try:
                    user_input = input(f"\nEnter the number of epochs for model {i + 1}\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                    if user_input.lower() == 'b':
                        return (False,False,False,False)
                    if user_input.lower() == 'e':
                        return (None,None,None,None)
                    input_num_epochs = int(user_input)  
                    break
                except ValueError:
                    print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
            num_epochs.append(input_num_epochs) 

            while True:
                try:
                    user_input = input(f"\nEnter the pooling size for model {i + 1}\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                    if user_input.lower() == 'b':
                        return (False,False,False,False)
                    if user_input.lower() == 'e':
                        return (None,None,None,None)
                    pooling_size = int(user_input)
                    break
                except ValueError:
                    print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
            pooling_sizes.append(pooling_size)
            
            while True:
                user_input = input(f"\nEnter the padding for model {i + 1} (valid, same)\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                if user_input.lower() == 'b':
                    return (False,False,False,False)
                if user_input.lower() == 'e':
                    return (None,None,None,None)
                padding_type = user_input.lower()
                if padding_type == 'valid' or padding_type == 'same':
                    padding.append(padding_type) 
                    break
                else:
                    print("\n\nWrong Input!!!\n\nPlease enter 'valid' or 'same' or 'b' or 'e'\n")
            
            layers = []
            while True:
                try:
                    user_input = input(f"\nPlease enter the number of layers for model {i + 1}\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                    if user_input.lower() == 'b':
                        return (False,False,False,False)
                    if user_input.lower() == 'e':
                        return (None,None,None,None)
                    num_layers = int(user_input)
                    break
                except ValueError:
                    print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
           
            
            for j in range(num_layers):
                while True:
                    user_input = input(f"\nEnter the layer type for layer {j + 1} (Conv2D or Dense)\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                    if user_input.lower() == 'b':
                        return (False,False,False,False)
                    elif user_input.lower() == 'e':
                        return (None,None,None,None)
                    
                    layer_type = user_input
                    if layer_type == 'Conv2D':
                        
                        while True:
                            try:
                                user_input = input(f"\nEnter the number of filters for layer {j + 1}\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
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
                                user_input = input(f"\nEnter the kernel size for layer {j + 1}\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                                if user_input.lower() == 'b':
                                    return (False,False,False,False)
                                if user_input.lower() == 'e':
                                    return (None,None,None,None)
                                kernel_size = int(user_input)
                                break
                            except ValueError:
                                print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")
                        while True:
                            user_input = input(f"\nEnter the activation function for layer {j + 1} (relu, sigmoid, tanh)\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                            if user_input.lower() == 'b':
                                return (False,False,False,False)
                            if user_input.lower() == 'e':
                                return (None,None,None,None)
                            activation = user_input
                            if activation in allowed_activations:
                                layers.append(('Conv2D', filters, kernel_size, activation))
                                break
                            else:
                                print("\n\nWrong Input!!!\n\nPlease enter a valid activation function (relu, sigmoid, tanh) or 'b' or 'e'\n")
                    
                    elif layer_type == 'Dense':
                        
                        while True:
                            try:
                                user_input = input(f"\nEnter the number of nodes for layer {j + 1}\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                                if user_input.lower() == 'b':
                                    return (False,False,False,False)
                                if user_input.lower() == 'e':
                                    return (None,None,None,None)
                                nodes = int(user_input)
                                break
                            except ValueError:
                                print("\n\nWrong Input!!!\n\nPlease enter an integer or 'b' or 'e'\n")

                        while True:
                            user_input = input(f"\nEnter the activation function for layer {j + 1} (relu, sigmoid, tanh)\nPress 'b' to go back to main menu or 'e' to exit\n\nPlease enter: ")
                            if user_input.lower() == 'b':
                                return (False,False,False,False)
                            if user_input.lower() == 'e':
                                return (None,None,None,None)
                            activation = user_input
                            if activation in allowed_activations:
                                layers.append(('Dense', nodes, activation))
                                break
                            else:
                                print("\n\nWrong Input!!!\n\nPlease enter a valid activation function (relu, sigmoid, tanh) or 'b' or 'e'\n")
                    else:
                        print("\n\nWrong Input!!!\n\nPlease enter a valid layer type (Conv2D or Dense) or 'b' or 'e'\n")
                    
                    if layer_type == 'Conv2D' or layer_type == 'Dense':
                        break
               
            architectures.append(layers)
        
        return architectures, pooling_sizes, padding, num_epochs