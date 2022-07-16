import pandas as pd
import re
import numpy as np
import math
#from google.colab import output
import matplotlib.pyplot as plt
#from imp import reload
#reload(plt)
#output.clear()

def seleccion(orig, info, info_orig):
  listafinal = []
  if ',' in orig:
    orig = orig.split(',')
  else:
    orig = [orig]

  for a in orig:
    a = a.strip()
    if info_orig[-1] != 'No especificado':
      if ':' in a:
        a = a.split(':')
        for b in [0,1]:
          a[b] = a[b].strip()
        if info[a[0]]>info[a[1]]:
          a[0], a[1] = a[1], a[0]
        rango = range(info[a[0]], info[a[1]]+1)
        for c in rango:
          if c not in listafinal:
            listafinal.append(c)
      else:
        if info[a] not in listafinal:
          listafinal.append(info[a])
    else:
      if ' a ' in a:
        a = a.split(' a ')
        for b in [0,1]:
          a[b] = a[b].strip(' años').strip()
          if 'y' in a[b] or 'm' in a[b]: a[b] = 100
          elif 'e' in a[b]: a[b] = 105
          elif 't' in a[b]: a[b] = -5
          a[b] = math.floor(int(a[b])/5) + 1
        if a[0] > a[1]:
          a[0], a[1] = a[1], a[0]
        rango = range(a[0], a[1] + 1)
        for c in rango:
          if c not in listafinal:
            listafinal.append(c)
      else:
        try:
          a = math.floor(int(a)/5 + 1)
          if a not in listafinal:
            listafinal.append(a)
        except:
          if 'y' in a and 21 not in listafinal:
            listafinal.append(21)
          elif 't' in a and 0 not in listafinal:
            listafinal.append(0)
          elif 'e' in a and 22 not in listafinal:
            listafinal.append(22)
  listafinal.sort()
  for a in range(0, len(listafinal)):
    listafinal[a] = info_orig[listafinal[a]]


  return listafinal


fechas =            {'1990': 0, '1995': 1, '2000': 2, '2005': 3, '2010': 4, '2020': 5}

fechas_originales = ['1990', '1995', '2000', '2005', '2010', '2020']

entidades = {'Estados Unidos Mexicanos': 0, 'Aguascalientes': 1, 'Baja California': 2, 'Baja California Sur': 3, 'Campeche': 4, 'Coahuila De Zaragoza': 5, 'Colima': 6, \
             'Chiapas': 7, 'Chihuahua': 8, 'Ciudad De México': 9, 'Durango': 10, 'Guanajuato': 11, 'Guerrero': 12, 'Hidalgo': 13, 'Jalisco': 14, 'México': 15, 'Michoacán De Ocampo': 16,\
             'Morelos': 17, 'Nayarit': 18, 'Nuevo León': 19, 'Oaxaca': 20, 'Puebla': 21, 'Querétaro': 22, 'Quintana Roo': 23, 'San Luis Potosí': 24, 'Sinaloa': 25, 'Sonora': 26,\
             'Tabasco': 27, 'Tamaulipas': 28, 'Tlaxcala': 29, 'Veracruz De Ignacio De La Llave': 30, 'Yucatán': 31, 'Zacatecas': 32}

