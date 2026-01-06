import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# --- CONFIGURACIÓN GENERAL ---
CANTIDAD = 50000
FECHA_INICIO = '2024-01-01'
FECHA_FIN = '2026-01-03'

fake = Faker('es_MX') 

# --- 1. CONFIGURACIÓN DE FOTOS ---
BASE_IMG = "https://github.com/JUANCITOPENA/GENERADOR_IMAGENES_PERSONAS/blob/main/FOTOS_PERSONAS_UBER_MAS"
RAW_SUFFIX = "?raw=true"

# --- 2. LISTAS DE NOMBRES ---
NOMBRES_HOMBRES = [
    "Juan", "Luis", "Pedro", "Carlos", "José", "Manuel", "Antonio", "Miguel", "Francisco", "David",
    "Jorge", "Alberto", "Rafael", "Fernando", "Roberto", "Andrés", "Daniel", "Gabriel", "Ricardo",
    "Héctor", "Emilio", "Ramón", "Mario", "Diego", "Javier", "Ángel", "Víctor", "Jesús", "Samuel",
    "Eduardo", "Oscar", "Rubén", "Santiago", "Martín", "Julio", "Pablo", "Alejandro", "Félix"
]

NOMBRES_MUJERES = [
    "María", "Ana", "Carmen", "Rosa", "Laura", "Isabel", "Patricia", "Lucía", "Marta", "Elena",
    "Cristina", "Juana", "Francisca", "Antonia", "Dolores", "Paula", "Raquel", "Teresa", "Beatriz",
    "Andrea", "Sofía", "Daniela", "Julia", "Verónica", "Carolina", "Natalia", "Silvia", "Adriana",
    "Gabriela", "Mariana", "Alejandra", "Paola", "Lorena", "Claudia", "Valeria", "Yessica"
]

# --- 3. VEHÍCULOS ---
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
colores = ['Rojo', 'Azul', 'Blanco', 'Negro', 'Gris', 'Plateado', 'Dorado', 'Vino']
anos_vehiculo = list(range(2016, 2025))

# --- 4. CREACIÓN DE BASE DE DATOS DE CONDUCTORES ---
conductores_db = []
print("🔨 Construyendo base de datos de conductores blindada...")

# GRUPO A: HOMBRES
for i in range(1, 24): 
    veh = random.choice(catalogo_vehiculos)
    nombre_hombre = f"{random.choice(NOMBRES_HOMBRES)} {fake.last_name()}"
    foto_hombre = f"{BASE_IMG}/mpersona_{i}.png{RAW_SUFFIX}"
    conductores_db.append({
        'id': f"DRV-M{100+i}", 'nombre': nombre_hombre, 'genero': 'Masculino', 'foto': foto_hombre,
        'vehiculo_data': veh, 'vehiculo_color': random.choice(colores), 'vehiculo_ano': random.choice(anos_vehiculo),
        'placa': fake.bothify(text='A##-####').upper(), 'rating_base': round(random.uniform(4.5, 5.0), 1)
    })

# GRUPO B: MUJERES
for i in range(1, 18):
    veh = random.choice(catalogo_vehiculos)
    nombre_mujer = f"{random.choice(NOMBRES_MUJERES)} {fake.last_name()}"
    foto_mujer = f"{BASE_IMG}/fpersona_{i}.png{RAW_SUFFIX}"
    conductores_db.append({
        'id': f"DRV-F{200+i}", 'nombre': nombre_mujer, 'genero': 'Femenino', 'foto': foto_mujer,
        'vehiculo_data': veh, 'vehiculo_color': random.choice(colores), 'vehiculo_ano': random.choice(anos_vehiculo),
        'placa': fake.bothify(text='A##-####').upper(), 'rating_base': round(random.uniform(4.7, 5.0), 1)
    })

