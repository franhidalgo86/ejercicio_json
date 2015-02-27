import json
fich=open("/home/franhidalgo/Documentos/LM/Json/asociaciones.txt","r")
asociaciones=json.load(fich)
fich.close()
for a in asociaciones ["directorios"]["directorio"]:
	print a["nombre"]["content"]
asociacion=raw_input("Mete una Asociacion: ")
for pre in asociaciones:
	if pre["nombre"]["content"]==asociacion:
		print pre["descripcion"]["content"] 
