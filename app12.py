import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# --- CONFIGURACIÓN GENERAL ---
CANTIDAD = 25000
FECHA_INICIO = '2023-01-01'
FECHA_FIN = '2026-01-03'

fake = Faker('es_MX')

# --- 1. CONFIGURACIÓN DE FOTOS ---
BASE_IMG = "https://github.com/JUANCITOPENA/GENERADOR_IMAGENES_PERSONAS/blob/main/FOTOS_PERSONAS_UBER_MAS"
RAW = "?raw=true"

# --- 2. VEHÍCULOS ---
motos = [
    {'marca': 'Suzuki', 'modelo': 'Ax100', 'tipo': 'Uber Moto', 'url': 'https://acdn-us.mitiendanube.com/stores/002/819/620/products/ax-100-11-c2939b756d9857f46916837342288718-1024-1024.webp'},
    {'marca': 'Bajaj', 'modelo': 'Platina', 'tipo': 'Uber Moto', 'url': 'https://bajajmotos.com.mx/wp-content/uploads/2024/04/image-73-1024x623.webp'},
    {'marca': 'Yamaha', 'modelo': 'DT', 'tipo': 'Uber Moto', 'url': 'https://www.santodomingomotors.com.do/wp-content/uploads/2022/12/ce8904c1-2183-4899-b390-d46f5a748fa9-sdmweb.png'}
]

carros = [
    {'marca': 'Hyundai', 'modelo': 'Sonata Y20', 'tipo': 'UberX', 'url': 'https://islarentacar.net/wp-content/uploads/2020/02/Sonata-Y20.png'},
    {'marca': 'Toyota', 'modelo': 'Corolla', 'tipo': 'UberX', 'url': 'https://www.toyocosta.com/wp-content/uploads/2024/10/corolla_sedan_plateado.png'},
    {'marca': 'Kia', 'modelo': 'K5', 'tipo': 'UberX', 'url': 'https://www.kia.com/content/dam/kia/us/en/vehicles/k5/2026/trims/lxs-fwd/exterior/ffffff/360/36.png'},
    {'marca': 'Honda', 'modelo': 'Civic', 'tipo': 'UberX', 'url': 'https://automobiles.honda.com/-/media/Honda-Automobiles/Vehicles/Family-Pages/Civic-Family/Civic-Hatchback/2026/MY26_Civic_Family_Card_Jelly_2x.png'}
]

suvs = [
    {'marca': 'Honda', 'modelo': 'CR-V', 'tipo': 'Uber Comfort', 'url': 'https://platform.cstatic-images.com/xlarge/in/v2/stock_photos/001ed902-2f64-4015-bfae-882789d2e4c4/d0e55ab8-fda8-4644-a068-5384ade0983e.png'},
    {'marca': 'Toyota', 'modelo': 'Fortuner', 'tipo': 'Uber Comfort', 'url': 'https://static.vecteezy.com/system/resources/previews/017/281/514/non_2x/toyota-fortuner-top-model-2755cc-automatic-transmission-turbo-engine-6-speed-gear-free-png.png'}
]

catalogo_vehiculos = motos + carros + suvs
colores = ['Rojo', 'Azul', 'Blanco', 'Negro', 'Gris', 'Plateado']
anos_vehiculo = list(range(2016, 2025))

# --- 3. CONDUCTORES ---
conductores_db = []

# HOMBRES
for i in range(23):
    veh = random.choice(catalogo_vehiculos)
    conductores_db.append({
        'id': f"DRV-M{100+i}",
        'nombre': fake.name_male(),
        'genero': 'Masculino',
        'foto': f"{BASE_IMG}/mpersona_{i+1}.png{RAW}",
        'vehiculo_data': veh,
        'vehiculo_color': random.choice(colores),
        'vehiculo_ano': random.choice(anos_vehiculo),
        'placa': fake.bothify(text='A##-####').upper(),
        'rating_base': round(random.uniform(4.5, 5.0), 1)
    })

# MUJERES
for i in range(17):
    veh = random.choice(catalogo_vehiculos)
    conductores_db.append({
        'id': f"DRV-F{200+i}",
        'nombre': fake.name_female(),
        'genero': 'Femenino',
        'foto': f"{BASE_IMG}/fpersona_{i+1}.png{RAW}",
        'vehiculo_data': veh,
        'vehiculo_color': random.choice(colores),
        'vehiculo_ano': random.choice(anos_vehiculo),
        'placa': fake.bothify(text='A##-####').upper(),
        'rating_base': round(random.uniform(4.7, 5.0), 1)
    })

