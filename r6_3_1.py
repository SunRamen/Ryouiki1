import zipfile
import json
import tkinter as tk
import time

#window
root = tk.Tk()
root.geometry("800x600")

#canvas
canvas = tk.Canvas(root, width = 800, height = 600, bg = "white")
canvas.place(x=0, y=0)

people1=[]
people2=[]


with zipfile.ZipFile('kabeposter.zip', 'r') as zip_data:
    for name in zip_data.namelist():
        if "0000" in name:
            with zip_data.open(name,'r') as json_file:
                
                data = json.load(json_file)
                
                people_data = data["people"]
                people1.append(people_data[0])
                people2.append(people_data[1])

n=0                
def human():
    global n
        
    person_data1 = people1[n]
    person_data2 = people2[n]   

    canvas.create_rectangle(0,0,800,600,fill = 'White')

    for i in range(4):
        canvas.create_line(person_data1["pose_keypoints_2d"][3*i + 0]/2,
                            person_data1["pose_keypoints_2d"][3*i + 1]/2,
                            person_data1["pose_keypoints_2d"][3*(i+1) + 0]/2,
                            person_data1["pose_keypoints_2d"][3*(i+1) + 1]/2)
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*1 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*1 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*5 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*5 + 1]/2)
                        
    for i in range(2):
        canvas.create_line(person_data1["pose_keypoints_2d"][3*(i+5) + 0]/2,
                            person_data1["pose_keypoints_2d"][3*(i+5) + 1]/2,
                            person_data1["pose_keypoints_2d"][3*(i+6) + 0]/2,
                            person_data1["pose_keypoints_2d"][3*(i+6) + 1]/2)
    for i in range(2): 
        canvas.create_line(person_data1["pose_keypoints_2d"][3*(i+8) + 0]/2,
                            person_data1["pose_keypoints_2d"][3*(i+8) + 1]/2,
                            person_data1["pose_keypoints_2d"][3*(i+9) + 0]/2,
                            person_data1["pose_keypoints_2d"][3*(i+9) + 1]/2)
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*8 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*8 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*12 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*12 + 1]/2)
                            
    for i in range(1):
        canvas.create_line(person_data1["pose_keypoints_2d"][3*(i+12) + 0]/2,
                            person_data1["pose_keypoints_2d"][3*(i+12) + 1]/2,
                            person_data1["pose_keypoints_2d"][3*(i+13) + 0]/2,
                            person_data1["pose_keypoints_2d"][3*(i+13) + 1]/2)
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*14 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*14 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*21 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*21 + 1]/2)                                      
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*14 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*14 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*19 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*19 + 1]/2)
                    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*19 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*19 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*20 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*20 + 1]/2)
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*0 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*0 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*15 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*15 + 1]/2)
                                                
    canvas.create_line(person_data1["pose_keypoints_2d"][3*0 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*0 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*16 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*16 + 1]/2)
                                                
    canvas.create_line(person_data1["pose_keypoints_2d"][3*15 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*15 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*17 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*17 + 1]/2)
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*1 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*1 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*8 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*8 + 1]/2) 

    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*16 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*16 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*18 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*18 + 1]/2)
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*11 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*11 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*24 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*24 + 1]/2)
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*11 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*11 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*22 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*22 + 1]/2)
    
    canvas.create_line(person_data1["pose_keypoints_2d"][3*22 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*22 + 1]/2,
                        person_data1["pose_keypoints_2d"][3*23 + 0]/2,
                        person_data1["pose_keypoints_2d"][3*23 + 1]/2)
                                            
    for i in range(4):
        canvas.create_line(person_data2["pose_keypoints_2d"][3*i + 0]/2,
                        person_data2["pose_keypoints_2d"][3*i + 1]/2,
                        person_data2["pose_keypoints_2d"][3*(i+1) + 0]/2,
                        person_data2["pose_keypoints_2d"][3*(i+1) + 1]/2)
        
    canvas.create_line(person_data2["pose_keypoints_2d"][3*1 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*1 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*5 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*5 + 1]/2)
        
    for i in range(2):
        canvas.create_line(person_data2["pose_keypoints_2d"][3*(i+5) + 0]/2,
                            person_data2["pose_keypoints_2d"][3*(i+5) + 1]/2,
                            person_data2["pose_keypoints_2d"][3*(i+6) + 0]/2,
                            person_data2["pose_keypoints_2d"][3*(i+6) + 1]/2)
    for i in range(2): 
        canvas.create_line(person_data2["pose_keypoints_2d"][3*(i+8) + 0]/2,
                            person_data2["pose_keypoints_2d"][3*(i+8) + 1]/2,
                            person_data2["pose_keypoints_2d"][3*(i+9) + 0]/2,
                            person_data2["pose_keypoints_2d"][3*(i+9) + 1]/2)
    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*8 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*8 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*12 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*12 + 1]/2)
                            
    for i in range(1):
        canvas.create_line(person_data2["pose_keypoints_2d"][3*(i+12) + 0]/2,
                            person_data2["pose_keypoints_2d"][3*(i+12) + 1]/2,
                            person_data2["pose_keypoints_2d"][3*(i+13) + 0]/2,
                            person_data2["pose_keypoints_2d"][3*(i+13) + 1]/2)
    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*14 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*14 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*21 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*21 + 1]/2)                                      
    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*14 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*14 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*19 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*19 + 1]/2)
    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*19 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*19 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*20 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*20 + 1]/2)
    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*0 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*0 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*15 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*15 + 1]/2)
                                                
    canvas.create_line(person_data2["pose_keypoints_2d"][3*0 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*0 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*16 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*16 + 1]/2)
                                                
    canvas.create_line(person_data2["pose_keypoints_2d"][3*15 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*15 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*17 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*17 + 1]/2)
    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*1 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*1 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*8 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*8 + 1]/2)
    canvas.create_line(person_data2["pose_keypoints_2d"][3*16 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*16 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*18 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*18 + 1]/2)
                    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*11 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*11 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*24 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*24 + 1]/2)
    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*11 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*11 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*22 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*22 + 1]/2)
    
    canvas.create_line(person_data2["pose_keypoints_2d"][3*22 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*22 + 1]/2,
                        person_data2["pose_keypoints_2d"][3*23 + 0]/2,
                        person_data2["pose_keypoints_2d"][3*23 + 1]/2)
    n += 1
    root.after(3,human)

root.after(3,human)
root.mainloop()