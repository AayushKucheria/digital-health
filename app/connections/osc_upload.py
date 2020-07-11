import glob


if __name__ == "__main__":

    print("Upload function running")
    file_list = glob.glob("data/*.csv")
    if len(file_list) > 1:
        print("Available Files:", file_list)
        chosen = input("Please enter file name (without path or .csv): ")
    print(chosen)
    # with open(filename, 'r') as read_obj:
    #     csv_reader = reader(read_obj)
    #     messages = list(csv_reader)
    #     print(messages)