import os
while True:
    try:
        path = input("Enter folder path:")
        file_list = sorted(os.listdir(path))
        break
    except FileNotFoundError:
        print("Folder does not exist!")
    continue


try:
    for i,file in enumerate(file_list,start = 1):
        base_name,extension = os.path.splitext(file)
        old_name = os.path.join(path,file)
        new_name = os.path.join(path,f"file{i}{extension}")
        if not os.path.exists(new_name):
            os.rename(old_name,new_name)
        else:
            print("Rename skipped,file already exists")
except PermissionError:
    print("Access denied!")
except OSError:
    print("Unexpected system error occurred!")