#Code from here:
#https://levelup.gitconnected.com/install-tensorflow-2-0-0-on-ubuntu-18-04-with-nvidia-gtx1650-gtx1660ti-9fd7a837d5fd

#Keras has a built in way to separate time steps" https://keras.io/examples/timeseries/timeseries_weather_forecasting/ 
#Extensive use of the keras documentation 

#For reshaping y: 
#https://stackoverflow.com/questions/54948059/keras-2d-dense-layer-for-output

#Help from here: https://stackoverflow.com/questions/40426502/is-there-a-way-to-suppress-the-messages-tensorflow-prints
#On suppressing annoying tf output!!
#These two lines suppress annoying tf output 

#Plotting help from here: https://stackabuse.com/matplotlib-plot-multiple-line-plots-same-and-different-scales/ 

#Getting numpy column help from here: https://stackoverflow.com/questions/4455076/how-do-i-access-the-ith-column-of-a-numpy-multidimensional-array 

#Pickle help here: https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/WorkingWithFiles.html 

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']  = '3'
#
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
from tensorflow.keras import datasets, layers, models
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import dataset_generator as dg 
config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9
gpu_devices = tf.config.experimental.list_physical_devices("GPU")
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)
# (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
# train_images, test_images = train_images / 255.0, test_images / 255.0
# class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship', 'truck']
# model = models.Sequential()
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.Flatten())
# model.add(layers.Dense(64, activation='relu'))
# model.add(layers.Dense(10))
# model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
# history = model.fit(train_images, train_labels,batch_size= 64, epochs=10,validation_data=(test_images, test_labels))
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)


#NOTES - You need to better define your saving/loading naming schema for a particular dataset. 

experiment_1 = {
    "model":{
        "model_type": "Sequential",
        #Don't include input, code will figure it out. 
        #Don't include output, code will figure it out. 
        "layers": 
            [
                {
                    "type": "LSTM",
                    "num_nodes": 31
                },
                {
                    "type": "Dropout",
                    "percent": 0.2,
                },
            ],
        "final_activation": "relu",
        "loss": "mse",
        #"loss_function": "mean_square_error",
        "optimizer": "adam",
        "batch_size": 32,
        "epochs": 4,
        "test_split": 0.1,
        "validation_split": 0.2,
        "use_multiprocessing": True,
        #"metrics": ["mse"]
        "metrics": ["mae", "mape", "mse"]

    }
}


def split_training_test(prepared_dataset, experiment_object):
    model_def = experiment_object["model"]
    if "test_split" in list(model_def.keys()):
        test_split = model_def["test_split"]
    else:
        test_split = 0.2
    random_state=None
    if "random_state" in list(model_def.keys()):
        random_state = random_state
    x_train, x_test, y_train, y_test, x_train_key, x_test_key, y_train_key, y_test_key = train_test_split(
        prepared_dataset["x"], prepared_dataset["y"], prepared_dataset["x_key"], prepared_dataset["y_key"],
        test_size=test_split,
        random_state=random_state
    )
    prepared_dataset["x_train"] = x_train
    prepared_dataset["x_test"] = x_test
    prepared_dataset["y_train"] = y_train
    prepared_dataset["y_test"] = y_test
    prepared_dataset["x_train_key"] = x_train_key
    prepared_dataset["x_test_key"] = x_test_key
    prepared_dataset["y_train_key"] = y_train_key
    prepared_dataset["y_test_key"] = y_test_key
    return prepared_dataset


def build_layer(model, layer_object):
    layer_type = layer_object["type"]
    #LSTM layer 
    if layer_type == "LSTM":
        if "num_nodes" in list(layer_object.keys()):
            num_nodes=layer_object["num_nodes"]
        else:
            num_nodes = 20 
        #Change is here!!! #MARKED 
        model.add(layers.LSTM(num_nodes))
    #Dropout Layer 
    if layer_type == "Dropout":
        if "percent" in list(layer_object.keys()):
            percent = layer_object["percent"]
        else:
            percent = 0.5
        model.add(layers.Dropout(percent))
    return model
    #Dense Layer 
    if layer_type == "Dense":
        activation = None
        use_bias = True
        if "num_nodes" in list(layer_object.keys()):
            num_nodes=layer_object["num_nodes"]
        else:
            num_nodes = 20 
        if "activation" in list(layer_object.keys()):
            activation = layer_object["activation"]
        if "use_bias" in list(layer_object.keys()):
            use_bias = layer_object["use_bias"]
        
        model.add(layers.Dense(num_nodes,
        activation=activation,
        use_bias=use_bias,
        ))
    return model

