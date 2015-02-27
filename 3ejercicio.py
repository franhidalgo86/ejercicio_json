import json
fich=open("/home/franhidalgo/Documentos/LM/Json/asociaciones.txt","r")
asociaciones=json.load(fich)
fich.close()
socios=raw_input(int("Mete un numero de socios: "))
for soc in asociaciones ["directorios"]["directorio"]:
	print soc["descripcion"]["content"]>=socios