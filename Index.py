import gspread
from time import sleep
from Enviaremail import sendemail

gc = gspread.service_account(filename='Ligateaterra.json')

sh = gc.open('Ligateaterra').sheet1


for linha in range(1, 20):
    if sh.acell(f'H{linha}').value != '1':
        nome = (sh.acell(f'A{linha}')).value
        site = (sh.acell(f'E{linha}')).value
        email = (sh.acell(f'C{linha}')).value
        texto = f"""Olá {nome}, seu pedido está pronto!
        Para conferir, visite {site}
        """
        assunto = "Liga-te à Terra"
        sendemail(texto, assunto, email)
        sh.update(f'H{linha}', '1')
        sleep(5)

