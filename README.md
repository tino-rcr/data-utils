# data-utils
Código para reutilizar.

# 📊 Data Utils - Módulo de Análisis de Datos en Python

Este repositorio contiene un conjunto de funciones útiles para la manipulación, análisis y visualización de datos en **Pandas, NumPy y Matplotlib**. Estas funciones permiten realizar operaciones como manejo de valores faltantes, cálculos estadísticos, generación de gráficos y agregaciones de datos.

## 📂 **Estructura del Repositorio**

```
📁 data-utils/
│── utils.py            # Módulo con funciones de análisis de datos
│── README.md           # Documentación del repositorio
│── requirements.txt    # Dependencias necesarias
```

---

## 🔧 **Funciones Disponibles**

### 🟢 **1. Manejo de valores faltantes**
- `missing_values_percentage(df, column=None)`: Calcula el porcentaje de valores faltantes en el DataFrame o en una columna específica.
- `drop_high_missing(df, threshold=0.5)`: Elimina columnas con más de un umbral de valores faltantes.
- `impute_missing(df, method='mean')`: Rellena valores faltantes con la media, mediana o moda.

### 📊 **2. Estadísticas generales del DataFrame**
- `calculate_statistics(df)`: Devuelve estadísticas descriptivas de todas las columnas numéricas.
- `column_distribution(df, column)`: Calcula la distribución de valores únicos en una columna.
- `detect_outliers(df, column, method='zscore', threshold=3)`: Detecta valores atípicos con Z-Score o IQR.

### 🔄 **3. Agregaciones y cálculos de métricas**
- `group_by_segment(df, group_cols, metrics)`: Agrupa el DataFrame por segmentos y calcula métricas clave.
- `monthly_variation(df, column)`: Calcula la variación porcentual mensual de una columna.
- `add_calculated_columns(df, calculations)`: Agrega columnas derivadas mediante operaciones matemáticas entre otras columnas.

### 📈 **4. Visualización de datos**
- `plot_missing_values(df)`: Genera un gráfico de barras con el porcentaje de valores faltantes.
- `plot_distribution(df, column)`: Crea un histograma para visualizar la distribución de una columna.
- `plot_correlation(df)`: Genera una matriz de correlación entre las variables numéricas.
- `plot_time_series(df, date_col, metric_col)`: Grafica una serie de tiempo para una métrica específica.

### 📌 **5. Análisis de Representación y Comparación**
- `calculate_representation(df, segment_col, metric_col)`: Calcula el porcentaje que representa cada segmento dentro del total.
- `compare_periods(df, date_col, metric_col, period='month')`: Compara métricas entre períodos (mensual, trimestral, anual).

---

## ⚡ **Cómo Usar**

1️⃣ **Instalar las dependencias**
```bash
pip install pandas numpy matplotlib seaborn
```

2️⃣ **Importar el módulo en un script de Python**
```python
import pandas as pd
import utils

df = pd.read_csv("dataset.csv")
print(utils.missing_values_percentage(df))
```

3️⃣ **Ejecutar una visualización**
```python
utils.plot_correlation(df)
```

---

## 🚀 **Contribuciones**
Si deseas contribuir con nuevas funciones o mejoras, puedes abrir un **Pull Request** en este repositorio.

📩 Para consultas, puedes contactarme en **GitHub**.

---

✍️ **Autor:** _[Tu Nombre]_  
📅 **Última actualización:** _[Fecha]_

