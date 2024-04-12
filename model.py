
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Create an image data generator object
datagen = ImageDataGenerator(rescale=1./255)  # normalize pixel values

# Define the directory containing your images
test_image_dir = r'C:\Users\cefb8t\Documents\Code\My Trials\AI ML\dataset\dataset\test'

# Load images from the directory
train_images = datagen.flow_from_directory(
    test_image_dir,
    target_size=(224, 224),  # resize images to the size expected by your model
    class_mode='binary',  # for binary classification
    batch_size=32  # number of images to load at each iteration
)

# Define the directory containing your test images
test_image_dir = r'C:\Users\cefb8t\Documents\Code\My Trials\AI ML\dataset\dataset\train_validate'

# Load test images from the directory
test_data = datagen.flow_from_directory(
    test_image_dir,
    target_size=(224, 224),  # resize images to the size expected by your model
    class_mode='binary',  # for binary classification
    batch_size=32  # number of images to load at each iteration
)



# Load the pre-trained MobileNetV2 model, excluding the top layer
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model
base_model.trainable = False

# Add a new top layer
x = Flatten()(base_model.output)
output = Dense(1, activation='sigmoid')(x)

# Create a new model
model = Model(inputs=base_model.input, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Assuming train_images and train_labels are your training data and labels
model.fit(train_images, epochs=10)

# Assuming test_images and test_labels are your test data and labels
test_loss, test_acc = model.evaluate(test_data)



# Define the path to your image
image_path = r"C:\Users\cefb8t\Documents\Code\My Trials\AI ML\dataset\dataset\new images\download.jpg"

# Load the image
img = load_img(image_path, target_size=(224, 224))  # resize the image to the size expected by your model

# Convert the image to an array
img_array = img_to_array(img)

# Normalize the image
img_array = img_array / 255

# Expand dimensions to create a batch of 1 image
img_batch = np.expand_dims(img_array, axis=0)

# Use the image batch as your new_images
new_images = img_batch

# Assuming new_images is your new data
# Make a prediction
predictions = model.predict(new_images)

# Get the index of the maximum prediction
pred_index = np.argmax(predictions)

# Define the class names
class_names = ['Mask', 'No Mask']

# Map the prediction index to the class name
pred_class = class_names[pred_index]

# Print the prediction
print("This image most likely is: ", pred_class)