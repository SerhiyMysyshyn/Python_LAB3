from array import array

from flask import Flask, render_template
from datetime import datetime
import os
import sys
import platform

app = Flask(__name__)

def getFooterData():
    OS_info = os.name + " " + platform.system() + " " + platform.release()
    current_datetime = datetime.now()
    pythonVersion = sys.version
    return [OS_info, pythonVersion, current_datetime]

skills = ["Java Core and Pro", "MySQL", "SQL", "Kotlin", "Dagger 2", "OOP", "MVP", "MVVM", "REST-API", "Unit Testing",
          "RXJava", "Retrofit", "Git", "AndroidX", "Room Database", "UI layout / UI style xml", "Android SDK", "Google Maps / OSM API", "HTML / CSS / JS"]

projectsData = [
    {
        'name': 'Password Reminder',
        'imageURL': '/static/images/prog1.png',
        'android': 'Android 5.0',
        'description': 'Програма створена для збереження Ваших паролів та нагадування їх випадку, якщо Ви забули один із них!'
    },
    {
        'name': 'Cocomo/Cocomo II Calculator',
        'imageURL': '/static/images/prog2.png',
        'android': 'Android 5.0',
        'description': 'Програма створена для обчисленя трудоємності створення програм за допомогою калькуляторів Cocomo, Cocomo2 та Functional Points!'
    },
    {
        'name': 'Simple Weather',
        'imageURL': '/static/images/prog3.png',
        'android': 'Android 4.4',
        'description': 'Програма створена для відображення погоди в різних містах світу!'
    }
]

@app.route('/')
def home():
    return render_template('home.html', data=getFooterData())

@app.route('/about/')
def about():
    return render_template('about.html', data=getFooterData(), skills=skills)

@app.route('/myworks/')
def myworks():
    return render_template('myworks.html', data=getFooterData(), projectsData=projectsData)

if __name__ == '__main__':
    app.run(debug=True)