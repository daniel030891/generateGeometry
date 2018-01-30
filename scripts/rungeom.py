# -*- coding: utf-8 -*-
import sys, shapefile, shutil
from coordinates import *

# PARAMETROS
code = sys.argv[1]  # Codigo de petitorio
table = sys.argv[2]  # Tabla consultada
name = sys.argv[3]  # Nombre de salida de polygono
wkid = int(sys.argv[4])  # Codigo EPSG del sistema de referencia
concession = sys.argv[5]    # Concesion minera
resignation = sys.argv[6]   # Tipo de renuncia


'''
Variable global de direccion donde se almacenara el archivo
resultante
'''
output = os.path.join(Statics().out, '{}.shp'.format(name))

'''
Objeto que permite obtener los datos del
petitorio consultado.
Recibe como parametro el codigo del petitorio;
La conexion a base de datos y las tablas 
consultadas pueden conocerse desde el archivo 
.\settings\model.py
'''


class GetData:
    # Inicializando objeto
    def __init__(self, code):
        self.code = code
        self.table = GetTable(table).table

    '''
    Obtiene las coordenadas a partir del objeto 
    atributo 'self.table' el cual instancia al 
    objeto 'GetTable()', las propiedasdes y 
    funcionalidades de el objeto mencionado se 
    puede consultar en el archivo 'coordinates.py'
    '''

    def getCoordsOfTable(self):
        '''
        Metodo 'setcode', permite configurar
        el identificador del registro minero
        de interes, con le fin de obtener nuevas
        coordenadas
        '''
        self.table.settable(code, wkid)
        '''
        Almacenando las coordenadas en el atributo
        self.coords
        '''
        self.coords = self.table.getcoords()

    # Metodo principal del oobjeto actual
    def main(self):
        # # Intenta
        # try:
        #     # Ejecuta el proceso
        self.getCoordsOfTable()
        # # Si se obtiene un error
        # except Exception as e:
        #     # Imprime el error
        #     print e


'''
Objeto que permite la construccion de un archivo
shapefile a partir del conjunto de
coordenadas obtenidos desde el objeto GetData
'''


class MakeGeometry:
    # Inicializando objeto
    def __init__(self, coord):
        # Coordenadas
        self.coord = coord

    def getSpatialReference(self):
        # Obtener el prj segun la variable 'wkid'
        prjfile = os.path.join(Statics().prj, '{}.prj'.format(wkid))
        # Crear el nombre de salida del prj
        prj = os.path.basename(output).split(".")[0] + '.prj'
        # Copiar el prj en la ubicacion adecuada
        shutil.copy(prjfile, os.path.join(os.path.dirname(output), prj))

    # Construye el archivo shapefile
    def generatePolygon(self):
        # Iniciando la escritura del nuevo shapefile
        shp = shapefile.Writer(shapefile.POLYGON)
        # Agregando coordenadas
        shp.poly(parts=self.coord)
        # Creando campo para asignar el codigo ingresado
        shp.field('CODIGOU', 'C', '40')
        shp.field('CONCESION', 'C', '50')
        shp.field('TIPO_RENUN', 'C', '40')
        shp.field('HAS', 'N', decimal=4)

        # Registrando el codigo dentro del campo
        shp.record(code, concession, resignation, None)
        # Almacenando shapefile segun parametro 'output'
        shp.save(output)

        shp = shapefile.Reader(output)
        temp = shp.shape(0)
        geojson = temp.__geo_interface__

        from shapely.geometry import shape

        area = shape(geojson).area/10000

        e = shapefile.Editor(output)
        self.modify('HAS', area, e)
        e.save(output)

        # Eliminando la variable shp
        del shp
        # Adignando Sistema de referencia
        self.getSpatialReference()


    def modify(self, key, value, e):
        for i in e.records[0]:
            if not i:
                idx = e.records[0].index(i)
                e.records[0][idx] = value
                break


    # Metodo principal del objeto
    def main(self):
        # Intentar
        try:
            # Ejecutar proceso
            self.generatePolygon()
        # Si se obtiene un error
        except Exception as e:
            # Imprime la causa del error
            print e


# Si se ejecuta el archivo actual
if __name__ == "__main__":
    poo = GetData(code)
    poo.main()
    # Instancia el objeto MakeGeometry
    foo = MakeGeometry(poo.coords)
    # Ejecuta el proces principal
    foo.main()
