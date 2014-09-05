pb = {}
import random
import string
import time
import bisect
while len(pb) < 100000:
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
    phonebook = {}
    for stroka in file:
        stroka = stroka.split()
        phon_numb = int(stroka[0])
        name = stroka[-1]
        phonebook[phon_numb] = name
    return phonebook
        
def file_to_list(x):
    file = open(x,"r")
    phonebook = []
    for stroka in file:
        stroka = stroka.split()
        phon_numb = int(stroka[0])
        name = stroka[-1]
        tupl = (phon_numb,name)
        phonebook.append(tupl)
    return phonebook
def file_to_list_sort(x):
    file = open(x,"r")
    phonebook = []
    for stroka in file:
        stroka = stroka.split()
        phon_numb = int(stroka[0])
        name = stroka[-1]
        tupl = (phon_numb,name)
        phonebook.append(tupl)
    phonebook = sorted(phonebook, key = lambda x : x[0])
    return phonebook
def get_name_d(phone):
    n = file_to_dict("phonebook.txt")
    if phone not in n:
        return "Not Found"
    else:
        return n[phone]
def get_name_l(phone):
    m = file_to_list("phonebook.txt")
    n = next((x for x in m if phone in x),None)
    return n[-1]
def get_name_sort_bin(phone):
    q = file_to_list_sort("phonebook.txt")
    phonies = [x[0] for x in q]
    n = q[bisect.bisect_left(phonies,phone)]
    return n[-1]
def compare(f,g,h):
    i = 0
    t1 = 0
    t2 = 0
    t3 = 0
    m = file_to_list("phonebook.txt")
    phones = [x[0] for x in file_to_list("phonebook.txt")]
    while i<1000:
        last_time = time.clock()
        n = random.randint(1,len(phones))
        inp = phones[n]
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
