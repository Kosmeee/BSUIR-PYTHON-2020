import tempfile
import linecache


def len_of_file(filename):
    i = 0
    with open(filename) as f:
        for lines in f:
            i += 1
    return i


def change_line_infile(filename1, num, str1):
    i = 0
    temp = tempfile.NamedTemporaryFile
    with open(filename1, 'r') as file1:
        with open(temp.__name__, 'w') as file2:
            for lines in file1:
                if i == num:
                    file2.write(str1)
                else:
                    file2.write(lines)
                i += 1
    with open(filename1, 'w') as file1:
        with open(temp.__name__, 'r') as file2:
            for lines in file2:
                file1.write(lines)


def set_value(filename1, filename2, num1, num2):
    j = 0
    str2 = ""
    with open(filename2, 'r') as file2:
        for lines in file2:
            if j == num2:
                str2 = lines
            j += 1
    change_line_infile(filename1, num1, str2)


def merge(my_file):
    cur_len = len_of_file(my_file)
    if cur_len > 1:
        mid = cur_len // 2
        L = tempfile.TemporaryFile(delete=False)
        R = tempfile.TemporaryFile(delete=False)
        L.close()
        R.close()
        i = 1
        with open(my_file, 'r', encoding='utf-8') as g:
            with open(L.name, 'w', encoding='utf-8') as L:
                with open(R.name, 'w', encoding='utf-8') as R:
                    for line in g:
                        if i <= mid:
                            L.write(line)
                        else:
                            R.write(line)
                        i += 1
        merge(L.name)
        merge(R.name)
        i = j = k = 0
        while i < len_of_file(L.name) and j < len_of_file(R.name):
            if float(linecache.getline(L.name, i+1)) < float(linecache.getline(R.name, j+1)):
                set_value(my_file, L.name, k, i)
                i += 1
            else:
                set_value(my_file, R.name, k, j)
                j += 1
            k += 1
        while i < len_of_file(L.name):
            set_value(my_file, L.name, k, i)
            i += 1
            k += 1
        while j < len_of_file(R.name):
            set_value(my_file, R.name, k, j)
            j += 1
            k += 1
