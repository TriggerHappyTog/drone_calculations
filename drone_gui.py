from Tkinter import Tk, Label, Button
import drone_calcs


class DroneGUI:

    def __init__(self, master):
        self.master = master
        master.title("Pressure and Density Calculator")

        self.label = Label(master, text="Useful little tool for calculating pressure and density.")
        self.label.pack()

        self.pressure_button = Button(master, text="Pressure", command=self.pressure)
        self.pressure_button.pack()

        self.density_button = Button(master, text="Density", command=self.density)
        self.density_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def pressure(self):
        qnh = 1027
        air_elev = 4400
        result = drone_calcs.pres_alt_calc(qnh, air_elev)
        print(result)

    def density(self):
        temp = 25
        qnh = 1027
        air_elev = 4400
        result = drone_calcs.den_alt_calc(temp, qnh, air_elev)
        print(result)


root = Tk()
my_gui = DroneGUI(root)
root.mainloop()
