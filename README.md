# Pytorch-Sketch-RNN
Fork from https://github.com/alexis-jacq/Pytorch-Sketch-RNN

A pytorch implementation of https://arxiv.org/abs/1704.03477

In order to draw other things than cats, you will find more drawing data here: https://github.com/googlecreativelab/quickdraw-dataset

Default hyperparameters for training has been found here: https://github.com/tensorflow/magenta/blob/master/magenta/models/sketch_rnn/README.md

## Trained Weight
```python
encoder_pth = 'encoderRNN_sel_0.579462_epoch_40000.pth'
decoder_pth = 'decoderRNN_sel_0.579462_epoch_40000.pth'

from sketch_rnn import Model
model = Model()
model.load(encoder_pth, decoder_pth)
```

## Generate Samples
create folder which name is outputs on root directory
```
$ python generator.py
```
