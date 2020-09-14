from flask import Flask,render_template, url_for,flash, redirect, request
from e_cell import app,db
from e_cell.forms import Startup_Registration
from e_cell.models import StartUp
import os



@app.route("/register",methods=['GET','POST'])
def register():
	form = Startup_Registration()
	'''if request.method == 'POST':
		if request.files:
			file= request.files['inputfile']'''
	if form.validate_on_submit():
		startup= StartUp(startup_name=form.startup_name.data,poc_name=form.poc_name.data,poc_email=form.poc_email.data,poc_phone_no=form.poc_phone_no.data,incentive=form.incentive.data,duration=form.duration.data,website=form.website.data)
		db.session.add(startup)
		db.session.commit()
		return redirect(url_for('apply'))
	return render_template('startup_register.html',form=form,title='E-Cell|SIP Startups')



@app.route("/apply",methods=['GET','POST'])
def apply():
	startup_list = StartUp.query.all()
	return render_template('startup_apply.html',title='E-Cell|SIP Students',startup_list=startup_list)