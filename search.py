index = 0;
def search(input_string,string_file):
    window_size= len(input_string)
    start=0
    global index
    index_of_string=0
    while index < window_size and index_of_string < len(string_file):
        if input_string[index] == string_file[index_of_string]:
            index+=1

            index_of_string+=1
        else:
            index=0
            start+=1
            index_of_string=start
        if(index == window_size):
            return True

    return False

def read_chunck(filename):
  f = open(filename,"r")
  while True:
      s = f.read(3)
      respone = search("rna",s)
      if(respone == True):
          print("Found")
          break
      else:
          print("NOT")
      if not s:
          break;



read_chunck("input.txt")
