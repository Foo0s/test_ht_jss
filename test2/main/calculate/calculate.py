import tkinter
import settings
import math


from tkinter import *
from tkinter import messagebox

class Application:

    def __init__(self):

        self.app = tkinter.Tk()
        self.app.title(settings.NAME_APPLICATION)
        self.app.geometry(f"{settings.SCREEN_WEIGHT}x{settings.SCREEN_HEIGHT}")
        self.app.resizable(False, False)
        self.icon = PhotoImage(file='../../static/img/m_icon.png')
        self.app.iconphoto(False, self.icon)

        #Кнопки цифр
        self.frame_main = tkinter.Frame(self.app, bg='black', bd=1)
        self.frame_main.configure(width=10, height=20)


        self.bt_0 = tkinter.Button(self.frame_main, text='0', command=lambda: self.btn_clicked(self.bt_0.config('text')[-1]))
        self.bt_0.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.bt_1 = tkinter.Button(self.frame_main, text='1', command=lambda: self.btn_clicked(self.bt_1.config('text')[-1]))
        self.bt_1.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])


        self.bt_2 = tkinter.Button(self.frame_main, text='2', command=lambda: self.btn_clicked(self.bt_2.config('text')[-1]))
        self.bt_2.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.bt_3 = tkinter.Button(self.frame_main, text='3', command=lambda: self.btn_clicked(self.bt_3.config('text')[-1]))
        self.bt_3.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.bt_4 = tkinter.Button(self.frame_main, text='4', command=lambda: self.btn_clicked(self.bt_4.config('text')[-1]))
        self.bt_4.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.bt_5 = tkinter.Button(self.frame_main, text='5', command=lambda: self.btn_clicked(self.bt_5.config('text')[-1]))
        self.bt_5.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.bt_6 = tkinter.Button(self.frame_main, text='6', command=lambda: self.btn_clicked(self.bt_6.config('text')[-1]))
        self.bt_6.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.bt_7 = tkinter.Button(self.frame_main, text='7', command=lambda: self.btn_clicked(self.bt_7.config('text')[-1]))
        self.bt_7.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.bt_8 = tkinter.Button(self.frame_main, text='8', command=lambda: self.btn_clicked(self.bt_8.config('text')[-1]))
        self.bt_8.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.bt_9 = tkinter.Button(self.frame_main, text='9', command=lambda: self.btn_clicked(self.bt_9.config('text')[-1]))
        self.bt_9.configure(width=settings.SIZE_OF_BUTTON.split('x')[0], height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.result = tkinter.Button(self.frame_main, text="=", bg='yellow', fg='black')
        self.result.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0]), height=settings.SIZE_OF_BUTTON.split('x')[-1], command=self.result_operations)

        self.btn_point = tkinter.Button(self.frame_main, text='.', command=lambda: self.btn_clicked(self.btn_point.config('text')[-1]))
        self.btn_point.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0]), height=settings.SIZE_OF_BUTTON.split('x')[-1])

        self.frame_main.pack()
        self.bt_0.grid(row=0, column=1, padx=2, pady=2)
        self.bt_1.grid(row=0, column=2, padx=2, pady=2)
        self.bt_2.grid(row=0, column=3, padx=2, pady=2)
        self.bt_3.grid(row=1, column=1, padx=2, pady=2)
        self.bt_4.grid(row=1, column=2, padx=2, pady=2)
        self.bt_5.grid(row=1, column=3, padx=2, pady=2)
        self.bt_6.grid(row=2, column=1, padx=2, pady=2)
        self.bt_7.grid(row=2, column=2, padx=2, pady=2)
        self.bt_8.grid(row=2, column=3, padx=2, pady=2)
        self.bt_9.grid(row=3, column=1, padx=2, pady=2)
        self.btn_point.grid(row=3, column=2, padx=2, pady=2)
        self.result.grid(row=3, column=3, columnspan=2)


        self.entry_main = tkinter.Entry( bg='black', foreground='white', justify='left')
        self.entry_main.place(width=settings.SCREEN_WEIGHT, height=35)

        self.frame_main.place(x=settings.SCREEN_WEIGHT // 4, y=70)


        self.frame_operations = tkinter.Frame(self.app, bg='black', bd=1)

        self.bt_clear = tkinter.Button(self.frame_operations, text='C', bg='orange', fg='black')
        self.bt_clear.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=settings.SIZE_OF_BUTTON.split('x')[-1], command=self.clear_entry)

        self.bt_pl = tkinter.Button(self.frame_operations, text='+')
        self.bt_pl.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=settings.SIZE_OF_BUTTON.split('x')[-1], command=lambda: self.btn_clicked(self.bt_pl.config('text')[-1]))

        self.bt_mn = tkinter.Button(self.frame_operations, text='-')
        self.bt_mn.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=settings.SIZE_OF_BUTTON.split('x')[-1], command=lambda: self.btn_clicked(self.bt_mn.config('text')[-1]))

        self.bt_ml = tkinter.Button(self.frame_operations, text='*')
        self.bt_ml.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=settings.SIZE_OF_BUTTON.split('x')[-1], command=lambda: self.btn_clicked(self.bt_ml.configure('text')[-1]))

        self.bt_dv = tkinter.Button(self.frame_operations, text='/')
        self.bt_dv.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=settings.SIZE_OF_BUTTON.split('x')[-1], command=lambda: self.btn_clicked(self.bt_dv.configure('text')[-1]))

        self.bt_clear.grid(row=0, column=0, padx=2, pady=2)
        self.bt_pl.grid(row=1, column=0, padx=2, pady=2)
        self.bt_mn.grid(row=2, column=0, padx=2, pady=2)
        self.bt_ml.grid(row=3, column=0, padx=2, pady=2)
        self.bt_dv.grid(row=4, column=0, padx=2, pady=2)


        self.frame_dop_operations = tkinter.Frame(self.app, bg='black', bd=1)

        self.bt_sk_1 = Button(self.frame_dop_operations, text='(', bg='yellow', fg='black')
        self.bt_sk_1.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0]), height=int(settings.SIZE_OF_BUTTON.split('x')[-1])-1, command=lambda: self.btn_clicked(self.bt_sk_1.configure('text')[-1]))

        self.bt_sk_2 = Button(self.frame_dop_operations, text=')', bg='yellow', fg='black')
        self.bt_sk_2.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0]), height=int(settings.SIZE_OF_BUTTON.split('x')[-1])-1, command=lambda: self.btn_clicked(self.bt_sk_2.configure('text')[-1]))

        self.bt_clear_s = Button(self.frame_dop_operations, text='C--', bg='orange', fg='black')
        self.bt_clear_s.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0]), height=int(settings.SIZE_OF_BUTTON.split('x')[-1])-1, command=self.btn_clear_s)

        self.bt_sk_1.grid(row=0, column=1, padx=2, pady=2)
        self.bt_sk_2.grid(row=0, column=2, padx=2, pady=2)
        self.bt_clear_s.grid(row=0, column=0, padx=2, pady=2)

        self.frame_dop_operations.place(x=settings.SCREEN_WEIGHT - 187, y=35)

        self.frame_operations.place(x=settings.SCREEN_WEIGHT - 58, y=30)



        self.frame_d_operations = tkinter.Frame(self.app, bg='black', bd=1)

        self.bt_st = Button(self.frame_d_operations, text='x^y')
        self.bt_st.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=int(settings.SIZE_OF_BUTTON.split('x')[-1]), command=self.bt_step_click)

        self.bt_fact = Button(self.frame_d_operations, text='x!')
        self.bt_fact.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=int(settings.SIZE_OF_BUTTON.split('x')[-1]), command=self.factoriaB)

        self.bt_cos = Button(self.frame_d_operations, text='cos')
        self.bt_cos.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=int(settings.SIZE_OF_BUTTON.split('x')[-1]), command=lambda: self.cos_sin_log(self.bt_cos.configure('text')[-1]))

        self.bt_sin = Button(self.frame_d_operations, text='sin')
        self.bt_sin.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=int(settings.SIZE_OF_BUTTON.split('x')[-1]), command=lambda: self.cos_sin_log(self.bt_sin.configure('text')[-1]))

        self.bt_ln = Button(self.frame_d_operations, text='ln')
        self.bt_ln.configure(width=int(settings.SIZE_OF_BUTTON.split('x')[0])+2, height=int(settings.SIZE_OF_BUTTON.split('x')[-1]), command=lambda: self.cos_sin_log(self.bt_ln.configure('text')[-1]))

        self.bt_st.grid(row=0, column=0, padx=2, pady=2)
        self.bt_fact.grid(row=1, column=0, padx=2, pady=2)
        self.bt_cos.grid(row=2, column=0, padx=2, pady=2)
        self.bt_sin.grid(row=3, column=0, padx=2, pady=2)
        self.bt_ln.grid(row=4, column=0, padx=2, pady=2)



        self.frame_d_operations.place(x=settings.SCREEN_WEIGHT - 247, y=30)


    def bt_step_click(event):
        event.entry_main.insert(len(event.entry_main.get()), "**")

    def clear_entry(event):
        event.entry_main.delete(0, len(event.entry_main.get()))

    def btn_clear_s(event):
        event.entry_main.delete(len(event.entry_main.get())-1, len(event.entry_main.get()))

    def btn_clicked(event, text):
        event.entry_main.insert(len(event.entry_main.get()), text)
        print(event.entry_main)


    def factoriaB(event):
        event.entry_main.insert(len(event.entry_main.get()), "!")


    def result_operations(event):
        try:
            text_ans = event.entry_main.get()
            flag_res = False

            if "!" in text_ans:
                indx_factorial = event.entry_main.get().index("!")

                flag_res = True

                result = event.factorial_results()
                event.entry_main.delete(0, len(event.entry_main.get()))
                event.entry_main.insert(0, result)

            else:
                event.entry_main.delete(0, len(event.entry_main.get()))

            if flag_res == False:

                result = eval(text_ans)
                event.entry_main.delete(0, len(text_ans))
                event.entry_main.insert(0, result)

        except Exception:
            event.entry_main.delete(0, len(event.entry_main.get()))
            event.entry_main.insert(0, 'Некорректный ввод данных!')

    def factorial_results(event) -> int:
        number = int(event.entry_main.get()[:event.entry_main.get().index("!")])
        flag_otr = True if number < 0 else False
        number = abs(number)
        res = 1
        while number >= 1:
            if flag_otr == True:
                res *= number*-1
            else:
                res *= number
            number -= 1
        return res

    def message_box_exit(self):
        self.ms_b = messagebox.askokcancel('Выход', "Вы уверены?")
        if self.ms_b:
            self.app.destroy()

    def cos_sin_log(event, text):

        numbs = event.entry_main.get()
        event.entry_main.delete(0, len(event.entry_main.get()))
        if text == 'cos':
            event.entry_main.insert(0, str(math.cos(int(numbs))))
        elif text == 'ln':
            event.entry_main.insert(0, str(math.log(abs(int(numbs)))))
        else:
            event.entry_main.insert(0, str(math.sin(int(numbs))))

    def display(self):
        self.app.protocol("WM_DELETE_WINDOW", self.message_box_exit)
        self.app.mainloop()


