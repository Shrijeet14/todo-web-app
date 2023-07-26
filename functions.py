def file_reader(filename):
    file=open(filename,'r')
    Todos=file.readlines()
    file.close()
    return Todos

def file_writer(Todos ,filename):
    file=open(filename ,'w')
    file.writelines(Todos)
    file.close()

