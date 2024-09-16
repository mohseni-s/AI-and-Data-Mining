# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 19:46:49 2018

@author: hs
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 18:51:48 2018

@author: hs
"""

from textblob.classifiers import NaiveBayesClassifier
#from textblob import TextBlob
#train = [
#    ('It is good', 'positive'),
#    ('I feel good about it', 'positive'),
#    ('It is bad', 'negative'),
#    ('It is good', 'positive'),
#    ('It is bad', 'negative'),
#     ('I feel bad about it', 'negative'),
#     ('I feel it is not bad about', 'positive'),
#     ('I feel not good about', 'negative')
# ]
import csv
import codecs

#with codecs.open(file_name, "r",encoding='utf-8', errors='replace') as fdata:
    
train=[]
with  codecs.open(r"C:\Users\hs\Desktop\data mining-last exp\python1\trainall.csv", encoding="utf8", errors='replace') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
       
      train=train+[row]
#print(train)
csvFile.close()

test=[]
with  codecs.open(r"C:\Users\hs\Desktop\data mining-last exp\python1\testall.csv", encoding="utf8", errors='replace') as csvFile:
    reader1 = csv.reader(csvFile)
    for row1 in reader1:
       
      test=test+[row1]
#print(train)
csvFile.close()

NB = NaiveBayesClassifier(train)
print("Accuracy: {0}".format(NB.accuracy(test)))
#print(NB.classify('These Harry Potter movies really suck.'))  # 'positive'
#print(NB.classify('i will love the lakers.'))   # 'negative'
#print(NB.classify('I reallllllly hate Tom Cruise...'))
#print(NB.classify('Have to say, I hate Paris Hiltons behavior but I do think shes kinda cute..'))

unclassifydata=[]
with  codecs.open(r"C:\Users\hs\Desktop\data mining-last exp\python1\unclassifieddata1.csv", encoding="utf8", errors='replace') as csvFile3:
    reader3 = csv.reader(csvFile3)
    for row3 in reader3:
      # print(row3)
      # print(NB.classify('Have to say, I hate Paris Hiltons behavior but I do think shes kinda cute..'))
     #  print(NB.classify(str(row3)))
       unclassifydata=unclassifydata+[row3,NB.classify(str(row3))]
       #print(unclassifydata)
       # Open File
resultFile = open('1111.txt','w',encoding='utf8')


# Create Writer Object
wr = csv.writer(resultFile,lineterminator='\r\n',delimiter='\t',skipinitialspace = 0
 ,quoting=csv.QUOTE_MINIMAL,dialect='excel')
# Write Data to File
for item in unclassifydata:
    resultFile.write("%s\n" % str(item))
resultFile.close()
