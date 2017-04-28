from Tkinter import Tk, Label, Button, Entry, IntVar, W, E
import drone_calcs


class DroneGUI:

    def __init__(self, master):
        self.master = master
        master.title("Pressure and Density Calculator")

        self.label = Label(master, text="Useful little tool for calculating pressure and density.")
        self.label.pack()

        self.label = Label(master, text="Temp")
        self.label.pack()

        vcmd = master.register(self.validate)  # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P', "temp"))
        self.entry.pack()

        self.label = Label(master, text="QNH")
        self.label.pack()

        self.entry2 = Entry(master, validate="key", validatecommand=(vcmd, '%P', "qnh"))
        self.entry2.pack()

        self.label = Label(master, text="Air Elevation")
        self.label.pack()

        self.entry3 = Entry(master, validate="key", validatecommand=(vcmd, '%P', "air_elev"))
        self.entry3.pack()

        self.pressure_button = Button(master, text="Pressure", command=self.pressure)
        self.pressure_button.pack()

        self.density_button = Button(master, text="Density", command=self.density)
        self.density_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.total = 0
        self.qnh = 0
        self.air_elev = 0
        self.temp = 0

        self.label2 = Label(master, text="Answer:")
        self.label2.pack()

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.total_label.pack()

    def pressure(self):
        result = drone_calcs.pres_alt_calc(self.qnh, self.air_elev)
        self.total_label_text.set(result)

    def density(self):
        result = drone_calcs.den_alt_calc(self.temp, self.qnh, self.air_elev)
        self.total_label_text.set(result)

    def validate(self, new_text, data_type):
        if not new_text:
            if data_type == "temp":
                self.temp = 0
            elif data_type == "qnh":
                self.qnh = 0
            elif data_type == "air_elev":
                self.air_elev = 0
            return True

        try:
            if data_type == "temp":
                self.temp = int(new_text)
            elif data_type == "qnh":
                self.qnh = int(new_text)
            elif data_type == "air_elev":
                self.air_elev = int(new_text)
            return True
        except ValueError:
            return False


root = Tk()
my_gui = DroneGUI(root)
root.mainloop()
