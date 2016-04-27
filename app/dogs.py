import numpy
import matplotlib.pyplot as plot

greyhounds = 500
labs = 500

grey_height = 28 + 4 * numpy.random.randn(greyhounds)
lab_height = 24 + 4 * numpy.random.randn(labs)

plot.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
plot.show()