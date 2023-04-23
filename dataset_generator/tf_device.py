import tensorflow as tf
print(tf.__version__)

physical_devices = tf.config.list_physical_devices('GPU')
print("Num GPUs:", len(physical_devices))

#tensorman +latest-gpu run python3 tf_device.py
 
#nvcc --version #check cuda version 