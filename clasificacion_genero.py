import os
import uuid
import cv2
import numpy as np
from deepface import DeepFace

# Suprimir logs de TensorFlow para que no ensucien la consola
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def renombrar_definitivo():
    # --- RUTA DE TU CARPETA ---
    ruta_carpeta = r"C:\Users\User\Downloads\FOTOS_PERSONAS (5)\FOTOS_PERSONAS"
    
    if not os.path.exists(ruta_carpeta):
        print(f"❌ Carpeta no encontrada: {ruta_carpeta}")
        return

    # 1. Obtener archivos
    archivos = [f for f in os.listdir(ruta_carpeta) 
                if os.path.isfile(os.path.join(ruta_carpeta, f)) and not f.endswith('.py')]
    
    print(f"🚀 Iniciando análisis en {len(archivos)} archivos...")

    # 2. Renombrar a temporal
    lista_temporales = []
    for archivo in archivos:
        path_origen = os.path.join(ruta_carpeta, archivo)
        ext = os.path.splitext(archivo)[1]
        temp_name = f"temp_{uuid.uuid4()}{ext}"
        path_temp = os.path.join(ruta_carpeta, temp_name)
        try:
            os.rename(path_origen, path_temp)
            lista_temporales.append(temp_name)
        except:
            pass

    # 3. Análisis
    cM = 1
    cF = 1
    cX = 1
    
    for archivo_temp in lista_temporales:
        ruta_temp = os.path.join(ruta_carpeta, archivo_temp)
        ext = os.path.splitext(archivo_temp)[1]
        nuevo_nombre = ""

        try:
            img = cv2.imread(ruta_temp)
            
            # ---> AQUÍ ESTABA EL ERROR, YA LO QUITÉ <---
            analisis = DeepFace.analyze(
                img_path = img, 
                actions = ['gender'], 
                detector_backend = 'retinaface', 
                enforce_detection = False
                # Se eliminó 'verbose=0' que causaba el crash
            )
            
            genero = analisis[0]['dominant_gender']
            
            if genero == 'Man':
                nuevo_nombre = f"mpersona_{cM}{ext}"
                cM += 1
            elif genero == 'Woman':
                nuevo_nombre = f"fpersona_{cF}{ext}"
                cF += 1
            else:
                nuevo_nombre = f"persona_{cX}{ext}"
                cX += 1
                
        except Exception as e:
            print(f"⚠️ No detectado: {archivo_temp}")
            nuevo_nombre = f"desconocido_{cX}{ext}"
            cX += 1

        # Renombrar final
        try:
            ruta_final = os.path.join(ruta_carpeta, nuevo_nombre)
            os.rename(ruta_temp, ruta_final)
            print(f"✅ Guardado: {nuevo_nombre}")
        except:
            pass

    print(f"\n🎉 TERMINADO.")
    print(f"Hombres: {cM-1} | Mujeres: {cF-1}")

if __name__ == "__main__":
    renombrar_definitivo()