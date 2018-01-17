import sys, getopt

def arff2csv(arff_path, csv_path=None, _encoding='utf8'):
    with open(arff_path, 'r', encoding=_encoding) as fr:
        attributes = []
        if csv_path is None:
            csv_path = arff_path[:-4] + 'csv'  # *.arff -> *.csv
        write_sw = False
        with open(csv_path, 'w', encoding=_encoding) as fw:
            for line in fr.readlines():
                if write_sw:
                    fw.write(line)
                elif '@data' in line:
                    fw.write(','.join(attributes) + '\n')
                    write_sw = True
                elif '@attribute' in line:
                    attributes.append(line.split()[1])  # @attribute attribute_tag numeric
    print("Convert {} to {}.".format(arff_path, csv_path))

if __name__ == '__main__':

    input_file = None
    output_file= None  
    args, _ = getopt.getopt(sys.argv[1:], "i:o:")

    for o, a in args:
        if o == '-i' and a:
            input_file = a
        elif o == '-o' and a:
            output_file = a

    if not input_file:
        print("Usage: %s -i input_file.arff [-o output_file.csv])" % sys.argv[0])
        exit(0)

    arff2csv(input_file, output_file)