import time 
score = 0 
inventory = []

# Функція для виведення введеного тексту з паузою 
def print_with_pause(text):
    print(text)
    time.sleep(1)
    
# Початок гри 
print_with_pause("Ласкаво просимо до текстової гри!")
print_with_pause("Ви знаходитесь у великому покинутому будинку. Виберіть напрямок подорожі:")
choice = input("1. Відчинити перші двері.\n2. Відчинити другі двері.\n")

if choice == '1':
    print_with_pause("Ви відчинили перші двері.")
    print_with_pause("Після декількох хвилин блукання ви натрапили на ключ.")
    print_with_pause("Згодом ви побачили два сейфи.")
choice = input("1. Відчинити перший сейф.\n2. Відчинити другий сейф.\n")

if choice == '2' :
    print_with_pause("В сейфі ви знайшли 100000$")
    print_with_pause("Ваш баланс зріс на 100000$!")
    score += 100000
    inventory.append("$")
    print_with_pause("Забравши гроші, ви почули гуркіт з сусідньої кімнати.")
    print_with_pause("Ви починаєте тікати.")
    print_with_pause("Раптом ви бачете перед собою сходи які ведуть, до таємничої двері, прикритої пітьмою. ")
    choice = input("1. Відчинити двері.\n2. Повернутися назад.\n")
    if choice == '1' :
        print_with_pause("Відчинивши двері ви побачили перед собою кімнату.")
        choice = input("1. Оглянути кімнату та пошукати можливі виходи з будинку.\n2. Заховатись в шафу.\n")
        if choice == '1' :
         print_with_pause("Оглянувши кімнату ви помітили відчинене вікно.")         
         choice = input("1. Втекти через вікно.\n2. Залишитись у кімнаті.\n")
         if choice == '1' :
             print_with_pause("Ви втекли")
             print_with_pause("Ви продовжуєте свою подорож, не знаючи, що вас чекає.")
             print_with_pause("Гра завершена. Ваш рахунок: " + str(score))
             print_with_pause("Дякуємо за гру!")
         else:
             print_with_pause("Ви не встигли втекти, вас зарізали.")     
             print_with_pause("Ви мертві")
             print_with_pause("Це кінець!")
        else:
             print_with_pause("Вас застрелили")
             print_with_pause("Це кінець гри!")
else:
    print_with_pause("Ви відчинили другі двері.")
    print_with_pause("Перед вами великий коридор.")
    choice = ("1. Піти праворуч.\n2. Піти ліворуч.\n")
    
    if choice == '2' :
        print_with_pause("Ви пішли ліворуч та натрапили на кімнату, переповнену токсичним газом - Фосген.")
        print_with_pause("Ви померли!")
        print_with_pause("Це кінець гри!")
    else:
        print_with_pause("Ви пішли праворуч")
        print_with_pause("Ви опинилися в кімнаті з температурою -50°C.")
        print_with_pause("Ви відчуваєте як ваші кінцівки замерзають.")
        print_with_pause("Оглядаючи кімнату ви помітили люк")
        choice = ("Куди піти?\n1. Втекти через люк\n2. Залишитись в кімнаті ")
        if choice == '1':
            print_with_pause("Люк був зачиненим, його не вдалося відчинити")
            print_with_pause("Ви залишились в кімнаті")
            print_with_pause("Вітаю ви бурулька.")
            print_with_pause("Це кінець гри!")
        else:
            print_with_pause("Ви вийшли та продовжили свою подорож")
            print_with_pause("Ви продовжуєте свою подорож, не знаючи, що вас чекає.")
            print_with_pause("Гра завершена. Ваш рахунок: " + str(score))
            print_with_pause("Ваш інвентар: " +','.join(inventory))
            print_with_pause("Дякуємоза гру!")