entidades_originales = ['Estados Unidos Mexicanos', 'Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Coahuila de Zaragoza', 'Colima', \
             'Chiapas', 'Chihuahua', 'Ciudad de México', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán de Ocampo',\
             'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', \
             'Tamaulipas', 'Tlaxcala', 'Veracruz de Ignacio de la Llave', 'Yucatán', 'Zacatecas']

edades  =            {'Total': 0, '0 a 4 años': 1, '5 a 9 años': 2, '10 a 14 años': 3, '15 a 19 años': 4, '20 a 24 años': 5, '25 a 29 años': 6, '30 a 34 años': 7,\
                      '35 a 39 años': 8, '40 a 44 años': 9, '45 a 49 años': 10, '50 a 54 años': 11, '55 a 59 años': 12, '60 a 64 años': 13, '65 a 69 años': 14,\
                      '70 a 74 años': 15, '75 a 79 años': 16, '80 a 84 años': 17, '85 a 89 años': 18, '90 a 94 años': 19, '95 a 99 años': 20, '100 años y más': 21, 'No especificado': 22}

edades_originales = [ 'Total', '0 a 4 años', '5 a 9 años', '10 a 14 años', '15 a 19 años', '20 a 24 años', '25 a 29 años', '30 a 34 años',\
                      '35 a 39 años', '40 a 44 años', '45 a 49 años', '50 a 54 años', '55 a 59 años', '60 a 64 años', '65 a 69 años', '70 a 74 años',\
                      '75 a 79 años', '80 a 84 años', '85 a 89 años', '90 a 94 años', '95 a 99 años', '100 años y más', 'No especificado']

genero = {'Total': 0, 'Hombres': 1, 'Mujeres': 2}

genero_original = ['Total', 'Hombres', 'Mujeres']

funciones = {'Tasa o proporción de masculinidad (T.M.)': 0, 'Índice o razón de masculinidad (I.M.)': 1, 'Índice o razón de masculinidad por edades (I.M.E.)': 2,
             'Tasa de dependencia (T.D.)': 3, 'Índice de dependencia (I.D.)': 4, 'Índice de dependencia corregido (I.D.C.)': 5, 'Índice de dependencia juvenil (I.D.J.)': 6,
             'Índice de dependencia de los viejos (I.D.V.)': 7, 'Tasa de juventud (T.J.)': 8, 'Tasa de envejecimiento (T.E.)': 9, 'Índice de envejecimiento (I.E.)': 10}

funciones_originales = ['Tasa o proporción de masculinidad (T.M.)', 'Índice o razón de masculinidad (I.M.)', 'Índice o razón de masculinidad por edades (I.M.E.)',
             'Tasa de dependencia (T.D.)', 'Índice de dependencia (I.D.)', 'Índice de dependencia corregido (I.D.C.)', 'Índice de dependencia juvenil (I.D.J.)',
             'Índice de dependencia de los viejos (I.D.V.)', 'Tasa de juventud (T.J.)', 'Tasa de envejecimiento (T.E.)', 'Índice de envejecimiento (I.E.)']

print('¿Que funcion quieres obtener? Estas son tus opciones:\n')
for x in [0,1,2,3]:
  try: print(funciones_originales[0+3*x:3+3*x])
  except: print(funciones_originales[3*x:])
abcd0 = input('\nDame el acronimo de la funcion\t\t\t\t\t').upper()

listafuncion = []
if abcd0 == '':
  abcd0 = ['T.M.', 'I.M.']         # Para la forma predeterminada
else:
  abcd0 = abcd0.split(',')
for a in range(0,len(funciones)):
  for b in range(0, len(abcd0)):
    c = abcd0[b].strip().strip('(').strip(')').strip('.')
    if f'({c}.)' in funciones_originales[a] and funciones[funciones_originales[a]] not in listafuncion:
      listafuncion.append(funciones[funciones_originales[a]])
listafuncion.sort()
for a in range(0,len(listafuncion)):
  listafuncion[a] = (funciones_originales[listafuncion[a]] , listafuncion[a])

# aqui pido la primer variable, el año (los años)
print(f'\n¿Sobre que fecha quieres tomar la informacion? Estas son tus opciones:\n\n{fechas_originales}')
abcd1 = input(f'\nEscribelo de la manera "Fecha:Fecha" si quieres un rango, y "Fecha, Fecha" si quieres multiples resultados\n\n\t\t\t\t\t\t\t\t\t')
if abcd1 == '':
  abcd1 = '1990 : 2020'         # Para la forma predeterminada, o editable para cuando quieras probar otras variables sin tener que escribirlo cada vez
listafechas = seleccion(abcd1, fechas, fechas_originales)



# aqui pido la segunda variable, la(s) entidad(es)

print('\n\n¿Sobre que estado quieres tomar la informacion? Estas son tus opciones: \n')
print(f'''{entidades_originales[0:5]}\n{entidades_originales[5:11]}\n{entidades_originales[11:17]}\n{entidades_originales[17:23]}\n{entidades_originales[23:29]}\n{entidades_originales[29:]}''')
abcd2 = input('\nEscribelo de la manera "Entidad:Entidad" si quieres un rango, y "Entidad, Entidad" si quieres multiples resultados (usa acentos)\n\n\t\t\t\t\t\t\t\t\t').title()
if abcd2 == '':
  abcd2 = 'Estados Unidos Mexicanos : Zacatecas'               # Para la forma predeterminada, o editable para cuando quieras probar otras variables sin tener que escribirlo cada vez
listaentidades = seleccion(abcd2, entidades, entidades_originales)


# aqui pido la tercer variable, Sexo(s)
funciones_sin_genero_requerido = ['T.M.', 'I.M.']
for a in listafuncion:
  if a[1] != 0 and a[1] != 1:
    print('\n¿Cual es el genero de investigacion? Estas son tus opciones:\n\n', genero_original, '\nEscribelo de la manera "Genero: Genero" si quieres un rango, y "Genero, Genero" si quieres multiples resultados')
    abcd3 = input('\t'*12).title()
  else:
    abcd3 = ''
    continue
if abcd3 == '':
  abcd3 = 'Total : Mujeres'        # Para la forma predeterminada, o editable para cuando quieras probar otras variables sin tener que escribirlo cada vez
listagenero = seleccion(abcd3, genero, genero_original)


# aqui pido la cuarta variable, la(s) edad(es) quinquenal(es)
funciones_sin_edad_requerida = ['T.M.', 'I.M.']
for a in listafuncion:
  if a[1] != 0 and a[1] != 1:
    print('\n¿Sobre que edades quieres tomar la informacion? Estas son tus opciones:\n')
    [print(edades_originales[0+6*x:6+6*x]) for x in [0,1,2,3]]
    print('Escribelo de la manera "Edad a Edad" y agrega "," si quieres multiples rangos u opciones (No escribas "años")\n')
    abcd4 = input('\t'*12).capitalize()
  else:
    abcd4 = 'Total'
if abcd4 == '':
  abcd4 = 'Total a no especificado'         # Para la forma predeterminada, o editable para cuando quieras probar otras variables sin tener que escribirlo cada vez
listaedades = seleccion(abcd4, edades, edades_originales)



# aqui es la construccion del Dataframe

c = pd.read_csv("Poblacion completa proyecto.csv",
                skiprows= 3, header= None,
                usecols= range(2,20), nrows= 2)
columnas = [np.array(c.iloc[0]),
            np.array(c.iloc[1])]
f  = pd.read_csv("Poblacion completa proyecto.csv",
                 skiprows= 4, usecols= [0,1],
                 nrows= 759)
filas    = [np.array(f['Entidad federativa']),
            np.array(f['Grupo quinquenal de edad'])]
df = pd.read_csv("Poblacion completa proyecto.csv",  skiprows= 4,
                 usecols= range(2,20),
                 nrows= 759)
informacioncompleta = pd.DataFrame(data = df).set_axis(columnas, axis=1).set_axis(filas, axis=0)
informacion_a_graficar = informacioncompleta[listafechas].loc[listaentidades]


dfconcat = [informacion_a_graficar[(a, b)] for a in listafechas for b in listagenero]
informacion_a_graficar2 = pd.concat(dfconcat, axis = 1)


dfconcat = [informacion_a_graficar2.transpose()[(a,b)] for a in listaentidades for b in listaedades]
informacion_a_graficar2 = pd.concat(dfconcat, axis= 1).transpose()

#output.clear()
print(f'Fechas: "{abcd1}", es decir: ', listafechas)
print(f'Entidades: "{abcd2}", es decir: ', listaentidades)
print(f'Generos: "{abcd3}", es decir: ', listagenero)
print(f'Edades: "{abcd4}", es decir: ', listaedades, '\n')

lista1 = []
for a in listaentidades:
  for b in informacion_a_graficar2.loc[(a,'Total')]:
    lista1.append(int(re.sub(" ", "", b)))

tasas_masc = []
t_masc     = []
col_t_masc = []
indic_masc = []
i_masc     = []
col_i_masc = []
for a in range(0, len(listafechas)):
  for b in range(0, len(listaentidades)):
    pobl_total  = lista1[    a*3 + b*3*len(listafechas)]
    pobl_hombre = lista1[1 + a*3 + b*3*len(listafechas)]
    pobl_mujer  = lista1[2 + a*3 + b*3*len(listafechas)]
    temp1 = round(pobl_hombre / pobl_total  * 100   ,   3)
    temp2 = round(pobl_hombre / pobl_mujer  * 100   ,   3)
    t_masc.append((temp1, listafechas[a], listaentidades[b]))
    col_t_masc.append(listaentidades[b])
    tasas_masc.append(temp1)
    i_masc.append((temp2, listafechas[a], listaentidades[b]))
    col_i_masc.append(listaentidades[b])
    indic_masc.append(temp2)

'''for a, b, c in t_masc:
  print(f'La tasa de masculinidad (T.M.) de {c} en {b} es: {a}')
for a, b, c in i_masc:
  print(f'El indice de masculinidad (I.M.) de {c} en {b} es: {a}')'''

def mostrargrafico(listafechas, listaentidades, indic_masc, nombre, nombrey):
    colores = ['green', 'blue', 'red', 'brown', 'purple', 'black']
    y = int(len(indic_masc)/len(listafechas))
    plt.figure(figsize = (y/3, 7.0))
    for x in range(0, len(listafechas)):
      m = listafechas[x]
      rd = colores[x]
      datos = indic_masc[x*y: y+ x*y]
      plt.plot(listaentidades,  datos, marker = '_', markersize = 8 , c = rd, label = m)
      #output.clear()

    plt.legend(bbox_to_anchor=(1.05, 1),loc= 'upper right')
    plt.xlabel('Estado', fontsize = 10)
    plt.xticks(rotation= 90)
    plt.ylabel(nombrey , fontsize = 10)
    plt.title(f'{nombre} por estado', fontsize = 20)
    plt.show()
    return


for funcion in listafuncion:
  if funcion[1] == 0:
    x = input(f'\n¿Quieres una grafica (por fecha) de la Tasa o proporción de masculinidad (T.M.)?    (SI/NO, "Enter" = NO)\n\n').lower()
    if x == 'si':
      print('')
      mostrargrafico(listafechas, listaentidades, tasas_masc, 'Tasa o proporción de masculinidad (T.M.)', 'Población Masc / Poblacion Total  (%)')
  if funcion[1] == 1:
    x = input('\n¿Quieres una grafica (por fecha) de el Índice o razón de masculinidad (I.M.)?    (SI/NO, "Enter" = NO)\n\n').lower()
    if x == 'si':
      print('')
      mostrargrafico(listafechas, listaentidades, indic_masc,  'Índice o razón de masculinidad (I.M.)', 'Población Masc / Poblacion Femen  (%)')

#output.clear()
num_funciones = len(listafuncion)
y = int(len(indic_masc)/len(listafechas))
informacion_a_graficar3 = []
for r in listafuncion:
  dfconcat = []
  fun = []
  if r[1] == 0:
    for x in range(0, len(listafechas)):
      df3 = pd.DataFrame(data = tasas_masc[x*y : y+x*y]).set_axis(listaentidades, axis = 0)
      dfconcat.append(df3)
    a = len(listafechas)*[r[0]]
    fun = fun + a
    columnas = [np.array(fun),
                np.array(listafechas)]
    df_indice_masc = pd.concat(dfconcat, axis= 1).set_axis(columnas, axis = 1)
    informacion_a_graficar3.append(df_indice_masc)

  if r[1] == 1:
    for x in range(0, len(listafechas)):
      df3 = pd.DataFrame(data = indic_masc[x*y : y+x*y]).set_axis(listaentidades, axis = 0)
      dfconcat.append(df3)
    a = len(listafechas) * [r[0]]
    fun = fun + a
    columnas = [np.array(fun),
                np.array(listafechas)]
    df_tasa_masc = pd.concat(dfconcat, axis= 1).set_axis(columnas, axis = 1)
    informacion_a_graficar3.append(df_tasa_masc)


for a in range(0,len(informacion_a_graficar3)):
    print(informacion_a_graficar3[a])
#informacion_a_graficar2

