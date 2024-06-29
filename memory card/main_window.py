from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
# all import, from PyQt5

app = QApplication([])

main_wind = QWidget()
main_wind.resize(600,500)
main_wind.move(300,300)
main_wind.setWindowTitle('Memory card')
# Creat widget(button, timer, inscr)

btn_Menu = QPushButton("Меню")
btn_Sleep = QPushButton("Відпочити")
btn_OK = QPushButton("Відповісти")
# button menu, sleep and ok

box_Minutes = QSpinBox()
box_Minutes.setValue(30)
# minutes 30 goto slepp

lb_Question = QLabel("")
#question lb

#creat panel

RadioGroup = QButtonGroup()
RadioGroupBox = QGroupBox("Варіанти відповідею:")

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
# create radiogroup all rbtn radiogroupbox

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
# radiogroup addbutton rbtn

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
# layout answer qhboxlayout, qvboxlayout

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
# answer vertikal line layout 2

layout_ans1.addWidget(rbtn_3)
layout_ans1.addWidget(rbtn_4)
# answer vertikal line layout 1

RadioGroupBox.setLayout(layout_ans1)
RadioGroupBox.setLayout(layout_ans2)
RadioGroupBox.setLayout(layout_ans3)
# creat line layout add
#creat panel(frame)

ANSGroupBox = QGroupBox("Результат тесту:")
lb_Result = QLabel('')
lb_Corect = QLabel('')
# result inscr test corect or no all lb_result, corect
# to place frame

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Corect, alignment=Qt.AlignHCenter, stretch=2)
ANSGroupBox.setLayout(layout_res)
ANSGroupBox.hide()
# layout result aligment qt, ansgroup hide
# location of widgets on the window

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('Хвлини'))
# location line qhboxlayout (button, menu and inscr)

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignLeft | Qt.AlignTop))
# location line 2 qhboxlayout (button, menu and inscr)

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(ANSGroupBox)

# location line 3 qhboxlayout (button ok)
layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK,stretch=2)
layout_line4.addStretch(1)
# location line 4 qhboxlayout (button ok)
# 4 qhboxlayout 1 qvboxlayout
layout_cards = QVBoxLayout()
layout_cards.addLayout(layout_line1,stretch=1)
layout_cards.addLayout(layout_line2,stretch=2)
layout_cards.addLayout(layout_line3,stretch=8)
layout_cards.addStretch(1)
layout_cards.addLayout(layout_line4,stretch=1)
layout_cards.addSpacing(5)
# layout cards
main_wind.setLayout(layout_cards)
main_wind.show()
app.exec_()