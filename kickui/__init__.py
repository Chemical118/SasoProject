from flask import Flask, render_template, request

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config.update(DB='db/db.txt')


# kickboard : x, y, bat, T/F
def get_kickboard():
    with open(app.config['DB']) as f:
        klist = f.read().splitlines()
    return [i.split() for i in klist]


def save_kickboard(klist):
    with open(app.config['DB'], 'w') as f:
        for k in klist:
            f.write(' '.join(k))


def add_kickboard(*arg):
    with open(app.config['DB'], 'a') as f:
        f.write(' '.join(arg))


def sort_kickboard(x, y):
    with open(app.config['DB']) as f:
        klist = f.read().splitlines()
    return sorted(filter(lambda t: (t[3] == "T" and int(t[2]) > 30), [i.split() for i in klist]),
                  key=lambda t: (int(t[0] - x)) ** 2 + (int(t[1] - y)) ** 2)


@app.route("/admin")
def result():
    return render_template("admin.html", klist=get_kickboard())


@app.route("/adresult", methods=["POST"])
def adresult():
    pass
