import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def missing_values_percentage(df, column=None):
    """
    Calcula el porcentaje de valores faltantes en el DataFrame o en una columna específica.
    """
    if column:
        return df[column].isnull().mean() * 100
    return df.isnull().mean() * 100

def drop_high_missing(df, threshold=0.5):
    """
    Elimina columnas con más del threshold de valores faltantes.
    """
    return df.loc[:, df.isnull().mean() < threshold]

def impute_missing(df, method='mean'):
    """
    Rellena valores faltantes con la media, mediana o moda.
    """
    df_copy = df.copy()
    for col in df.select_dtypes(include=[np.number]).columns:
        if method == 'mean':
            df_copy[col].fillna(df[col].mean(), inplace=True)
        elif method == 'median':
            df_copy[col].fillna(df[col].median(), inplace=True)
        elif method == 'mode':
            df_copy[col].fillna(df[col].mode()[0], inplace=True)
    return df_copy

def calculate_statistics(df):
    """
    Retorna estadísticos básicos de todas las columnas numéricas.
    """
    return df.describe()

def column_distribution(df, column):
    """
    Calcula la distribución de valores únicos de una columna.
    """
    return df[column].value_counts(normalize=True) * 100

def detect_outliers(df, column, method='zscore', threshold=3):
    """
    Detecta valores atípicos utilizando Z-Score o IQR.
    """
    if method == 'zscore':
        mean, std = df[column].mean(), df[column].std()
        return df[(df[column] - mean).abs() > threshold * std]
    elif method == 'iqr':
        Q1, Q3 = df[column].quantile(0.25), df[column].quantile(0.75)
        IQR = Q3 - Q1
        return df[(df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))]

def group_by_segment(df, group_cols, metrics):
    """
    Agrupa por una o más columnas y calcula métricas clave.
    """
    return df.groupby(group_cols)[metrics].sum().reset_index()

def monthly_variation(df, column):
    """
    Calcula la variación porcentual mensual de una columna.
    """
    df['prev_month'] = df[column].shift(1)
    df['variation'] = (df[column] - df['prev_month']) / df['prev_month'] * 100
    return df.drop(columns=['prev_month'])

def add_calculated_columns(df, calculations):
    """
    Agrega nuevas columnas derivadas de otras según operaciones definidas.
    """
    df_copy = df.copy()
    for new_col, (col1, operation, col2) in calculations.items():
        if operation == '+':
            df_copy[new_col] = df_copy[col1] + df_copy[col2]
        elif operation == '-':
            df_copy[new_col] = df_copy[col1] - df_copy[col2]
        elif operation == '*':
            df_copy[new_col] = df_copy[col1] * df_copy[col2]
        elif operation == '/':
            df_copy[new_col] = df_copy[col1] / df_copy[col2]
    return df_copy

def plot_missing_values(df):
    """
    Muestra un gráfico de valores faltantes por columna.
    """
    missing = df.isnull().mean() * 100
    missing = missing[missing > 0]
    missing.sort_values(inplace=True)
    missing.plot(kind='barh', figsize=(10, 5), color='red')
    plt.xlabel('% de valores faltantes')
    plt.title('Valores faltantes por columna')
    plt.show()

def plot_distribution(df, column):
    """
    Muestra la distribución de una columna numérica con un histograma.
    """
    plt.figure(figsize=(8,5))
    sns.histplot(df[column].dropna(), kde=True, bins=30)
    plt.title(f'Distribución de {column}')
    plt.show()

def plot_correlation(df):
    """
    Muestra una matriz de correlación entre variables numéricas.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Matriz de correlación')
    plt.show()

def plot_time_series(df, date_col, metric_col):
    """
    Genera una serie de tiempo para una métrica específica.
    """
    df_sorted = df.sort_values(by=date_col)
    plt.figure(figsize=(12,5))
    plt.plot(df_sorted[date_col], df_sorted[metric_col], marker='o', linestyle='-')
    plt.xlabel('Fecha')
    plt.ylabel(metric_col)
    plt.title(f'Evolución de {metric_col} en el tiempo')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def calculate_representation(df, segment_col, metric_col):
    """
    Calcula el porcentaje que representa cada segmento dentro del total.
    """
    return df.groupby(segment_col)[metric_col].sum() / df[metric_col].sum() * 100

def compare_periods(df, date_col, metric_col, period='month'):
    """
    Compara métricas entre períodos definidos (mensual, trimestral, anual).
    """
    df[date_col] = pd.to_datetime(df[date_col])
    if period == 'month':
        df['period'] = df[date_col].dt.to_period('M')
    elif period == 'quarter':
        df['period'] = df[date_col].dt.to_period('Q')
    elif period == 'year':
        df['period'] = df[date_col].dt.year
    return df.groupby('period')[metric_col].sum().reset_index()

if __name__ == "__main__":
    print("Módulo de funciones de análisis de datos cargado correctamente.")
