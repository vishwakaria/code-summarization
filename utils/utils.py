def split_src_tgt(in_file, data_file_role):
    '''
	Splits a given input file that has the form "target input_data" into two separate files
	Params:
		in_file: full path to the dataset that has the target first and then the input separated by spaces
		data_file_role: string containing one of the following: {train, val, test}
	EX: 
		split_src_tgt('java-small.train.txt', 'train')
		split_src_tgt('java-small.val.txt', 'val')
		split_src_tgt('java-small.test.txt', 'test')
    '''
    src_path = 'src.{}.txt'.format(data_file_role)
    tgt_path = 'tgt.{}.txt'.format(data_file_role)
    
    with open(in_file, 'r') as in_file, open(src_path, 'w') as src_file, open(tgt_path, 'w') as tgt_file:
        for line in in_file:
            
            parts = line.rstrip('\n').split(' ')
            
            target_data = parts[0]
            src_data = ''.join(parts[1:])
            
            src_file.write(src_data + '\n')
            tgt_file.write(target_data + '\n')
                
    return 'done'
	
