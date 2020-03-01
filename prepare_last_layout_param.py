import sys
import difflib
import csv

#USAGE: python prepare_last_layout_param output2.csv data_file output3.csv

out2=sys.argv[1]
data=sys.argv[2]
out3=sys.argv[3]

with open(data, 'r') as f1_input:
    reader1 = csv.reader(f1_input, dialect='excel', delimiter='\t')
    with open(out2, 'r') as f2_input:    
        reader2 = csv.reader(f2_input, dialect='excel', delimiter='\t')
        ofile  = open(out3, "w")
        writer = csv.writer(ofile, delimiter='\t')
        for line in reader1:
            seq2=line[1]
            strain=line[0]
            print"seq2=%s strain=%s" % (seq2, strain)
            for row in reader2:
                top=row[0]
                seq1=row[1]
                dist=row[2]
                print"top=%s seq1=%s dist=%s" % (top, seq1, dist)
                if(seq1==seq2):
                    print top, strain, dist
                    result=top+"\t"+strain+"\t"+dist+"\n"
                    ofile.write(result)
            f2_input.seek(0)
f1_input.close()
f2_input.close()
ofile.close()

