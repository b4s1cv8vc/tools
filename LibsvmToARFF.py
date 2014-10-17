# -*- coding: utf-8 -*-
 # #Transport file.libsvm to file.arff in weka,
#Attention: only processed the arff file which attributes are numerical format.
#暂不支持 sparse files
import sys
def ls_to_arff(datafile, configfile, arfffile):
    #print datafile
    #print configfile
    #print arfffile
    with open(datafile, 'r') as df, open(configfile, 'r') as cf, open(arfffile, 'w') as af:
        cflist = cf.readlines()
        cflist = [x.replace('\n','') for x in cflist]
        new_cflist = ['@ATTRIBUTE ' + x + ' NUMERIC'   for x in cflist]
        #对 relation 要单独处理
        new_cflist[0] = new_cflist[0].replace('ATTRIBUTE', 'RELATION')
        new_cflist[0] = new_cflist[0].replace('NUMERIC','')

        #增加 class NUMERIC， libsvm只支持numeric格式的class，所以，此处默认arff格式class为NUMERIC
        new_cflist.append('@ATTRIBUTE class NUMERIC')
        new_cflist.append('@DATA')
        print new_cflist
#        print new_cflist

        for each_item in new_cflist:
            af.write(each_item + '\n')

        for each_line in df:
            tmp_data = each_line.split(' ') #空格分开
            tmp_data.pop() #为了把'\n' 去掉
            tmp_class = tmp_data[0]
            afline = '' #可对啊 这样初始化

            del tmp_data[0] #.del(0) #删除 calss value
            for ea in tmp_data:
                #print ea
                tmp = ea.split(':')
              #  print tmp
                try:

                    afline += tmp[1]
                    afline += ', '
                except:
                    pass
            afline += tmp_class
            af.write(afline + '\n')
    af.close()

#以下是读入参数 并调用函数ls_to_arff
#args = str(sys.argv)
print sys.argv
#print args
print len(sys.argv)
datafile = sys.argv[1]
configfile = sys.argv[2]
arfffile = sys.argv[3]
print datafile
print configfile
print arfffile
ls_to_arff(datafile, configfile, arfffile)
