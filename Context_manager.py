# from datetime import datetime
# import time
#
# class Timer:
#     def __init__(self):
#         pass
#     def __enter__(self):
#         self.start = datetime.now()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"Time passed: {(datetime.now()-self.start).total_seconds()}")
# with Timer():
#     time.sleep(2)

# --------------------------------------------------------------------------------
# class Filemanage:
#     def __init__(self, path, opentype):
#         self.path = path
#         self.opentype = opentype
#         self.f = None
#     def __enter__(self):
#         self.f = open(self.path, self.opentype, encoding="utf8")
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.f:
#             if __name__ == '__main__':
#                 self.f.close()
#
#
# with open("tekst.txt", "r", encoding="utf8") as f:
#     f.readlines()

