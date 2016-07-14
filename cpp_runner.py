import subprocess
import os


class CppRunner:
    def __init__(self, algorithm_name):
        self.name = algorithm_name
        self.cpp_file_name = self.name + ".cpp"
        self.out_file_name = self.name + ".out"
        self.path = os.path.dirname(os.path.abspath(__file__))

    def compile(self):
        command = ["g++", "-o", self.out_file_name, "-std=c++11", os.path.join(self.path, self.cpp_file_name)]
        subprocess.call(command)

    def get_output(self, user_input):
        p = subprocess.Popen("./" + self.out_file_name,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )
        out, err = p.communicate(input=bytes(user_input, 'utf-8'))
        output = out.decode("utf-8")
        return output

    def tidy_up(self):
        os.remove(os.path.join(self.path, self.out_file_name))


if __name__ == '__main__':
    # cpp = CppRunner('test')
    # cpp.compile()
    # print(cpp.get_output("testproba"))
    # cpp.tidy_up()
    pass