# --- 5. UBICACIONES ---
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
    'Cristo Rey': (18.5000, -69.9300), 'Megacentro': (18.5050, -69.8600),
    'Higüey': (18.6150, -68.7070), 'Parque Central Higüey': (18.6165, -68.7075), 'Basílica de Higüey': (18.6160, -68.7072), 
    'El Morro de Montecristi': (19.8660, -71.6490), 'Centro de Montecristi': (19.8500, -71.6500),
    'San Francisco de Macorís': (19.3000, -70.2500), 'Parque Duarte SFM': (19.3010, -70.2520), 
    'Nagua': (19.3830, -69.8500), 'Malecón de Nagua': (19.3840, -69.8520), 'Baní': (18.2800, -70.3300), 
    'Playa Los Almendros': (18.2500, -70.3300), 'Hato Mayor del Rey': (18.7600, -69.2600), 
    'Parque Central Hato Mayor': (18.7610, -69.2620), 'Santa Cruz de El Seibo': (18.7600, -69.0400), 
    'Mao': (19.5500, -71.0800), 'Parque Central Mao': (19.5520, -71.0820), 'Jimaní': (18.4900, -71.8500), 
    'Lago Enriquillo': (18.5000, -71.7000), 'Pedernales': (18.0400, -71.7400), 'Parque Central Pedernales': (18.0420, -71.7420) ,
    'Santiago de los Caballeros': (19.4708, -70.6920),
    'Barahona': (18.2085, -71.1008),
    'Puerto Plata': (19.7934, -70.6884),
    'La Romana': (18.4273, -68.9728),
    'San Pedro de Macoris': (18.4539, -69.3086),
    'La Vega': (19.2236, -70.5296),
    'San Cristobal': (18.4167, -70.1000),
    'San Juan de la Maguana': (18.8059, -71.2299),
    'Bonao': (18.9369, -70.4092),
    'Moca': (19.3935, -70.5260),
    'Azua': (18.4532, -70.7349),
    'Cotui': (19.0527, -70.1494),
    'Esperanza': (19.5847, -70.9849),
    'Villa Altagracia': (18.6730, -70.1710),
    'Villa Vasquez': (19.7479, -71.4404),
    'San Jose De Ocoa': (18.5466, -70.5063),
    'Tamayo': (18.3935, -71.0019),
    'Las Matas De Farfan': (19.0724, -71.5087),
    'Constanza': (18.9092, -70.7450),
    'San Jose De Las Matas': (19.3392, -70.9382),
    'Neiba': (18.4814, -71.4197),
    'Duverge': (18.3784, -71.5247),
    'Santo Domingo Oeste': (18.5000, -70.0000),
    'Santo Domingo Este': (18.4850, -69.8480),
    'Punta Cana': (18.5820, -68.4040),
    'Jarabacoa': (19.1167, -70.6333),
    'Sosua': (19.7522, -70.5199),
    'Cabarete': (19.7509, -70.4144),
    'Las Terrenas': (19.3110, -69.5428),
    'Samana': (19.2056, -69.3369),
    'Bayahibe': (18.3687, -68.8397),
    'Bahia de las Aguilas': (17.8621, -71.6456),
    'Pico Duarte': (19.0205, -70.9922),
    'Los Haitises National Park': (19.0439, -69.5929),
    'Isla Saona': (18.1533, -68.6930),
    'Altos de Chavon': (18.4188, -68.8872),
    'Cueva de las Maravillas': (18.4533, -69.1444),
    '27 Charcos de Damajagua': (19.7319, -70.8259),
    'Salto El Limon': (19.2608, -69.4513),
    'Cayo Levantado': (19.1663, -69.2758),
    'La Esperilla': (18.4720, -69.9200),
    'La Julia': (18.4667, -69.9333),
    'Mirador Sur': (18.4500, -69.9600),
    'Evaristo Morales': (18.4630, -69.9420),
    'Serralles': (18.4700, -69.9300),
    'Paraiso': (18.4700, -69.9500),
    'El Vergel': (18.4737, -69.9156),
    'Renacimiento': (18.4464, -69.9689),
    'Los Rios': (18.5050, -69.9800),
    'Capotillo': (18.5000, -69.9000)
}

