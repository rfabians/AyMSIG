from dataclasses import dataclass

@dataclass
class RutasOptimasAym:
    NombreRuta:str
    Costo:int
    RutaID:str
    


    @staticmethod
    def almacenarRuta(ruta:str, costo:int, rutaID:str)->'RutasOptimasAym':
      
        rutaPath = ruta.split('\\')
        nombre = rutaPath[-1].split('.')[0]
        
        return RutasOptimasAym(
            Costo= costo,
            NombreRuta = nombre,
            RutaID=rutaID
        )