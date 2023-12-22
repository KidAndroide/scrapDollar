import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import font
from PIL import ImageTk
import ttkbootstrap as ttk

urls = ["https://dolarhoy.com/cotizaciondolarblue", "https://dolarhoy.com/cotizacion-dolar-oficial",
        "https://dolarhoy.com/cotizaciondolarbolsa"]

valores = []

for url in urls:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    divs = soup.findChild('div', {'class': 'value'})

    for div in divs:
        valor = div.text
        valores.append(valor)

print(f"El valor del dólar oficial es de: {valores[1]}")
print(f"El valor del dólar blue es de: {valores[0]}")
print(f"El valor del dólar mep es de: {valores[2]}")


def mostrar_valor_dolar_oficial():
    value = valores[1]
    label.config(text=f"El valor del dólar oficial es de: {value}")


# Function to display the blue dollar value
def mostrar_valor_dolar_blue():
    value = valores[0]
    label.config(text=f"El valor del dólar blue es de: {value}")


def mostrar_valor_dolar_mep():
    value = valores[2]
    label.config(text=f"El valor del dólar mep es de: {value}")


window = ttk.Window(themename="flatly")
window.geometry("400x250")

# Create buttons
button_oficial = ttk.Button(window, text="Dólar Oficial", command=mostrar_valor_dolar_oficial, bootstyle="success",
                            width=50)
button_blue = ttk.Button(window, text="Dólar Blue", command=mostrar_valor_dolar_blue, bootstyle="success", width=50)
button_mep = ttk.Button(window, text="Dólar Mep", command=mostrar_valor_dolar_mep, bootstyle="success", width=50)

# Create label to display the values
label = tk.Label(window, text="", font=("helvetica", 15), pady=10)

# Add buttons and label to the window
button_oficial.pack(pady=5)
button_blue.pack(pady=5)
button_mep.pack(pady=5)
label.pack()

# Run the tkinter event loop
window.mainloop()
