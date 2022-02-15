from dotenv import load_dotenv

from auth.db.email_verify import check_verify_code, db_create_verify
load_dotenv()

from flask import Flask
from auth.auth import auth

app = Flask(__name__)

app.register_blueprint(auth)

print(check_verify_code('c36810b28e1c11ecb741a85e45cffbcb'))

db_create_verify(234324)

@app.route('/')
def board():
    return "index"

app.run(host="0.0.0.0", port=5001, debug=True)