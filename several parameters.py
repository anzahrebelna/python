def user_data(name: str, lastname: str, birthyear: int, city:str, email: str, phonenumber:int):
    print(f"Name - {name}", end=',')
    print(f"last name - {lastname}", end=',')
    print(f"birth year - {birthyear}", end=',')
    print(f"city - {city}", end=',')
    print(f"email - {email}", end=',')
    print(f"phone number - {phonenumber}", end='.')

user_data(name='Anastazia', lastname='Zahrebelna', birthyear=1996, city='Katowice', email='an.zahrebelna@gmail.com', phonenumber=77777)
