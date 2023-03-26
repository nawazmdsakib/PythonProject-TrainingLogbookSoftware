# PythonProject-TrainingLogbookSoftware

Training Logbook Software:


Description:


This software is designed to perform image classification tasks using deep learning techniques. It can load a dataset, preprocess the data, create an appropriate neural network architecture, train the model, and save the trained models with a CSV file of model details for future use. The software is written in Python and utilizes libraries such as tensorflow, keras, sys, pandas, os, pathlib, requests, tqdm, and matplotlib.

This software has one main code Python file named main.py and 4 Class Python files named getDataset.py, getArchitecture.py, buildTrain.py, and saveModels.py. In getDataset.py file there is GetDatasetClass, in getArchitecture.py file there is GetArchitectureClass, in buildTrain.py file there are BuildTrainModelsClass, CustomEarlyStoppingand class, TqdmProgressCallback class, in saveModels.py file there is SaveModelsClass.

Class GetDatasetClass:
This class downloads the flower dataset and loads the Fashion MNIST dataset. It checks for an active internet connection before downloading and during downloading. It aslo displays a progress bar during the download and plots a sample image from the dataset.
The following functions are available:
* __init__(self): The class Constructor that initializes the class, checks for internet connectivity before and during downloading, and triggers the download and loading of the datasets. It also sets class names and plots a sample image.
* download_file_with_progress(self, url, filename): This function downloads a file from a given URL with a progress bar, and saves it with the specified filename. If the download is successful, it returns the filename; otherwise, it returns None with OSError logs.
* is_connected(self): This function checks if the device has an active internet connection by making a request to google.com. It returns True if connected and False otherwise.
* plot_sample_image(self): This function plots a sample image from the dataset using the matplotlib.pyplot library.

Class GetArchitectureClass:
This class helps to get architecture configurations for multiple models based on user input. The class handles user input to configure the models with different layers, activation functions, pooling sizes, padding types, and number of epochs.
The following functions are available:
* __init__(self, num_models): The class constructor initializes the class with the number of models to configure. It calls the get_architecture method to set the architectures, pooling sizes, padding types, and number of epochs for each model.
* get_architecture(self, num_models): This method gets architecture configurations for a specified number of models. It takes the user input to configure the number of epochs, pooling sizes, padding types, number of layers, and layer details (such as type, filters, kernel size, nodes, and activation functions) for each model. It returns the collected architectures, pooling sizes, padding types, and number of epochs.

Class BuildTrainClass:
This class is designed to build and train multiple models based on user-defined architecture configurations. It takes in architectures, pooling sizes, padding, number of epochs, and training and evaluation datasets as input and returns trained models.
The following functions are available:
* __init__(self, architectures, pooling_sizes, padding, num_epochs, train_images, train_labels, eval_images, eval_labels): The class constructor initializes the class with the provided architectures, pooling sizes, padding, number of epochs, and training and evaluation datasets. It calls the build_and_train_models method to build and train the models.
* build_and_train_models(self): This function builds and trains the models based on the provided architecture, pooling sizes, padding, and number of epochs. It reshapes the input images, constructs the model architectures using the given configurations, compiles the models, and trains them. The function returns a list of trained models and their training histories.

Class CustomEarlyStopping:
This custom class extends the EarlyStopping class from Keras and is designed to stop the training process early if overfitting occurs. It adds a model number attribute to the base class for better logging and feedback.
The following functions are available:
* __init__(self, model_number, *args, **kwargs): Initializes the custom early stopping callback with the model number and passes any additional arguments to the base class.
* on_train_end(self, logs=None): This method is called when the training process ends. It checks if the training was stopped early due to overfitting and prints a message with the stopped epoch and model number.

Class TqdmProgressCallback:
This custom class extends the Callback class from Keras and is designed to display the training progress using the tqdm library. It shows the progress bar for each epoch and displays the training and validation metrics.
The following functions are available:
* on_train_begin(self, logs=None): This method is called when the training process begins. It sets the total number of epochs based on the training parameters.
* on_epoch_begin(self, epoch, logs=None): This method is called at the beginning of each epoch. It initializes the progress bar for the current epoch and sets the number of steps.
* on_batch_end(self, batch, logs=None): This method is called at the end of each batch. It updates the progress bar with the current batch's metrics.
* on_epoch_end(self, epoch, logs=None): This method is called at the end of each epoch. It displays the validation metrics and closes the progress bar.

