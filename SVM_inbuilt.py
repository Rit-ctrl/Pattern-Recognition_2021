#import numpy as np

from sklearn import svm 

X=[[3,1],[3,-1],[6,1],[6,-1],[1,0],[0,1],[0,-1],[-1,0]]
Y=[0,0,0,0,1,1,1,1]
classifier=svm.SVC(kernel='linear')
classifier.fit(X,Y)
# print(classifier.support_vectors_)
print(classifier.intercept_)
print(classifier.coef_)
