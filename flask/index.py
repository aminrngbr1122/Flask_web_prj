from flask import Flask, request, render_template, redirect, send_file, url_for
from tmp.tools.flask.database import *

app = Flask(__name__, template_folder='tmp')


@app.route('/')
def rspindex():
    return redirect(url_for('index'))


@app.route('/index', methods=['GET', 'POST'])
def index():
    # Result rsp
    data = info
    return render_template('index.html', title=data['title'], lenS=data['lens']), 200


@app.errorhandler(404)
@app.errorhandler(405)
def rsperror(e):
    return redirect(url_for('index'))


@app.route('/tools/<filename>')
def send_tools(filename):
    return send_file(f'tmp\\tools\\{filename}', as_attachment=True)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80, debug=True)
