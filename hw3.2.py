def user_data(firstname, lastname, year_birth, city, email, phone):
    print(f"Имя - {firstname}; Фамилия - {lastname}; Год рождения - {year_birth}; Город проживания - {city}; "
          f"Email - {email}; Номер телефона - {phone}")


fname = input('Введите, пожалуйста, свое имя - ')
lname = input('Введите, пожалуйста, свою фамилию - ')
birth_y = int(input('Введите, пожалуйста, год своего рождения - '))
city_u = input('Введите, пожалуйста, город своего проживания - ')
email_u = input('Введите, пожалуйста, свой email - ')
phone_u = input('Введите, пожалуйста, номер своего телефона - ')
user_data(firstname=fname, lastname=lname, year_birth=birth_y, city=city_u, email=email_u, phone=phone_u)
