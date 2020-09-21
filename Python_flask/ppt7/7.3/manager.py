from application import app,db

if __name__ == "__main__":
    from common.models.user import User
    db.create_all()
    app.run( host = "0.0.0.0",debug=True )