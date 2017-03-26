import os
def rename_files():
    file_list = os.listdir(r"/Users/dxh3992/Darshan/Python/Test/Prank")
    print(file_list)

    os.chdir(r"/Users/dxh3992/Darshan/Python/Test/Prank")
    
    for file_name in file_list:
        os.rename(file_name,file_name.translate(str.maketrans(dict.fromkeys("0123456789"))))

    file_list = os.listdir(r"/Users/dxh3992/Darshan/Python/Test/Prank")
    print(file_list)

rename_files()
