"""MI-FGSM method adapted from the 2023 research notebook MI-FGSM.ipynb.

Historical notebook: https://colab.research.google.com/drive/1Xw75zdLYlw59gdu-3QNy4rH_TzgzFX1A

Preserves the archived notebook's six iterations, epsilon=0.01,
momentum decay=1.2, the newly predicted label every iteration,
gradient computed at ORIGINAL image rather than the evolving input,
and a global L1 norm of the first image's gradient.

These details reflect the archived code. Reported measurements are documented
separately in docs/FINAL_PAPER_RESULTS.md.
The original 'cat-2.JPEG' input is not in this repository.
"""
import tensorflow as tf


def momentum_iterative_fgsm(model, image, epsilon=0.01, steps=6, decay=1.2):
    adv = tf.identity(image)
    momentum = tf.zeros_like(image[0])
    alpha = epsilon / steps
    for _ in range(steps):
        current_prediction = model(adv, training=False)
        label_idx = tf.argmax(current_prediction, axis=-1, output_type=tf.int32)
        label = tf.one_hot(label_idx, depth=tf.shape(current_prediction)[-1])
        # Historical notebook differentiates the *original* image, not adv.
        with tf.GradientTape() as tape:
            tape.watch(image)
            pred = model(image, training=False)
            loss = tf.keras.losses.categorical_crossentropy(label, pred)
        gradient = tape.gradient(loss, image)[0]
        # The original notebook computed a single global L1 denominator.
        norm = tf.norm(gradient, ord=1)
        momentum = decay * momentum + gradient / norm
        adv = tf.clip_by_value(adv + alpha * tf.sign(momentum), -1.0, 1.0)
    return adv
