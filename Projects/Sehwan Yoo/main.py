# %%
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

# %%
path = './dataset/' 

train = pd.read_csv(path + 'sign_mnist_train.csv')
test =  pd.read_csv(path + 'sign_mnist_test.csv')


print(len(train))

# %%

plt.imshow(train.iloc[:, 1:], cmap='gray')
plt.colorbar()
plt.show() 
print(train.iloc[:, 1:])

# print(train.head())
# print('----------------------')
# print(test.head())
# print('----------------------')
# print(len(train), '  ', len(test))


# %% 
train_X = train.iloc[:, 1:].values
train_Y = train.iloc[:, 0].values

test_X = test.iloc[:, 1:].values
test_Y = test.iloc[:, 0].values

print('Before')
print(train_X.shape)
print(train_Y.shape)

train_X = train_X.reshape(-1, 28, 28) 
# test_Y = test_Y.reshape(-1, 28, 28, 1)
test_X = test_X.reshape(-1, 28, 28)

print('After') 
print(train_X.shape)
print(test_X.shape)

# %% 
plt.imshow(train_X[0], cmap='gray')
plt.colorbar()
plt.show() 
print(train_Y[0])


# %%

train_X = train_X / 255.0 
test_X = test_X / 255.0 

print(train_X)
print(test_X)

# %% 
# One-hot 

train_X = tf.keras.utils.to_categorical(train_Y, num_classes=26)
test_X = tf.keras.utils.to_categorical(test_Y, num_classes=26)


print(train_X)
print(test_X)


# %% 

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), 
    tf.keras.layers.Dense(units=128, activation='relu'),
    tf.keras.layers.Dense(units=26, activation='softmax')
])


model.compile(optimizer=tf.keras.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()


# %%

print(train_X.shape)
print(train_Y.shape)

history = model.fit(train_X, train_Y, epochs=25, validation_split=0.25)


# %%

import matplotlib.pyplot as plt 

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], 'b-', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')

plt.xlabel('Epoch')
plt.legend() 

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], 'g-', label='accuracy')
plt.plot(history.history['val_accuracy'], 'k--', label='val_accuracy')
plt.xlabel('Epoch')
plt.ylim(0.7, 1)
plt.legend() 

plt.show()


# %% 
# ------------------------------------------------------------------
# CNN 처리

train_X = train.iloc[:, 1:].values
train_Y = train.iloc[:, 0].values

test_X = test.iloc[:, 1:].values
test_Y = test.iloc[:, 0].values

print('Before')
print(train_X.shape)
print(train_Y.shape)

train_X = train_X.reshape(-1, 28, 28, 1) 
test_X = test_X.reshape(-1, 28, 28, 1)

print('After') 
print(train_X.shape)
print(test_X.shape)


# %%
import matplotlib.pyplot as plt 

plt.figure(figsize=(10, 10)) 

for c in range(16):
    plt.subplot(4, 4, c+1)
    plt.imshow(train_X[c].reshape(28, 28), cmap='gray')

plt.show() 

print(train_Y[:25])


# %% 

# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(input_shape=(28, 28, 1), kernel_size=(3, 3), filters=16),
#     tf.keras.layers.Conv2D(kernel_size=(3, 3), filters=32),
#     tf.keras.layers.Conv2D(kernel_size=(3, 3), filters=64),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(units=128, activation='relu'),
#     tf.keras.layers.Dense(units=26, activation='softmax')
# ])

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(input_shape=(28, 28, 1), kernel_size=(3, 3), filters=32),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(kernel_size=(3, 3), filters=32),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=512, activation='relu'),
    tf.keras.layers.Dense(units=26, activation='softmax')
])


model.compile(optimizer=tf.keras.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary() 

# %%
history = model.fit(train_X, train_Y, epochs=10, validation_split=0.25)


import matplotlib.pyplot as plt 

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], 'b-', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')

plt.xlabel('Epoch')
plt.legend() 

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], 'g-', label='accuracy')
plt.plot(history.history['val_accuracy'], 'k--', label='val_accuracy')
plt.xlabel('Epoch')
plt.ylim(0.7, 1)
plt.legend() 

plt.show()
