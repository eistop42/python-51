from tkinter import *
from yandex import YandexGPT

token = ''
catalog = ''

yandex = YandexGPT(token, catalog)

root = Tk()
frame = Frame(root, padx=10, pady=10)
frame.grid()

question = StringVar()
def get_answer():
    output.delete('1.0', END)
    question_text = question.get()
    answer = yandex.get_answer(question_text)
    output.insert(END, answer)

    question.set('')

Label(frame, text='Привет').grid(column=0, row=0)
user_input = Entry(frame, textvariable=question)
user_input.grid(column=0, row=1)
user_input.bind("<Return>", lambda event: get_answer())

button = Button(frame, text='Сохранить', command=get_answer)
button.grid(column=0, row=2)
# button.bind("<Return>", lambda event: get_answer())

output = Text(frame, width=50, height=10)
output.grid(column=1, row=0, rowspan=3)

root.mainloop()
