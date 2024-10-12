import tkinter as tk
from tkinter import ttk, font, messagebox

# Classe principal do app
class AppTarefa:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Tarefa")
        self.root.configure(bg="#F0F0F0")
        self.root.geometry("500x600")
        
        self.tarefas = []  # Lista para armazenar as tarefas
        
        # Configuração do título
        self.titulo = font.Font(family="Garamond", size=24, weight="bold")
        self.tituloMenu = tk.Label(self.root, text="Menu de Tarefas", font=self.titulo, bg="#F0F0F0", fg="#333")
        self.tituloMenu.pack(pady=20)
        
        # Frame para entrada e botão de adicionar tarefa
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(pady=10)
        
        self.entrada = tk.Entry(self.frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
        self.entrada.pack(side=tk.LEFT, padx=10)
        
        self.btnAdicionar = tk.Button(self.frame, text="Adicionar", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT, command=self.adicionar_tarefa)
        self.btnAdicionar.pack(side=tk.LEFT, padx=10)
        
        # Frame para a lista de tarefas
        self.frameLista = tk.Frame(self.root, bg="white")
        self.frameLista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.canvas = tk.Canvas(self.frameLista, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = ttk.Scrollbar(self.frameLista, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvasInterior = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.canvasInterior, anchor="nw")
        self.canvasInterior.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.atualizar_lista_tarefas()

    # Função para adicionar tarefa
    def adicionar_tarefa(self):
        tarefa = self.entrada.get()
        if tarefa != "":
            self.tarefas.append({"nome": tarefa, "feita": False})  # Adiciona uma tarefa com status "não feita"
            self.entrada.delete(0, tk.END)
            self.atualizar_lista_tarefas()
        else:
            messagebox.showwarning("Entrada inválida", "Digite uma tarefa válida.")
    
    # Função para marcar como feita ou desfazer
    def marcar_feita(self, tarefa):
        tarefa["feita"] = not tarefa["feita"]  # Alterna entre feita e não feita
        self.atualizar_lista_tarefas()
    
    # Função para remover tarefa
    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
            self.atualizar_lista_tarefas()
    
    # Função para atualizar a lista de tarefas na interface
    def atualizar_lista_tarefas(self):
        for widget in self.canvasInterior.winfo_children():
            widget.destroy()
        
        for tarefa in self.tarefas:
            frame_tarefa = tk.Frame(self.canvasInterior, bg="white")
            frame_tarefa.pack(fill=tk.X, padx=5, pady=5)
            
            # Verifica se a tarefa está marcada como "feita" para riscar o texto
            if tarefa["feita"]:
                lbl_tarefa = tk.Label(frame_tarefa, text=tarefa["nome"], font=("Garamond", 14, "overstrike"), bg="white", anchor="w")
            else:
                lbl_tarefa = tk.Label(frame_tarefa, text=tarefa["nome"], font=("Garamond", 14), bg="white", anchor="w")
            lbl_tarefa.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            # Botão para marcar como feita/desfazer
            btn_feita = tk.Button(frame_tarefa, text="Feita" if not tarefa["feita"] else "Desfazer", bg="#2196F3", fg="white", command=lambda t=tarefa: self.marcar_feita(t))
            btn_feita.pack(side=tk.LEFT, padx=5)
            
            # Botão para remover tarefa
            btn_remover = tk.Button(frame_tarefa, text="Remover", bg="#f44336", fg="white", command=lambda t=tarefa: self.remover_tarefa(t))
            btn_remover.pack(side=tk.RIGHT, padx=10)

# Inicializando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = AppTarefa(root)
    root.mainloop()
