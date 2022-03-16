from distutils.command.build import build
from imghdr import tests
import build_decisionTree as DT

import splitter as SP
import csv
import easygui
import random

def findAppropriateNode(node ,data):
    if node.dim == 0:
        return node.data[0][0]
    if float(data[node.dim])<float(node.val):
        return findAppropriateNode(node.leftChild, data)
    else:
        return findAppropriateNode(node.rightChild, data)

def testDecisionTree(root, testset):
 
    r_ans, tot_test= 0, 0

    for row in testset:
        cls= findAppropriateNode(root, row)
        print([row[0],  cls,  cls == row[0]])
        
        if cls == row[0]:
            r_ans+=1
        tot_test+=1
    ac = (r_ans/tot_test)*100

    msg='Accuracy: '+str(ac)+'%\n'+'Sample testset size: '+str(tot_test)
    
    print(msg)
   

'''def printTree(Node,space):

    if Node == None: 
        return

    space += 1
    print('')
    for i in range(space):
        print(end=' ')

    for i in range(len(Node.data[0])): 
        printTree(Node.dim,Node.val)
'''
    

def printTree(node, depth):
    if node.leftChild!=None:
        printTree(node.leftChild, depth+1)
    if node.rightChild!=None:
        printTree(node.rightChild, depth+1)
    for i in range(depth): print(end='\t')
    print(node.dim, ',',node.val)

def seperateDataset(dataset):
    testset,trainSet=[],[]
    for row in dataset:
        if random.random()>0.8:
            testset.append(row)
        else: trainSet.append(row)
    return trainSet, testset


file = open('wine.csv')
csvreader = csv.reader(file)
dataset = []
for row in csvreader:
    dataset.append(row)

trainSet, testset= seperateDataset(dataset)
n_class = 3
root = DT.build_decision_tree(trainSet, n_class)
printTree(root,0)
testDecisionTree(root, testset)
file.close()

