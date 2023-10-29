from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/bot")
def bot():
    return render_template('bot.html')

# Add a route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    name = request.form['name']
    language = request.form['email']
    location = request.form['loc']
    charge = request.form['charge']
    time = request.form['time']
    practise = request.form['prac']
    demograph = request.form['demograph']
    flaw = request.form['flaw']
    feedback = request.form['feedback']



    # Store data in a CSV file
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, language,location,charge,time,practise,demograph,flaw,feedback])

    return 'Data has been saved successfully.'

if __name__ == "__main__":
    app.run(debug=True)