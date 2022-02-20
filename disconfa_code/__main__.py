import argparse
import os
from numpy import append, array
from .version import __version__

def main():
    scriptname = 'Búsqueda de facturas Disconfa 1988' 
    parser = argparse.ArgumentParser()
    parser.add_argument('codigo', type=str, help='Name of the input file.')
    parser.add_argument('-p', '--path', type=str, default='carpeta de facturas o Todo', help='Donde buscar')
    args = parser.parse_args()
    
    print(f'Running {scriptname} V{__version__}')
    archivos_con_codigo_en_path=buscar_archivos_con_condigo_en_path(args.codigo, args.path)
    print(f'Los archivos encontrados con codigo {args.codigo} en {args.path} son los siguientes: {archivos_con_codigo_en_path}')

def buscar_archivos_con_condigo_en_path(codigo, path):
    return [os.path.join(dirtpath, filename) for dirpath, dirnames, files in os.walk(path) if codigo in files]
    
if __name__ == '__main__':
    main()