#from gulagcleaner import gulagcleaner_extract
import gulagcleaner_extract
from os.path import exists
import argparse

def main():
    '''
    Main function called from the "gulagcleaner" CLI command.
    The gulagcleaner command takes an argv for the path and tries to deembed the pages inside it.
    The pages are saved in a new PDF in the same folder.
    '''
    
    import sys        
    if len(sys.argv)>1:
        replace = False
        parser = argparse.ArgumentParser(prog="GulagCleaner",
                            description='Eliminador de anuncios de pdfs de Wuolah.')
        parser.add_argument('-v', action='versión', version='%(prog)s 4.1.6')
        parser.add_argument('-r', dest='reemplazar', action='store_true',
                            help='reemplaza el pdf original')        

        args = parser.parse_args()
        for arg in args:
            if exists(arg):
                return_msg=gulagcleaner_extract.deembed(arg,parser.)
                if return_msg["Success"]:
                    print("Deembedding successful. File saved in",return_msg["return_path"])
                    print("Metadata:")
                    print("Archivo: "+return_msg["Meta"]["Archivo"])
                    print("Autor: "+return_msg["Meta"]["Autor"])
                    print("Asignatura: "+return_msg["Meta"]["Asignatura"])
                    print("Curso y Grado: "+return_msg["Meta"]["Curso y Grado"])
                    print("Facultad: "+return_msg["Meta"]["Facultad"])
                    print("Universidad: "+return_msg["Meta"]["Universidad"])

                else:
                    print("Error:",return_msg["Error"])
            else:
                print("File not found.")
        else:
            pass
    else:
        print('Usage: gulagcleaner "filename". Type "gulagcleaner -h" for more information.')

if __name__ == "__main__":
    print('Call from the "gulagcleaner" command.')
