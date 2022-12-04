from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config.update(DB='db\\db.txt')

# user location
xloc, yloc = 350, 150

# kickboard : id, x, y, bat, T/F
def get_kickboard():
    with open(app.config['DB']) as f:
        klist = f.read().splitlines()
    return [i.split() for i in klist]


def save_kickboard(klist):
    with open(app.config['DB'], 'w') as f:
        for k in klist:
            f.write(' '.join(k) + '\n')


def add_kickboard(*arg):
    with open(app.config['DB'], 'a') as f:
        f.write(' '.join(arg))


def sorted_get_kickboard(x, y):
    with open(app.config['DB']) as f:
        klist = f.read().splitlines()
    return sorted(filter(lambda t: (t[4] == "T" and int(t[3]) > 25), [i.split() for i in klist]),
                  key=lambda t: (int(t[1]) - int(x)) ** 2 + (int(t[2]) - int(y)) ** 2, reverse=True)


def use_kickboard(kid, end=False):
    klist = get_kickboard()
    id_list = [i[0] for i in klist]
    if kid in id_list:
        klist[id_list.index(kid)][-1] = 'T' if end else 'F'
    save_kickboard(klist)


@app.route("/")
def login():
    return render_template("login.html")


@app.route('/loginresult', methods=['POST'])
def loginresult():
    return redirect('/ui')


@app.route('/uiresult', methods=['POST'])
def uiresult():
    return redirect(url_for('ui', x=request.form['x'], y=request.form['y']))


@app.route('/chkick', methods=['POST'])
def chkick():
    use_kickboard(request.form['kickid'], end=False if request.form['type'] == 'T' else True)
    return redirect(url_for('ui', x=request.form['x'], y=request.form['y'], nowkick=request.form['kickid']))


@app.route("/ui")
def ui():
    x = request.args.get('x')
    y = request.args.get('y')
    if x is None and y is None:
        return render_template("uib.html", klist=get_kickboard(), x=xloc, y=yloc)
    else:
        return render_template("uia.html", klist=sorted_get_kickboard(x, y)[:5], x=xloc, y=yloc)


@app.route("/admin")
def admin():
    return render_template("admin.html", klist=get_kickboard())



@app.route("/adresult", methods=["POST"])
def adresult():
    pass