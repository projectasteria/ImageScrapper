import os

def csv_generator(folder):
    csv_data = ["image_path,class\n"]
    main_folder_contents = os.listdir("./{}".format(folder))
    for folders in main_folder_contents:
        sub_folder_contents = os.listdir("./{}/{}".format(folder, folders))
        for file_name in sub_folder_contents:
            csv_data.append("{}\\{}\\{}, {}\n".format(folder, folders, file_name, folders))
    open("csvfile.csv", "w").writelines(csv_data)

csv_generator("Project\\Animals")