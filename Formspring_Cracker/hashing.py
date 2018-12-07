__author__ = 'Akshat'
import hashlib
def read_from_file():
    with open('formspring.txt') as hashes, open('hk_hlm_founds.txt', encoding = "utf-8") as wordlist, open('crackedpasswords.txt','w') as writer:
        password_set = set()
        for hash in hashes:
            password_set.add(hash.rstrip())
        for ptr in range(0,99):
            for word in wordlist:
                if(ptr<10):
                    salted_word = str(0) + str(ptr) + word.rstrip()
                else:
                    salted_word = str(ptr)+word.rstrip()
                if hashlib.sha256(salted_word.encode()).hexdigest() in password_set:
                    writer.write(hashlib.sha256(salted_word.encode()).hexdigest()+ " " + word.rstrip()+"\n")
                    print("Match Found! Hash:"+hashlib.sha256(salted_word.encode()).hexdigest()+" Password:"+word)
read_from_file()