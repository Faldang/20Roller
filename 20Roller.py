import tkinter
# import Dict


# def multiply(x):
#     output_label['text'] = str(x*2)


# create root widget, a window
root = tkinter.Tk()
root.title('DnD4 to Radiance Monster Converter')
root.state('zoomed')

first_frame = tkinter.Frame(root)
first_frame.place(relheight=0.05, relwidth=1, rely=0)
second_frame = tkinter.Frame(root)
second_frame.place(relheight=0.05, relwidth=1, rely=0.05)
third_frame = tkinter.Frame(root)
third_frame.place(relheight=0.05, relwidth=1, rely=0.1)
fourth_frame = tkinter.Frame(root)
fourth_frame.place(relheight=0.05, relwidth=1, rely=0.15)
eighth_frame = tkinter.Frame(root)
eighth_frame.place(relheight=0.05, relwidth=1, rely=0.2)
fifth_frame = tkinter.Frame(root)
fifth_frame.place(relheight=0.05, relwidth=1, rely=0.25)
sixth_frame = tkinter.Frame(root)
sixth_frame.place(relheight=0.05, relwidth=1, rely=0.3)
seventh_frame = tkinter.Frame(root)
seventh_frame.place(relheight=0.6, relwidth=1, rely=0.35)
ninth_frame = tkinter.Frame(root)
ninth_frame.place(relheight=0.05, relwidth=1, rely=0.95)

name_label = tkinter.Label(first_frame, text="Name")
name_label.place(relx=0, relwidth=0.13)
name_input = tkinter.Entry(first_frame)
name_input.place(relx=0.13, relwidth=0.2)

level_label = tkinter.Label(first_frame, text="Level")
level_label.place(relwidth=0.13, relx=0.33)
level_input = tkinter.Spinbox(first_frame, from_=1, to=30)
level_input.place(relwidth=0.2, relx=0.46)

class_label = tkinter.Label(first_frame, text="Class")
class_label.place(relwidth=0.13, relx=0.66)
class_input = tkinter.Entry(first_frame)
class_input.place(relwidth=0.2, relx=0.8)

size_label = tkinter.Label(second_frame, text="Size")
size_label.place(relx=0, relwidth=0.13)
size_input = tkinter.Spinbox(second_frame, values=("Tiny", "Small", "Medium",
                                                   "Large", "Huge",
                                                   "Gargantuan"), wrap=True)
size_input.place(relx=0.13, relwidth=0.2)

race_label = tkinter.Label(second_frame, text="Race")
race_label.place(relx=0.33, relwidth=0.13)
race_input = tkinter.Entry(second_frame)
race_input.place(relx=0.46, relwidth=0.2)

initiative_label = tkinter.Label(third_frame, text="Initiative")
initiative_label.place(relx=0, relwidth=0.13)
initiative_input = tkinter.Entry(third_frame)
initiative_input.place(relx=0.13, relwidth=0.2)

senses_label = tkinter.Label(third_frame, text="Senses")
senses_label.place(relx=0.33, relwidth=0.13)
senses_input = tkinter.Entry(third_frame)
senses_input.place(relx=0.46, relwidth=0.2)

ac_label = tkinter.Label(fourth_frame, text="Armor Class")
ac_label.place(relx=0, relwidth=0.13)
ac_input = tkinter.Entry(fourth_frame)
ac_input.place(relx=0.13, relwidth=0.2)

fort_label = tkinter.Label(fourth_frame, text="Fortitude")
fort_label.place(relx=0.33, relwidth=0.13)
fort_input = tkinter.Entry(fourth_frame)
fort_input.place(relx=0.46, relwidth=0.2)

ref_label = tkinter.Label(eighth_frame, text="Reflex")
ref_label.place(relx=0, relwidth=0.13)
ref_input = tkinter.Entry(eighth_frame)
ref_input.place(relx=0.13, relwidth=0.2)

will_label = tkinter.Label(eighth_frame, text="Will")
will_label.place(relx=0.33, relwidth=0.13)
will_input = tkinter.Entry(eighth_frame)
will_input.place(relx=0.46, relwidth=0.2)

spd_label = tkinter.Label(fifth_frame, text="Speed")
spd_label.place(relx=0, relwidth=0.13)
spd_input = tkinter.Entry(fifth_frame)
spd_input.insert('end', '6')
spd_input.place(relx=0.13, relwidth=0.2)

ap_label = tkinter.Label(fifth_frame, text="Action Points")
ap_label.place(relx=0.33, relwidth=0.13)
ap_input = tkinter.Entry(fifth_frame)
ap_input.insert('end', '0')
ap_input.place(relx=0.46, relwidth=0.2)

align_label = tkinter.Label(sixth_frame, text="Alignment")
align_label.place(relx=0, relwidth=0.13)
align_input = tkinter.Spinbox(sixth_frame, values=("Lawful good",
                                                   "Lawful neutral",
                                                   "Lawful evil",
                                                   "Neutral good",
                                                   "True neutral",
                                                   "Neutral evil",
                                                   "Chaotic good",
                                                   "Chaotic neutral",
                                                   "Chaotic evil"), wrap=True)
