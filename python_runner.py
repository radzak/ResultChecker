import subprocess
import os


class PythonRunner:
    def __init__(self, algorithm_name):
        self.name = algorithm_name
        self.python_file_name = self.name + ".py"
        self.path = os.path.dirname(os.path.abspath(__file__))

    def get_output(self, user_input):
        p = subprocess.Popen(["python", "-c", "import {}".format(self.name)],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )

        out, err = p.communicate(input=bytes(user_input, 'utf-8'))
        output = out.decode("utf-8")
        return output


if __name__ == '__main__':
    pass
