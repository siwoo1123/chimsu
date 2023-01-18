from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import random as rd

data = {
    "minute": [],
    "an overflowing amount": []
}

window = Tk()
lalala = 0

window.title("침수 예측 시스템")
window.geometry('1050x600+100+100')


def insertText(widget, tt):
    widget.configure(state='normal')
    widget.insert(0.0, tt + "\n")
    widget.configure(state='disabled')


def start():
    global e1, e2, e3, e4, text, data, window, lalala

    text.configure(state='normal')
    text.delete("0.0", "end")
    text.configure(state='disabled')
    data = {
        "minute": [],
        "an overflowing amount": []
    }
    try:
        precipitation = float(e1.get())
        maximum_capacity = float(e2.get())
        volume = float(e3.get())
        foreign_matter = float(e4.get())
    except:
        if lalala >= 50:
            insertText(text, "......")
        elif lalala >= 40:
            insertText(text, "버튼이 고통받는 중입니다....")
        elif lalala >= 30:
            insertText(text, "제발 그만 하세요!!")
        elif lalala >= 20:
            insertText(text, "언제까지 애러만 보실 거예요?")
        elif lalala >= 10:
            insertText(text, "숫자만 넣으시라구요!")
        else:
            insertText(text, "모든 칸에 숫자만 넣어주십시오.")
        lalala += 1
        return 0
    if volume > maximum_capacity or precipitation > 1000:
        insertText(text, "뭔가 이상하지 않나요?")
        return 0
    isChimsu = False
    maximum_capacity /= 6

    for minute in range(1, 1451, 10):
        nounImmuljil = abs(rd.uniform(0, foreign_matter))
        nounImmuljil = round(nounImmuljil, 5)
        foreign_matter -= nounImmuljil
        volume -= nounImmuljil + precipitation
        volume += 95
        if volume > maximum_capacity:
            volume = maximum_capacity
        data["minute"].append(minute)
        if volume < 0:
            data["an overflowing amount"].append(-1 * volume)
            if -1 * volume >= 25.5:
                isChimsu = True
        else:
            data["an overflowing amount"].append(0)

        df = pd.DataFrame(data)
        figure = plt.Figure(figsize=(6, 5), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, window)
        chart_type.get_tk_widget().grid(row=1, rowspan=119, column=3)
        df = df[['minute', 'an overflowing amount']].groupby('minute').sum()
        df.plot(kind='line', legend=True, ax=ax)

        if isChimsu:
            insertText(text, f"이물질이 {nounImmuljil}만큼 들어감 -> {minute}분 뒤 침수 시작")
        else:
            insertText(text, f"이물질이 {nounImmuljil}만큼 들어감 -> {minute}분 뒤 침수 없음")
        minute += 1
        if isChimsu:
            break


t1 = Label(window, text='시간당 강수량 (mm)')
e1 = Entry(window)
t2 = Label(window, text='배수구 최대 용량 (mm)')
e2 = Entry(window)
t3 = Label(window, text='배수구의 비어있는 용량 (mm)')
e3 = Entry(window)
t4 = Label(window, text='배수구 주변의 이물질 양 (mm)')
e4 = Entry(window)

startbtn = Button(window, text="시작", command=start)

t1.grid(row=0, column=1)
e1.grid(row=1, column=1)
t2.grid(row=2, column=1)
e2.grid(row=3, column=1)
t3.grid(row=4, column=1)
e3.grid(row=6, column=1)
t4.grid(row=7, column=1)
e4.grid(row=8, column=1)
startbtn.grid(row=9, column=1)

text = Text(window, width=30)
text.configure(state='disabled')
text.grid(row=1, rowspan=9, column=2)

window.mainloop()
