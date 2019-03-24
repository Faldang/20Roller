# import json
#
# a = input("unesi poop:\n")
# print(a)
#
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#         }
#     }
#
# json_string = json.dumps(data, indent=4)
# print(json_string)

import tkinter as tk


def write_slogan():
    print("Ovo je print poop")


# create root widget, a window
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="QUIT", command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame, text="Hello", command=write_slogan)
slogan.pack(side=tk.LEFT)

w = tk.Label(root, text="Hello Poop")
w.pack()

# keeps it running until exit
root.mainloop()