Class SaveModelsClass:
This class is designed to save trained models as .h5 files and their details in a .csv file. It takes in the trained models and the desired .csv filename as input and saves the corresponding model details to disk.
The following functions are available:
* __init__(self, trained_models, csv_filename): The class constructor initializes the class with the trained models and the desired .csv filename. It calls the save_models_to_csv method to save the models and their details.
* save_models_to_csv(self): This function saves the trained models as .h5 files and their details in a .csv file. It creates a 'saved_models' directory if it doesn't exist, iterates through the trained models to save them as .h5 files, extracts and stores model information for the .csv file, creates a DataFrame to store the model data, and saves the DataFrame as a .csv file. If successful, it prints the model name and file locations; if an error occurs, it sets the error_occurred attribute to True.


Workflow:


The workflow for this image classification application using the MNIST dataset consists of the following steps:
Import necessary libraries and classes: Import the sys and os libraries, as well as the custom classes GetDatasetClass, GetArchitectureClass, BuildTrainModelsClass, and SaveModelsClass.
Print a welcome message and display the main menu options to the user.
Initialize the data variables for train_images, train_labels, eval_images, eval_labels, and class_names.
Implement a loop for the main menu, which allows users to choose between loading a dataset, training models, removing loaded data, and exiting the program.

If the user chooses to load a dataset:
a. Implement a loop for the dataset loading menu.
b. Allow the user to load the default dataset or a dataset from a URL (not supported in this version).
c. If the default dataset is loaded, create an instance of GetDatasetClass and load the dataset.
d. Confirm if the dataset is loaded successfully and return to the main menu.

If the user chooses to start training:
a. Check if the dataset is loaded.
b. Prompt the user to enter the number of models to be trained.
c. Create an instance of GetArchitectureClass and get the architecture, pooling sizes, padding, and number of epochs.
d. Train the models by creating an instance of BuildTrainModelsClass and get the trained models.
e. Prompt the user for a file name to save the model details and handle potential file name conflicts.
f. Create an instance of SaveModelsClass to save the trained models and the .csv file containing their details.
g. Return to the main menu.

If the user chooses to remove loaded data:
a. Check if any data is loaded.
b. Remove the loaded data by setting data variables to None.
c. Confirm that the data has been removed and return to the main menu.

If the user chooses to exit the program, display a thank-you message and exit the application.
If the user inputs an invalid option, display an error message and continue displaying the main menu.
Throughout the application, various loops and input handling are implemented to ensure smooth operation and user interaction.


Installation:


To get started, you'll need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/
You'll also need to install the Python packages: tensorflow, keras, sys, pandas, os, pathlib, requests, tqdm, and matplotlib.

Once you have Python and the required packages installed, you can run the code. Make sure other class files such as getDataset.py, getArchitecture.py, buildTrain.py, and saveModels.py are in the same directory.

Load main.py file and RUN!


Examples:


* Welcome note and main menu

      Welcome to the Training Logbook Software

This software can train deep learning models for image
classification using the popular MNIST dataset. You can
choose the number of models you want to train including
customization of different types of architecture.

Which function would you like to perform?

 1. Load Dataset
 2. Start Training
 3. Remove Loaded Data
 4. Exit

Please choose a function between 1 to 4: 


* Load dataset menu

Load a training dataset from below functions 

 1. Load default dataset
 2. Load data from url
 3. Exit to main menu
 4. Exit

Enter your choice between 1 to 4:


* Load default dataset

Dataset is downloading:

100%|██████████| 229M/229M [00:17<00:00, 13.3MiB/s]

Data loading successfull

Returning to the main menu . . .

Which function would you like to perform?

 1. Load Dataset
 2. Start Training
 3. Remove Loaded Data
 4. Exit

Please choose a function between 1 to 4: 


* If internet connection is lost during the download process

Dataset is downloading:

 20%|██        | 46.6M/229M [00:06<00:25, 7.23MiB/s]

Error occurred: HTTPSConnectionPool(host='storage.googleapis.com', port=443): Read timed out.

Data loading unsuccessful !!!

Internet connection lost during the download process
or other system-related operations failed

Please ensure you have an internet connection to load the dataset
or check your system error logs and try loading the file again

Returning to the loading menu . . .

Load a training dataset from below functions 

 1. Load default dataset
 2. Load data from url
 3. Exit to main menu
 4. Exit

Enter your choice between 1 to 4: 


* If there is no internet connection

Data loading unsuccessfull !!!

Please ensure you have an internet connection to load the dataset

Returning to the loading menu . . .

Load a training dataset from below functions 

 1. Load default dataset
 2. Load data from url
 3. Exit to main menu
 4. Exit

Enter your choice between 1 to 4: 


* Load data from url

!!! SORRY !!!

This option is not available for this software version!

Please load default dataset instead

Load a training dataset from below functions 

 1. Load default dataset
 2. Load data from url
 3. Exit to main menu
 4. Exit

