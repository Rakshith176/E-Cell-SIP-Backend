from e_cell import db


class StartUp(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	startup_name = db.Column(db.String(30),unique=True,nullable=False)
	poc_name = db.Column(db.String(30),unique=False,nullable=False)
	poc_email = db.Column(db.String,nullable=False,unique=False)
	poc_phone_no= db.Column(db.Integer,nullable=False,unique=False)
	#profile_doc = db.Column(db.LargeBinary,nullable=True)
	incentive = db.Column(db.String(30),nullable=False)
	duration = db.Column(db.String(30),nullable=False)
	website = db.Column(db.String,unique=True,nullable=True)

	def __repr__(self):

	    return f"StartUp('{self.startup_name}', '{self.poc_name}', '{self.poc_email}','{self.poc_phone_no}','{self.profile_doc}','{self.incentive}','{self.duration}','{self.website}')"

