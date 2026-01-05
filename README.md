# 🇩🇴 Uber RD | Analytics Command Center Premium

> **Versión:** 2.1.0 (Stable)
> **Estado:** Producción
> **Tecnología:** Serverless SPA (Single Page Application)

---

## 📑 1. Planteamiento del Problema

En la gestión operativa de flotas de transporte y conductores independientes de Uber en República Dominicana, los administradores se enfrentan a los siguientes desafíos críticos:

1.  **Fragmentación de Datos:** La información financiera, operativa y geográfica se encuentra dispersa en hojas de cálculo masivas (Excel) difíciles de interpretar.
2.  **Falta de Visibilidad en Tiempo Real:** No existe una herramienta nativa que permita visualizar la ubicación geográfica de los viajes históricos o el rendimiento individual de los conductores de manera agregada.
3.  **Análisis Financiero Tedioso:** Calcular la rentabilidad neta (Ingresos - Costos), el cumplimiento de OKRs y la segmentación por métodos de pago requiere fórmulas manuales propensas a errores humanos.
4.  **Pérdida de Contexto:** Al recargar las herramientas de visualización web tradicionales, se pierde la carga de datos, obligando al usuario a re-subir archivos constantemente.

---

## 💡 2. Solución Tecnológica Propuesta

Se ha desarrollado el **Analytics Command Center Premium**, una solución de inteligencia de negocios (BI) basada en navegador que transforma datos crudos en insights accionables mediante:

*   **Procesamiento Client-Side:** Todo el análisis de datos se realiza en el navegador del usuario utilizando JavaScript, garantizando la privacidad de los datos (ningún dato se envía a servidores externos).
*   **Persistencia Robusta (IndexedDB):** Implementación de una capa de base de datos local en el navegador que permite almacenar grandes volúmenes de datos históricos, manteniendo la sesión activa incluso después de reiniciar el equipo o recargar la página.
*   **Visualización Interactiva:** Integración de mapas geoespaciales, gráficos dinámicos y tablas interactivas con paginación.
*   **Diseño Adaptativo:** Interfaz moderna con soporte nativo para **Modo Oscuro (Dark Mode)** y **Modo Claro**, optimizado para largas jornadas de trabajo.

---

## 🛠 3. Stack Tecnológico y Herramientas

La aplicación está construida como un monolito front-end (un solo archivo HTML) para facilitar la portabilidad y el despliegue sin dependencias de backend.

| Categoría | Tecnología / Librería | Uso Principal |
| :--- | :--- | :--- |
| **Core** | HTML5, CSS3, JavaScript (ES6+) | Estructura, Estilos y Lógica de Negocio. |
| **UI Framework** | **Bootstrap 5.3.2** | Sistema de rejilla, componentes responsivos y modales. |
| **Visualización** | **ApexCharts.js** | Gráficos estadísticos (Barras, Líneas, Donas) con soporte de temas dinámicos. |
| **Geoespacial** | **Leaflet.js + OSM** | Renderizado de mapas interactivos y marcadores de ubicación. |
| **Data Parsing** | **SheetJS (XLSX)** | Lectura y conversión de archivos Excel (.xlsx) a objetos JSON. |
| **Persistencia** | **IndexedDB** | Base de datos NoSQL en el navegador para almacenamiento persistente de datasets masivos (>5MB). |
| **Iconografía** | **FontAwesome 6.4** | Iconos vectoriales para la interfaz de usuario. |

---

## 🚀 4. Instalación y Despliegue

Al ser una aplicación **Serverless Client-Side**, no requiere instalación de Node.js, Python ni servidores web complejos.

### Opción A: Ejecución Directa (Recomendada)
1.  Descarga el archivo `otro.html` (o renómbralo a `index.html`).
2.  Haz doble clic para abrirlo en tu navegador favorito (Chrome, Edge, Firefox, Brave).
3.  ¡Listo! La aplicación está corriendo.

### Opción B: Clonación y Entorno Local (Para Desarrolladores)
Si deseas modificar el código o contribuir:

```bash
# 1. Clona tu repositorio (simulado) o descarga la carpeta
git clone https://github.com/tu-usuario/uber-analytics-rd.git

# 2. Navega al directorio
cd uber-analytics-rd

# 3. (Opcional) Si usas VS Code, puedes usar Live Server
code .
# Click derecho en 'index.html' -> "Open with Live Server"
```

---

## 📖 5. Manual de Usuario Completo

### 5.1. Carga de Datos
1.  En el menú lateral izquierdo, ubica el botón azul **"Cargar Excel"**.
2.  Selecciona tu archivo `Uber_RD_Dataset_Final.xlsx`.
3.  El sistema procesará los datos automáticamente.
    *   *Nota:* Gracias a **IndexedDB**, la próxima vez que entres, los datos seguirán ahí sin necesidad de volver a cargar el archivo.

