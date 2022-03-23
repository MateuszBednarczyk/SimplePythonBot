import pyautogui as p

for i in range (2):

    p.sleep(2)

    #kopiowanie
    p.leftClick(299,566)

    #przelaczenie karty na solve
    p.leftClick(350,17)

    #scroll na solvie
    p.leftClick(556,199)
    p.vscroll(-2500)

    #press zaglosuj
    p.leftClick(491,930)

    p.sleep(1)

    #wcisniecie na pole edyc i wklejka
    p.leftClick(491,270)
    p.hotkey('ctrl','v')

    #klikniecie vote
    p.leftClick(475,360)

    #klikniecie na refresh
    p.leftClick(81,58)

    p.sleep(1)

    #powrot do 10 min mail
    p.leftClick(102,28)

    p.sleep(1)

    #generate new mail
    p.leftClick(178,670)

    p.sleep(1)