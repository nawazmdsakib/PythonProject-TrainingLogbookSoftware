# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:27:12 2023

@author: Md Sakib Nawaz
"""

import pathlib
import requests
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tqdm import tqdm

class GetDatasetClass:
    def __init__(self):
        if not self.is_connected():
            print("\n\nData loading unsuccessfull !!!\n\nPlease ensure you have an internet connection to load the dataset")
            self.train_images, self.train_labels, self.eval_images, self.eval_labels, self.class_names = None, None, None, None, None
        else:
            dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
            
            
            print("\nDataset is downloading:\n")
            data_dir = self.download_file_with_progress(dataset_url, 'flower_photos.tgz')
            data_dir = pathlib.Path(data_dir)

            # Extract the downloaded file
            tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True, extract=False, archive_format='auto')
            
            fashion_mnist = keras.datasets.fashion_mnist
            (self.train_images, self.train_labels), (self.eval_images, self.eval_labels) = fashion_mnist.load_data()

            self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

            self.plot_sample_image()

    def download_file_with_progress(self, url, filename):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

        with open(filename, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()

        if total_size != 0 and progress_bar.n != total_size:
            print("Error: Download failed")
            return None

        return filename

    def is_connected(self):
        try:
            response = requests.get("https://www.google.com/", timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    def plot_sample_image(self):
        plt.figure()
        plt.imshow(self.train_images[2])
        plt.colorbar()
        plt.grid(False)
        plt.show()

