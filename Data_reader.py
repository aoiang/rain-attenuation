import tensorflow as tf
import numpy as np

def data_extracter(decode=True, feature_num = 90, file_name = './resource/ets.csv', data_size = 614):
    filename_queue = tf.train.string_input_producer([file_name])

    reader = tf.TextLineReader()
    key, value = reader.read(filename_queue)


    record_defaults = [['']] * feature_num
    col = tf.decode_csv(value, record_defaults=record_defaults)


    with tf.Session() as sess:
        # tf.initialize_all_variables().run()
        # Start populating the filename queue.
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        data = []
        for i in range(data_size):
            # example, label = sess.run([features, col[4]])
            feature = sess.run(col)
            data.append(feature)

    if decode:
        for i in range(len(data)):
            for j in range(len(data[i])):
                try:
                    data[i][j] = data[i][j].decode()
                except:
                    print('error position at ', i, j)
                    data[i][j] = ''

    return data


def data_formatting(data, type_to=float):
    for i in range(len(data)):
        for j in range(len(data[i])):
            try:
                data[i][j] = type_to(data[i][j])
            except:
                pass
    return data


def feature_extracter(data, feature_name=None, islabel=True, has_name=True):
    if feature_name is None:
        feature_name = []
    feature_col = []
    for i in range(len(data[0])):
        if data[0][i] in feature_name:
            feature_col.append(i)
    data = np.array(data)
    feature = []
    label = []
    for i in feature_col:
        if islabel and i == feature_col[-1]:
            if not has_name:
                label.append(list(data[:, i])[1:-1])
            else:
                label.append(list(data[:, i]))
            break
        if not has_name:
            feature.append(list(data[:, i])[1:-1])
        else:
            feature.append(list(data[:, i]))
    return feature, label







