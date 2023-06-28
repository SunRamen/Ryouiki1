import zipfile
import json

with zipfile.ZipFile('kabeposter.zip', 'r') as zip_data:
    for name in zip_data.namelist():
        if "0000_" in name:
            with zip_data.open(name,'r') as json_file:
                data = json.load(json_file)
                people_data = data["people"]
                person_data1 = people_data[0]
                person_data2 = people_data[1]

                print("1人目: X座標= ",person_data1["pose_keypoints_2d"][3*0 + 0])
                print("1人目: y座標= ",person_data1["pose_keypoints_2d"][3*0 + 1])
                print("1人目: 信頼度= ",person_data1["pose_keypoints_2d"][3*0 + 2])
                
                print("2人目: X座標= ",person_data2["pose_keypoints_2d"][3*0 + 0])
                print("2人目: y座標= ",person_data2["pose_keypoints_2d"][3*0 + 1])
                print("2人目: 信頼度= ",person_data2["pose_keypoints_2d"][3*0 + 2])
                