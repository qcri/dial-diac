import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_mail import Mail
import tensorflow as tf
from opennmt.runner import Runner
from opennmt.config import load_model, load_config

# INFO:tensorflow:Restoring parameters from toy-ende/model.ckpt-485000
# tf.logging.set_verbosity(getattr(tf.logging, "ERROR"))

app = Flask(__name__)
# app.config['USE_X_SENDFILE'] = True
app.config['SECRET_KEY'] = os.environ.get('DIALDIAC_SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DISOOQI_DB_URI')
# GA_TRACKING_ID = os.environ['GA_TRACKING_ID']

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


ca_config = load_config(["diacritizer/opennmt-defaults.yml", "diacritizer_ca/toy-ende.yml"])
ca_model = load_model(
    ca_config["model_dir"],
    model_file="",
    model_name="",
    serialize_model=False)
ca_runner = Runner(
    ca_model,
    ca_config,
    seed=None,
    num_devices=1,
    gpu_allow_growth=False)

msa_config = load_config(["diacritizer/opennmt-defaults.yml", "diacritizer_msa/toy-ende.yml"])
msa_model = load_model(
    msa_config["model_dir"],
    model_file="",
    model_name="",
    serialize_model=False)
msa_runner = Runner(
    msa_model,
    msa_config,
    seed=None,
    num_devices=1,
    gpu_allow_growth=False)

tn_config = load_config(["diacritizer/opennmt-defaults.yml", "diacritizer_tn/toy-ende.yml"])
tn_model = load_model(
    tn_config["model_dir"],
    model_file="",
    model_name="",
    serialize_model=False)
tn_runner = Runner(
    tn_model,
    tn_config,
    seed=None,
    num_devices=1,
    gpu_allow_growth=False)

ma_config = load_config(["diacritizer/opennmt-defaults.yml", "diacritizer_ma/toy-ende.yml"])
ma_model = load_model(
    ma_config["model_dir"],
    model_file="",
    model_name="",
    serialize_model=False)
ma_runner = Runner(
    ma_model,
    ma_config,
    seed=None,
    num_devices=1,
    gpu_allow_growth=False)

# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'                            # SMTP Host
# app.config['MAIL_PORT'] = 465                                                # SMTP Port
# app.config['MAIL_USE_SSL'] = True     # whither to use TLS (Port: 465 (SSL) or 587 (TLS))
# # app.config['MAIL_USE_TLS'] = True
# # https://serverfault.com/questions/413397/how-to-set-environment-variable-in-systemd-service
# # https://askubuntu.com/questions/1071415/passing-environment-variables-to-systemd-service
# # https://serverfault.com/questions/868373/how-to-use-variables-in-a-systemd-service-file
# # https://serverfault.com/questions/868373/how-to-use-variables-in-a-systemd-service-file
# app.config['MAIL_USERNAME'] = os.environ.get('ARABIC_SPEECH_EMAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('ARABIC_SPEECH_EMAIL_PASSWORD')
# app.config['MAIL_DEFAULT_SENDER'] = 'info@arabicspeech.org'
# info_mail = Mail(app)

# app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdzFoQUAAAAAAQvRiVYSSa3YTZubwwaRAM2ULK1'
# app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ.get('AS_reCAPTCHA_SECRET_KEY')
# # optional
# app.config['RECAPTCHA_API_SERVER'] = 'https://www.google.com/recaptcha/api.js'
# # app.config['RECAPTCHA_PARAMETERS'] = ''
# # app.config['RECAPTCHA_DATA_ATTRS'] = {'theme': 'dark'}
# app.config['RECAPTCHA_USE_SSL'] = 'True'


from . import routes