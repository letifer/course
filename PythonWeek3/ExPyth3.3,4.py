pb = {}
import random
import string
import time
for i in range(100000):
    phone = str(random.randint(1000000,9999999))
    if phone in pb:
        continue
    else:
        name = (random.choice(string.ascii_uppercase)) + \
               "".join(random.choice(string.ascii_lowercase) for x \
                       in range(random.randint(2,9)))
    pb[phone] = name

my_file = open("phonebook.txt","w")
for i in pb:
    my_file.write(str(i))
    my_file.write(" " + pb[i] + "\n")
my_file.close()

def file_to_dict(x):
    file = open(x,"r")
    phobok = {}
    for stroka in file:
        stroka = stroka.split()
        phon_numb = int(stroka[0])
        name = stroka[-1]
        phobok[phon_numb] = name
    return phobok
        
def file_to_list(x):
    file = open(x,"r")
    phobook = []
    for stroka in file:
        stroka = stroka.split()
        phon_numb = int(stroka[0])
        name = stroka[-1]
        tupl = (phon_numb,name)
        phobook.append(tupl)
    return phobook
def file_to_list_sort(x):
    file = open(x,"r")
    phoobook = []
    for stroka in file:
        stroka = stroka.split()
        phon_numb = int(stroka[0])
        name = stroka[-1]
        tupl = (phon_numb,name)
        phoobook.append(tupl)
    phoobook = sorted(phoobook, key = lambda x : x[0])
    return phoobook
def compare(f,g,h,inp):
    i = 0
    t1 = 0
    t2 = 0
    t3 = 0
    while i<1000:
        last_time = time.clock()
        f(inp)
        t1 += time.clock() - last_time
        last_time = time.clock()
        g(inp)
        t2 += time.clock() - last_time
        last_time = time.clock()
        h(inp)
        t3 += time.clock() - last_time
        i += 1
    print(t3 / t2, t2 / t1, t3/t1)
compare(file_to_dict,file_to_list,file_to_list_sort,"phonebook.txt")
