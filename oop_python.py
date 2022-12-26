from user import User
from post import Post

app_user_one = User("nn@gmail.com","Nana Janashia","pwd1","Student")
app_user_one.get_user_info()
app_user_one.change_job_title("DevOps intern")
app_user_one.get_user_info()

app_user_two = User("jamesbond@gmail.com", "James Bond", "secretmessage","Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today ", app_user_two.name)
new_post.get_post_info()