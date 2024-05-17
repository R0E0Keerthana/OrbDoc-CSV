from flask import Flask, request, render_template, url_for, redirect
import csv
app = Flask(__name__,template_folder = "templates") 

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/assessment', methods=['GET','POST'])
def assessment():
    if request.method == 'GET':
        return render_template("index.html") # to display form
    elif request.method == 'POST': # after submit
        email = request.form.get("email") # to get email from form
        like = request.form.get('like') # to get boolean value from form
        if like == "yes":
            like = True
        else:
            like = False
        fav_num = request.form.get("fav") # to get favourite number from form
        with open("cust_disc.csv", mode='a+', newline="") as file: # to apppend contents
            file_writer = csv.writer(file, delimiter =',') # to write
            file_reader = csv.reader(file, delimiter =',') # to read
            file.seek(0) # to search from beginning of the file
            for row in file_reader: # to traverse
                if row[0] == email: # if already exits
                    return render_template("result.html",alert_msg="Thank You, we already have your preference stored!")
            else: #else write in csv file
                file_writer.writerow([email,like,fav_num])
                return render_template("result.html",alert_msg="Thank You, Your preference has been stored successfully!")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5555, debug = False) #debug = true while developing
