# Spice status app

To run app:

1. clone repo
2. Delete folder migrations and spice_status/spice_status.db
3. console - pip install -r requirements.txt
4. console - db_init.bat
5. console - run.bat



to access admin view:
1. in terminal (on working app) after register
2. flask shell
3. from spice_status.models.user_models import User
4. from spice_status import db
5. user = User.query.filter_by(username={ YOUR_USERNAME ).first()
6. user.is_admin = True
7. db.session.commit()
8. exit()
 
 You have granted yourself a admin. You can see check admin views (navbar)
 
 To add metrics fast use Add metrics Excel and pick excel from uploads folder
 