# --- 4. UBICACIONES ---
geo_barrios = {
    'Piantini': (18.4716, -69.9377), 'Naco': (18.4760, -69.9280),
    'Gazcue': (18.4695, -69.9015), 'Zona Colonial': (18.4727, -69.8858),
    'Bella Vista': (18.4491, -69.9535), 'Los Cacicazgos': (18.4450, -69.9650),
    'Arroyo Hondo': (18.5029, -69.9542), 'AILA (Aeropuerto)': (18.4302, -69.6765),
    'Ágora Mall': (18.4827, -69.9390), 'Blue Mall': (18.4718, -69.9405),
    'UASD': (18.4610, -69.9190), 'Villa Mella': (18.5520, -69.9100),
    'Herrera': (18.4700, -69.9700), 'Los Alcarrizos': (18.5150, -70.0150),
    'San Isidro': (18.4950, -69.7900), 'Malecón': (18.4550, -69.9100),
    'Ensanche Quisqueya': (18.4680, -69.9480), 'Ciudad Juan Bosch': (18.4900, -69.7500),
    'Invivienda': (18.5100, -69.8200), 'Las Caobas': (18.4600, -69.9800),
    'Los Prados': (18.4800, -69.9500), 'Villa Juana': (18.4850, -69.9050),
    'Cristo Rey': (18.5000, -69.9300), 'Megacentro': (18.5050, -69.8600)
}

# --- 5. DATASET ---
data = []
start_date = datetime.strptime(FECHA_INICIO, "%Y-%m-%d").date()
end_date = datetime.strptime(FECHA_FIN, "%Y-%m-%d").date()

for i in range(1, CANTIDAD + 1):
    chofer = random.choice(conductores_db)
    veh = chofer['vehiculo_data']
    tarifa_base = {'Uber Moto': {'base':75,'km':18,'min':5,'costo_op':0.12},
                   'UberX': {'base':120,'km':32,'min':7,'costo_op':0.18},
                   'Uber Comfort': {'base':180,'km':45,'min':9,'costo_op':0.22}}
    COMISION_UBER = 0.25
    tarifa = tarifa_base[veh['tipo']]

    origen = random.choice(list(geo_barrios.keys()))
    lat, lon = geo_barrios[origen]
    destino = random.choice(list(geo_barrios.keys()))
    distancia = round(random.uniform(2,25),1)
    tiempo_estimado = int(distancia * random.uniform(3.5,5))

    estado = random.choices(['Completado','Cancelado'], weights=[92,8])[0]

    if estado == 'Completado':
        precio = int(tarifa['base'] + distancia*tarifa['km'] + tiempo_estimado*tarifa['min'])
        comision = int(precio*COMISION_UBER)
        costo = int(precio*tarifa['costo_op'])
        ganancia = precio - comision - costo
        tiempo_real = int(tiempo_estimado * random.uniform(0.9,1.05))
        retraso = max(0, tiempo_real-tiempo_estimado)
        cumple_okr = "SI" if retraso==0 else "NO"
    else:
        precio = costo = comision = ganancia = tiempo_real = retraso = 0
        cumple_okr = "N/A"

    data.append({
        'Trip_ID': f"UB-{30000+i}",
        'Fecha': fake.date_between(start_date,end_date),
        'Hora': fake.time(),
        'Conductor_ID': chofer['id'],
        'Conductor': chofer['nombre'],
        'Genero': chofer['genero'],
        'Conductor_Foto_URL': chofer['foto'],
        'Rating': round(chofer['rating_base']+random.uniform(-0.2,0.1),1),
        'Servicio': veh['tipo'],
        'Vehiculo': f"{veh['marca']} {veh['modelo']}",
        'Vehiculo_Marca': veh['marca'],
        'Vehiculo_Modelo': veh['modelo'],
        'Vehiculo_Color': chofer['vehiculo_color'],
        'Vehiculo_Ano': chofer['vehiculo_ano'],
        'Vehiculo_Placa': chofer['placa'],
        'Vehiculo_Foto_URL': veh['url'],
        'Origen': origen,
        'Latitud_Origen': lat + random.uniform(-0.005,0.005),
        'Longitud_Origen': lon + random.uniform(-0.005,0.005),
        'Destino': destino,
        'Tiempo_Real_Min': tiempo_real,
        'Meta_Tiempo_Min': tiempo_estimado,
        'Retraso_Min': retraso,
        'Cumplio_OKR': cumple_okr,
        'Estado': estado,
        'Metodo_Pago': random.choice(['Efectivo','Tarjeta','Uber Cash']),
        'Precio_DOP': precio,
        'Costo_DOP': costo,
        'Comision_Uber_DOP': comision,
        'Ganancia_DOP': ganancia
    })

df = pd.DataFrame(data)
df.to_excel("Uber_RD_Dataset_Final.xlsx", index=False)
print("✅ Dataset FINAL generado correctamente con todos los campos originales y datos realistas.")
