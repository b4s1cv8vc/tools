#tools
=====

some tools I wrote for better life

#*@LibsvmToARFF.py*

A tool that can convert file.libsvm to file.arff. Attention, this tool can't support sparse libsvm file format or sparse arff format.

Example (in Windows):

####LibsvmToARFF.py filename.libsvm configname.txt filename.arff 

The filename.libsvm and configname.txt are files you should prepare in advance, filename.arff is the result file of executing the last command line.
Here is an example of the configname.txt: 


BANK

feature1

feature2

feature3

feature4

feature5

feature6

feature7

feature8

feature9

feature10


The "BANK" is the relation of the arff data, and the rest of lines are the attributes of the arff data.

