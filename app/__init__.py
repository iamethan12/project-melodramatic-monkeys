import os
import dotenv
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
 
   print(mydb)


isKayla = True

@app.route('/')
def mario_index():
    return render_template('mario_index.html', url=os.getenv("URL"))

@app.route('/mario_about')
def mario_about():
    return render_template('mario_about.html', url=os.getenv("URL"))

@app.route('/mario_experience')
def mario_experience():
    return render_template('mario_experience.html', url=os.getenv("URL"))

@app.route('/mario_education')
def mario_education():
    return render_template('mario_education.html', url=os.getenv("URL"))

@app.route('/mario_hobbies')
def mario_hobbies():
    return render_template('mario_hobbies.html', url=os.getenv("URL"))

@app.route('/mario_places')
def mario_places():
    return render_template('mario_places.html', url=os.getenv("URL"))



@app.route('/kayla')
def kayla_index():
    return render_template('kayla_index.html', url=os.getenv("URL"))

@app.route('/kayla_about')
def kayla_about():
    return render_template('kayla_about.html', url=os.getenv("URL"))

@app.route('/kayla_experience')
def kayla_experience():
    return render_template('kayla_experience.html', url=os.getenv("URL"))

@app.route('/kayla_education')
def kayla_education():
    return render_template('kayla_education.html', url=os.getenv("URL"))

@app.route('/kayla_hobbies')
def kayla_hobbies():
    return render_template('kayla_hobbies.html', url=os.getenv("URL"))

@app.route('/kayla_places')
def kayla_places():
    return render_template('kayla_places.html', url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts':[
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    name = request.form['name']
    
    matches = {
        'timeline_posts':[
            model_to_dict(p)
            for p in TimelinePost.select().where(TimelinePost.name==name)
        ]
    }
    TimelinePost.delete().where(TimelinePost.name==name).execute()
    return matches

@app.route('/timeline')
def timeline():
    return render_template('timeline.html',title="Timeline")

#Database creation and connection
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

