import tkinter
from tkinter import filedialog
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class CalculusController:
    def __init__(self) -> None:
        self.bar_parameters = []
        self.specimen_parameters = []
        self.time = []
        self.ai1 = []
        self.ai2 = []

    def import_bar_settings(self):
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
        self.bar_parameters = bar_parameters
        bar_material = bar_parameters[0]
        if bar_parameters[1] == "compression":
            bar_type = -1
        else:
            bar_type = 1
        bar_length = bar_parameters[2]
        bar_diameter = bar_parameters[3]
        bar_volume = bar_parameters[4]
        bar_mass = bar_parameters[5]
        bar_density = bar_parameters[6]
        bar_signal_celerity = bar_parameters[7]
        bar_young_modulus = bar_parameters[8]
        bar_j1_sample = bar_parameters[9]
        bar_j2_sample = bar_parameters[10]

    def import_speciment_settings(self):
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
        self.specimen_parameters = specimen_parameters
        specimen_length = specimen_parameters[0]
        specimen_diameter = specimen_parameters[1]

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

    def display_and_limiting(self):
        time = self.time
        ai1 = self.ai1
        ai2 = self.ai2
        tk = tkinter
        FIG_WIDTH = 1280
        FIG_HEIGHT = 720
        # 5) CREATE GRAPH
        fig, ax = matplotlib.pyplot.subplots(
            figsize=(FIG_WIDTH / 100, FIG_HEIGHT / 100)
        )
        ax.plot(time, ai1, label="ai1")
        ax.plot(time, ai2, label="ai2")
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.legend()

        # CREATE CANVAS AND TOOLBAR
        # Create window
        graph_window = tk.Tk()
        graph_window.title("Graph")
        # Create graph canvas in window
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # Create toolbar
        toolbar = NavigationToolbar2Tk(canvas, graph_window)
        toolbar.update()
        toolbar.pack(side="top", fill="both", expand=1)
        # Remove Home, Subplots and Save buttons from toolbar
        toolbar._buttons["Home"].pack_forget()
        toolbar._buttons["Subplots"].pack_forget()
        toolbar._buttons["Save"].pack_forget()

        # CLOSE WINDOW BUTTON
        def window_close():
            graph_window.destroy()
            graph_window.quit()

        close_button = tk.Button(
            master=graph_window, text="Close", command=window_close
        )
        close_button.pack()

        # SELECT POINT BUTTON
        global left_border_time, right_border_time
        left_border_time = None
        right_border_time = None
        cid = None

        def find_closest_index(x):
            # Find the index of the closest point to x
            distances = []
            for line in ax.lines:
                xdata = line.get_xdata()
                distances.append((((xdata - x) ** 2) ** 0.5))
            min_distance = float("inf")
            for j in range(len(distances[0])):
                if min_distance > distances[0][j]:
                    min_distance = distances[0][j]
            closest_index = None
            for j in range(len(distances[0])):
                if distances[0][j] == min_distance:
                    closest_index = j
            return closest_index

        def select_point(event):
            global left_border_time, right_border_time
            if (left_border_time is not None) and (right_border_time is not None):
                print(f"The two borders have already been defined.")
                return
            closest_index = find_closest_index(event.xdata)
            closest_time = time[closest_index]
            if (left_border_time is not None) and (right_border_time is None):
                right_border_time = closest_time
            if (left_border_time is None) and (right_border_time is None):
                left_border_time = closest_time
            ax.axvline(x=closest_time, color="r")
            canvas.draw()
            fig.canvas.mpl_disconnect(cid)

        def start_selection():
            global cid
            cid = fig.canvas.mpl_connect("button_press_event", select_point)

        select_point_button = tk.Button(
            master=graph_window, text="Select a point", command=start_selection
        )
        select_point_button.pack()

        # MAIN LOOP
        tk.mainloop()

        # 6) REDUCE THE GRAPH DATA
        left_border_index = -1
        right_border_index = -1

        for index in range(len(time)):
            if time[index] == left_border_time:
                left_border_index = index
            if time[index] == right_border_time:
                right_border_index = index

        data_time_cropped = []
        data_ai1_cropped = []
        data_ai2_cropped = []
        for index in range(len(time)):
            if left_border_index <= index <= right_border_index:
                data_time_cropped.append(time[index])
                data_ai1_cropped.append(ai1[index])
                data_ai2_cropped.append(ai2[index])

        self.time = data_ai1_cropped
        self.ai1 = data_ai1_cropped
        self.ai2 = data_ai2_cropped