align_input.place(relx=0.13, relwidth=0.2)

lang_label = tkinter.Label(sixth_frame, text="Languages")
lang_label.place(relx=0.33, relwidth=0.13)
lang_input = tkinter.Entry(sixth_frame)
lang_input.place(relx=0.46, relwidth=0.2)

acrobatics_label = tkinter.Label(seventh_frame, text="Acrobatics")
acrobatics_label.place(relx=0, relwidth=0.13, rely=0, relheight=0.1)
acrobatics_input = tkinter.Entry(seventh_frame)
acrobatics_input.insert('end', '0')
acrobatics_input.place(relx=0.13, relwidth=0.2, rely=0, relheight=0.1)

arcana_label = tkinter.Label(seventh_frame, text="Arcana")
arcana_label.place(relx=0, relwidth=0.13, rely=0.1, relheight=0.1)
arcana_input = tkinter.Entry(seventh_frame)
arcana_input.insert('end', '0')
arcana_input.place(relx=0.13, relwidth=0.2, rely=0.1, relheight=0.1)

athletics_label = tkinter.Label(seventh_frame, text="Athletics")
athletics_label.place(relx=0, relwidth=0.13, rely=0.2, relheight=0.1)
athletics_input = tkinter.Entry(seventh_frame)
athletics_input.insert('end', '0')
athletics_input.place(relx=0.13, relwidth=0.2, rely=0.2, relheight=0.1)

bluff_label = tkinter.Label(seventh_frame, text="Bluff")
bluff_label.place(relx=0, relwidth=0.13, rely=0.3, relheight=0.1)
bluff_input = tkinter.Entry(seventh_frame)
bluff_input.insert('end', '0')
bluff_input.place(relx=0.13, relwidth=0.2, rely=0.3, relheight=0.1)

diplomacy_label = tkinter.Label(seventh_frame, text="Diplomacy")
diplomacy_label.place(relx=0, relwidth=0.13, rely=0.4, relheight=0.1)
diplomacy_input = tkinter.Entry(seventh_frame)
diplomacy_input.insert('end', '0')
diplomacy_input.place(relx=0.13, relwidth=0.2, rely=0.4, relheight=0.1)

dungeoneering_label = tkinter.Label(seventh_frame, text="Dungeoneering")
dungeoneering_label.place(relx=0, relwidth=0.13, rely=0.5, relheight=0.1)
dungeoneering_input = tkinter.Entry(seventh_frame)
dungeoneering_input.insert('end', '0')
dungeoneering_input.place(relx=0.13, relwidth=0.2, rely=0.5, relheight=0.1)

endurance_label = tkinter.Label(seventh_frame, text="Endurance")
endurance_label.place(relx=0, relwidth=0.13, rely=0.6, relheight=0.1)
endurance_input = tkinter.Entry(seventh_frame)
endurance_input.insert('end', '0')
endurance_input.place(relx=0.13, relwidth=0.2, rely=0.6, relheight=0.1)

heal_label = tkinter.Label(seventh_frame, text="Heal")
heal_label.place(relx=0, relwidth=0.13, rely=0.7, relheight=0.1)
heal_input = tkinter.Entry(seventh_frame)
heal_input.insert('end', '0')
heal_input.place(relx=0.13, relwidth=0.2, rely=0.7, relheight=0.1)

history_label = tkinter.Label(seventh_frame, text="History")
history_label.place(relx=0, relwidth=0.13, rely=0.8, relheight=0.1)
history_input = tkinter.Entry(seventh_frame)
history_input.insert('end', '0')
history_input.place(relx=0.13, relwidth=0.2, rely=0.8, relheight=0.1)

insight_label = tkinter.Label(seventh_frame, text="Insight")
insight_label.place(relx=0.33, relwidth=0.13, rely=0, relheight=0.1)
insight_input = tkinter.Entry(seventh_frame)
insight_input.insert('end', '0')
insight_input.place(relx=0.46, relwidth=0.2, rely=0, relheight=0.1)

intimidate_label = tkinter.Label(seventh_frame, text="Intimidate")
intimidate_label.place(relx=0.33, relwidth=0.13, rely=0.1, relheight=0.1)
intimidate_input = tkinter.Entry(seventh_frame)
intimidate_input.insert('end', '0')
intimidate_input.place(relx=0.46, relwidth=0.2, rely=0.1, relheight=0.1)

nature_label = tkinter.Label(seventh_frame, text="Nature")
nature_label.place(relx=0.33, relwidth=0.13, rely=0.2, relheight=0.1)
nature_input = tkinter.Entry(seventh_frame)
nature_input.insert('end', '0')
nature_input.place(relx=0.46, relwidth=0.2, rely=0.2, relheight=0.1)

perception_label = tkinter.Label(seventh_frame, text="Perception")
perception_label.place(relx=0.33, relwidth=0.13, rely=0.3, relheight=0.1)
perception_input = tkinter.Entry(seventh_frame)
perception_input.insert('end', '0')
perception_input.place(relx=0.46, relwidth=0.2, rely=0.3, relheight=0.1)

