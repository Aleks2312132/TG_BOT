File = open("File\Save.txt", 'r+', encoding='utf-8')
Name_list = []
Index_list = []
lines = File.readlines()
Count_Index_PR = -1
line_Count = 0

def load_Save():
    Save_List = []
    for line in lines:
        Save_List.append(line.strip())
        Count_Index_PR = line.count("index")
    else:
        for i in lines:
            index_One = i.find(":")
            index_Two = i.find(",")
            Name_list.append(i[index_One + 2:index_Two])
            continue
        else:
            for i in lines:
                index_one = i.rfind(":")
                index_two = i.rfind("\n")
                Index_list.append(i[index_one + 1:index_two])
                continue

def File_delite_All():
    File.truncate(0)

def Save(Name, index):
    if Name not in Name_list:
        Save = (f"\"name\": {Name}, \"index\":{index} \n")
        Index_list.append(index)
        Count_Index_PR = index
        File.write(str(Save))
        File.close()


#def Delete_index_Str(index):
#   index = int(index)  # Convert the string to an integer
#    line_Text = f"\"name\": {Name_list[index]}, \"index\":{index} \n"
#    lines_list = []
#
#    for liner in lines:
#        if liner == line_Text:
#            continue
#        lines_list.append(liner)

#    with open('File/Save.txt', 'w') as File:
#        for line in lines_list:
#            File.write(f"{line}\n")


