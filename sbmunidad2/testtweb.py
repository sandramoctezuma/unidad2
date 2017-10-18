from flask import Flask, render_template, request, redirect
from test_prac import velocidad, aseleracion

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='examen unidad 2')


@app.route('/exec_velocidad', methods=['GET', 'POST'])
def execute() -> 'html':
    l = float(request.form['l'])
    t = float(request.form['t'])
    title = 'volumen'
    result = velocidad (l, t)
    return render_template('result.html',
                           the_title=title,
                           the_l=l,
                           the_t=t,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5002, debug=True)