Enter your choice between 1 to 4: 


* Start Training

Enter the number of Models to be trained (1-5)
|'b' for main menu | 'e' to exit

Please enter: 2


Enter the number of Epochs for model 1
|'b' for main menu | 'e' to exit

Please enter: 1


Enter the Pooling size for model 1
|'b' for main menu | 'e' to exit

Please enter: 1


Enter the Padding for model 1 (valid, same)
|'b' for main menu | 'e' to exit

Please enter: same


Enter the number of Layers for model 1
|'b' for main menu | 'e' to exit

Please enter: 1


Enter the Layer Type for layer 1 of model 1 (Conv2D or Dense)
|'b' for main menu | 'e' to exit

Please enter: dense


Enter the number of Nodes for layer 1 of model 1
|'b' for main menu | 'e' to exit

Please enter: 1


Enter the Activation function for layer 1 of model 1 (relu, sigmoid, tanh)
|'b' for main menu | 'e' to exit

Please enter: relu


Enter the number of Epochs for model 2
|'b' for main menu | 'e' to exit

Please enter: 1


Enter the Pooling size for model 2
|'b' for main menu | 'e' to exit

Please enter: 1


Enter the Padding for model 2 (valid, same)
|'b' for main menu | 'e' to exit

Please enter: same


Enter the number of Layers for model 2
|'b' for main menu | 'e' to exit

Please enter: 1


Enter the Layer Type for layer 1 of model 2 (Conv2D or Dense)
|'b' for main menu | 'e' to exit

Please enter: dense


Enter the number of Nodes for layer 1 of model 2
|'b' for main menu | 'e' to exit

Please enter: 1


Enter the Activation function for layer 1 of model 2 (relu, sigmoid, tanh)
|'b' for main menu | 'e' to exit

Please enter: relu


* After providing all the inputs

Training started

Don't worry, the software will automatically
check the overfitting and end the training.

It might take some time to finish the training.

Please wait while we finish the training . . .


Model 1:

Epoch 1/1: 100%|██████████| 1875/1875 [00:13<00:00, 136.61it/s,  - loss: 0.8938 - accuracy: 0.6767 - val_loss: 0.4917 - val_accuracy: 0.8284]

Model 2:

Epoch 1/1: 100%|██████████| 1875/1875 [00:07<00:00, 258.21it/s,  - loss: 0.9425 - accuracy: 0.7095 - val_loss: 0.5359 - val_accuracy: 0.8195]


* If overfitting happens

Model 1:

Epoch 1/50: 100%|██████████| 1875/1875 [00:11<00:00, 163.79it/s,  - loss: 1.0074 - accuracy: 0.7375 - val_loss: 0.5077 - val_accuracy: 0.8214]
Epoch 2/50: 100%|██████████| 1875/1875 [00:05<00:00, 336.94it/s,  - loss: 0.4476 - accuracy: 0.8433 - val_loss: 0.4483 - val_accuracy: 0.8395]
Epoch 3/50: 100%|██████████| 1875/1875 [00:06<00:00, 271.28it/s,  - loss: 0.4041 - accuracy: 0.8573 - val_loss: 0.4328 - val_accuracy: 0.8454]
Epoch 4/50: 100%|██████████| 1875/1875 [00:06<00:00, 306.90it/s,  - loss: 0.3778 - accuracy: 0.8652 - val_loss: 0.4502 - val_accuracy: 0.8492]
Epoch 5/50: 100%|██████████| 1875/1875 [00:06<00:00, 302.50it/s,  - loss: 0.3624 - accuracy: 0.8695 - val_loss: 0.4065 - val_accuracy: 0.8565]
Epoch 6/50: 100%|██████████| 1875/1875 [00:08<00:00, 225.54it/s,  - loss: 0.3450 - accuracy: 0.8753 - val_loss: 0.3995 - val_accuracy: 0.8598]
Epoch 7/50: 100%|██████████| 1875/1875 [00:06<00:00, 269.10it/s,  - loss: 0.3369 - accuracy: 0.8790 - val_loss: 0.4020 - val_accuracy: 0.8621]
Epoch 8/50: 100%|██████████| 1875/1875 [00:07<00:00, 252.81it/s,  - loss: 0.3266 - accuracy: 0.8810 - val_loss: 0.4110 - val_accuracy: 0.8560]
Epoch 9/50: 100%|██████████| 1875/1875 [00:05<00:00, 317.24it/s,  - loss: 0.3210 - accuracy: 0.8825 - val_loss: 0.3940 - val_accuracy: 0.8635]
Epoch 10/50: 100%|██████████| 1875/1875 [00:06<00:00, 268.68it/s,  - loss: 0.3144 - accuracy: 0.8863 - val_loss: 0.3986 - val_accuracy: 0.8620]
Epoch 11/50: 100%|██████████| 1875/1875 [00:06<00:00, 306.10it/s,  - loss: 0.3114 - accuracy: 0.8859 - val_loss: 0.3913 - val_accuracy: 0.8634]
Epoch 12/50: 100%|██████████| 1875/1875 [00:05<00:00, 316.70it/s,  - loss: 0.3078 - accuracy: 0.8875 - val_loss: 0.3901 - val_accuracy: 0.8677]
Epoch 13/50: 100%|██████████| 1875/1875 [00:06<00:00, 268.58it/s,  - loss: 0.3028 - accuracy: 0.8892 - val_loss: 0.3895 - val_accuracy: 0.8660]
Epoch 14/50: 100%|██████████| 1875/1875 [00:05<00:00, 326.30it/s,  - loss: 0.2999 - accuracy: 0.8908 - val_loss: 0.4029 - val_accuracy: 0.8640]
Epoch 15/50: 100%|██████████| 1875/1875 [00:06<00:00, 277.84it/s,  - loss: 0.2973 - accuracy: 0.8910 - val_loss: 0.3923 - val_accuracy: 0.8674]
Epoch 16/50: 100%|██████████| 1875/1875 [00:07<00:00, 246.19it/s,  - loss: 0.2943 - accuracy: 0.8912 - val_loss: 0.4019 - val_accuracy: 0.8648]
Epoch 17/50: 100%|██████████| 1875/1875 [00:05<00:00, 329.86it/s,  - loss: 0.2936 - accuracy: 0.8927 - val_loss: 0.4017 - val_accuracy: 0.8647]
Epoch 18/50: 100%|██████████| 1875/1875 [00:06<00:00, 274.98it/s,  - loss: 0.2915 - accuracy: 0.8936 - val_loss: 0.4152 - val_accuracy: 0.8622]


