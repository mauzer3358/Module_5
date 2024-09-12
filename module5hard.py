import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


    def __eq__(self, other): return self.nickname == other.nickname and self.password == other.password

    def __hash__(self): return hash((self.password))


class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0


class UrTube:

    def __init__(self):
        self.users = []
        self.current_user = None
        self.videos = []

    def add(self, *args):

        for i in args:
            if self.videos == []:
                self.videos.append([i.title, i.duration, i.adult_mode, i.time_now])
            else:
                 self.videos.append([i.title, i.duration, i.adult_mode, i.time_now])




        #Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        # содержащих поисковое слово.Следует учесть, что слово 'UrbaN' присутствуеn в строке 'Urban the best'
        # (не учитывать регистр).
    def get_videos(self, *args):
        lst = []
        a = args[0].lower()
        for i in range(len(self.videos)):
            self.b = self.videos[i][0].lower()
            if a in self.b:
                lst.append(self.videos[i][0])
        return lst



    # Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя
    # в список, если пользователя не существует(с таким же nickname).Если существует, выводит на
    # экран: "Пользователь {nickname} уже существует".После регистрации, вход выполняется автоматически.


    def register(self,nickname, password, age):

        self.use = User(nickname, password, age)

        if self.users == []:
            self.users.append([self.use.nickname, hash(self.use.password), self.use.age])
            self.current_user = [self.use.nickname, hash(self.use.password), self.use.age]

        else:
             for i in self.users:
                 if i[0] != self.use.nickname:
                     self.users.append([self.use.nickname, hash(self.use.password), self.use.age])
                     self.current_user = self.log_in(self.use.nickname, hash(self.use.password))
                     #print(self.current_user[0])
                 elif i[0] == self.use.nickname:
                     print(f'Пользователь {self.use.nickname} уже существует')
                     print(self.current_user[0])
                 break
        return

    # Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя
    # в users с такими же логином и паролем.Если такой пользователь существует, то current_user меняется
    # на найденного.Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    def log_in(self, nickname, password):
        for i in self.users:
            if i[0] == nickname and i[1] == password:
                self.current_user = i
                return self.current_user



    # Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
    # то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    # После текущее время просмотра данного видео сбрасывается.

    def watch_video(self, name):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user != None:
            v_name = [name]
            for i in self.videos:
                if self.current_user[2] < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    break
                else:
                    for j in range(len(self.videos)):
                        if v_name == [self.videos[j][0]]:
                            for k in range(1, self.videos[j][1] + 1):
                                print(k)
                                time.sleep(1)
                            print('Конец видео')
                        else:
                            continue
                return self.videos[j][1]

    def __del__(self):
        self.current_user = None





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



# Вывод в консоль:
#
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist