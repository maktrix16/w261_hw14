#!/usr/bin/env python
import sys

def rules_python(input_file, output_file):
    
    spacing = '    '
    
    with open(input_file,'r') as f_in:
        with open(output_file,'w+') as f_out:
            all_lines = []

            for line in f_in:
                # print(model.toDebugString())
    #             model.txt = model.toDebugString().split('\n')

    #             for line in model.txt:
                text = line.split()
                if text == []:
                    pass
                else:
                    all_lines.append(text)

            starting_indent = 1
            if_indents = {0: starting_indent}
            if_num = 0

            for i in range(len(all_lines)):
                if all_lines[i][0] == 'Tree':
                    indents = starting_indent - 1
                    bin_num = 0
#                     tabs = '\t'*starting_indent
                    tabs = spacing*starting_indent
                    tree_num = int(all_lines[i][1].strip(':'))
#                     print tabs + '# Tree ' + str(tree_num)
                    f_out.write(tabs + '# Tree ' + str(tree_num)+'\n')

                elif all_lines[i][0] == 'If':
                    indents = indents + 1
                    if_indents[if_num] = indents
#                     tabs = '\t'*indents
                    tabs = spacing*indents
#                     print tabs + 'if ' + all_lines[i][1] + '[' + all_lines[i][2] + ']' + all_lines[i][3] + all_lines[i][4] + ':'
                    f_out.write(tabs + 'if ' + all_lines[i][1] + '[' + all_lines[i][2] + ']' + all_lines[i][3] + all_lines[i][4] + ':'+'\n')
                    if_num += 1

                elif all_lines[i][0] == 'Else':
                    indents = if_indents[if_num - 1]
#                     tabs = '\t'*indents
                    tabs = spacing*indents
#                     print tabs + 'else:'
                    f_out.write(tabs + 'else:'+'\n')
                    if_num -= 1

                elif all_lines[i][0] == 'Predict:':
                    indents = indents + 1
#                     tabs = '\t'*indents
                    tabs = spacing*indents
#                     print tabs + 'bin_num[' + str(tree_num) + '] = ' + str(bin_num)
                    f_out.write(tabs + 'bin_num[' + str(tree_num) + '] = ' + str(bin_num)+'\n')
                    bin_num += 1
                    indents = indents - 1

if __name__== '__main__':
    rules_python(sys.argv[1],sys.argv[2])
    