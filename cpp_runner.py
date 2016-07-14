import subprocess
import os


class CppRunner:
    def __init__(self, input_directory, algorithm_name):
        self.name = algorithm_name
        self.cpp_file_name = self.name + ".cpp"
        self.out_file_name = self.name + ".out"
        self.input_directory = input_directory

    def compile(self):
        command = ["g++",
                   "-o",
                   os.path.join(self.input_directory, self.out_file_name),
                   "-std=c++11",
                   os.path.join(self.input_directory, self.cpp_file_name)]
        subprocess.call(command)

    def get_output(self, user_input):
        p = subprocess.Popen(os.path.join(self.input_directory, self.out_file_name),
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )
        out, err = p.communicate(input=bytes(user_input, 'utf-8'))
        output = out.decode("utf-8")
        return output

    def tidy_up(self):
        os.remove(os.path.join(self.input_directory, self.out_file_name))


if __name__ == '__main__':
    pass
