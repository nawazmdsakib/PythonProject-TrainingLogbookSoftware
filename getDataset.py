# -*- coding: utf-8 -*-
'''
Created on Tue Mar 21 22:27:12 2023

@author: Md Sakib Nawaz
'''

# Class code.

# pathlib, requests, tensorflow and matplotlib.pyplot libraries is imported. 
import pathlib
import requests
import tensorflow as tf
import matplotlib.pyplot as plt

# tqdm module is imported from tqdm library.
from tqdm import tqdm

# Keras module from the TensorFlow library is imported.
from tensorflow import keras

'''
This class downloads the flower dataset from the given URL 
and loads the Fashion MNIST dataset from TensorFlow. It 
checks if there is an internet connection before downloading
and provides a progress bar while downloading the dataset. 
The class also plots a sample image from the dataset.
'''
class GetDatasetClass:
    
    # Define the class constructor.
    def __init__(self):
        
        # Check if there is an active internet connection.
        if not self.is_connected():
            print("\n\nData loading unsuccessfull !!!\n\nPlease ensure you have an internet connection to load the dataset")
            self.train_images, self.train_labels, self.eval_images, self.eval_labels, self.class_names = None, None, None, None, None
        else:
            
            # Set the dataset URL.
            dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
            
            # Download the dataset with a progress bar.
            print("\nDataset is downloading:\n")
            data_dir = self.download_file_with_progress(dataset_url, 'flower_photos.tgz')
            if not data_dir:
                print("Dataset download failed due to OS error.")
                return
            
            data_dir = pathlib.Path(data_dir)

            # Extract the downloaded file.
            tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True, extract=False, archive_format='auto')
            
            # Load the Fashion MNIST dataset.
            fashion_mnist = keras.datasets.fashion_mnist
            (self.train_images, self.train_labels), (self.eval_images, self.eval_labels) = fashion_mnist.load_data()
            
            # Set the class names.
            self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
            
            # Plot a sample image from the dataset.
            self.plot_sample_image()

    # Download progress bar show function.
    def download_file_with_progress(self, url, filename):
    
        try:
            # Download the file with a progress bar.
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            
            # 1 Kibibyte.
            block_size = 1024  
            progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
            
            # Write the downloaded data to a file.
            with open(filename, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
    
            progress_bar.close()
            
            # Check if the download was successful.
            if total_size != 0 and progress_bar.n != total_size:
                print("Error: Download failed")
                return False
    
            return filename
        
        except OSError as e:
                print(f"OS error occurred: {e}")
                return False
    
    # Internet connection checking function.
    def is_connected(self):
        
        # Check if the device is connected to the internet.
        try:
            response = requests.get("https://www.google.com/", timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False
        
    # Plot function.
    def plot_sample_image(self):
        
        # Plot a sample image from the dataset.
        plt.figure()
        plt.imshow(self.train_images[2])
        plt.colorbar()
        plt.grid(False)
        plt.show()

