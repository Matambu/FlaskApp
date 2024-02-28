from flask import Flask, render_template, url_for, flash, redirect
from forms import UserDetailsForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'psMsFJX3K6zwDchi'

posts = [
    {
        'player': 'Kylian Mbappe',
        'club': 'PSG',
        'position': 'Forward'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = UserDetailsForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/loginpage")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login Page', form=form)




if __name__ == '__main__':
    app.run(debug=True)