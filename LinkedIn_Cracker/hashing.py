__author__ = 'Akshat'
import hashlib
def read_from_file():
    with open('SHA1.txt') as hashes, open('hk_hlm_founds.txt', encoding='utf-8') as wordlist, open('crackedpasswords.txt','w') as writer:
        password_set = set()
        for hash in hashes:
            password_set.add(str(hash[5:].rstrip()))
        for word in wordlist:
            if str(hashlib.sha1(word.rstrip().encode()).hexdigest()[5:]) in password_set:
                writer.write(hashlib.sha1(word.rstrip().encode()).hexdigest()+ " " + word.rstrip()+"\n")
                print("Match Found! Hash:"+hashlib.sha1(word.encode()).hexdigest()+" Password:"+word)
read_from_file()