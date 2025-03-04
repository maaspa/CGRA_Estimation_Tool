import csv
import re

def export(infile, outfile):

    csv_content = []

    with open(infile) as f:
        reader = csv.reader(f)
    
        for row in reader:
            csv_content.append(row)

    out_string = ""

    for row in csv_content:
        # If the row contains the timestamp 
        match = re.match(r"(\d+)", row[0])
        if match :
            out_string += "T = {}\n".format(row[0])
            
        
        # If the row contains isntructions
        else:
            for instr in row:
                out_string += "{}\n".format(instr)

    out_string += "T = 0\n"
    with open(outfile, "w") as f:
        f.write(out_string)

