import zipfile
import json
import tkinter as tk

#window
root = tk.Tk()
root.geometry("2000x1000")

#canvas
canvas = tk.Canvas(root, width = 2000, height = 1000, bg = "white")
canvas.place(x=0, y=0)

with zipfile.ZipFile('kabeposter.zip', 'r') as zip_data:
    for name in zip_data.namelist():
        if "0000_" in name:
            with zip_data.open(name,'r') as json_file:
                data = json.load(json_file)
                people_data = data["people"]
                person_data1 = people_data[0]
                person_data2 = people_data[1]

   
                canvas.create_line(person_data1["pose_keypoints_2d"][3*1 + 0],
                                   person_data1["pose_keypoints_2d"][3*1 + 1],
                                   person_data1["pose_keypoints_2d"][3*2 + 0],
                                   person_data1["pose_keypoints_2d"][3*2 + 1])
                
                canvas.create_line(person_data1["pose_keypoints_2d"][3*1 + 0],
                                   person_data1["pose_keypoints_2d"][3*1 + 1],
                                   person_data1["pose_keypoints_2d"][3*5 + 0],
                                   person_data1["pose_keypoints_2d"][3*5 + 1])

                
                canvas.create_line(person_data2["pose_keypoints_2d"][3*1 + 0],
                                   person_data2["pose_keypoints_2d"][3*1 + 1],
                                   person_data2["pose_keypoints_2d"][3*2 + 0],
                                   person_data1["pose_keypoints_2d"][3*2 + 1])
                
                canvas.create_line(person_data2["pose_keypoints_2d"][3*1 + 0],
                                   person_data2["pose_keypoints_2d"][3*1 + 1],
                                   person_data2["pose_keypoints_2d"][3*5 + 0],
                                   person_data1["pose_keypoints_2d"][3*5 + 1])

root.mainloop()
