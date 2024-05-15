from tkinter import *
from PIL import Image, ImageTk
import csv
from Harvensine import Distance_Haversine
from CSP import CSP

_OPTIONS = [
    "Burn Center",
    "Cardiac Emergency",
    "Dental Emergency",
    "Diabetology Emergency",
    "General Emergency",
    "Gastrointestinal Emergency",
    "Gynecology Emergency",
    "Infectious Disease Emergency",
    "Medical-Surgical Emergency",
    "Medical-Surgical Emergency",
    "Neurological Emergency",
    "Ophtalmology Emergency",
    "ORL",
    "Orthopedic Emergencies",
    "Pediatric Emergency",
    "Psyciatric Emergency",
    "Renadial Hemodialysis",
    "respiratory emergencies",
    "Trauma center"
]

_options = [
    "5",
    "10",
    "15",
    "20",
    "25",
    "30"]

master = Tk()
master.geometry("500x700") 
master.title("Service Menu")  

img = Image.open("doctor.jpg")
photo = ImageTk.PhotoImage(img)

canvas = Canvas(master, width=master.winfo_width(), height=master.winfo_height())
canvas.pack(fill="both", expand=True)

img_x = (master.winfo_width() - img.width)/ 2 + 80
img_y = (master.winfo_height() - img.height) / 2 + 180

canvas.create_image(img_x, img_y, image=photo, anchor="nw")

label1 = Label(master, text="Please select the needed information:")
label1.pack(pady=10)  
label1.config(font=("Arial", 16))
label2 = Label(master, text="enter your coordinates:")
label2.pack(pady=20)  
label2.config(font=("Arial", 16))


def store_selected_information():
    global selected_service
    selected_service = str(variable.get())
    global max_distance
    max_distance = int(distance.get())*1000 
    entered_coordinates = coordinates.get()
    global x
    global y
    x, y = entered_coordinates.split(',')
    master.destroy()
    

variable = StringVar(master)
variable.set("Medical service") # ask user for the needed service 

distance = StringVar(master)
distance.set("Maximum distance(Km)") #ask the user to enter his distance according to which we'll select the field of search  

coordinates = StringVar(master)

c = Entry(master, textvariable=coordinates)
c.config(font=("Arial", 14), bg="#B9D9EB", fg="black", width=25)
c.pack(pady=25)
# Create the OptionMenu widget
w = OptionMenu(master, variable, *_OPTIONS)
w.config(font=("Arial", 14), bg="#B9D9EB", fg="black", width=20)  # Configure visual properties
z = OptionMenu(master, distance, *_options)
z.config(font=("Arial", 14), bg="#B9D9EB", fg="black", width=20)  # Configure visual properties


w.pack(pady=20)
z.pack(pady=20)
button = Button( master, text = "select" , command = store_selected_information,bg="#ffffff", fg="#72A0C1", font=("Arial", 14), padx=10, pady=5, borderwidth=-1,relief="raised").pack()

label = Label(master, text=" ")
service = label.pack()
mainloop()

constraints = (selected_service,max_distance)

with open("Hospitals_Clinics.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    all_hospitals = []
    # ID,commune,facility,coordinates,services,Capacity
    for hospital in csv_reader:
      
  
      ID, _, facility, coordinates, services, Capacity = hospital
      
      X, Y = coordinates.split(",")
      distance = Distance_Haversine((float(x), float(y)), (float(X), float(Y)))
      services_string = services.strip('"""')
      services_list = [service.strip() for service in services_string.split(',')]
      #print(services_list)
      
      dict= {
      "name": facility,
      "id":int(ID),
      "distance":float(distance),
      "service":services_list,
      "capacity":int(Capacity)
      
      }
      all_hospitals.append(dict)
      
    

problem = CSP(all_hospitals,constraints)
hospital = problem.best_hospital()
print(hospital)
#36.74484690762721,3.03621889932779
if hospital is None:
    print("No hospital found that satisfies the given constraints.")
else:
    print("The best hospital to this bnadem: ")
    for key, item in hospital.items():
        print(f"{key}--->{item}")
