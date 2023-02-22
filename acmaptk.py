from appJar import gui 
import json
import customtkinter
import tkintermapview
import tkinter
# Load race data from JSON file
with open('acdata.json') as f:
    data = json.load(f)

# Define function to populate table with race data
td = [pc['name:']for pc in data['tracks']]
print(td)

app = tkinter.Tk()
app.title("TK AC MAPS")
app.geometry(f"{800}x{600}")

map = tkintermapview.TkinterMapView(app, width=800, height=500, corner_radius=0)
map.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

input = customtkinter.CTkEntry(app)
input.place(relx=0.5, rely=0.5, anchor=tkinter.)
app.mainloop()