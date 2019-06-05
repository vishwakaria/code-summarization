

def load_doc(filename):
    f = open(filename, encoding="utf8")
    lines = f.readlines()
    return lines


directory = 'D:/Books/Spring 2019/CS230/Project/code-summarization/data/python/original data/'

ast_list = load_doc(directory + "parallel_AST")
print(ast_list[0:10])
decl_list = load_doc(directory + "updated_parallel_decl.txt")
print(decl_list[0:10])
desc_list = load_doc(directory + "updated_parallel_desc.txt")
print(desc_list[0:10])


file1 = open(directory + "unprocessed_ast_list_train.txt", "w", encoding="utf8")
file2 = open(directory + "unprocessed_ast_list_dev.txt", "w", encoding="utf8")
file3 = open(directory + "unprocessed_ast_list_test.txt", "w", encoding="utf8")
for index in range(len(ast_list)):
    if index < 68000:
        file1.write(str(decl_list[index]) + " " + str(ast_list[index]) + "\n")
    elif index <70000:
        file2.write(str(decl_list[index]) + " " + str(ast_list[index]) + "\n")
    else:
        file3.write(str(decl_list[index]) + " " + str(ast_list[index]) + "\n")
file1.close()
file2.close()
file3.close()

file1 = open(directory + "unprocessed_summary_train.txt", "w", encoding="utf8")
file2 = open(directory + "unprocessed_summary_dev.txt", "w", encoding="utf8")
file3 = open(directory + "unprocessed_summary_test.txt", "w", encoding="utf8")
for index in range(len(desc_list)):
    if index < 68000:
        file1.write(str(desc_list[index]) + "\n")
    elif index <70000:
        file2.write(str(desc_list[index]) + "\n")
    else:
        file3.write(str(desc_list[index]) + "\n")
file1.close()
file2.close()
file3.close()