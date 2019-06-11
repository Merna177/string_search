# how to test it ?
#first input  --> file name  ex: input.txt
#second input --> input string ex: engineering 

#Complexity : O(N*100) where N is the length of the string in the input file	
#possible optimization : using kmp string matching algorithm
#so the complexity would be reduced to O(N)
#O(N*M) where M <= 100 so will approximately be O(N)



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
          print("Yes")
          flag=1
          break
      if not s:
          break;
  if flag ==0:
      print("False")





if __name__ == '__main__':
    file_name= input()
    input_string =  input()
    read_chunck(file_name,input_string)
