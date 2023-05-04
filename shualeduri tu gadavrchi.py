import  sqlite3
connec=sqlite3.connect("survey.sqlite")
cursor=connec.cursor()
selec_rezult=cursor.execute("SELECT * FROM STUDENTS")
# for row in selec_rezult:
#     print(row)
# selec_rezult=cursor.execute("SELECT * FROM STUDENTS WHERE SelfStudyHour >2")
# for row in selec_rezult:
#      print(row)
# cursor.execute("UPDATE students SET Device='gela' WHERE Age >19")
# print(cursor.rowcount)
# connec.commit()
# ID  =18
# Age=13
# OnlineClassTIme=4
# Device="jarti"
# SelfstudyHour="6"
# FitnesTime="0.1"
# Sleep="10"
# SocialMedia="8"
# SocialMediaPlatform="sqplt"
# connec.execute(f"INSERT INTO students ( Age,OnlineClassTIme,Device, SelfstudyHour,FitnessTime,Sleep,SocialMedia,SocialMediaPlatform) VALUES (?,?,?,?,?,?,?,?)",(Age,OnlineClassTIme,Device,SelfstudyHour,FitnesTime,Sleep,SocialMedia,SocialMediaPlatform));

#dav 2
import json

with open('sample.json') as sample_file:
    data = json.load(sample_file)
    person= data["person"]
    eyeColor = person["eyeColor"]
    print("პიროვნების თვალის ფერია:", eyeColor)
    friends=person["friends"]
for friends in person["friends"]:
    print(friends["id"], friends["name"])
def find_field_value(person, field):
    if field not in data[0]:
        print("შეცდომა: ველი '{}' არ არსებობს".format(field))
        return
    for row in person[1:]:
        if field in row:
            print(row[field])
            return
    print("შეცდომა: ველი '{}' ცხრილში ვერ მოიძებნა".format(field))
find_field_value(person,"balance")