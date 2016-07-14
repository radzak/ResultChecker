import subprocess
import os


class PythonRunner:
    def __init__(self, input_directory, algorithm_name):
        self.algorithm_name = algorithm_name
        self.python_file_name = self.algorithm_name + '.py'
        self.input_directory = input_directory

    def get_output(self, user_input):

        p = subprocess.Popen(["python", os.path.join(self.input_directory, self.python_file_name)],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )

        out, err = p.communicate(input=bytes(user_input, 'utf-8'))
        output = out.decode("utf-8")
        return output


if __name__ == '__main__':
    pass
