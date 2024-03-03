from sklearn.datasets import load_iris

iris = load_iris()
a = iris['data'][45:55]
b = iris['target'][45:55]

mydata = np.c_[a, b]
