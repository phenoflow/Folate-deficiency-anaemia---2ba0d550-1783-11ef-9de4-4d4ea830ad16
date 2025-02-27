# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"D012.00","system":"readv2"},{"code":"24870","system":"readv2"},{"code":"22715","system":"readv2"},{"code":"98709","system":"readv2"},{"code":"42117","system":"readv2"},{"code":"4080","system":"readv2"},{"code":"36634","system":"readv2"},{"code":"56114","system":"readv2"},{"code":"55481","system":"readv2"},{"code":"37082","system":"readv2"},{"code":"53783","system":"readv2"},{"code":"D52","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('folate-deficiency-anaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["deficiency---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["deficiency---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["deficiency---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
