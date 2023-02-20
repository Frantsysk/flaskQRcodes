from QRapp import app
from QRapp import qr_gen
from flask import render_template, request, redirect, session, make_response
from QRapp.database.user import add_user, get_user
from QRapp.database.qr_codes import add_qr, get_qr, get_qr_by_id


@app.route('/qr_codes')
def qr_codes():
    user_id = session.get('id')
    all_qr = get_qr(user_id)
    view_qr = list(map(lambda qr: (qr[0], qr[2], qr_gen.generate(qr[2])), all_qr))
    return render_template('qr_codes.html', view_qr=view_qr)


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    user_id = session.get('id')
    data = request.form.get('data')
    qr_img = qr_gen.generate(data)
    qr_id = add_qr(user_id, data)
    return render_template('preview.html', svg=qr_img, qr_id=qr_id)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        row = get_user(username, password)
        if row is not None:
            session['id'] = row[0]
            return redirect('/home')
        else:
            error = 'Incorrect username and/or password'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        add_user(username, email, password)
        return redirect('/home')
    return render_template('register.html')


@app.route('/download', methods=['GET'])
def download():
    user_id = session.get('id')
    if user_id is not None:
        qr_id = request.args.get('id')
        data = get_qr_by_id(qr_id)
        qr_img = qr_gen.generate_png(data)
        qr_res = make_response(qr_img)
        qr_res.headers.set('Content-Type', 'image/png')
        qr_res.headers.set('Content-Disposition', 'attachment', filename='QR.png')
        return qr_res
    else:
        return redirect('register')