### 5.2. Navegación por el Dashboard
*   **KPIs Financieros:** Tarjetas superiores que muestran Ingresos Totales, Ticket Promedio, Ganancia Neta y Costos.
*   **KPIs Operativos:** Métricas de Viajes, Efectividad (OKR), Rating y Tasa de Cancelación.
*   **Filtros Globales:** Utiliza la barra superior para filtrar por:
    *   Búsqueda de texto (Nombre, Placa, Vehículo).
    *   Tipo de Servicio (UberX, Moto, Comfort).
    *   Rango de Fechas.
    *   Año y Mes Fiscal.

### 5.3. Módulos de Visualización
*   **Tendencias:** Gráfico combinado de ingresos vs. cantidad de viajes.
*   **Distribución:** Gráfico de barras apiladas mostrando el estatus (Completado/Cancelado) por tipo de servicio.
*   **Mapa Vivo:** Mapa de calor con marcadores de todos los orígenes de viajes.
*   **Métodos de Pago:** Gráfico de dona (Efectivo, Tarjeta, etc.).

### 5.4. Gestión de Conductores
1.  Despliega el menú **"Operaciones"** en la barra lateral o ve a la sección inferior.
2.  En la tabla **"Directorio de Socios Conductores"**, haz clic en cualquier fila.
3.  Se abrirá el **Perfil del Conductor (Modal)** con:
    *   Foto y Datos del Vehículo (Placa, Color, Año).
    *   Estadísticas acumuladas (Ganancias, Viajes, Rating).
    *   Gráfico de rendimiento personal.
    *   Historial de últimos viajes.

### 5.5. Detalles de Viajes (Raw Data)
1.  En la tabla **"Últimos Registros"**, haz clic en cualquier fila.
2.  Se abrirá la **Ficha Técnica del Viaje** con detalles del cliente, ruta, desglose de tarifa y mapa financiero.

---

## 💾 6. Estructura de Datos Requerida (Excel)

Para que el sistema funcione correctamente, el archivo Excel debe contener las siguientes columnas en la primera hoja:

| Columna Excel | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `Trip_ID` | String/Number | Identificador único del viaje. |
| `Fecha` | Date | Fecha y hora del servicio. |
| `Conductor` | String | Nombre del chofer. |
| `Conductor_Foto_URL` | URL | Enlace a la foto del perfil. |
| `Vehiculo` | String | Modelo del vehículo (ej. Kia K5). |
| `Vehiculo_Foto_URL` | URL | Enlace a la foto del auto. |
| `Placa` | String | Número de placa. |
| `Color` | String | Color del vehículo. |
| `Anio` | Number | Año del vehículo. |
| `Cliente` | String | Nombre del pasajero. |
| `Servicio` | String | Tipo (UberX, Moto, etc.). |
| `Origen` | String | Dirección de recogida. |
| `Destino` | String | Dirección de destino. |
| `Latitud_Origen` | Decimal | Coordenada GPS. |
| `Longitud_Origen` | Decimal | Coordenada GPS. |
| `Precio_DOP` | Money | Monto total cobrado. |
| `Costo_DOP` | Money | Costo operativo/comisión. |
| `Ganancia_DOP` | Money | `Precio - Costo`. |
| `Metodo_Pago` | String | Efectivo, Tarjeta, Wallet. |
| `Estado` | String | Completado, Cancelado. |
| `Cumplio_OKR` | String | SI / NO. |
| `Rating` | Number | Calificación (1-5). |

---

## ⚙️ 7. Opciones Avanzadas y Personalización

### Persistencia de Datos (IndexedDB)
El sistema utiliza una base de datos local llamada `UberAnalyticsDB`.
*   **Ventaja:** Permite guardar archivos Excel muy grandes (+50MB) que `localStorage` no soportaría.
*   **Limpiar Caché:** Si deseas borrar los datos guardados, puedes limpiar la caché del navegador o subir un archivo Excel nuevo (esto sobrescribe los datos anteriores).

### Modo Oscuro (Dark Mode)
El sistema detecta automáticamente tu preferencia, pero puedes alternarlo manualmente con el botón de la luna/sol en la esquina superior derecha.
*   *Nota:* Los gráficos se re-renderizan automáticamente para cambiar el color de los textos y ejes a blanco/negro según corresponda para mantener la legibilidad.

---

## 📄 8. Licencia

Este proyecto es de uso privado y educativo para análisis de datos de transporte.
**Copyright © 2026 - Uber RD Analytics Team.**
