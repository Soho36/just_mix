# print(time.ctime())
# print(time.time())
# print(time.gmtime())
# print(time.localtime())
# print(time.monotonic())
# print(time.strftime("%H:%M:%S %Y"))
# print(time.ctime())
# import time
# i = 10
# while i >= 0:
#     print(i)
#     time.sleep(1)
#     i -= 1
# print("Vremja vyshlo!")
# import os
# # print(os.getcwd())
# # print(os.path.join(os.getcwd(),"huu"))
# #
# # print(list((os.walk(os.getcwd()))))
import os.path

# import os
# import time
# pycharmprojects_dir = input("Please enter a path to look through: ")
# time.sleep(1)
# print("")
# print("Walking through, please wait...")
# print("")
# time.sleep(1)
# if not pycharmprojects_dir:
#     current_dir_parce = os.walk(os.getcwd())
#     for path, folders, files in current_dir_parce:
#         print(f"Directory is: {path}")
#         print(f"Folders are: {folders}")
#         print(f"Files are: {files}")
#         print("-------------------------------------------------------")
#         time.sleep(1)
# else:
#     user_input_parce = os.walk(pycharmprojects_dir)
#     for path, folders, files in user_input_parce:
#         print(f"Directory is: {path}")
#         print(f"Folders are: {folders}")
#         print(f"Files are: {files}")
#         print("-------------------------------------------------------")
#         time.sleep(1)
#
# print("Parcing is complete!")

# f = open("tekst.txt", "w", encoding="utf8")
# print(f)
# f.write("Vot probnyj tekst!\n"
#         "тохохо вторяа сторча туту\n"
#         "a tut tretja strochka\n"
#         "a tut chetvertaja strochka uzha\n"
#         "nu i tut pjatja hana\n", )
# f.write("Vot probnyj tekst!2")
# f.flush()
# f.close()
# f = open("tekst.txt", "r", encoding="utf8")
# for line in f:
#     print(line)
# f.close()
#
# with open("tekst.txt", "w", encoding="utf8") as f:
#     f.write("1. Vot probnyj tekst!\n"
#         "2. тохохо вторяа сторча туту\n"
#         "3. a tut tretja strochka\n"
#         "4. a tut chetvertaja strochka uzha\n"
#         "5. nu i tut pjatja hana\n", )
# #
#
# with open ("tekst.txt", "r", encoding="utf8") as f:
#     print("ukazatel", f.tell())
#     for line in f:
#         print(line)


# print(os.path.dirname("E:\YandexDisk\Скриншоты"))
# print(os.path.basename("E:\YandexDisk\Скриншоты"))
# print(os.path.normpath("E:\YandexDisk\Скриншоты"))
# print(os.path.exists("E:\YandexDisk\Скриншоты"))
# print(os.listdir("E:\YandexDisk\Скриншоты"))
# for file in os.listdir("E:\YandexDisk\Скриншоты"):
#     print(file)

# f = open("tekst.txt", "a", encoding="utf8")
# dozapis = "\nda vot tut pudet dozapis na"
# f.write(dozapis)
# f.close()

# f = open("tekst.txt", "r", encoding="utf8")
# lines_list = f.readlines()
# print(lines_list)
# for line in lines_list:
#     print(line)
#
# remove_last_lines = lines_list[:-3]
# print(remove_last_lines)
# removed_lines = "".join(remove_last_lines)

# f = open("tekst.txt","w",encoding="utf8")
# f.write(removed_lines)



# print(remove_last_lines)
# for line in remove_last_lines:
#     print(line)
# f = open("tekst.txt", "w", encoding="utf8")
# f.write(remove_last_lines)
#

# f = open("tekst.txt", "r", encoding="utf8")
# print(f.read())

# f = open("tekst.txt", "r", encoding="utf8")
# lines_list = f.readlines()
# f.close()
# f = open("output.txt", "x", encoding="utf8")
# f.write("".join(lines_list))
# f.close()

# list = []
# with open("tekst.txt", "r", encoding="utf8") as input_file:
#     for line in input_file:
#         list.append(line)
# print(list)
# with open("output.txt", "x", encoding="utf8") as output_file:
#     output_file.write("".join(list))

# with open("numbers.txt", "r", encoding="utf8") as inputfile:
#     input_lines = list(map(int, inputfile.readlines()))
#     max_number = max(input_lines)
#     min_number = min(input_lines)
#     max_min_sum = max_number + min_number
#
# with open("output.txt", "x", encoding="utf8") as outputfile:
#     outputfile.write(str(max_min_sum))
#
# with open("tekst.txt", "r", encoding="utf8") as file:
#     for name in file:
#         if int(name[-2]) < 3:
#             print(name)

# with open("tekst.txt", "r", encoding="utf8") as file:
#     names_list = file.readlines()[::-1]
#     print(names_list)
#     reversed_list = []
#     for name in names_list:
#         reversed_list.append(name)
#     print(reversed_list)
# #     joined_list = "".join(reversed_list)
# #     print(joined_list)
#
# with open("output.txt", "a", encoding="utf8") as file:
#     file.write(joined_list)

# with open("tekst.txt", "r", encoding="utf8") as file:
#     names_list = file.readlines()[::-1]
#     joined_list = "".join(names_list)
#     print(joined_list)
#
# with open("output.txt", "a", encoding="utf8") as file:
#     file.write(joined_list)