def csv_split(filename, user_specified_size):
    accepted_fmt = ["json", "csv"]
    doc_name, extension = filename.split(".")[0], filename.split(".")[1]
    """checking if file is an accepted fmt"""
    if extension not in accepted_fmt:
        raise TypeError("Sorry input a an accepted format json or csv file")
    elif extension == "csv":
        size_of_file = os.path.getsize(filename)
        chunk_file_size = math.ceil(size_of_file / user_specified_size)
        total_lenght_of_file = len(pd.read_csv(filename).index)
        row_per_file = math.ceil(total_lenght_of_file / chunk_file_size)
        num = 1
        for each_file in pd.read_csv(filename, chunksize=row_per_file, header=None):
            each_file.to_csv(f"{doc_name}{num}.csv")
            num += 1
        return
