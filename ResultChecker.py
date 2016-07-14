import os
import pyperclip
from cpp_runner import CppRunner
from python_runner import PythonRunner
from my_sorts import human_sorted
from utils import CustomList


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def find_test_data_directory(name):
    """
    Function looking for all directories with a certain 'name' within directory of script. If it finds zero
    or more than one directory it raises a NameError. Script assumes there should be only one folder
    called by the name of algorithm.
    :return: path containing .in and .out test files
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_directories = CustomList(1)

    for root, directories, file_names in os.walk(current_dir):
        for directory in directories:
            if name.lower() == directory.lower():
                input_directories.append(os.path.join(root, directory))

    input_directories.is_okey()
    return input_directories[0]


def convert_file_into_string(path):
    """
    Function converts a file of given path into string and returns 2-elem list with file path and its content.
    :param path: path to a file
    """
    with open(path, "r") as file:
        content = "".join(file.readlines()).replace('\n', os.linesep).replace(" ", os.linesep)
        file_data = {'name': os.path.basename(path), 'content': content}
        return file_data


def get_out_file_content(input_directory, input_filename):
    with open(os.path.join(input_directory, input_filename[:-3] + ".out"), "r") as file:
        return file.readlines()


def get_input_files_data(input_directory):
    input_files = []

    for input_filename in os.listdir(input_directory):
        if input_filename[-3:] == ".in":
            input_files.append(convert_file_into_string(os.path.join(input_directory, input_filename)))

    return input_files


def get_cpp_result(input_directory, algorithm_name, in_file_content):
    cpp = CppRunner(input_directory, algorithm_name)  # założenie że algorytm jest w tym samym folderze co skrypt
    cpp.compile()
    algorithm_result = cpp.get_output(in_file_content)
    cpp.tidy_up()
    return algorithm_result


def get_python_result(input_directory, algorithm_name, in_file_content):
    python = PythonRunner(input_directory, algorithm_name)  # założenie że algorytm jest w tym samym folderze co skrypt
    algorithm_result = python.get_output(in_file_content)
    return algorithm_result


class LanguageError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


def check_results(algorithm_name, input_directory, programming_lang):
    input_files = human_sorted(get_input_files_data(input_directory))

    if len(input_files) == 0:
        print('Katalog nie zawiera plików wejściowych...')

    for in_file_data in input_files:
        in_file_name = in_file_data['name']
        in_file_content = in_file_data['content']

        languages = {'cpp': get_cpp_result,
                     'python': get_python_result}

        try:
            algorithm_result = languages[programming_lang](input_directory, algorithm_name, in_file_content)
        except KeyError:
            raise LanguageError('{} not supported yet.'.format(programming_lang))

        # print(in_file_content)  # temporary
        # print(algorithm_result)
        # print("".join(get_out_file_content(input_directory, in_file_name)))
        pyperclip.copy(in_file_content)  # temporary

        if algorithm_result == "".join(get_out_file_content(input_directory, in_file_name)):
            print(BColors.OKGREEN + 'Testcase z pliku {0} zakończony pomyślnie :)'.format(in_file_name) + BColors.ENDC)
        else:
            print(BColors.FAIL + 'Testcase z pliku {0} zakończony niepowodzeniem :('.format(in_file_name) +
                  BColors.ENDC)
        # input()


def result_checker():
    while True:
        try:
            algorithm_name = input('Podaj nazwę algorytmu, którego poprawność chcesz sprawdzić: ')
            programming_lang = input('Podaj język, w którym napisany jest algorytm: ').lower()
            input_directory = find_test_data_directory(algorithm_name)

            try:
                check_results(algorithm_name, input_directory, programming_lang)
            except LanguageError as lang_err:
                print(lang_err.__str__())
            else:
                print('Created by Jatimir...')

            break
        except NameError as err:
            print(BColors.FAIL + err.__str__() + BColors.ENDC)


def main():
    result_checker()


if __name__ == '__main__':
    main()

# TODO: error management jeżeli brak pliku .out
