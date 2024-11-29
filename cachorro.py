class Veiculo:
    def __init__(self, marca, modelo, ano, torque):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  
        self.torque = torque  

    def mover(self, velocidade):
        self.velocidade = velocidade
        print(f"O {self.marca} {self.modelo} ({self.ano}) com torque de {self.torque} Nm está se movendo a {self.velocidade} km/h.")
    
    def parar(self):
        if self.velocidade > 0:
            self.velocidade = 0
            print(f"O {self.marca} {self.modelo} ({self.ano}) reduziu a {self.velocidade} km/h.")
        else:
            print("O veículo já está parado.")

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        self.motor_ligado = False
    
    def ligar(self):
        if not self.motor_ligado:
            self.motor_ligado = True
            print(f"Motor movido a {self.tipo} ligado com uma potência de {self.potencia} CV.")
        else:
            print("O motor já está ligado.")

    def desligar(self):
        if self.motor_ligado:
            self.motor_ligado = False
            print(f"Motor movido a {self.tipo} desligado.")
        else:
            print("O motor já está desligado.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_de_portas, motor, torque):
        super().__init__(marca, modelo, ano, torque)
        self.numero_de_portas = numero_de_portas
        self.motor = motor  

    def abrir_porta(self, porta):
        if 1 <= porta <= self.numero_de_portas:
            print(f"A porta {porta} do {self.marca} {self.modelo} foi aberta.")
        else:
            print(f"Porta {porta} inválida! O carro tem apenas {self.numero_de_portas} portas.")

if __name__ == "__main__":
    motor = Motor(tipo="Gasolina", potencia=258)  # Atualizado: Potência e tipo de motor
    
    carro = Carro(
        marca="Mercedes-Benz", 
        modelo="C300", 
        ano=2023, 
        numero_de_portas=4, 
        motor=motor, 
        torque=400  # Atualizado: Torque
    )

    carro.motor.ligar()    
    carro.mover(80)         # Atualizado: Velocidade do carro
    carro.parar()           
    carro.motor.desligar()