def return_base_model(model_type):
    if model_type == "Sequential":
        model = models.Sequential()
        return model 



def add_input_layer(model, prepared_dataset, experiment_object):
    x = prepared_dataset["x"]
    dims = (x.shape[1], x.shape[2])
    model.add(layers.Input(shape=dims))
    return model 

def add_output_layer(model, prepared_dataset, experiment_object):
    model_def = experiment_object["model"]
    activation = model_def["final_activation"]
    y = prepared_dataset["y"]
    #LATER - put dimension checking here  #MARKED
    dim = y.shape[1]
    #MARKED 
    model.add(layers.Dense(dim,
        activation=activation))
    return model 

def build_model(prepared_dataset, experiment_object):
    model_def = experiment_object["model"]
    model_type = model_def["model_type"]
    model = return_base_model(model_type)
    #Create input layer 
    model = add_input_layer(model, prepared_dataset, experiment_object)
    #Create defined layers
    layer_list = model_def["layers"]
    for layer in layer_list:
        model = build_layer(model, layer)
    #Create output layer
    model = add_output_layer(model, prepared_dataset, experiment_object)
    #Compile the model 
    model = compile_model(model, experiment_object)
    return model 

def compile_model(model, experiment_object):
    model_def = experiment_object["model"]
    optimizer = None
    loss = None
    metrics = None
    loss_weights = None
    weighted_metrics = None
    run_eagerly = True
    steps_per_execution=None
    jit_compile=None
    if "optimizer" in list(model_def.keys()):
        optimizer = model_def["optimizer"]
    if "loss" in list(model_def.keys()):
        loss = model_def["loss"]
    if "metrics" in list(model_def.keys()):
        metrics = model_def["metrics"]
    if "loss_weights" in list(model_def.keys()):
        loss_weights = model_def["loss_weights"]
    if "weighted_metrics" in list(model_def.keys()):
        weighted_metrics = model_def["weighted_metrics"]
    if "run_eagerly" in list(model_def.keys()):
        run_eagerly = model_def["run_eagerly"]
    if "steps_per_execution" in list(model_def.keys()):
        steps_per_execution = model_def["steps_per_execution"]
    if "jit_compile" in list(model_def.keys()):
        jit_compile = model_def["jit_compile"]
    
    model.compile(
        optimizer=optimizer,
        loss=loss,
        metrics=metrics,
        loss_weights=loss_weights,
        weighted_metrics=weighted_metrics,
        run_eagerly=run_eagerly,
        steps_per_execution=steps_per_execution,
        jit_compile=jit_compile
    )
    return model 


def fit_model(model, prepared_dataset, experiment_object):
    model_def = experiment_object["model"]
    if "x_train" in list(prepared_dataset.keys()):
        x_vect = prepared_dataset["x_train"]
        y_vect = prepared_dataset["y_train"]
    else:
        x_vect = prepared_dataset["x"]
        y_vect = prepared_dataset["y"]
    batch_size=None
    epochs=1
    verbose=True
    callbacks=None
    validation_split=0.0
    validation_data=None
    shuffle=True
    use_multiprocessing=False

    if "batch_size" in list(model_def.keys()):
        batch_size = model_def["batch_size"]
    if "epochs" in list(model_def.keys()):
        epochs = model_def["epochs"]
    if "verbose" in list(model_def.keys()):
        verbose = model_def["verbose"]
    if "callbacks" in list(model_def.keys()):
        callbacks = model_def["callbacks"]
    if "validation_split" in list(model_def.keys()):
        validation_split = model_def["validation_split"]
    if "validation_data" in list(model_def.keys()):
        validation_data = model_def["validation_data"]
    if "shuffle" in list(model_def.keys()):
        shuffle = model_def["shuffle"]
    if "use_multiprocessing" in list(model_def.keys()):
        use_multiprocessing = model_def["use_multiprocessing"]

    #Actually train it 
    history = model.fit(
        x_vect, 
        y_vect, 
        batch_size=batch_size, 
        epochs=epochs,
        verbose=verbose,
        callbacks=callbacks,
        validation_split=validation_split,
        validation_data=validation_data,
        shuffle=shuffle,
        use_multiprocessing=use_multiprocessing)
    return history




def evaluate_model(model, prepared_dataset, experiment_object):
    pass
    if "x_test" in list(prepared_dataset.keys()):
        x_vect = prepared_dataset["x_test"]
        y_vect = prepared_dataset["y_test"]
    else:
        x_vect = prepared_dataset["x"]
        y_vect = prepared_dataset["y"]

    final_metrics = model.evaluate(x=x_vect, y=y_vect)
    print("Final metrics", final_metrics)
    return final_metrics
    # Model.evaluate(
    #     x=None,
    #     y=None,
    #     batch_size=None,
    #     verbose="auto",
    #     sample_weight=None,
    #     steps=None,
    #     callbacks=None,
    #     max_queue_size=10,
    #     workers=1,
    #     use_multiprocessing=False,
    #     return_dict=False,
    #     **kwargs
    # )

