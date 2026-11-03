"""Vanilla FGSM method described in the 2023–2024 FGSM research paper.

A separate original FGSM notebook was not found in the STC 2023 archive.
This is a minimal transcription of the paper's one-step gradient-sign method,
not a recovered original implementation.

Input images must already be preprocessed to the archived ResNet50V2 [-1, 1]
range. This module does not supply input images or run experiments.
"""
import tensorflow as tf


def fgsm(model, image, label_index, epsilon):
    """Return a one-step untargeted FGSM perturbation of a preprocessed image."""
    predictions = model(image, training=False)
    label = tf.one_hot(
        tf.reshape(tf.cast(label_index, tf.int32), [-1]),
        depth=tf.shape(predictions)[-1],
    )
    with tf.GradientTape() as tape:
        tape.watch(image)
        pred = model(image, training=False)
        loss = tf.keras.losses.categorical_crossentropy(label, pred)
    signed_gradient = tf.sign(tape.gradient(loss, image))
    return tf.clip_by_value(image + epsilon * signed_gradient, -1.0, 1.0)
