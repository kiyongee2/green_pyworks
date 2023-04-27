from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/season', methods=['GET'])
def season():
    season = '봄'
    seasons = ['봄', '여름', '가을','겨울']
    return render_template(
            'season.html',
            season=season,
            seasons=seasons
    )

@app.route('/loopindex', methods=['GET'])
def loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loopindex.html', items=items)

@app.route('/even_odd', methods=['GET', 'POST'])
def even_odd():
    #try ~ except ~ else 구문
    if request.method == 'POST':
        try:
            num = int(request.form['num'])
        except ValueError:
            error_message = "숫자를 입력해주세요"
            return render_template('even_odd.html', error_msg=error_message)
        else:
            if num % 2 == 0:
                result = "짝수입니다"
            else:
                result = "홀수입니다"
            return render_template('calc_result.html', num=num, result=result)
    else:
        return render_template('even_odd.html')

    """
    if request.method == 'POST':
        num = int(request.form['num'])
        if num % 2 == 0:
            result = "짝수입니다"
        else:
            result = "홀수입니다"
        return render_template('calc_result.html', num=num, result=result)
    else:
        return render_template('even_odd.html')
    """

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

app.run()