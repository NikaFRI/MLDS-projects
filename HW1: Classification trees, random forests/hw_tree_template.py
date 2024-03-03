import numpy as np
from sklearn.datasets import load_iris

# dummy dataset
iris = load_iris()
a = iris['data'][45:55]
b = iris['target'][45:55]
mydata = np.c_[a, b]


# TODO funkcija za določanje thresholda, z gini impurity
def gini_impurity(X, y):  

def all_columns(X, rand):
    return range(X.shape[1])


def random_sqrt_columns(X, rand):
    c = ... # select random columns
    return c


class Tree:

    def __init__(self, rand=None,
                 get_candidate_columns=all_columns,
                 min_samples=2):
        self.rand = rand  # for replicability
        self.get_candidate_columns = get_candidate_columns  # needed for random forests
        self.min_samples = min_samples

    def build(self, X, y):
        return TreeNode(...) # build a tree out of these nodes


class TreeNode:

    def __init__(self, threshold):    # rand component here?
        self.threshold = threshold    # a je to treba tukej
        self.left
        self.right

    # kje se določi threshold?
    
    def predict(self, X):
        # tukej se razdelijo data instances glede na i-th column value v levo in desno
        # vrne se pa ?
        return np.ones(len(X))  # dummy output


class RandomForest:

    def __init__(self, rand=None, n=50):
        self.n = n
        self.rand = rand
        self.rftree = Tree(...)  # initialize the tree properly

    def build(self, X, y):
        # ...
        return RFModel(...)


# class RFModel:

#     def __init__(self, ...):
#         # ...

#     def predict(self, X):
#         # ...
#         return predictions

#     def importance(self):
#         imps = np.zeros(self.X.shape[1])
#         # ...
#         return imps


if __name__ == "__main__":
    # learn, test, legend = tki()
    #print("full", hw_tree_full(learn, test))
    #print("random forests", hw_randomforests(learn, test))
    print('hello')
    print(mydata)
