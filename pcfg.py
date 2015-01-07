# -*- coding: UTF-8 -*-
from collections import Counter

'''
example.txt store the training set, e.g.
(S(NP(DT The)(NN boy))(VP(VP(VBD saw)(NP(DT a)(NN girl)))(PP(IN with)(NP(DT a)(NN telescope)))))
(S(NP(DT The)(NN girl))(VP(VBD saw)(NP(NP(DT a)(NN boy))(PP(IN with)(NP(DT a)(NN telescope))))))

the result(dictionary) store the result of pcfg: each pattern and its probability
'''


standpattern = [] #save the standard pattern
pattern = []
one_two = 0 # ((
two_three = 0 # ((
one_blank = 0
blankindex = 0
with open('example.txt', 'r') as infile, open('outpattern.txt', 'w') as outfile:
    for each_sec in infile.readlines():
       # outfile.write("This sentence's pattern" + '\n')
        length = len(each_sec)
        for i in range(length):
            tmpspn = []


            if each_sec[i:i+1] == '(':
                nexti = i + 1
                cnt = 1
                one_two = 1 #( 后cnt=1，开始找起始元素
                one_begin = i+1 #起始元素起始位置
                for _ in range(length)[nexti:]:
                    if each_sec[_:_+1] == '(':
                        cnt += 1
                        if cnt == 2 and one_two == 1:
                            one_end = _ - 1 #起始元素结束位置
                            tmpspn.append(each_sec[one_begin:one_end+1])
                            one_two = 0
                        if cnt == 2 and one_two == 0:
                            two_three = 1
                            two_begin = _ + 1
                        if cnt == 3 and two_three == 1:
                            two_three = 0
                            two_end = _ - 1
                            tmpspn.append(each_sec[two_begin:two_end+1])
                    elif each_sec[_:_+1] == ')':
                        cnt -= 1

                    elif each_sec[_:_+1] == ' ':
                        if one_two == 1:
                            one_blank = 1
                            blankindex = _+1
                            one_two = 0
                            tmpspn.append(each_sec[one_begin:_])
                        if two_three == 1:
                            two_three = 0
                            tmpspn.append(each_sec[two_begin:_])

                    if cnt == 0:
                        if one_blank == 1:
                            one_blank = 0
                            tmpspn.append(each_sec[blankindex:_])
                        pattern.append(each_sec[i+1:_])
                        #outfile.write(each_sec[i+1:_] + '\n')
                        outfile.write(str(tmpspn) + '\n')
                        standpattern.append(tmpspn)
                        break
                #end for


#for _ in pattern:
 #   print _
for _ in standpattern:
    print _

print len(standpattern)

with open('model.file', 'w') as outfile:
    for _ in standpattern:
        for tmp in _[0:len(_)-1]:
            outfile.write(tmp + '#')
       # for i in range(len(_)-1):
       #     outfile.write(_[i:i+1] + '#')
        for tmp in _[len(_)-1:]:
            outfile.write(tmp + '\n')



tmplist = [''.join(_[0:1]) for _ in standpattern]
dicsum = Counter(tmplist)
print dicsum

tmplist2 = [''.join(_) for _ in standpattern]
diceach = Counter(tmplist2)
print diceach

result = {} #save the pattern and its probability
for eck, ecv in zip(diceach.keys(), diceach.values()):
    for smk, smv in zip(dicsum.keys(), dicsum.values()):
        if eck[0:len(smk)] == smk:
            ecv = float(ecv)/float(smv)
            result[eck] = ecv

print result



