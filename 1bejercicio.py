import json
fich=open("/home/franhidalgo/Documentos/LM/Json/asociaciones.txt","r")
asociaciones=json.load(fich)
fich.close()
for a in asociaciones ["directorios"]["directorio"]:
	print a["nombre"]["content"]