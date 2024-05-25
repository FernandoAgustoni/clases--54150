




class Cliente:
    def __init__ (self,Nombre_Cliente,Contraseña,Dni,mail):
        
        print ("Ejecutando el init")
        self.Nombre_Cliente = Nombre_Cliente
        self.Contraseña = Contraseña
        self.Dni= Dni 
        self.mail= mail   
        
    def AgregarAlDiccionario(self,Diccionario):        
        Diccionario [self.Nombre_Cliente] = self   
        
    def cambiarContraseña (self,Contraseña_nueva):
          self.Contraseña= Contraseña_nueva
          
    def __repr__(self):
        
        return f"(Cliente con DNI: {self.Dni}, Nombre: {self.Nombre_Cliente}, Contraseña: {self.Contraseña}, mail:{self.mail})"
         
 

    
  
        
         
            