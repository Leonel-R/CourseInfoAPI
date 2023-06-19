import json
import urllib.request

def retrieve_course(course_name:str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    course_data = json.loads(request.read())
    hours = 0
    exercises = 0
    students = 1
    for week, info in course_data.items():
        if info["students"] > students:
            students = info["students"]
        exercises += info["exercise_total"]
        hours += info["hour_total"]
    course_info = {
        "Weeks" : len(course_data),
        "Total Students" : students,
        "Total Hours" : hours,
        "Average Hours" : hours//students,
        "Total Exercises" : exercises,
        "Average Exercises" : exercises//students
    }
    print(course_info)

# You can retrieve course infromation from the following courses:
# docker18, docker2019, docker2020, beta-dwk-20, ofs2019, CCFUN, fullstack2019, rails2018
retrieve_course("docker2019")
    