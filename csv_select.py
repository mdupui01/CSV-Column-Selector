#!/usr/bin/env python

import csv
import argparse

def main():
    '''
    Script is meant to be called from terminal command line. Look at help for more
    information on the inputs.
    '''
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Input file name ending in .csv')
    parser.add_argument('-o', '--output', help ='Output file name ending in .csv')
    parser.add_argument('-c', '--columns', action='store', nargs = '*', help = 'Column index OR title. The output columns will be in the same order as the user input.')

    args = parser.parse_args()
    
    with open(args.output,'w') as output_file:
        w = csv.writer(output_file)
    
        with open(args.input, 'r') as input_file:
            reader = csv.reader(input_file)
            header = reader.next()
            
            ind = [n if n.isdigit() else header.index(n) for n in args.columns]
            included_cols = map(int, ind)
            
            fid = csv.reader(input_file, delimiter = ',')
            
            header_new = [header[i] for i in included_cols]
            w.writerow(header_new)
            for row in fid:
                item = [row[i] for i in included_cols]
                w.writerow(item)
            

if __name__ == '__main__':
    main()