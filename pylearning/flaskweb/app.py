from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/season')
def season():
    season = '봄'
    seasons = ['봄', '여름', '가을','겨울']
    return render_template(
            'season.html',
            season=season,
            seasons=seasons
    )

@app.route('/loopindex')
def loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loopindex.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        id = request.form['memberid']
        pwd = request.form['passwd']
        name = request.form['name']
        gender = request.form['gender']
        return render_template('memberlist.html', id=id, pwd=pwd,
                    name=name, gender=gender)
    else:
        return render_template('register.html')

# @app.route('/memberlist')
# def memberlist():
#     return render_template('memberlist.html')

app.run()