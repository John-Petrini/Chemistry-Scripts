#GENERIC FUNCTION 1
#INPUT - file path
#OUTOUT - list [all folders in file path]
def parse_folders(directory_path):
    # if paths are valid directory, obtain all folders in valid paths
    subFolders = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]

    return subFolders

#GENERIC FUNCTION 2
#INPUT - base file path, file path addendum
#OUTPUT - concatenated file path
def path_extender(base_path, path_extension):
    extended_path = os.path.join(base_path, path_extension)
    
    return extended_path

#GENERIC FUNCTION 3
#INPUT - folder path containing word docs
#OUTPUT list of [all word docx]
def get_word_docs(word_folder_path):
    # 'word_file_pattern' indicates all documents ending in .docx in word_folder_path
    word_file_pattern = os.path.join(word_folder_path, '*.docx') 
    word_files = glob.glob(word_file_pattern) # glob.glob() retrieves all files of indicated pattern
    
    return word_files
