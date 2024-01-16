import tkinter as tk
from tkinter import ttk


# Conversion functions
def convert_mass():
    try:
        value = float(entry_mass.get())
        unit_from = combo_mass_from.get()
        unit_to = combo_mass_to.get()

        # Conversion logic
        if unit_from == "Grams":
            converted_value = convert_mass_to_grams(value, unit_to)
        elif unit_from == "Kilograms":
            converted_value = convert_mass_to_kilograms(value, unit_to)
        elif unit_from == "Pounds":
            converted_value = convert_mass_to_pounds(value, unit_to)

        label_result_mass.config(text=f"Result: {converted_value} {unit_to}")
    except ValueError:
        label_result_mass.config(text="Invalid input. Please enter a number.")


def convert_volume():
    try:
        value = float(entry_volume.get())
        unit_from = combo_volume_from.get()
        unit_to = combo_volume_to.get()

        # Conversion logic
        if unit_from == "Liters":
            converted_value = convert_volume_to_liters(value, unit_to)
        elif unit_from == "Milliliters":
            converted_value = convert_volume_to_milliliters(value, unit_to)
        elif unit_from == "Gallons":
            converted_value = convert_volume_to_gallons(value, unit_to)

        label_result_volume.config(text=f"Result: {converted_value} {unit_to}")
    except ValueError:
        label_result_volume.config(
            text="Invalid input. Please enter a number.")


def convert_distance():
    try:
        value = float(entry_distance.get())
        unit_from = combo_distance_from.get()
        unit_to = combo_distance_to.get()

        # Conversion logic
        if unit_from == "Meters":
            converted_value = convert_distance_to_meters(value, unit_to)
        elif unit_from == "Kilometers":
            converted_value = convert_distance_to_kilometers(value, unit_to)
        elif unit_from == "Miles":
            converted_value = convert_distance_to_miles(value, unit_to)

        label_result_distance.config(
            text=f"Result: {converted_value} {unit_to}")
    except ValueError:
        label_result_distance.config(
            text="Invalid input. Please enter a number.")

# Mass conversion functions


def convert_mass_to_grams(value, unit_to):
    if unit_to == "Grams":
        return value
    elif unit_to == "Kilograms":
        return value * 0.001
    elif unit_to == "Pounds":
        return value * 0.00220462


def convert_mass_to_kilograms(value, unit_to):
    if unit_to == "Grams":
        return value * 1000
    elif unit_to == "Kilograms":
        return value
    elif unit_to == "Pounds":
        return value * 2.20462


def convert_mass_to_pounds(value, unit_to):
    if unit_to == "Grams":
        return value * 453.592
    elif unit_to == "Kilograms":
        return value * 0.453592
    elif unit_to == "Pounds":
        return value

# Volume conversion functions


def convert_volume_to_liters(value, unit_to):
    if unit_to == "Liters":
        return value
    elif unit_to == "Milliliters":
        return value * 1000
    elif unit_to == "Gallons":
        return value * 0.264172


def convert_volume_to_milliliters(value, unit_to):
    if unit_to == "Liters":
        return value * 0.001
    elif unit_to == "Milliliters":
        return value
    elif unit_to == "Gallons":
        return value * 0.000264172


def convert_volume_to_gallons(value, unit_to):
    if unit_to == "Liters":
        return value * 3.78541
    elif unit_to == "Milliliters":
        return value * 3785.41
    elif unit_to == "Gallons":
        return value

# Distance conversion functions


def convert_distance_to_meters(value, unit_to):
    if unit_to == "Meters":
        return value
    elif unit_to == "Kilometers":
        return value * 0.001
    elif unit_to == "Miles":
        return value * 0.000621371


def convert_distance_to_kilometers(value, unit_to):
    if unit_to == "Meters":
        return value * 1000
    elif unit_to == "Kilometers":
        return value
    elif unit_to == "Miles":
        return value * 0.621371


def convert_distance_to_miles(value, unit_to):
    if unit_to == "Meters":
        return value * 1609.34
    elif unit_to == "Kilometers":
        return value * 1.60934
    elif unit_to == "Miles":
        return value


# Main application window
app = tk.Tk()
app.title("Unit Converter")

# Mass conversion section
frame_mass = ttk.Frame(app, padding="16")
frame_mass.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_mass = ttk.Label(frame_mass, text="Mass Converter", font=("Arial", 16))
label_mass.grid(column=0, row=0, columnspan=2, pady=(0, 10))

label_mass_value = ttk.Label(frame_mass, text="Enter value:")
label_mass_value.grid(column=0, row=1, sticky=tk.E)

