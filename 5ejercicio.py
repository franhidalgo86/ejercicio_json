import json
fich=open("/home/franhidalgo/Documentos/LM/Json/asociaciones.txt","r")
asociaciones=json.load(fich)
fich.close()
for telf in asociaciones ["directorios"]["directorio"]:
	if " // " in telf["telefono"]["content"]:
		print telf["nombre"]["content"] 
