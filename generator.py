from sketch_rnn import Model

encoder_pth = 'encoderRNN_sel_0.579462_epoch_40000.pth'
decoder_pth = 'decoderRNN_sel_0.579462_epoch_40000.pth'

if __name__=='__main__':
    model = Model()
    model.load(encoder_pth, decoder_pth)

    for i in range(1, 1001):
        model.conditional_generation(i, name='', fpath='./outputs/')