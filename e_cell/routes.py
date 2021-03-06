from flask import Flask,render_template, url_for, redirect, request,send_file,flash
from e_cell import app,db
from e_cell.forms import Startup_Registration
from e_cell.models import StartUp
from io import BytesIO


#the route where user can register their startups
@app.route("/register",methods=['GET','POST'])
def register():
	form = Startup_Registration() #the registration form is passed to the registration page
	
	if form.validate_on_submit():
		file=request.files['inputfile'] #inputfile is the name used in the startup_register.html file for taking document as input
		startup= StartUp(startup_name=form.startup_name.data,poc_name=form.poc_name.data,poc_email=form.poc_email.data,poc_phone_no=form.poc_phone_no.data,profile_doc=file.read(),incentive=form.incentive.data,duration=form.duration.data,website=form.website.data)
		db.session.add(startup)
		db.session.commit()
		flash(f'Congrats your Startup "{form.startup_name.data}" is added.. To see the list of startups click STARTUPS button','success')
		return redirect(url_for('register'))
	return render_template('startup_register.html',form=form,title='E-Cell|SIP Startups')

#the route for the page where details of startups registered is displayed
@app.route("/apply",methods=['GET','POST'])
def apply():
	startup_list = StartUp.query.all()
	return render_template('startup_apply.html',title='E-Cell|SIP Students',startup_list=startup_list)


#this route id will remain unknown to prevent direct access by the user and no redirects will happen to this route for download
@app.route("/download<int:id>",methods=['GET'])
#a function to download the profile of the startup
def download(id):
	if id:
		file_data = StartUp.query.filter_by(id=id).first() #this filters the required file to download by taking the id arugument from the download button from the startup details
		file_name = file_data.startup_name
		return send_file(BytesIO(file_data.profile_doc),attachment_filename=file_name,as_attachment=True)#downloads the required profile of startup(Startup name will be the filename of downloaded file)