religion_label = tkinter.Label(seventh_frame, text="Religion")
religion_label.place(relx=0.33, relwidth=0.13, rely=0.4, relheight=0.1)
religion_input = tkinter.Entry(seventh_frame)
religion_input.insert('end', '0')
religion_input.place(relx=0.46, relwidth=0.2, rely=0.4, relheight=0.1)

stealth_label = tkinter.Label(seventh_frame, text="Stealth")
stealth_label.place(relx=0.33, relwidth=0.13, rely=0.5, relheight=0.1)
stealth_input = tkinter.Entry(seventh_frame)
stealth_input.insert('end', '0')
stealth_input.place(relx=0.46, relwidth=0.2, rely=0.5, relheight=0.1)

streetwise_label = tkinter.Label(seventh_frame, text="Streetwise")
streetwise_label.place(relx=0.33, relwidth=0.13, rely=0.6, relheight=0.1)
streetwise_input = tkinter.Entry(seventh_frame)
streetwise_input.insert('end', '0')
streetwise_input.place(relx=0.46, relwidth=0.2, rely=0.6, relheight=0.1)

trick_label = tkinter.Label(seventh_frame, text="Thievery")
trick_label.place(relx=0.33, relwidth=0.13, rely=0.7, relheight=0.1)
trick_input = tkinter.Entry(seventh_frame)
trick_input.insert('end', '0')
trick_input.place(relx=0.46, relwidth=0.2, rely=0.7, relheight=0.1)

strength_label = tkinter.Label(seventh_frame, text="Strength")
strength_label.place(relx=0.66, relwidth=0.13, rely=0, relheight=0.1)
strength_input = tkinter.Entry(seventh_frame)
strength_input.insert('end', '0')
strength_input.place(relx=0.79, relwidth=0.2, rely=0, relheight=0.1)

constitution_label = tkinter.Label(seventh_frame, text="Constitution")
constitution_label.place(relx=0.66, relwidth=0.13, rely=0.1, relheight=0.1)
constitution_input = tkinter.Entry(seventh_frame)
constitution_input.insert('end', '0')
constitution_input.place(relx=0.79, relwidth=0.2, rely=0.1, relheight=0.1)

dexterity_label = tkinter.Label(seventh_frame, text="Dexterity")
dexterity_label.place(relx=0.66, relwidth=0.13, rely=0.2, relheight=0.1)
dexterity_input = tkinter.Entry(seventh_frame)
dexterity_input.insert('end', '0')
dexterity_input.place(relx=0.79, relwidth=0.2, rely=0.2, relheight=0.1)

intelligence_label = tkinter.Label(seventh_frame, text="Intelligence")
intelligence_label.place(relx=0.66, relwidth=0.13, rely=0.3, relheight=0.1)
intelligence_input = tkinter.Entry(seventh_frame)
intelligence_input.insert('end', '0')
intelligence_input.place(relx=0.79, relwidth=0.2, rely=0.3, relheight=0.1)

wisdom_label = tkinter.Label(seventh_frame, text="Wisdom")
wisdom_label.place(relx=0.66, relwidth=0.13, rely=0.4, relheight=0.1)
wisdom_input = tkinter.Entry(seventh_frame)
wisdom_input.insert('end', '0')
wisdom_input.place(relx=0.79, relwidth=0.2, rely=0.4, relheight=0.1)

charisma_label = tkinter.Label(seventh_frame, text="Charisma")
charisma_label.place(relx=0.66, relwidth=0.13, rely=0.5, relheight=0.1)
charisma_input = tkinter.Entry(seventh_frame)
charisma_input.insert('end', '0')
charisma_input.place(relx=0.79, relwidth=0.2, rely=0.5, relheight=0.1)

equipment_label = tkinter.Label(seventh_frame, text="Equipment")
equipment_label.place(relx=0.66, relwidth=0.13, rely=0.6, relheight=0.1)
equipment_input = tkinter.Entry(seventh_frame)
equipment_input.place(relx=0.79, relwidth=0.2, rely=0.6, relheight=0.1)

# _label = tkinter.Label(, text="")
# _label.place(relx=0, relwidth=0)
# _input = tkinter.Entry()
# _input.place(relx=0, relwidth=0)


# button = tkinter.Button(first_frame, text="Button",
#                         command=lambda: multiply(int(input_box.get())))
# button.place(relx=0.45, rely=0, relwidth=0.1, relheight=0.5)

# output_label = tkinter.Label(first_frame)
# output_label.place(relx=0.6, rely=0, relwidth=0.3, relheight=0.5)

# quit button
# quit_button = tkinter.Button(root, text="QUIT", command=quit)
# quit_button.pack()
#
# # json encode button
# json_button = tkinter.Button(root,
#                              text="RUN JSON RUN",
#                              command=Dict.json_encode)
# json_button.pack()

# keeps it running until exit
root.mainloop()
