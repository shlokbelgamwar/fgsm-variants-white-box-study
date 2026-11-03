"""T-FGSM method transcribed from the 2023 research notebook T-FGSM.ipynb.

Historical notebook source: https://colab.research.google.com/drive/1aZ0KbOuC1hG-5A5lHyjW4tEPxs35Z9vA

The archived code used target ImageNet class index 281, corresponding to
'tabby' in Keras, and the update image - epsilon * sign(gradient).
This preserves those archived choices. Reported measurements are documented
separately in docs/FINAL_PAPER_RESULTS.md.

Input must be preprocessed with tf.keras.applications.resnet_v2.preprocess_input.
The original 'cat.jpg' input is not included in this repository.
"""
import tensorflow as tf


def targeted_fgsm(model, image, target_index=281, epsilon=0.005):
    predictions = model(image, training=False)
    target = tf.one_hot(
        tf.fill([tf.shape(image)[0]], tf.cast(target_index, tf.int32)),
        depth=tf.shape(predictions)[-1],
    )
    with tf.GradientTape() as tape:
        tape.watch(image)
        pred = model(image, training=False)
        loss = tf.keras.losses.categorical_crossentropy(target, pred)
    gradient = tape.gradient(loss, image)
    return tf.clip_by_value(image - epsilon * tf.sign(gradient), -1.0, 1.0)
