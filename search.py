

# i think if we use KMP algorithm we can search for string in linear time but i found it useless because input string
#max size is 100 char  so this algorithm has complexity O(100*n) so i think if we make it O(n)
#wont make a different



index = 0;
remaining_string = ""
#search : loop and compare each 2 character if they are similar then continue
#not then we increment start pointer by one
#complexity O(inputsize* file size) which is approx. O(n)
def search(input_string,string_file):
    #length of input string
    ln= len(input_string)
    start=0
    global index
    global  remaining_string
   #if there is matching substring from the previous chunk so i added to new chunk to complete the comparsion
    index_of_string=index
    string_file = remaining_string + string_file
    while index < ln and index_of_string < len(string_file):
        #if equal continue
        if input_string[index] == string_file[index_of_string]:
            index+=1

            index_of_string+=1
        else:
            # make index = 0 and start incremented by one
            index=0
            start+=1
            index_of_string=start
        if(index == ln):
            return True
    remaining_string = string_file[len(string_file)-index:]

    return False

def read_chunck(filename,input_string):
  flag=0
  f = open(filename,"r")
  while True:
      # read 100 char only per iteration due to the large size of the file
      s = f.read(100)
      respone = search(input_string,s)
      if(respone == True):
          print("Found")
          flag=1
          break
      if not s:
          break;
  if flag ==0:
      print("NOT FOUND")





if __name__ == '__main__':
    input_data = input()
    lst = input_data.split(",")
    read_chunck(lst[0],lst[1])

