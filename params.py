#import alphabets

# about data and net
#alphabet = alphabets.alphabet
keep_ratio = False # whether to keep ratio for image resize
manualSeed = 1234 # reproduce experiemnt
random_sample = True # whether to sample the dataset with random sampler
imgH = 64 # the height of the input image to network
imgW = 160 # the width of the input image to network
nh = 256 # size of the lstm hidden state
nc = 1
pretrained = '' # path to pretrained model (to continue training)
expr_dir = './ckpt' # where to store samples and models
dealwith_lossnan = False # whether to replace all nan/inf in gradients to zero

# hardware
cuda = True # enables cuda
multi_gpu = False # whether to use multi gpu
ngpu = 1 # number of GPUs to use. Do remember to set multi_gpu to True!
workers = 4 # number of data loading workers

# training process
displayInterval = 1 # interval to be print the train loss
valInterval = 1000 # interval to val the model loss and accuray
saveInterval = 5 # interval to save model
n_val_disp = 10 # number of samples to display when val the model

# finetune
nepoch = 200 # number of epochs to train for
batchSize = 32 # input batch size
lr = 0.0001 # learning rate for Critic, not used by adadealta
beta1 = 0.5 # beta1 for adam. default=0.5
adam = False # whether to use adam (default is rmsprop)
adadelta = False # whether to use adadelta (default is rmsprop)
