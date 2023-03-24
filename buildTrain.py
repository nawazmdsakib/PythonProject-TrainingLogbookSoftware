# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 00:54:37 2023

@author: Sakib
"""

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras import layers
from tensorflow import keras
from tensorflow.keras.callbacks import EarlyStopping, Callback
from tqdm import tqdm


class BuildTrainModelsClass:
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

    def build_and_train_models(self):
        try:
            train_images_reshaped = self.train_images.reshape(60000, 28, 28, 1)
            eval_images_reshaped = self.eval_images.reshape(10000, 28, 28, 1)
            trained_models = []

            for i, architecture in enumerate(self.architectures):
                print(f"\nModel {i + 1}:\n")
                model = Sequential()
                model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 1)))

                for layer in architecture:
                    layer_type = layer[0]
                    if layer_type == 'Conv2D':
                        filters, kernel_size, activation = layer[1], layer[2], layer[3]
                        model.add(keras.layers.Conv2D(filters, (kernel_size, kernel_size), padding=self.padding[i], activation=activation))
                        model.add(keras.layers.MaxPooling2D(self.pooling_sizes[i]))
                    elif layer_type == 'Dense':
                        nodes, activation = layer[1], layer[2]
                        model.add(keras.layers.Dense(nodes, activation=activation))

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

class CustomEarlyStopping(EarlyStopping):
    def __init__(self, model_number, *args, **kwargs):
        super(CustomEarlyStopping, self).__init__(*args, **kwargs)
        self.model_number = model_number

    def on_train_end(self, logs=None):
        if self.stopped_epoch > 0:
            print(f"\n\nTraining stopped early due to overfitting at epoch {self.stopped_epoch + 1} for model {self.model_number}.\n")


class TqdmProgressCallback(Callback):
    def __init__(self):
        super(TqdmProgressCallback, self).__init__()

    def on_train_begin(self, logs=None):
        self.total_epochs = self.params['epochs']

    def on_epoch_begin(self, epoch, logs=None):
        self.steps = self.params['steps']
        self.epoch_bar = tqdm(total=self.steps, desc=f'Epoch {epoch + 1}/{self.total_epochs}', position=0)

    def on_batch_end(self, batch, logs=None):
        metrics = f" - loss: {logs['loss']:.4f} - accuracy: {logs['accuracy']:.4f}"
        self.epoch_bar.set_postfix_str(metrics)
        self.epoch_bar.update(1)

    def on_epoch_end(self, epoch, logs=None):
        val_metrics = f" - val_loss: {logs['val_loss']:.4f} - val_accuracy: {logs['val_accuracy']:.4f}"
        self.epoch_bar.set_postfix_str(self.epoch_bar.postfix + val_metrics)
        self.epoch_bar.close()


