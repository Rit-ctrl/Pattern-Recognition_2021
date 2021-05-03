import svm,numpy as np

x1=[0,0,1,1]
x2=[0,1,0,1]

X=np.array(list(zip(x1,x2)))

Y_svm=np.array([1,1,1,-1])

svm.demo(X,Y_svm,plot_title="q1")