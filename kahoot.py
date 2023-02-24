from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def botin_luonti(koodi, montako, nimi):
    
    luku = 0
    while luku < montako:
        #Avaa Edge selaimen
        selain = webdriver.Edge()
        selain.get("https://kahoot.it")

        #Pin-koodi
        pin = selain.find_element(By.ID, "game-input")
        pin.send_keys(koodi)
        pin.send_keys(Keys.RETURN)
        time.sleep(1)

        #Nimi
        nickname = selain.find_element(By.ID, "nickname")
        if luku == 0:
            nickname.send_keys(nimi)

        else:
            nimi2 = nimi + str(luku)
            nickname.send_keys(nimi2)
        
        nickname.send_keys(Keys.RETURN)
        luku += 1
        time.sleep(1)
        
def main():

    koodi = input("Pelin koodi: ")
    montako = int(input("Montako bottia: "))
    nimi = input("Botin nimi: ")

    botin_luonti(koodi, montako, nimi)

if __name__ == "__main__":
    main()
