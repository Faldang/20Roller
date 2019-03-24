import tkinter
import Dict

# create root widget, a window
root = tkinter.Tk()

# quit button
quit_button = tkinter.Button(root, text="QUIT", command=quit)
quit_button.pack()

# json encode button
json_button = tkinter.Button(root,
                             text="RUN JSON RUN",
                             command=Dict.json_encode)
json_button.pack()

# keeps it running until exit
root.mainloop()
