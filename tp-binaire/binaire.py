from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def conversion(n):
    ch = ""
    while n != 0:
        res = str(n % 2)
        ch = res + ch
        n = n // 2
    return ch


def verif(x):
    i = 0
    ver = True
    while (ver is True) and (i < len(x)):
        if "0" <= x[i] <= "9":
            i = i + 1
        else:
            ver = False
    return ver


def interface():
    x = f.a.text()
    if verif(x) is False:
        msg = "error"
        res = ""
    else:
        res = conversion(int(x))
        nf = res.count("0")
        nt = res.count("1")
        if nf == nt:
            msg = "proprieté vérifiée"
        else:
            msg = "prprieté non vérifiée"
    f.b.setText(res)
    f.c.setText(msg)


app = QApplication([])
f = loadUi("interface.ui")
f.show()
f.d.clicked.connect(interface)
app.exec_()