def predict_values(model, prepared_dataset, experiment_object, x_key=None, prediction_key=None):
    values_to_predict = ["x", "x_train", "x_test"]
    suffix = "_predictions"

    if x_key == None:
        x_vals = prepared_dataset["x"]
    else:
        x_vals = prepared_dataset[x_key]
    predictions = model.predict(x_vals)
    if prediction_key == None:
        prediction_label = "predictions"
    else:
        prediction_label = prediction_key
    prepared_dataset[prediction_label] = predictions
    return prepared_dataset
    # Model.predict(
    #     x,
    #     batch_size=None,
    #     verbose="auto",
    #     steps=None,
    #     callbacks=None,
    #     max_queue_size=10,
    #     workers=1,
    #     use_multiprocessing=False,
    # )


def graph_predictions(prepared_dataset, pred_key=None, y_key=None):
    pass
    if pred_key == None:
        pred_index = "predictions"
    else:
        pred_index = pred_key
    if y_key == None:
        y_index = "y_key"
    else:
        y_index = y_key
    fig, ax = plt.subplots()
    ax.plot(prepared_dataset[y_index], prepared_dataset[pred_index][:, 0])
    plt.show()
    

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5, 6]
# y = [2, 4, 6, 5, 6, 8]
# y2 = [5, 3, 7, 8, 9, 6]

# fig, ax = plt.subplots()

# ax.plot(x, y)
# ax.plot(x, y2)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# line_1 = np.random.randint(low = 0, high = 50, size = 50)
# line_2 = np.random.randint(low = -15, high = 100, size = 50)

# fig, ax = plt.subplots()

# ax.plot(line_1, color = 'green', label = 'Line 1')
# ax.plot(line_2, color = 'red', label = 'Line 2')
# ax.legend(loc = 'upper left')
# plt.show()


def experiment_from_experiment_object(experiment_object):
    #Test for now 
    prepared_dataset = dg.return_test_dataset()
    prepared_dataset = split_training_test(prepared_dataset, experiment_object)
    #Change is here - uncomment 
    model = build_model(prepared_dataset, experiment_object)
    print(model.summary())
    history = fit_model(model, prepared_dataset, experiment_object)
    test_metrics = evaluate_model(model, prepared_dataset, experiment_object)
    prepared_dataset = predict_values(model, prepared_dataset, experiment_object)
    #Graph
    graph_predictions(prepared_dataset, pred_key=None, y_key=None)
    return history, test_metrics

history, test_metrics = experiment_from_experiment_object(experiment_1)
print(history.history)
print(test_metrics)

# x = prepared_dataset["x"]
# y = prepared_dataset["y"]
# print(x.shape)
# print(y.shape)


#https://keras.io/api/losses/regression_losses/#meansquarederror-class 
#model.compile(optimizer='sgd', loss=tf.keras.losses.MeanSquaredError())


# #https://towardsdatascience.com/choosing-the-right-hyperparameters-for-a-simple-lstm-using-keras-f8e9ed76f046 
# # Build the model
# print('Build model...')
# model = Sequential()
# model.add(LSTM(hidden_nodes, return_sequences=False, input_shape=(word_vec_length, char_vec_length)))
# model.add(Dropout(0.2))
# model.add(Dense(units=output_labels))
# model.add(Activation('softmax'))
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
# batch_size=1000
# model.fit(train_x, train_y, batch_size=batch_size, epochs=10, validation_data=(validate_x, validate_y))
# view raw






# EXPERIMENT
# Layers: (dict)
#     key with num layer index, 
#     nodes: number of nodes (value)
#     activation_function: activation function
#     type - LSTM 
# Optimization (Like adam)
# Initial LR
# Number of epochs?
# Early stopping
# Metrics (list)
# Model save path (do you need multiple? Maybe per number of epochs)
# Save values (model history) - what to save 
# Save path as well ...

#Tomorrow - start with figuring out your scaling
#Maybe small network just to check 
#Also loading in the dataset. 

#https://www.tensorflow.org/api_docs/python/tf/keras/losses


#https://www.tensorflow.org/api_docs/python/tf/keras/metrics

#TODO: Output Sequence:
#Look into: https://www.kaggle.com/code/kmkarakaya/lstm-output-types-return-sequences-state 

#TODO: 
#Split training and test set 