# --- NUEVO: MAPEO DE CIUDADES/PROVINCIAS (Para Power BI) ---
mapping_ciudades = {
    # Gran Santo Domingo
    'Piantini': 'Santo Domingo', 'Naco': 'Santo Domingo', 'Gazcue': 'Santo Domingo', 'Zona Colonial': 'Santo Domingo',
    'Bella Vista': 'Santo Domingo', 'Los Cacicazgos': 'Santo Domingo', 'Arroyo Hondo': 'Santo Domingo', 
    'Ágora Mall': 'Santo Domingo', 'Blue Mall': 'Santo Domingo', 'UASD': 'Santo Domingo', 
    'Herrera': 'Santo Domingo', 'Los Alcarrizos': 'Santo Domingo', 'Malecón': 'Santo Domingo', 
    'Ensanche Quisqueya': 'Santo Domingo', 'Los Prados': 'Santo Domingo', 'Villa Juana': 'Santo Domingo', 
    'Cristo Rey': 'Santo Domingo', 'La Esperilla': 'Santo Domingo', 'La Julia': 'Santo Domingo', 
    'Mirador Sur': 'Santo Domingo', 'Evaristo Morales': 'Santo Domingo', 'Serralles': 'Santo Domingo', 
    'Paraiso': 'Santo Domingo', 'El Vergel': 'Santo Domingo', 'Renacimiento': 'Santo Domingo', 
    'Los Rios': 'Santo Domingo', 'Capotillo': 'Santo Domingo', 'Santo Domingo Oeste': 'Santo Domingo',
    'Villa Mella': 'Santo Domingo Norte', 'AILA (Aeropuerto)': 'Santo Domingo Este', 
    'San Isidro': 'Santo Domingo Este', 'Ciudad Juan Bosch': 'Santo Domingo Este', 
    'Invivienda': 'Santo Domingo Este', 'Megacentro': 'Santo Domingo Este', 'Las Caobas': 'Santo Domingo Oeste', 
    'Santo Domingo Este': 'Santo Domingo Este',

    # Santiago
    'Santiago de los Caballeros': 'Santiago', 'San Jose De Las Matas': 'Santiago', 

    # La Altagracia
    'Higüey': 'La Altagracia', 'Parque Central Higüey': 'La Altagracia', 'Basílica de Higüey': 'La Altagracia', 
    'Punta Cana': 'La Altagracia', 'Bayahibe': 'La Altagracia', 'Isla Saona': 'La Altagracia',

    # Monte Cristi
    'El Morro de Montecristi': 'Monte Cristi', 'Centro de Montecristi': 'Monte Cristi', 'Villa Vasquez': 'Monte Cristi',

    # Duarte
    'San Francisco de Macorís': 'Duarte', 'Parque Duarte SFM': 'Duarte',

    # María Trinidad Sánchez
    'Nagua': 'María Trinidad Sánchez', 'Malecón de Nagua': 'María Trinidad Sánchez',

    # Peravia
    'Baní': 'Peravia', 'Playa Los Almendros': 'Peravia',

    # Hato Mayor
    'Hato Mayor del Rey': 'Hato Mayor', 'Parque Central Hato Mayor': 'Hato Mayor',

    # El Seibo
    'Santa Cruz de El Seibo': 'El Seibo',

    # Valverde
    'Mao': 'Valverde', 'Parque Central Mao': 'Valverde', 'Esperanza': 'Valverde',

    # Independencia
    'Jimaní': 'Independencia', 'Lago Enriquillo': 'Independencia', 'Duverge': 'Independencia',

    # Pedernales
    'Pedernales': 'Pedernales', 'Parque Central Pedernales': 'Pedernales', 'Bahia de las Aguilas': 'Pedernales',

    # Barahona
    'Barahona': 'Barahona',

    # Puerto Plata
    'Puerto Plata': 'Puerto Plata', 'Sosua': 'Puerto Plata', 'Cabarete': 'Puerto Plata', 
    '27 Charcos de Damajagua': 'Puerto Plata',

    # La Romana
    'La Romana': 'La Romana', 'Altos de Chavon': 'La Romana',

    # San Pedro de Macorís
    'San Pedro de Macoris': 'San Pedro de Macorís', 'Cueva de las Maravillas': 'San Pedro de Macorís',

    # La Vega
    'La Vega': 'La Vega', 'Jarabacoa': 'La Vega', 'Constanza': 'La Vega', 'Pico Duarte': 'La Vega',

    # San Cristóbal
    'San Cristobal': 'San Cristóbal', 'Villa Altagracia': 'San Cristóbal',

    # San Juan
    'San Juan de la Maguana': 'San Juan', 'Las Matas De Farfan': 'San Juan',

    # Monseñor Nouel
    'Bonao': 'Monseñor Nouel',

    # Espaillat
    'Moca': 'Espaillat',

    # Azua
    'Azua': 'Azua',

    # Sánchez Ramírez
    'Cotui': 'Sánchez Ramírez',

    # San José de Ocoa
    'San Jose De Ocoa': 'San José de Ocoa',

    # Bahoruco
    'Tamayo': 'Bahoruco', 'Neiba': 'Bahoruco',

    # Samaná
    'Las Terrenas': 'Samaná', 'Samana': 'Samaná', 'Los Haitises National Park': 'Samaná', 
    'Salto El Limon': 'Samaná', 'Cayo Levantado': 'Samaná'
}

# --- 6. GENERACIÓN DE VIAJES ---
data = []
start_date = datetime.strptime(FECHA_INICIO, "%Y-%m-%d").date()
end_date = datetime.strptime(FECHA_FIN, "%Y-%m-%d").date()

print(f"🔄 Generando {CANTIDAD} viajes...")

