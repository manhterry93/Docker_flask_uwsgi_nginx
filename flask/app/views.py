from app import app
from app import User
@app.route("/")
def index():
    print ("on request comming")
    users = User.query.all()
    if users is None:
        return ":Hello from Flask"
    else:
        results = [
        {
            "name":user.name,
            "id":user.id,
            "email":user.email
        }for user in users]
        return {"count": len(results), "cars": results}
    
    