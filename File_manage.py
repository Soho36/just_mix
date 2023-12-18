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

with open("tekst.txt", "r", encoding="utf8") as f:
    for line in f:
        print(line)
