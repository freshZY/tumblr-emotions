import sys
import tensorflow as tf
from time import time
from image_model.im_model import download_pretrained_model
from image_model.im_model import fine_tune_model

if __name__ == '__main__':
    args = sys.argv[1:]
    num_steps = (int)(args.pop(0))

    if len(args) > 0:
        sys.stderr.write('Too many arguments given.\n')
    else:
        t0 = time()
        # Maybe download pre-trained model
        checkpoints_dir = 'image_model/pretrained_model'
        if not tf.gfile.Exists(checkpoints_dir):
            tf.gfile.MakeDirs(checkpoints_dir)
            url = 'http://download.tensorflow.org/models/inception_v1_2016_08_28.tar.gz'
            download_pretrained_model(url, checkpoints_dir)

        # Fine-tune model
        dataset_dir = 'data'
        checkpoints_dir = 'image_model/pretrained_model'
        train_dir = 'image_model/fine_tuned_model'
        fine_tune_model(dataset_dir, checkpoints_dir, train_dir, num_steps=num_steps)
        print('The training took: {0:.1f} mins'.format((time() - t0) / 60))