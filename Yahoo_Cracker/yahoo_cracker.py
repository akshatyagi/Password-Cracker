__author__ = 'Akshat'
start_index = 3072
end_index = 4072 #print only 1000 as opposed to all
with open('password.file') as password_file:
     file_lines = password_file.readlines()
with open('crackedpasswords.txt','w') as writer:
    for i in range(start_index,end_index):
        writer.write(file_lines[i].rstrip()+" "+file_lines[i].rstrip().split(":")[2]+"\n")