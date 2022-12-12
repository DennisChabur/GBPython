import ui_c
import Calculation as C

func = ui_c.input_c()


def check_action(func):
    if func[1] == '+': return C.sum_c()
    elif func[1] == '-': return C.sub_c()
    elif func[1] == '*': return C.mult_c()
    elif func[1] == '/': return C.div_c()


def check_c(func):
    if (type(func[0]) == float or type(func[0]) == complex) and func[1] in '+-*/' and (type(func[2]) == float or type(func[2]) == complex):
        return True
    else:
    print("Некорректный ввод")
    return False
