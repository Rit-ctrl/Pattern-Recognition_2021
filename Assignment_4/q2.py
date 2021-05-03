import svm,numpy as np,perceptron

x1=[2,-1,-1,0,1,-1,1,-1]
x2=[2,-3,2,-1,3,-2,-2,-1]

X=np.array(list(zip(x1,x2)))

Y_svm =np.array([1,-1,1,-1,1,-1,-1,1])
Y_perc=np.array([1,0,1,0,1,0,0,1])

perceptron.demo(X,Y_perc,learning_rate=0.01,plot_title="q2_a")
perceptron.demo(X,Y_perc,learning_rate=0.5,plot_title="q2_b")

svm.demo(X,Y_svm,plot_title="q2")