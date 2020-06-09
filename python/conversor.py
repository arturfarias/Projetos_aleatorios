import tkinter
import re 

app = tkinter.Tk()
app.geometry("400x230")

class Conversor():
	def __init__(self,root):

		self.tela = tkinter.Frame(root)
		self.tela.pack()

		self.nomeDoPrograma = tkinter.Label(self.tela,text="Conversor binário para decimal",font="times 22")
		self.nomeDoPrograma.pack()

		self.explicacao = tkinter.Label(self.tela,text="Digite um número binário")
		self.explicacao.pack()

		self.entrada = tkinter.Entry(self.tela)
		self.entrada.pack()

		self.botao = tkinter.Button(self.tela,text="Converter", command= self.converter)
		self.botao.pack()

		self.resposta = tkinter.Label(self.tela,text="",pady=40)
		self.resposta.pack()

	def converter(self):
		regex = re.compile('^[01]*$')
		binario = self.entrada.get()
		
		decimal = 0
		index = 0
		
		if(regex.match(binario) and len(binario) != 0):
			for b in binario[::-1]:
				decimal += int(b) * 2**index

				index +=1 
			
			self.resposta.configure(text=decimal,fg="black",font="times 28")  

		else:
			self.resposta.configure(text="Não é um número binário valido",fg="red",font="times 20")      





Conversor(app)
app.mainloop()