import sys
import difflib
import csv

#USAGE find_diff_param outfile_fromstep1 outputfile logfile

out1_file=sys.argv[1]
out2_file=sys.argv[2]
logfile=sys.argv[3]

cases=[]
count=0

with open(out1_file, 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    logfile= open(logfile, "w")
    ofile  = open(out2_file, "w")
    writer = csv.writer(ofile, delimiter='\t')
    first=1
    for row in reader:
        if first:
            #print "Consensus Allele is:",  row[0]
            logmessage = "Consensus Allele is:"+row[0]+"\n"
            logfile.write(logmessage)
            first_allele=row[0]
            first=0
        #print "Comparison:",  first_allele,  row[0]
        logmessage="Comparison:"+first_allele+" "+row[0]+"\n"
        logfile.write(logmessage)
        cases+=[(first_allele,  row[0])]
#print "Cases: ",  cases

for a,b in cases:     
    #print('Transformation to apply: {} => {}'.format(a,b))
    logmessage='Transformation to apply: {} => {}'.format(a,b)+"\n"
    logfile.write(logmessage)
    for i,s in enumerate(difflib.ndiff(a, b)):
        if s[0]==' ': continue
        elif s[0]=='-':
            #print(u'Delete "{}" from position {}'.format(s[-1],i))
            logmessage=u'Delete "{}" from position {}'.format(s[-1],i)+"\n"
            logfile.write(logmessage)
            count+=1
        elif s[0]=='+':
            #print(u'Add "{}" to position {}'.format(s[-1],i)) 
            logmessage=u'Add "{}" to position {}'.format(s[-1],i)+"\n"
            logfile.write(logmessage)
            count+=1
    if len(a) == len(b):
        count_diffs = 0
    for c1, c2 in zip(a, b):
        if c1!=c2:
            #if count_diffs: return False
            count_diffs += 1
    #return True
    print "Number of different symbols: ",  a,  b,  count_diffs
    result=a+"\t"+b+"\t"+str(count_diffs)+"\n"
    
    #print"Total n. operations needed: ",  count,  "\n"
    logmessage="Number of mutations: "+a+" "+b+" "+str(count)+"\n"
    logfile.write(logmessage)
    print "Number of mutations: ",  logmessage
    
    ofile.write(result)
    count=0

f.close()
ofile.close()
logfile.close()
