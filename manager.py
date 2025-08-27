from database import BASE , engine , Session
from models import User, Post
from termcolor import colored

BASE.metadata.create_all(engine)

session = Session()

def register():
    print(colored("Ro'yxatga olish boshlandi!" , "yellow"))
    username = input("USERNAME kiriting: ").lower()
    
    with Session() as session:
        result = session.query(User).filter(User.username == username).first()
       
        
        if result:
            print(colored("Bu username band! Iltimos qayta urining!" , "red"))
            return 
        
        user = User(username = username)
        session.add(user)
        session.commit()
        
        print(colored("Muvaffaqiyatli ro'yhatdan o'tildi!" , "green"))
        print(colored("Login qilib Accountingizga kirishingiz mumkin!" , "green"))

def login():
    print(colored("Accountingizga kiring!" , "green"))
    username = input("USERNAME kiriting: ").lower()
    
    with Session() as session:
        user = session.query(User).filter(User.username == username).first()
       
        
        if user:
            print(colored("Foydalanuvchi tasdiqlandi!" , "green"))
            return user
        else:
            print(colored("Foydalanuvchi topilmadi!" , "red"))
            return None
             
        
def create_post(user: User):
    title = input("Nomini kiriting: ").strip()
    content = input("Tavsifni kiriting: ").strip()
    
    with Session() as session:
        user = session.query(User).filter(User.username == user.username).first()
        post = Post(title=title , content=content)
        
        user.posts.append(post)
        session.add(user)
        session.commit()
        
        print(colored("Post muvaffaqyatli qo'shildi" , "green"))
        
def show_post(user: User):
    
    with Session() as session:
        user = session.query(User).filter(User.username == user.username).first()
        
        posts = user.posts
        
        
        if not posts:
            print(colored("Postlar ro'yxati bo'sh!", "red"))
            return
        
        print(colored("Postlar ro'yxatingiz!" , "cyan"))
        
        for i, post in enumerate(posts, start=1):
            print(colored(f"{i}. {post.title}", "blue"))
        
        
        
def main():
    while True:
        print(colored("------ Bosh Sahifa ------", "green"))
        print(colored("---- 1. Register --" , "cyan"))
        print(colored("---- 2. Login -----" , "cyan"))
        print(colored("---- 3. Chiqish ---", "red"))
        
        print(colored("--Amallardan birini tanlang!--" , "blue"))
        
        choose = input('--->  ')
        if choose == '1':
            register()
        
        elif choose == "2":
                user = login()
                while True:
                
                    if user:
                        print(colored("-------- Ilova Sahifalari! -------", "green"))
                        print(colored("---- 1. Post yaratish!       -----" , "cyan"))
                        print(colored("---- 2. Postlarimni ko'rish! -----" , "cyan"))
                        print(colored("---- 3. Chiqish ---", "red"))
                        
                        print(colored("--Amallardan birini tanlang!--" , "blue"))
                        option = input("--->  ")
                        
                        if option == "1":
                            create_post(user)
                            
                        elif option == "2":
                            show_post(user)
                            
                        elif option == "3":
                            print(colored("Dastur yakunlandi!" , "light_red"))
                            return True
        
        elif choose == "3":
            print(colored("Dastur yakunlandi!" , "light_red"))
            return True
main()
    
#user01 = User(username="Muhammadrizo")
#session.add(user01)
#session.commit()


#user02 = User(username="Abdulaziz")
#session.add(user02)
#session.commit()


#user03 = User(username="Eldor")
#session.add(user03)
#session.commit()


#post = Post(title="Kitob o'qish" , content="O'qish bu madaniy tomondan o'sish")
#session.add(post)

#user01 = session.query(User).filter(User.username=="Muhammadrizo").first()

#user01.posts.append(Post(title="Football o'ynash" , content="Do'stlar bilan vaqt o'tkazish!"))
#session.add(user01)
#session.commit()
