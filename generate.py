import numpy as np
import xlwings as xw
def main():
    app.screen_updating = False
    #壳体90.45-91.35,90.9
    wb.sheets[0].range("A1").options(transpose=True).value=np.round(np.random.normal(90.8, 0.1111, 100),2)
    #蜗杆90.875,90.14,90.5075
    wb.sheets[0].range("D1").options(transpose=True).value=np.round(np.random.normal(90.5, 0.1000, 100),2)
    app.screen_updating = True


#下面用于调试
if __name__ == '__main__':
    set_mock_caller()
app = xw.apps.active
wb = xw.Book.caller()
if __name__ == '__main__':
    main()