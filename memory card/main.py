from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication, QWidget,
QHBoxLayout, QVBoxLayout,
QGroupBox, QRadioButton,
QPushButton, QLabel
)
from random import shuffle

class question():
    def __init__ (self, question, right_answer, ans2, ans3, ans4):
        self.question = question
        self.right_answer = right_answer
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4

count_right = 0
count_total = 0

app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
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
lb_Result = QLabel('прав ты или нет?') 
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
RadioGroupBox.hide() 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

window = QWidget()


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')



def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroupBox.setExlusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroupBox.setExlusive(True)

def start_test():
    if ('Ответить')  == btn_OK.text:
        show_result()
    else:
        show_question()

def ask(q: question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.ans2)
    answers[2].setText(q.ans3)
    answers[3].setText(q.ans4)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    if btn_OK == answer[0]:
        show_correct(True)
    else:
        show_correct(False)


def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)
    print(count_total, "всего вопросов,", count_right, "правильные ответы")

    list["12345", "6789"]

#if next_question():
    count_total = +1

if check_answer == True:
    count_right = +1

total = count_right/count_total*100

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
q = question("12345", "1", "2", "3", "4")
ask(q)
btn_OK.clicked.connect(check_answer)
window.show()
app.exec()