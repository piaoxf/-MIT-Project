import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from train_utils import batchify_data, run_epoch, train_model, Flatten
import utils_multiMNIST as U
path_to_data_dir = '../Datasets/'
use_mini_dataset = True

batch_size = 64
nb_classes = 10
nb_epoch = 50
num_classes = 10
img_rows, img_cols = 42, 28 # input image dimensions



class CNN(nn.Module):

    def __init__(self, input_dimension):
        super(CNN, self).__init__()
        
        # hidden layers
        self.con1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        # 32ch -> 64ch 3x3 kernel
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        
        # dropout
        self.dropout = nn.Dropout(p=0.5)

        # Flatten layer (input: (64, 5, 5) -> output: 1600) 
        self.flatten = Flatten()

        # fully connected layers
        
        self.linear = nn.Linear(64 * 10 * 7, 128)

        # first output layers 128 -> 10
        self.first_digit = nn.Linear(128, 10)
        self.second_digit = nn.Linear(128, 10)

    def forward(self, x):

        # conv1 -> relu -> maxpool
        x = F.relu(self.con1(x))
        x = self.pool(x)

        # conv2 -> relu -> maxpool
        x = F.relu(self.conv2(x))
        x = self.pool(x)

        # dropout
        x = self.dropout(x)

        # flatten
        x = self.flatten(x)
        x = F.relu(self.linear(x))

        # output
        out_first_digit = F.leaky_relu(self.first_digit(x))
        out_second_digit = F.leaky_relu(self.second_digit(x))

        return out_first_digit, out_second_digit

def main():
    X_train, y_train, X_test, y_test = U.get_data(path_to_data_dir, use_mini_dataset)

    # Split into train and dev
    dev_split_index = int(9 * len(X_train) / 10)
    X_dev = X_train[dev_split_index:]
    y_dev = [y_train[0][dev_split_index:], y_train[1][dev_split_index:]]
    X_train = X_train[:dev_split_index]
    y_train = [y_train[0][:dev_split_index], y_train[1][:dev_split_index]]

    permutation = np.array([i for i in range(len(X_train))])
    np.random.shuffle(permutation)
    X_train = [X_train[i] for i in permutation]
    y_train = [[y_train[0][i] for i in permutation], [y_train[1][i] for i in permutation]]

    # Split dataset into batches
    train_batches = batchify_data(X_train, y_train, batch_size)
    dev_batches = batchify_data(X_dev, y_dev, batch_size)
    test_batches = batchify_data(X_test, y_test, batch_size)

    # Load model
    input_dimension = img_rows * img_cols
    model = CNN(input_dimension) # TODO add proper layers to CNN class above

    # Train
    train_model(train_batches, dev_batches, model)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)  # モデルをGPUへ送る
    ## Evaluate the model on test data
    loss, acc = run_epoch(test_batches, model.eval(), None, device)
    print('Test loss1: {:.6f}  accuracy1: {:.6f}  loss2: {:.6f}   accuracy2: {:.6f}'.format(loss[0], acc[0], loss[1], acc[1]))

if __name__ == '__main__':
    # Specify seed for deterministic behavior, then shuffle. Do not change seed for official submissions to edx
    np.random.seed(12321)  # for reproducibility
    torch.manual_seed(12321)  # for reproducibility
    main()
