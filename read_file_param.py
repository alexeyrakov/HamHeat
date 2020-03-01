import sys
import csv
import operator
from csvsort import csvsort

#USAGE: python read_file.py temp_out1_file test_out_file output1_file 

DataValue = "   0"
max_freq=9999999
pos=0
idx=1

tmp_out_file=sys.argv[1]
test_out_file=sys.argv[2]
output1_file=sys.argv[3]

with open(tmp_out_file, 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    ofile  = open(test_out_file, "w")
    writer = csv.writer(ofile, delimiter='\t')
    for row in reader:
        chars = set('-')
        if all((c in chars) for c in row[0]):
            row[1]=DataValue
        writer.writerow(row)
        #print "After substitution ",  row
f.close()
ofile.close()

with open(test_out_file, 'r') as f1:
    ofile1  = open(output1_file, 'w')
    writer1 = csv.writer(ofile1, delimiter='\t')
    #reader1 = csv.reader(open("ttest.csv"), delimiter='\t')
    reader1 = csv.reader(f1, dialect='excel', delimiter='\t')
    for row in reader1:
        sortedlist = sorted(reader1,  key=lambda row: row[1],  reverse=True)
        print "Sorted List: ",  sortedlist
        print "Max value:",  max(sortedlist,key=lambda item:item[1])[1]
    for element in sortedlist:
        if int(element[1]) < int(max_freq) :
            max_freq=element[1]
            pos += 1
        print ("%s\t%s" % (element[0],  pos))
        string=element[0]+"\t"+str(pos)+"\n"
        print("string: %s" % (string))
        ofile1.write(string)
ofile1.close()
    