entry_mass = ttk.Entry(frame_mass, width=15)
entry_mass.grid(column=1, row=1, sticky=tk.W)

label_mass_from = ttk.Label(frame_mass, text="From:")
label_mass_from.grid(column=0, row=2, sticky=tk.E)

combo_mass_from = ttk.Combobox(
    frame_mass, values=["Grams", "Kilograms", "Pounds"])
combo_mass_from.grid(column=1, row=2, sticky=tk.W)
combo_mass_from.set("Grams")

label_mass_to = ttk.Label(frame_mass, text="To:")
label_mass_to.grid(column=0, row=3, sticky=tk.E)

combo_mass_to = ttk.Combobox(
    frame_mass, values=["Grams", "Kilograms", "Pounds"])
combo_mass_to.grid(column=1, row=3, sticky=tk.W)
combo_mass_to.set("Kilograms")

button_convert_mass = ttk.Button(
    frame_mass, text="Convert", command=convert_mass)
button_convert_mass.grid(column=0, row=4, columnspan=2, pady=(10, 0))

label_result_mass = ttk.Label(frame_mass, text="")
label_result_mass.grid(column=0, row=5, columnspan=2, pady=(10, 0))

# Volume conversion section
frame_volume = ttk.Frame(app, padding="10")
frame_volume.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))

label_volume = ttk.Label(
    frame_volume, text="Volume Converter", font=("Arial", 16))
label_volume.grid(column=0, row=0, columnspan=2, pady=(0, 10))

label_volume_value = ttk.Label(frame_volume, text="Enter value:")
label_volume_value.grid(column=0, row=1, sticky=tk.E)

entry_volume = ttk.Entry(frame_volume, width=15)
entry_volume.grid(column=1, row=1, sticky=tk.W)

label_volume_from = ttk.Label(frame_volume, text="From:")
label_volume_from.grid(column=0, row=2, sticky=tk.E)

combo_volume_from = ttk.Combobox(
    frame_volume, values=["Liters", "Milliliters", "Gallons"])
combo_volume_from.grid(column=1, row=2, sticky=tk.W)
combo_volume_from.set("Liters")

label_volume_to = ttk.Label(frame_volume, text="To:")
label_volume_to.grid(column=0, row=3, sticky=tk.E)

combo_volume_to = ttk.Combobox(
    frame_volume, values=["Liters", "Milliliters", "Gallons"])
combo_volume_to.grid(column=1, row=3, sticky=tk.W)
combo_volume_to.set("Milliliters")

button_convert_volume = ttk.Button(
    frame_volume, text="Convert", command=convert_volume)
button_convert_volume.grid(column=0, row=4, columnspan=2, pady=(10, 0))

label_result_volume = ttk.Label(frame_volume, text="")
label_result_volume.grid(column=0, row=5, columnspan=2, pady=(10, 0))

# Distance conversion section
frame_distance = ttk.Frame(app, padding="10")
frame_distance.grid(column=0, row=2, sticky=(tk.W, tk.E, tk.N, tk.S))

label_distance = ttk.Label(
    frame_distance, text="Distance Converter", font=("Arial", 16))
label_distance.grid(column=0, row=0, columnspan=2, pady=(0, 10))

label_distance_value = ttk.Label(frame_distance, text="Enter value:")
label_distance_value.grid(column=0, row=1, sticky=tk.E)

entry_distance = ttk.Entry(frame_distance, width=15)
entry_distance.grid(column=1, row=1, sticky=tk.W)

label_distance_from = ttk.Label(frame_distance, text="From:")
label_distance_from.grid(column=0, row=2, sticky=tk.E)

combo_distance_from = ttk.Combobox(
    frame_distance, values=["Meters", "Kilometers", "Miles"])
combo_distance_from.grid(column=1, row=2, sticky=tk.W)
combo_distance_from.set("Meters")

label_distance_to = ttk.Label(frame_distance, text="To:")
label_distance_to.grid(column=0, row=3, sticky=tk.E)

combo_distance_to = ttk.Combobox(
    frame_distance, values=["Meters", "Kilometers", "Miles"])
combo_distance_to.grid(column=1, row=3, sticky=tk.W)
combo_distance_to.set("Kilometers")

button_convert_distance = ttk.Button(
    frame_distance, text="Convert", command=convert_distance)
button_convert_distance.grid(column=0, row=4, columnspan=2, pady=(10, 0))

label_result_distance = ttk.Label(frame_distance, text="")
label_result_distance.grid(column=0, row=5, columnspan=2, pady=(10, 0))

app.mainloop()
