from tkinter import *
from function import  *
from data import *

cor_x, cor_y = get_loc()
if cor_x != 0 and cor_y != 0:
    dis_dict = {}
    for key, value in location_canteens.items():
        distance = distance_a_b((cor_x, cor_y), value)  # calculate distance to each canteen
        dis_dict[key]= distance # add calculated distance to dis_dict
    new_root = Tk()
    new_root.title("LIST OF CANTEEN & DISTANCE")
    for widget in new_root.winfo_children():
        widget.destroy()
    sorted_distance = sort_distance(dis_dict)
    for k in sorted_distance:  # sort by distance
        Label(new_root,text = "Distance to {} is: {} m.".format(k, round(sorted_distance[k] / 138 * 200))).grid(sticky='n')
    Button(new_root, text='close', command=new_root.destroy).grid(sticky='s')
else:
    new_root = Tk()
    new_root.title("LIST OF CANTEEN & DISTANCE")
    Label(new_root, text="You haven't click any position!").grid(sticky='n')
    Button(new_root, text='close', command=new_root.destroy).grid(sticky='s')