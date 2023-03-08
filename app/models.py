from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    num_bedrooms = db.Column(db.Integer, nullable=False)
    num_bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    photo = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Property {self.id}>'