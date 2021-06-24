from selenium import webdriver
import time

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.find_element_by_class_name("s_ipt").send_keys("123")
# time.sleep(3)
# driver.quit()

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#          print("Sorry, we are out of green peppers right now.")
#     else:
#       print("Adding " + requested_topping + ".")
# print("\nFinished making your pizza!")

# ali={'11':'1','2':'2'}
# print(ali['11'])
# print(ali['2'])

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# # print("Original x-position: " + alien_0['x_position'])
# print(requested_toppings)
# # print("Original x-position: " + str(requested_toppings))
#
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# alien_0['speed'] = 'fast'
# print("Original x-position: " + str(alien_0['x_position']))
#
#
# # 向右移动外星人
# # 据外星人当前速度决定将其移动多远
# if alien_0['speed'] == 'slow':
#   x_increment = 1
# elif alien_0['speed'] == 'medium':
#   x_increment = 2
# else:
# # 这个外星人的速度一定很快
#   x_increment = 3
# # 新位置等于老位置加上增量
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-position: " + str(alien_0['x_position']))
#
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# del alien_0['speed']
# print(alien_0)
#
# favorite_languages = {
#     '1':'sdad',
#     '2':'eqeq',
#     '3':'31231',
#
# }
# for key,value in favorite_languages.items():
#     print("key:" + key)
#     print("value:" + value)
# # print(favorite_languages[1].upper())

# user_0 = {
# 'username': 'efermi',
# 'first': 'enrico',
# 'last': 'fermi',
# }
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

# aliens = []
#     # 创建30个绿色的外星人
# for alien_number in range(30):
#  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#  aliens.append(new_alien)
#     # 显示前五个外星人
# for alien in aliens[:5]:
#     print(alien)
#     print("...")
#     # 显示创建了多少个外星人
#     print("Total number of aliens: " + str(len(aliens)))
#     print(aliens)
# print("学号\t姓名\t语文\t数学\t英语")
# print("2017001\t曹操\t99\t\t88\t\t0")
# print("2017002\t周瑜\t92\t\t45\t\t93")
# print("2017008\t黄盖\t77\t\t82\t\t100")

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#   city = input('prompt')
#
#   if city == 'quit':
#    break
#   else:
#    print("I'd love to go to " + city.title() + "!")

# x = 1
# while x <= 5:
#  print(x)

# ticket =int(input('age'))
# if ticket< 3:
#     print("free")
# elif 12>ticket>3:
#     print(10)
# elif ticket>12:
#     print(12)

# unconfirmed_users = ['alice', 'brian','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print("verifying user:" + current_users.title())
#     confirmed_users.append(current_users)
#
# for confirmed_user in confirmed_users:
#         print(confirmed_user.title())

# def aa(a,b='dsada'):
#     print(a.title())
#     print('test'+b.title())
#
# aa(b='ada',a='dwqdqw')

# def build_person(first_name, last_name, age=''):
#
#     person = {'first': first_name, 'last': last_name}
#     if age:
#      person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

def get_formatted_name(first_name,last_name):
    full_name=first_name+""+last_name
    return full_name.title()

# while True:
#     a = input("first_name")
#     if a =='quit':
#         break
#     b = input("last_name")
#     if b=='quit':
#         break
#      print()

msg = get_formatted_name('a','b')
print(msg)
#
# def print_models(unprient_design,completed_models):
#     while unprient_design :
#         current_design = unprient_design.pop()
#         print(current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     print("\nthe follow models has print")
#     for completed_model in completed_models:
#         print(completed_model)
#
# users = ['1','2','hfahfaih']
# users2 = []
#
# print_models(users[:],users2)
# show_completed_models(users2)
# print(users)

def make_pizza(size, *toppings):

    print("\nMaking a " + str(size) +
"-inch pizza with the following toppings:")
    for topping in toppings:
       print("- " + topping + "\nMaking a ")

if __name__ == "__main__":
    print("执行前先print一下")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
