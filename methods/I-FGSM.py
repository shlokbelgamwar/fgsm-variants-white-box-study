"""I-FGSM method adapted from the 2023 research notebook I-FGSM.ipynb.

Historical notebook: https://colab.research.google.com/drive/1ujiHNES0NChZwqZiic1SD2dWp8hXMese

Preserves the archived experiment's six iterations, epsilon=0.005,
alpha=epsilon/steps, CURRENT predicted label each iteration, and clipping to
[-1, 1]. This historical behavior must not be described as a corrected,
standardized PGD-style attack. No new results are included.

The notebook's original 'cat2.jpg' input is not in this repository.
"""
import tensorflow as tf


def iterative_fgsm(model, image, epsilon=0.005, steps=6):
    adv = tf.identity(image)
    alpha = epsilon / steps
    for _ in range(steps):
        current_prediction = model(adv, training=False)
        current_index = tf.argmax(current_prediction, axis=-1, output_type=tf.int32)
        current_label = tf.one_hot(current_index, depth=tf.shape(current_prediction)[-1])
        with tf.GradientTape() as tape:
            tape.watch(adv)
            pred = model(adv, training=False)
            loss = tf.keras.losses.categorical_crossentropy(current_label, pred)
        gradient = tape.gradient(loss, adv)
        adv = tf.clip_by_value(adv + alpha * tf.sign(gradient), -1.0, 1.0)
    return adv
