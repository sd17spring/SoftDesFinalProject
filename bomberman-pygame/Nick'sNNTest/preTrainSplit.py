# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function

import argparse
import sys
import numpy as np

import tensorflow as tf
import os
import pandas as pd
from scipy.misc import imread
from sklearn.metrics import accuracy_score

def main():
    # Load datasets.
    training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename="walls.csv",
        target_dtype=np.int,
        features_dtype=np.int)


        # number of neurons in each layer
    input_num_units = 5*5
    hidden_num_units = 500
    output_num_units = 6

    seed = 128
    rng = np.random.RandomState(seed)

    # define placeholders
    x = tf.placeholder(tf.float32, [None, input_num_units])
    y = tf.placeholder(tf.float32, [None, output_num_units])

    # set remaining variables
    epochs = 5
    batch_size = 128
    learning_rate = 0.01

    ### define weights and biases of the neural network (refer this article if you don't understand the terminologies)

    weights = {
        'hidden': tf.Variable(tf.random_normal([input_num_units, hidden_num_units], seed=seed)),
        'output': tf.Variable(tf.random_normal([hidden_num_units, output_num_units], seed=seed))
    }

    biases = {
        'hidden': tf.Variable(tf.random_normal([hidden_num_units], seed=seed)),
        'output': tf.Variable(tf.random_normal([output_num_units], seed=seed))
    }

    hidden_layer = tf.add(tf.matmul(x, weights['hidden']), biases['hidden'])
    hidden_layer = tf.nn.relu(hidden_layer)

    output_layer = tf.matmul(hidden_layer, weights['output']) + biases['output']

    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(output_layer, y))

    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

    init = tf.initialize_all_variables()

    with tf.Session() as sess:
        # create initialized variables
        sess.run(init)

        ### for each epoch, do:
        ###   for each batch, do:
        ###     create pre-processed batch
        ###     run optimizer by feeding batch
        ###     find cost and reiterate to minimize

        for epoch in range(epochs):
            avg_cost = 0
            total_batch = int(train.shape[0]/batch_size)
            for i in range(total_batch):
                batch_x, batch_y = batch_creator(batch_size, train_x.shape[0], 'train')
                _, c = sess.run([optimizer, cost], feed_dict = {x: batch_x, y: batch_y})

                avg_cost += c / total_batch

            print "Epoch:", (epoch+1), "cost =", "{:.5f}".format(avg_cost)

        print "\nTraining complete!"


    # find predictions on val set
    pred_temp = tf.equal(tf.argmax(output_layer, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(pred_temp, "float"))
    print "Validation Accuracy:", accuracy.eval({x: val_x.reshape(-1, input_num_units), y: dense_to_one_hot(val_y)})

    predict = tf.argmax(output_layer, 1)
    pred = predict.eval({x: test_x.reshape(-1, input_num_units)})
        # Create the model
    num_feature = 25
    num_response = 6
    x = tf.placeholder(tf.float32, [None, num_feature])
    W = tf.Variable(tf.zeros([num_feature, num_response]), name='W')
    b = tf.Variable(tf.zeros([num_response]),name='b')
    tf.add_to_collection('vars',W)
    tf.add_to_collection('vars',b)
    y = tf.matmul(x, W) + b

    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, num_response])

    # Use tf.nn.softmax_cross_entropy_with_logits on the raw
    # outputs of 'y', and then average across the batch.
    # Use Gradient Descent to minize the loss
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    #Create saver and session
    saver = tf.train.Saver()
    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()

    # Train
    batch_xs, batch_ys = training_set.data, tf.one_hot(training_set.target,num_response)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys.eval()})
    saver.save(sess,'walls')
    print('training complete')

if __name__ == '__main__':
    main()