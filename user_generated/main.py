from global_com import firebase_api
from global_com.auth import User
from global_com.chan import chans

firebase_api.database.setup("C:\\Users\\Filip\\Desktop\\setup.json")
chans.setup()


user = User.login("filipdj98@gmail.com", "filip")


print(user.name)