for i in range(1, CANTIDAD + 1):
    chofer = random.choice(conductores_db)
    veh = chofer['vehiculo_data']
    
    tarifa_base = {'Uber Moto': {'base':75,'km':18,'min':5,'costo_op':0.12},
                   'UberX': {'base':120,'km':32,'min':7,'costo_op':0.18},
                   'Uber Comfort': {'base':180,'km':45,'min':9,'costo_op':0.22}}
    COMISION_UBER = 0.25
    tarifa = tarifa_base[veh['tipo']]

    # Ubicación
    origen_name = random.choice(list(geo_barrios.keys()))
    destino_name = random.choice(list(geo_barrios.keys()))
    while destino_name == origen_name:
        destino_name = random.choice(list(geo_barrios.keys()))
    
    # --- NUEVO: ASIGNACIÓN DE CIUDAD/PROVINCIA ---
    ciudad_origen = mapping_ciudades.get(origen_name, "Otra")
    ciudad_destino = mapping_ciudades.get(destino_name, "Otra")
    # ---------------------------------------------

    # Origen coords
    lat_o, lon_o = geo_barrios[origen_name]
    lat_origen_final = lat_o + random.uniform(-0.005, 0.005)
    lon_origen_final = lon_o + random.uniform(-0.005, 0.005)

    # Destino coords
    lat_d, lon_d = geo_barrios[destino_name]
    lat_destino_final = lat_d + random.uniform(-0.005, 0.005)
    lon_destino_final = lon_d + random.uniform(-0.005, 0.005)

    # Tiempos y Distancia
    distancia_km = round(random.uniform(2, 25), 1)
    tiempo_estimado = int(distancia_km * 4.5)
    
    if random.random() < 0.92:
        tiempo_real = int(tiempo_estimado * random.uniform(0.9, 1.0))
        retraso = 0
        cumple_okr = "SI"
        estado = "Completado"
    else:
        tiempo_real = int(tiempo_estimado * random.uniform(1.2, 1.5))
        retraso = tiempo_real - tiempo_estimado
        cumple_okr = "NO"
        estado = "Completado"

    if random.random() > 0.92:
        estado = 'Cancelado'
        tiempo_real = 0
        retraso = 0
        cumple_okr = "N/A"

    precio = int(tarifa['base'] + (distancia_km * tarifa['km']) + (tiempo_estimado * tarifa['min']))
    comision = int(precio * COMISION_UBER)
    costo = int(precio * tarifa['costo_op'])
    ganancia = precio - comision - costo

    cliente = f"{random.choice(NOMBRES_HOMBRES + NOMBRES_MUJERES)} {fake.last_name()}"

    data.append({
        'Trip_ID': f"UB-{30000+i}",
        'Fecha': fake.date_between(start_date, end_date),
        'Hora': fake.time(pattern="%H:%M"),
        
        'Conductor_ID': chofer['id'],
        'Conductor': chofer['nombre'],
        'Genero': chofer['genero'],
        'Conductor_Foto_URL': chofer['foto'],
        'Rating': round(chofer['rating_base'] + random.uniform(-0.2, 0.1), 1),
        
        'Servicio': veh['tipo'],
        'Vehiculo': f"{veh['marca']} {veh['modelo']}",
        'Vehiculo_Marca': veh['marca'],
        'Vehiculo_Modelo': veh['modelo'],
        'Vehiculo_Color': chofer['vehiculo_color'],
        'Vehiculo_Ano': chofer['vehiculo_ano'],
        'Placa': chofer['placa'],
        'Color': chofer['vehiculo_color'],
        'Anio': chofer['vehiculo_ano'],
        'Vehiculo_Foto_URL': veh['url'],
        
        # --- CAMPOS NUEVOS AGREGADOS ---
        'Ciudad_Origen': ciudad_origen,     # <--- NUEVO
        'Origen': origen_name,
        'Latitud_Origen': lat_origen_final,
        'Longitud_Origen': lon_origen_final,
        
        'Ciudad_Destino': ciudad_destino,   # <--- NUEVO
        'Destino': destino_name,
        'Latitud_Destino': lat_destino_final, 
        'Longitud_Destino': lon_destino_final,
        
        'Distancia_KM': distancia_km,       # <--- NUEVO (Para medidas en Power BI)
        # --------------------------------
        
        'Tiempo_Real_Min': tiempo_real,
        'Meta_Tiempo_Min': tiempo_estimado,
        'Retraso_Min': retraso,
        'Cumplio_OKR': cumple_okr,
        'Estado': estado,
        'Cliente': cliente,
        
        'Metodo_Pago': random.choice(['Efectivo', 'Tarjeta', 'Uber Cash']),
        'Precio_DOP': precio,
        'Costo_DOP': costo,
        'Comision_Uber_DOP': comision,
        'Ganancia_DOP': ganancia
    })

df = pd.DataFrame(data)
df.to_excel("Uber_RD_Dataset_Final.xlsx", index=False)
print("✅ Dataset generado exitosamente.")
print(f"   - Se agregaron las columnas: 'Ciudad_Origen', 'Ciudad_Destino' y 'Distancia_KM'.")
print(f"   - Archivo guardado: Uber_RD_Dataset_Final.xlsx")