# phekb, 2024.

import sys, csv, re

codes = [{"code":"84.1×","system":"icduncat"},{"code":"84.91","system":"icduncat"},{"code":"27295","system":"icduncat"},{"code":"27590","system":"icduncat"},{"code":"27591","system":"icduncat"},{"code":"27592","system":"icduncat"},{"code":"27598","system":"icduncat"},{"code":"27880","system":"icduncat"},{"code":"27781","system":"icduncat"},{"code":"27782","system":"icduncat"},{"code":"27888","system":"icduncat"},{"code":"27889","system":"icduncat"},{"code":"28800","system":"icduncat"},{"code":"28805","system":"icduncat"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peripheral-arterial-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peripheral-arterial-disease-amputation---icduncat-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peripheral-arterial-disease-amputation---icduncat-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peripheral-arterial-disease-amputation---icduncat-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
