# -*- coding: utf-8 -*-
'''
Created on Wed Mar 22 00:54:37 2023

@author: Md Sakib Nawaz
'''

# Class code.

# tensorflow library is imported. 
import tensorflow as tf

# Imported required modules from different libraries.
from tqdm import tqdm
from tensorflow import keras
from tensorflow.keras import Sequential, layers
from tensorflow.keras.callbacks import EarlyStopping, Callback

'''
A class definition with 2 functions where first one is init
function and second one will build and train the models.
'''
class BuildTrainModelsClass:
    
    # Define the class constructor.
    def __init__(self, architectures, pooling_sizes, padding, num_epochs, train_images, train_labels, eval_images, eval_labels):
        self.architectures = architectures
        self.pooling_sizes = pooling_sizes
        self.padding = padding
        self.num_epochs = num_epochs
        self.train_images = train_images
        self.train_labels = train_labels
        self.eval_images = eval_images
        self.eval_labels = eval_labels
        self.trained_models = self.build_and_train_models()

    '''
    This function builds and trains the models based on the provided
    architecture, pooling sizes, padding, and number of epochs. It also
    handles reshaping the input images and stores the trained models
    in a list.
    '''
    def build_and_train_models(self):
        try:
            train_images_reshaped = self.train_images.reshape(60000, 28, 28, 1)
            eval_images_reshaped = self.eval_images.reshape(10000, 28, 28, 1)
            trained_models = []
            
            # Iterate through the architectures and build the corresponding models.
            for i, architecture in enumerate(self.architectures):
                print(f"\nModel {i + 1}:\n")
                model = Sequential()
                model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 1)))
                
                # Add layers to the model based on the given architecture.
                for layer in architecture:
                    layer_type = layer[0]
                    if layer_type == 'Conv2D':
                        filters, kernel_size, activation = layer[1], layer[2], layer[3]
                        model.add(keras.layers.Conv2D(filters, (kernel_size, kernel_size), padding=self.padding[i], activation=activation))
                        model.add(keras.layers.MaxPooling2D(self.pooling_sizes[i]))
                    elif layer_type == 'Dense':
                        nodes, activation = layer[1], layer[2]
                        model.add(keras.layers.Dense(nodes, activation=activation))
                
                # Compile and train the model.
                model.add(keras.layers.Flatten())
                model.add(keras.layers.Dense(10, activation=tf.nn.softmax))
                model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

                early_stopping_callback = CustomEarlyStopping(model_number=i + 1, monitor='val_loss', patience=5, verbose=1, mode='min')
                tqdm_callback = TqdmProgressCallback()
                history = model.fit(train_images_reshaped, self.train_labels, epochs=self.num_epochs[i], validation_data=(eval_images_reshaped, self.eval_labels), callbacks=[early_stopping_callback, tqdm_callback], verbose=0)

                trained_models.append((model, history))

            return trained_models
        except Exception as e:
            print(f"\n\nError during training: {e}\n")
            return False

'''
Custom EarlyStopping callback class to stop training early 
if overfitting occurs.
'''
class CustomEarlyStopping(EarlyStopping):
    
    # Initialize the custom early stopping callback with the model number.
    def __init__(self, model_number, *args, **kwargs):
        super(CustomEarlyStopping, self).__init__(*args, **kwargs)
        self.model_number = model_number
    
    # Print a message if training stops early due to overfitting.
    def on_train_end(self, logs=None):
        if self.stopped_epoch > 0:
            print(f"\n\nTraining stopped early due to overfitting at epoch {self.stopped_epoch + 1} for model {self.model_number}.\n")

'''
Custom progress bar callback class for displaying training 
progress using tqdm.
'''
class TqdmProgressCallback(Callback):
    
    # Initialize the custom progress bar callback.
    def __init__(self):
        super(TqdmProgressCallback, self).__init__()

    # Set the total number of epochs when training begins.
    def on_train_begin(self, logs=None):
        self.total_epochs = self.params['epochs']

    # Initialize the progress bar for the current epoch.
    def on_epoch_begin(self, epoch, logs=None):
        self.steps = self.params['steps']
        self.epoch_bar = tqdm(total=self.steps, desc=f'Epoch {epoch + 1}/{self.total_epochs}', position=0)

    # Update the progress bar with the current batch's metrics after each batch.
    def on_batch_end(self, batch, logs=None):
        metrics = f" - loss: {logs['loss']:.4f} - accuracy: {logs['accuracy']:.4f}"
        self.epoch_bar.set_postfix_str(metrics)
        self.epoch_bar.update(1)

    # Display the validation metrics and close the progress bar at the end of each epoch.
    def on_epoch_end(self, epoch, logs=None):
        val_metrics = f" - val_loss: {logs['val_loss']:.4f} - val_accuracy: {logs['val_accuracy']:.4f}"
        self.epoch_bar.set_postfix_str(self.epoch_bar.postfix + val_metrics)
        self.epoch_bar.close()


