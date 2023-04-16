#модули
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import randint, shuffle

class Question():

    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#вопросы
list_question = list()

p1 = Question('Дата начала 2-ой мировой войны?', '1 сентября 1939 года', 
        '14 октября 1938 года', '3 апреля 1935 года', '22 июня 1941 года')

q2 = Question('К какому государству принадлежит остров Гренландия?',
        'Дания', 'Россия', 'Англия', 'США')

q3= Question('Какой океан самый пресный?', 'Северо-Ледовитый океан',
        'Атлантиченский океан', 'Тихий океан', 'Индийский океан')

q4 = Question('Государственный язык Бразилии?', 'Португальский',
        'Английский', 'Бразильский', 'Русский')

q5 = Question('К скольки океанам есть доступ у России?', 'к 3 (Антлантический, Северо-Ледовитый, Тихий)', 'ко всем 4', 
'к 2 (Тихий, Северо-Ледовитый)', 'к 1 (Северо-Ледовитый)')

q6 = Question('Какой день идет после понедельника?', 'вторник', 'банан', 'квадрат', 'смурфик')

q7 = Question('3 закон Ньютона?', 'Сила действия равна силе противодействия', 
        'Молекулы движутся беспорядочно', 'ускорение свободного падения равно 9,8 м/с²',
        'деформация, возникающая в упругом теле, пропорциональна приложенной к этому телу силе')

q8 = Question('Почему растения зеленые?', 'в них есть хлорофилл', 'природа так сказала',
            'они были окрашены человеком', 'животные позоботились об этом...')

q9 = Question('Сколько будет 2+2?', '4', '5', '...', '10')

q10 = Question('Столица Уганды?', 'Кампала', 'Москва', 'Хараре', 'Алжир')

q11 = Question('Почему русский мат самый интересный?', 'Им можно и похвалить, и оскорбить', 'Я не разрешал', 'Просто так', 'кит')

q12 = Question('Дата рождения Ивана Калиты', '1 ноября 1288 года', '5 августа 2022 года', '29 декабря 1576 года', '20 июня 2030 года')

q13 = Question('2 тигра играли в пинг понг, один розовый,' +
' а попугай поехал на северо-запад к бабушке. Сколько будет стоить 1 кг картошки, если у травмая было каре?', 
'8 тугриков', 'Автобус', 'Коромысло', 'Ни сколько, это иллюзия...')

q14 = Question('Зачему?', 'Патамукта', '5 копеек', 'Потому что', 'Поднять якорь')

q15 = Question('Сколько простоит еще школа №63', 'Она простоит дольше, чем пирамиды в Гизе', '24 тугрика', '5 лет', 'Ее снесут завтра')

q16 = Question('Сколько процентов оборот нефти у России от мирового', '8.4%', '200%', '5 тугриков', '10 рублей')

q17 = Question('Сколько запаса природного газа у России по сравнению с миром', '32%', '25%', 'Понедельник', 'яблоко')

q18 = Question('Человек произошел от...', 'Пока что неизвестно от кого точно', 'грибы', 'макака', 'дверь')

q19 = Question('Кто такой Чебурашка?', 'Неведомый зверек', 'Животное', 'Слабость', 'Киллер')

q20 = Question('Суббота -', 'не работа', 'Пчелка Майя', 'букашка', 'могу себе позволить')

#добавление вопросов в список list_question
list_question.append(q2)
list_question.append(q3)
list_question.append(q4)
list_question.append(q5)
list_question.append(q5)
list_question.append(q7)
list_question.append(q8)
list_question.append(q9)
list_question.append(q10)
list_question.append(q11)
list_question.append(q12)
list_question.append(q13)
list_question.append(q14)
list_question.append(q15)
list_question.append(q16)
list_question.append(q17)
list_question.append(q18)
list_question.append(q19)
list_question.append(q20)


app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Прав или нет')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        window.score += 1
        show_correct('Правильно!')
        print(f'Статистика\n-Всего вопросов: {window.total}\n-Правильных ответов {window.score}')
        print(f'Рейтинг: {window.score/window.total*100} %')

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print(f'Рейтинг: {window.score/window.total*100} %')

def next_question():
    
    '''Задает случайный вопрос из списка'''
    window.total += 1
    print(f'Статистика\n-Всего вопросов: {window.total}\n-Правильных ответов {window.score}')
    cur_question = randint(0, len(list_question) - 1)

    q = list_question[cur_question]
    ask(q)

    

def start_test():

    if btn_OK.text() == 'Ответить':
        check_answer()
    
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.resize(400, 300)
window.show()
window.score = 1
window.total = 1
ask(p1)
btn_OK.clicked.connect(start_test)

app.exec()

