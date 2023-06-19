import CalculusController
import tkinter
from tkinter import filedialog


c = CalculusController.CalculusController()


def import_bar_settings(calc):
    def extract_parameters(file):
        """
        bar_parameters[material, type, length, diameter, volume, mass, density, celerity, young modulus, j1-sample, sample-j2]
        :param file: txt file containing the bar parameters data
        :return: list containing the parameters' values in order
        """

        def load_txt(file_path):
            with open(file_path, "r") as f:
                return f.readlines()

        def clear_data(lines):
            result = []
            for line in lines:
                line = line.replace("\n", "")
                line = line.split("=")
                result.append(line[1])
            return result

        return clear_data(load_txt(file))

    # bar parameters from file
    root = tkinter.Tk()
    root.withdraw()
    FILE_NAME = filedialog.askopenfilename()
    if not FILE_NAME:
        exit()
    bar_parameters = extract_parameters(FILE_NAME)
    for index in range(len(bar_parameters)):
        if index >= 2:
            bar_parameters[index] = float(bar_parameters[index])
    calc.bar_parameters = bar_parameters
    return calc

def import_speciment_settings(calc):
    def extract_parameters(file):
        """
        bar_parameters[material, type, length, diameter, volume, mass, density, celerity, young modulus, j1-sample, sample-j2]
        :param file: txt file containing the bar parameters data
        :return: list containing the parameters' values in order
        """

        def load_txt(file_path):
            with open(file_path, "r") as f:
                return f.readlines()

        def clear_data(lines):
            result = []
            for line in lines:
                line = line.replace("\n", "")
                line = line.split("=")
                result.append(line[1])
            return result

        return clear_data(load_txt(file))

    root = tkinter.Tk()
    root.withdraw()
    FILE_NAME = filedialog.askopenfilename()
    if not FILE_NAME:
        exit()
    global specimen_parameters
    specimen_parameters = extract_parameters(FILE_NAME)
    for index in range(len(specimen_parameters)):
        specimen_parameters[index] = float(specimen_parameters[index])
    calc.specimen_parameters = specimen_parameters
    return calc

def import_data_file(self):
    def extract_data(file):
        def load_txt(file_path):
            with open(file_path, "r") as f:
                return f.readlines()

        def clean_data(lines):
            # Keep only lines that contain only numbers
            result = []
            for line in lines:
                if ("a" not in line) and ("e" not in line):
                    result.append(line)
            result_without_spaces = []
            for line in result:
                if ("\n" in line) and (line != "\n"):
                    line = line.replace("\n", "")
                if line != "\n":
                    result_without_spaces.append(line)
            return result_without_spaces

        def split_data(tab):
            # Split lines into time, ai1, and ai2 values
            split_time = []
            split_ai1 = []
            split_ai2 = []
            for line in tab:
                if " " in line:
                    line = line.replace(" ", ",")
                if "," in line:
                    line = line.split(",")
                line = list(filter(lambda x: x != "", line))
                split_time.append(float(line[0]))
                split_ai1.append(float(line[1]))
                split_ai2.append(float(line[2]))
            return [split_time, split_ai1, split_ai2]

        text = load_txt(file)
        numbers = clean_data(text)
        return split_data(numbers)

    root = tkinter.Tk()
    root.withdraw()
    FILE_NAME = filedialog.askopenfilename()
    if not FILE_NAME:
        exit()
    time, ai1, ai2 = extract_data(FILE_NAME)
    self.time = time
    self.ai1 = ai1
    self.ai2 = ai2

def test_all_data_is_accessible(self):
    print(self.bar_parameters)
    print(self.specimen_parameters)
    print(self.time)
    print(self.ai1)
    print(self.ai2)
