import pandas as pd

from django.db.utils import IntegrityError

from saber11.models import Departamento, Municipio, Colegio

def extract_from_excel():
    cols_dict = {
        'nombreinstitucion': 'nombre',
        'nombremunicipio': 'ubicacion',
        'promlecturacritica': 'lectura',
        'prommatematica': 'matematicas',
        'promsocialesyciudadanas': 'sociales',
        'promingles': 'ingles',
        'promcienciasnaturales': 'ciencias',
        'evaluado': 'evaluados',
    }
    filename = 'saber11/Resultados-Saber-11-2021-4.xlsx'
    df = pd.read_excel(filename, skiprows=6)
    df.columns = df.columns.str.lower()
    df.rename(columns=cols_dict, inplace=True)
    #print(df.iloc[123])
    #print(df.iloc[123].to_dict())
    return df

def pop_departamentos():
    df = extract_from_excel()
    departamentos = list(df['departamento'].unique())
    nombres = [item.title() for item in departamentos]
    for nombre in nombres:
        d = Departamento(nombre=nombre)
        d.save()
    print('Done...')

def populate_municipios():
    departamentos = Departamento.objects.all()
    dd = {dep.nombre: dep for dep in departamentos}
    df = extract_from_excel()
    codigos = list(df['codigomunicipio'].unique())
    for cod in codigos:
        vals = df[df['codigomunicipio'] == cod]
        val = vals.iloc[0]
        codmun = val.codigomunicipio
        ubicacion = val.ubicacion.title()
        dept = dd[val.departamento.title()]
        #dept = val.departamento.title()
        m = Municipio(codigo=codmun, nombre=ubicacion, departamento=dept)
        m.save()
    conteo = Municipio.objects.count()
    print(f'Se guardaron {conteo} registros')

def populate_colegios():
    eliminar = ['codigomunicipio', 'departamento', 'desvlecturacritica', 'desvmatematica',
        'desvsocialesyciudadanas', 'desvcienciasnaturales', 'desvingles']
    municipios = Municipio.objects.all()
    dm = {mun.codigo: mun for mun in municipios}
    df = extract_from_excel()[1:]
    for index, row in df.iterrows():
        drow = row.to_dict()
        drow['codigomunicipio'] = str(drow['codigomunicipio'])
        drow['codinst'] = str(drow['codinst'])
        drow['ubicacion'] = dm[drow['codigomunicipio']]
        for key in eliminar:
            del drow[key]
        col = Colegio(**drow)
        try:
            col.save()
        except IntegrityError as e:
            print(col, drow)
            print(e)
            break
    print('Done...')

#extract_from_excel()
#pop_departamentos()
#populate_municipios()
