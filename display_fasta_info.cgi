#!/usr/local/bin/python3
import jinja2

templateLoader = jinja2.FileSystemLoader( searchpath="./templates" )

   # This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('unit04.html')


header_ID=[]
seq_len=[]
rest_header=[]

count=0
count_len=0
with open("e_coli_k12_dh10b.faa") as f:
    next(f)
    for line in f:
        
        if '>' in line:
            seq_len.append(count_len)
            temp = line.split('|')
            rest_header.append(temp[4])
            header_ID.append(line[1:(len(line)-len(temp[4]))])
            count_len = 0
            count+=1
            if count==21:
                break
    
        else:
            count_len+=len(line.strip())
    seq_len=seq_len[1:]        

print("Content-Type: text/html\n\n")
print(template.render(out = list(zip(header_ID, seq_len, rest_header))))

#output
#http://bfx3.aap.jhu.edu/skushwa2/unit04/display_fasta_info.cgi