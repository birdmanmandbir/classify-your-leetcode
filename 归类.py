import os
from shutil import copyfile
# 标签格式：// @
annotation = "// @"
programing_language = ".cpp"
# output_dir = "/home/neil/Codes/leetcode/题型总结/"
output_dir = "/home/neil/Codes/classify-python/题型总结"
input_dir = "/home/neil/Codes/classify-python" # also work dir
# TODO log
# cur_dir is abs path
def recur(cur_dir):
    dirs = os.listdir(cur_dir)
    if len(dirs) == 0:
        return
    for dir in dirs:
        abs_dir = os.path.join(cur_dir, dir)
        if os.path.isdir(abs_dir) and abs_dir != output_dir:
            recur(abs_dir)
        elif os.path.isfile(abs_dir):
            # start processing
            dir_to_create_or_move = get_annotation(abs_dir)
            if dir_to_create_or_move == "":
                continue
            abs_dir_to_create_or_move = os.path.join(output_dir, dir_to_create_or_move)
            if (not os.path.exists(abs_dir_to_create_or_move)):
                os.mkdir(abs_dir_to_create_or_move)
            cp_src = abs_dir
            cp_tgt = os.path.join(abs_dir_to_create_or_move, cur_dir.split("/")[-1]+ "." + dir)
            copyfile(cp_src, cp_tgt)

def get_annotation(abs_filename):
    extend_name = os.path.splitext(abs_filename)[-1];
    res = ""
    if extend_name != programing_language:
        return res
    with open(abs_filename, "rt") as file:
        line = file.readline()
        while(line):
            if annotation in line:
                res = line.split(" ")[1].split("@")[1].replace("\n","")
                return res
            line = file.readline()
    return res

if __name__ == '__main__':
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    recur(input_dir)