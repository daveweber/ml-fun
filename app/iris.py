import numpy

from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()
test_index = [0, 50, 100]

# training data
train_target = numpy.delete(iris.target, test_index)
train_data = numpy.delete(iris.data, test_index, axis=0)

# testing data
test_target = iris.target[test_index]
test_data = iris.data[test_index]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

if __name__ == '__main__':
    print iris.target_names
    print iris.feature_names
    print iris.data[0]

    print test_target
    print clf.predict(test_data)