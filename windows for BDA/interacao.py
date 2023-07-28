import json
import tkinter as tk

counter = 0


def start():
    label.pack_forget()
    for i in button:
        i.pack(fill=tk.BOTH)
        i.bind("<Button-1>", click)


def click(e):
    for i in button:
        i.pack_forget()
    s = ''
    index = 0
    if (e.widget._name[len(e.widget._name) - 1] != 'n'):
        index = int(e.widget._name[len(e.widget._name) - 1]) - 1

    s = ''
    for i in objs['interacao'][index]:
        s += i[7:] + ": " + str(objs['interacao'][index][i]) + "\n"
    label['text'] = s
    label.pack(fill=tk.BOTH)


def importJsonTuya():
    f1 = open("csvOutPut.json", 'r')
    dados = json.loads(f1.read())
    f1.close()

    counter = 0
    importMongo = {"interacao": []}
    for i in range(2):
        print(dados['interacao'][i])
        importMongo['interacao'].append(dados['interacao'][i])
    # print(importMongo)

    return importMongo


objs = importJsonTuya()

window = tk.Tk()
window.title("Objetos")
window.configure(bg="white")
window.minsize(500, 400)
window.maxsize(500, 400)

menu = tk.Menu(window)
window.config(menu=menu)
menu.add_command(label="Voltar", command=start)

button = []
label = tk.Label(text="a", font=("Calibri", 14, "normal"), width=window.winfo_screenwidth(
), height=window.winfo_screenheight(), relief=tk.RIDGE, borderwidth=5, bg="white", fg="black", justify="left")
for i in objs['interacao']:
    button.append(tk.Button(text=str(i['intera_Obj_i']), font=(
        "Calibri", 16, "normal"), height=2, relief=tk.RIDGE, borderwidth=5, bg="white", fg="black"))

start()
window.mainloop()
