import json
fich=open("/home/franhidalgo/Documentos/LM/Json/asociaciones.txt","r")
asociaciones=json.load(fich)
fich.close()
contador=0
for corre in asociaciones ["directorios"]["directorio"]:
	if "@" in corre["correo-electronico"]:
