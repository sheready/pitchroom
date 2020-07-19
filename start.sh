export MAIL_USERNAME='africanblack361@gmail.com'
export MAIL_PASSWORD='workingkujikaza'
export DATABASE_URL=$(heroku config:get DATABASE_URL -a pitchroom)
python3.6 manage.py server