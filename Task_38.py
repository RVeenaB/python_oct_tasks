#write mode read mode append mode
#write mode 
# read_text = "hello this is a dummy text"
# # file = open("test_text.txt",mode = 'w')
# # write_data = file.write(read_text)
# # #print(read_text)
# # file.close()
# # #read mode
# file = open("test_text.txt",mode="r")
# read_data = file.read()
# print(f"before append: {read_data}")
# file.close()
# #append mode
# file = open("test_text.txt",mode="a")
# # read_data = file.read()
# # print(f"before append : {read_data}")
# file.writelines("\nthis is second line added by append\n")
# file.close()
# file = open("test_text.txt",mode="r")
# read_data = file.read()
# print(f"after append: {read_data}")
# file.close()

# #mode w+
# file = open("plus_mode.txt",mode="w+")
# file.write("this is mode w+\n")
# read_data = file.read()
# print(f"im w+ mode read {read_data}")
# file.close()

# #mode r+
# file = open("plus_mode.txt",mode="r+")
# file.write("this is mode r+\n")
# read_data = file.read()
# print(f"im r+ mode read {read_data}")
# file.close()

#mode a+
file = open("plus_mode.txt",mode="a+")
file.write("this is mode a+\n")
read_data = file.read()
print(f"im a+ mode read {read_data}")
file.close()
