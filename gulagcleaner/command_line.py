
#from gulagcleaner import gulagcleaner_extract
from gulagcleaner import gulagcleaner_extract
from os.path import exists
import argparse

def main():  
    import sys         
    parser = argparse.ArgumentParser(prog="GulagCleaner",
                        description='Eliminador de anuncios de pdfs de Wuolah.')
    parser.add_argument('pdf', nargs='+',default=[])
    parser.add_argument('-r','--replace', dest='reemplazar', action='store_true',
                        help='reemplaza el pdf original')
    parser.add_argument('-v','--verborse', dest='verbose', action='store_true',
                        help='aporta información del pdf')        
    args = parser.parse_args()
    for arg in args.pdf:
        print(arg)
        return_msg=gulagcleaner_extract.deembed(arg,args.reemplazar)
        if (return_msg["Success"] and args.verbose):
            print("Deembedding successful. File saved in",return_msg["return_path"])
            print("Metadata:")
            print("Archivo: "+return_msg["Meta"]["Archivo"])
            print("Autor: "+return_msg["Meta"]["Autor"])
            print("Asignatura: "+return_msg["Meta"]["Asignatura"])
            print("Curso y Grado: "+return_msg["Meta"]["Curso y Grado"])
            print("Facultad: "+return_msg["Meta"]["Facultad"])
            print("Universidad: "+return_msg["Meta"]["Universidad"])
            print("Error:",return_msg["Error"])
        else:
            pass
if __name__ == "__main__":
    print('Call from the "gulagcleaner" command.')