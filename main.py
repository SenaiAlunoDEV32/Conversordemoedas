
import customtkinter
 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
 
janela = customtkinter.CTk()
janela.geometry("600x600")
 

titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 28))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("", 16))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino",  font=("", 16))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"])  

def converter_moeda():
    print("Converter Moeda")

botao_converter = customtkinter.CTkButton(janela, text="CONVERTER",command=converter_moeda,  font=("", 14))
lista_moedas = customtkinter.CTkScrollableFrame(janela)
moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD: Dolar Americano")
moeda2 = customtkinter.CTkLabel(lista_moedas, text="EUR: Euro")
moeda3 = customtkinter.CTkLabel(lista_moedas, text="BRL: Real Brasileiro")
moeda4 = customtkinter.CTkLabel(lista_moedas, text="BTC:Bitcoin")

moedas_disponiveis = ("USD: Dolar Americano", "BTC:Bitcoin", "BRL: Real Brasileiro", "EUR: Euro")

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)

texto_moeda.pack
moeda1.pack()
moeda2.pack()
moeda3.pack()
moeda4.pack()

titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=0)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=0)
campo_moeda_destino.pack(padx=10, pady=0)
botao_converter.pack(padx=10, pady=0)
lista_moedas.pack(padx=10, pady=0)

janela.mainloop()