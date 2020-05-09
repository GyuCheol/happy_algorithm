from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import os
import torch
import torchvision
import torchvision.transforms as transforms
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import argparse
import csv
import os.path
import torch.nn.parallel
import torch.utils.data as data
import torchvision.datasets as datasets
import torchvision.models as models
from PIL import Image

from multiprocessing import Process, freeze_support

# 경로? path
# 상대 경로를 나타내는 keyword
# ./  : 지금 내 현재 경로
# ../ : 내 상위 폴더

class TrainImageFolder(datasets.ImageFolder):
    
    def __getitem__(self, index):
            filename = self.imgs[index]

            if 'cat.' in filename[0]: label = 0
            else : label = 1

            return super(TrainImageFolder, self).__getitem__(index)[0],  label

class TestImageFolder(datasets.ImageFolder):
    
    def __getitem__(self, index):
        filename = self.imgs[index]

        files = filename[0].split('\\')

        real_idx =  int(files[len(files) - 1].split('.')[0])
        return super(TestImageFolder, self).__getitem__(index)[0], real_idx

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(3,32,5)
        self.pool = nn.MaxPool2d(2,2)
        self.dout = nn.Dropout(0.2)
        self.conv2 = nn.Conv2d(32,64,3)
        self.conv3 = nn.Conv2d(64,128,5)
        self.conv4 = nn.Conv2d(128,256,5)
        
        self.fc1 = nn.Linear(21*21*256, 512)
        self.fc2 = nn.Linear(512, 128)
        self.fc3 = nn.Linear(128, 2)
    
    def forward(self,x):
        x = self.conv1(x)
        x = self.dout(x)
        x = self.pool(F.relu(x))
        x = self.conv2(x)
        x = self.dout(x)
        x = self.pool(F.relu(x))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.dout(x)
        x = F.relu(self.conv4(x))
        x = x.view(x.size(0),-1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


if __name__ == '__main__':    
    torch.multiprocessing.freeze_support()

    traindir = os.path.join('./200508_cat_classification/dogs-vs-cats', 'train')#경로를 병합함 .
    testdir = os.path.join('./200508_cat_classification/dogs-vs-cats', 'test')
    
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    
    train_loader = data.DataLoader(
            TrainImageFolder(traindir,
                            transforms.Compose([
                                transforms.RandomResizedCrop(224),
                                transforms.RandomHorizontalFlip(),
                                transforms.ToTensor(),
                                normalize,
                            ])),
                            batch_size=4,
                            shuffle=True,
                            num_workers=4,
                            pin_memory=True)
    
    test_loader = data.DataLoader(
        TestImageFolder(testdir,
                        transforms.Compose([
                            transforms.Resize(256),
                            transforms.CenterCrop(224),
                            transforms.ToTensor(),
                            normalize,
                        ])),
                        batch_size=1,
                        shuffle=False,
                        num_workers=1,
                        pin_memory=False)

    net = Net()
    
    if torch.cuda.device_count() > 1:
        print("Let's use", torch.cuda.device_count(), "GPUs!")

    net = nn.DataParallel(net)
    
    if torch.cuda.is_available():
        net.cuda()
    
    import torch.optim as optim
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr = 0.004)

    for epoch in range(45):
        running_loss = 0.0
        acc = 0.
        correct = 0
        for i, data in enumerate(train_loader, 0):
            inputs, labels = data
            inputs, labels = Variable(inputs.cuda()), Variable(labels.cuda())
            
            optimizer.zero_grad()
            outputs = net(inputs)
            #print(outputs)
            loss = criterion(outputs, labels)
                
            loss.backward()
            optimizer.step()
        
            running_loss += loss.data.item()
            
            prediction = torch.max(outputs.data,1)[1]
            
            correct += prediction.eq(labels.data.view_as(prediction)).cpu().sum()
                
            if i % 2000 == 1999:
                print('[%d, %5d] loss: %.6f acc : %.6f' % (epoch + 1, i+1, running_loss/2000, 100*correct/((i+1)*4)))
                running_loss = 0.0
                
    print('Finished Training')

