# phekb, 2024.

import sys, csv, re

codes = [{"code":"38.18","system":"icduncat"},{"code":"39.5","system":"icduncat"},{"code":"39.25","system":"icduncat"},{"code":"39.29","system":"icduncat"},{"code":"38.08","system":"icduncat"},{"code":"38.38","system":"icduncat"},{"code":"38.48","system":"icduncat"},{"code":" 39.49; 39.56","system":"icduncat"},{"code":"39.57","system":"icduncat"},{"code":"39.58","system":"icduncat"},{"code":"39.9","system":"icduncat"},{"code":"35302","system":"icduncat"},{"code":"35303","system":"icduncat"},{"code":"35304","system":"icduncat"},{"code":"35305","system":"icduncat"},{"code":"35306","system":"icduncat"},{"code":"35331","system":"icduncat"},{"code":"35351","system":"icduncat"},{"code":"35355","system":"icduncat"},{"code":"35361","system":"icduncat"},{"code":"35363","system":"icduncat"},{"code":"35371","system":"icduncat"},{"code":"35372","system":"icduncat"},{"code":"35381","system":"icduncat"},{"code":"35452","system":"icduncat"},{"code":"35454","system":"icduncat"},{"code":"35456","system":"icduncat"},{"code":"35459","system":"icduncat"},{"code":"35470","system":"icduncat"},{"code":"35472","system":"icduncat"},{"code":"35473","system":"icduncat"},{"code":"35474","system":"icduncat"},{"code":"35481","system":"icduncat"},{"code":"35482","system":"icduncat"},{"code":"35483","system":"icduncat"},{"code":"35485","system":"icduncat"},{"code":"35491","system":"icduncat"},{"code":"35492","system":"icduncat"},{"code":"35493","system":"icduncat"},{"code":"35495","system":"icduncat"},{"code":"35521","system":"icduncat"},{"code":"35533","system":"icduncat"},{"code":"35537","system":"icduncat"},{"code":"35538","system":"icduncat"},{"code":"35539","system":"icduncat"},{"code":"35540","system":"icduncat"},{"code":"35541","system":"icduncat"},{"code":"35546","system":"icduncat"},{"code":"35548","system":"icduncat"},{"code":"35549","system":"icduncat"},{"code":"35551","system":"icduncat"},{"code":"35556","system":"icduncat"},{"code":"35558","system":"icduncat"},{"code":"35563","system":"icduncat"},{"code":"35565","system":"icduncat"},{"code":"35566","system":"icduncat"},{"code":"35571","system":"icduncat"},{"code":"35582","system":"icduncat"},{"code":"35583","system":"icduncat"},{"code":"35585","system":"icduncat"},{"code":"35587","system":"icduncat"},{"code":"35621","system":"icduncat"},{"code":"35623","system":"icduncat"},{"code":"35637","system":"icduncat"},{"code":"35638","system":"icduncat"},{"code":"35641","system":"icduncat"},{"code":"35646","system":"icduncat"},{"code":"35647","system":"icduncat"},{"code":"35651","system":"icduncat"},{"code":"35654","system":"icduncat"},{"code":"35656","system":"icduncat"},{"code":"35661","system":"icduncat"},{"code":"35663","system":"icduncat"},{"code":"35665","system":"icduncat"},{"code":"35666","system":"icduncat"},{"code":"35671","system":"icduncat"},{"code":"35226","system":"icduncat"},{"code":"35256","system":"icduncat"},{"code":"35286","system":"icduncat"},{"code":"35700","system":"icduncat"},{"code":"35721","system":"icduncat"},{"code":"35741","system":"icduncat"},{"code":"35876","system":"icduncat"},{"code":"35879","system":"icduncat"},{"code":"35881","system":"icduncat"},{"code":"35883","system":"icduncat"},{"code":"35884","system":"icduncat"},{"code":"37184","system":"icduncat"},{"code":"37185","system":"icduncat"},{"code":"37186","system":"icduncat"},{"code":"37205","system":"icduncat"},{"code":"37206","system":"icduncat"},{"code":"37207","system":"icduncat"},{"code":"37208","system":"icduncat"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peripheral-arterial-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peripheral-arterial-disease-intervention---icduncat-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peripheral-arterial-disease-intervention---icduncat-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peripheral-arterial-disease-intervention---icduncat-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
