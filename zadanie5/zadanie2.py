import hashlib

def md5sum(text):
    n = hashlib.new('md5')
    n.update(text)
    return n.hexdigest()

def sha1sum(text):
    n = hashlib.new('sha1')
    n.update(text)
    return n.hexdigest()

def sha224sum(text):
    n = hashlib.new('sha224')
    n.update(text)
    return n.hexdigest()

def sha256sum(text):
    n = hashlib.new('sha256')
    n.update(text)
    return n.hexdigest()

def sha384sum(text):
    n = hashlib.new('sha384')
    n.update(text)
    return n.hexdigest()

def sha512sum(text):
    n = hashlib.new('sha512')
    n.update(text)
    return n.hexdigest()

def hamming_distance(text1, text2):
    different = int(sum(c1 != c2 for c1, c2 in zip(text1, text2))/2)
    length = len(text1)/2 - 14
    percentage = 100*float(different)/float(length)
    return "Ilosc roznych bitow: " + str(different) + "  tj. %.2f"%percentage+"% z "+"%.0d"%length

def find_bytes_string(text):
    bytes_string = ""
    j=0
    for i in range(len(text)):
        char_helper = ""
        char = bin(ord(text[i]))
        for i in range(2,len(char)):
            char_helper += char[i]
        if(len(char_helper) % 4 != 0):
            char_helper = (4-len(char_helper)%4)*"0"+char_helper ##bin.zfill()
            j+=1
        bytes_string += char_helper
    return bytes_string

def create_diff_list(hashlist):
    diff_list = [[] for k in range(len(hashlist))]
    for i in range(len(hashlist)):
        for j in range(len(hashlist[i])):
            diff_list[i].append(find_bytes_string(hashlist[i][j]))
    return diff_list


def writing(hashlist,difflist):
    file_hash = open("diff.txt","+w")
    commands = [['cat hash.pdf personal.txt | md5sum','cat hash.pdf personal_.txt | md5sum'],['cat hash.pdf personal.txt | sha1sum','cat hash.pdf personal_.txt | sha1sum'],['cat hash.pdf personal.txt | sha224sum','cat hash.pdf personal_.txt | sha224sum'],['cat hash.pdf personal.txt | sha256sum','cat hash.pdf personal_.txt | sha256sum'],['cat hash.pdf personal.txt | sha384sum','cat hash.pdf personal_.txt | sha384sum'],['cat hash.pdf personal.txt | sha512sum','cat hash.pdf personal_.txt | sha512sum']]
    file_hash.write("Wykoywane polecenia i wyniki: \n\n")
    for i in range(len(hashlist)):
        file_hash.write(commands[i][0]+'\n'+commands[i][1]+'\n')
        file_hash.write(hashlist[i][0]+hashlist[i][1])
        file_hash.write(hamming_distance(difflist[i][0],difflist[i][1])+'\n')
        file_hash.write('\n')
    file_hash.close()

def create_hashlist(text):
    for i in range(len(text)):
        for j in range(len(text[i])):
            element = ""
            if(text[i][j] != " " or text[i][j] != "-" or text[i][j] != "\n"):
                element += text[i][j]
    hashlist = [[] for k in range(int(len(text)/2))]
    i, j = 0, 0
    while(i < len(hashlist)):
        hashlist[i].append(text[j])
        j += 1
        if(j % 2 == 0):
            i += 1
    return hashlist

def main():
    hash_file = open("hash.txt","r")
    text = hash_file.readlines()
    hash_list = create_hashlist(text)
    diff_list = create_diff_list(hash_list)
    writing(hash_list,diff_list)

main()