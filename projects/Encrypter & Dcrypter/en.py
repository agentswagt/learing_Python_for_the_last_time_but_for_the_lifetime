import sys


file_name = sys.argv[1]
level = sys.argv[2]

print("[+]File_name: {}".format(file_name))
print("[+]Level:{}".format(level))


file_reader_inline = open(file_name, "r").read().split("\n")
file_reader_linecount = len(file_reader_inline)

file_reader_inline_inreverse = list(reversed(file_reader_inline))


print("[+]File_Total_line:{}\n".format(file_reader_linecount))
print("[+]File_Reader_Inline:\n{}".format(file_reader_inline))
print("\n")
print("[+]File_Reader_Inline_Inreverse:\n{}".format(file_reader_inline_inreverse))