Training stopped early due to overfitting at epoch 18 for model 1.


Model 2:

Epoch 1/50: 100%|██████████| 1875/1875 [02:10<00:00, 14.42it/s,  - loss: 2.3027 - accuracy: 0.0999 - val_loss: 2.3027 - val_accuracy: 0.1000]
Epoch 2/50:  74%|███████▎  | 1382/1875 [01:36<00:31, 15.42it/s,  - loss: 2.3028 - accuracy: 0.0986]
...continue


* If the file already exists

The file named 'training_1.csv' already exists.


Do you want to overwrite the file? Enter (yes/no)
|'b' for main menu | 'e' to exit

Please enter: no


Enter a file name to save the model details (without extension)
|'b' for main menu | 'e' to exit

Please enter: 


* If input is not 'yes' or 'no' or 'b' or 'e'

You didn't enter any of these ('yes' or 'no' or 'b' or 'e')

Going back to the name input . . .



Enter a file name to save the model details (without extension)
|'b' for main menu | 'e' to exit

Please enter: 


* After a non existing file name is provided, file saved and shows the name and locations of the file:

All model details have been saved successfully

CSV file name: training_6.csv
CSV file location: C:\Users\Sakib\Documents\GitHub\PythonProject-TrainingLogbookSoftware\training_6.csv

Models file location: C:\Users\Sakib\Documents\GitHub\PythonProject-TrainingLogbookSoftware\saved_models\training_6_model_2.h5

Returning to the main menu . . .

Which function would you like to perform?

 1. Load Dataset
 2. Start Training
 3. Remove Loaded Data
 4. Exit

Please choose a function between 1 to 4: 


* Remove Loaded Data

Loaded data has been removed

Returning to the main menu . . .

 1. Load Dataset
 2. Start Training
 3. Remove Loaded Data
 4. Exit

Please choose a function between 1 to 4: 


* Exit

Exiting the software . . .

***Thank you***


* Example of the details in CSV file:

Model Name   Architecture                      Number of Epochs   Training Accuracy    Validation Accuracy   Training Loss        Validation Loss
model_1      "Dense_1, Flatten",               1                  0.7812333106994629   0.8391000032424927    0.6662909388542175   0.493167906999588
model_2      "Dense_1, Flatten",               1                  0.7467833161354065   0.8159000277519226    0.7057321667671204   0.529076099395752
model_3      "Conv2D, MaxPooling2D, Flatten"   1                  0.8098833560943604   0.8377000093460083    0.5281296372413635   0.4474002420902252

 
License:


This code is licensed under the MIT License.


Contact:


If you have any questions or comments about this code, 
please feel free to contact me at nawazmdsakib@gmail.com .

