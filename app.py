import dash
from dash import html, dcc
import plotly.io as pio
import json
import os
from dash.dependencies import Input, Output


def cargar_figura(path):
    with open(path, 'r') as f:
        return json.load(f)

# Estilos
estilo_general = {
    'backgroundColor': '#f9f9f9',
    'color': '#1a237e',
    'fontFamily': 'Arial, sans-serif',
    'padding': '30px'
}

estilo_titulo = {
    'fontSize': '30px',
    'fontWeight': 'bold',
    'marginBottom': '20px',
    'color': '#1a237e'
}

estilo_subtitulo = {
    'fontSize': '22px',
    'fontWeight': 'bold',
    'marginTop': '20px',
    'color': '#1a237e'
}

estilo_parrafo = {
    'fontSize': '16px',
    'color': '#333'
}

# App Dash
app = dash.Dash(__name__, title="Home Credit Dashboard")
server = app.server

app.layout = html.Div(style=estilo_general, children=[
    html.H1("Home Credit Risk Analysis", style=estilo_titulo),

    dcc.Tabs(id="tabs", value="contexto", children=[
        dcc.Tab(label='Contexto',value="contexto", children=[
            html.Div(style={
                'backgroundColor': '#ffffff',
                'padding': '10px 40px 40px 40px',
                'display': 'flex',
                'justifyContent': 'center',
            }, children=[
                html.Div(style={
                    'display': 'flex',
                    'maxWidth': '1200px',
                    'width': '100%',
                    'justifyContent': 'space-between',
                    'alignItems': 'center'  # 👈 esto centra verticalmente imagen y texto
                }, children=[
                    html.Div(style={'width': '65%'}, children=[
                        html.H2("Contexto del Proyecto", style=estilo_subtitulo),
                        html.P(
                            "En el sector financiero, especialmente en países en desarrollo, "
                            "las instituciones enfrentan grandes retos para otorgar crédito a personas sin historial crediticio. "
                            "Home Credit, una institución que busca incluir financieramente a estas poblaciones, ha recopilado una extensa base de datos "
                            "para evaluar el riesgo de incumplimiento de sus clientes.",
                            style=estilo_parrafo
                        ),
                        html.P(
                            "El objetivo del análisis es construir un modelo de Machine Learning que permita predecir la probabilidad de que un solicitante "
                            "incumpla con el pago del préstamo, basándose en datos socioeconómicos, laborales, historial financiero, entre otros.",
                            style=estilo_parrafo
                        ),
                        html.P(
                            "Esta tarea permite, además, entender qué características tienen mayor peso en la decisión crediticia y cómo se relacionan con la probabilidad de incumplimiento.",
                            style=estilo_parrafo
                        ),
                        html.H3("Fuente de los Datos", style=estilo_subtitulo),
                        html.P("Kaggle - Home Credit Default Risk Competition", style=estilo_parrafo)
                    ]),

                    html.Div(style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',  # 👈 ahora sí centrado con respecto al texto
                        'width': '30%'
                    }, children=[
                        html.Img(
                            src="https://cdn-icons-png.flaticon.com/512/633/633611.png",
                            style={
                                'width': '180px',
                                'filter': 'drop-shadow(2px 2px 4px gray)'
                            }
                        )
                    ])
                ])
            ])
        ]),




       dcc.Tab(label='Planteamiento del Problema',value="problema", children=[
            html.Div(style={
                'backgroundColor': '#ffffff',
                'padding': '40px 80px',
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'flex-start',
                'justifyContent': 'flex-start'
            }, children=[
                html.H2("Planteamiento del Problema", style=estilo_subtitulo),

                html.P(
                    "Aunque Home Credit dispone de una base de datos con miles de solicitudes, los datos presentan múltiples retos analíticos: "
                    "una fuerte desproporción entre clientes cumplidores e incumplidores (desbalance de clases), alta dimensionalidad y presencia de valores nulos. "
                    "Esto dificulta la construcción de un modelo predictivo confiable y eficiente.",
                    style=estilo_parrafo
                ),
                html.H3("Pregunta problema:", style=estilo_subtitulo),
                html.P(
                    "¿Cuál es el modelo de clasificación más óptimo que permita predecir con precisión el riesgo de incumplimiento de crédito, considerando la naturaleza y complejidad de los datos disponibles?",
                    style={**estilo_parrafo, 'fontStyle': 'italic'}
                )
            ])
        ]),

        dcc.Tab(label='Objetivos y Justificación',value="objetivos",children=[
            html.Div([
                html.H2("Objetivo General", style=estilo_subtitulo),
                html.P("Analizar los datos de solicitantes de crédito para identificar factores asociados al riesgo de incumplimiento.", style=estilo_parrafo),
                html.H3("Objetivos Específicos", style=estilo_subtitulo),
                html.Ul([
                    html.Li("Explorar la estructura y calidad de los datos.", style=estilo_parrafo),
                    html.Li("Identificar variables con mayor correlación con la variable objetivo.", style=estilo_parrafo),
                    html.Li("Visualizar distribuciones y relaciones entre variables clave.", style=estilo_parrafo)
                ]),
                html.H3("Justificación", style=estilo_subtitulo),
                html.P("Mejorar la evaluación crediticia puede reducir el riesgo financiero y facilitar el acceso al crédito a poblaciones subatendidas.", style=estilo_parrafo)
            ])
        ]),

        dcc.Tab(label='Metodología',value="metodologia", children=[
            html.Div(style={
                'backgroundColor': '#ffffff',
                'padding': '40px 80px',
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'flex-start'
            }, children=[
                html.H2("Metodología", style=estilo_subtitulo),

                html.H4("Tipo de problema", style=estilo_subtitulo),
                html.P(
                    "Se aborda un problema de clasificación supervisada, cuyo objetivo es predecir si un solicitante de crédito incumplirá o no con el pago del préstamo. "
                    "La variable objetivo es binaria: `TARGET`, donde 1 indica incumplimiento y 0 buen comportamiento crediticio.",
                    style=estilo_parrafo
                ),

                html.H4("Análisis Exploratorio de Datos (EDA)", style=estilo_subtitulo),
                html.P(
                    "Se realizará un análisis descriptivo exhaustivo para entender la estructura y calidad de los datos, así como la relación entre las variables predictoras y el objetivo. "
                    "Este análisis incluirá:",
                    style=estilo_parrafo
                ),
                html.Ul([
                    html.Li("Distribución de la variable objetivo para evaluar el desbalance de clases."),
                    html.Li("Exploración de los porcentajes de valores nulos y filtrado de variables con alta ausencia de datos."),
                    html.Li("Cálculo de correlaciones entre variables numéricas para identificar redundancia o multicolinealidad."),
                    html.Li("Evaluación de la normalidad y simetría de las principales variables numéricas mediante histogramas y pruebas estadísticas."),
                    html.Li("Análisis de variables numéricas relevantes (como EXT_SOURCE, DAYS_BIRTH, AMT_BALANCE) por clase de `TARGET`."),
                    html.Li("Relación entre variables categóricas y la variable objetivo utilizando Chi-cuadrado y Cramér’s V."),
                    html.Li("Visualización de la distribución de categorías clave como ORGANIZATION_TYPE y NAME_INCOME_TYPE."),
                ], style=estilo_parrafo),

                html.H4("Preparación de los Datos", style=estilo_subtitulo),
                html.Ul([
                    html.Li("Imputación de valores faltantes con técnicas específicas según el tipo de variable."),
                    html.Li("Codificación de variables categóricas mediante One-Hot Encoding o Label Encoding."),
                    html.Li("Escalamiento de variables numéricas si es requerido por los modelos."),
                    html.Li("División del conjunto de datos en entrenamiento, validación y prueba para evitar data leakage.")
                ], style=estilo_parrafo)
            ])
        ]),
        
        dcc.Tab(label='Análisis Descriptivo',value="eda" ,children=[
            html.Div(style={
                'backgroundColor': '#ffffff',
                'padding': '40px 20px',
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center'
            }, children=[
                html.H2("Análisis Exploratorio de Datos (EDA)", style=estilo_subtitulo),
                html.Div(id="contenido-figuras")  # Aquí se mostrarán los gráficos dinámicamente
            ])
        ]),

    ])
])

@app.callback(
    Output("contenido-figuras", "children"),
    Input("tabs", "value")
)
def mostrar_figuras(tab):

    print("Tab activo:", tab)
    
    if tab != "eda":
        return html.Div()
    
    graficos = [
        ("Distribución de la variable objetivo", "fig_target.json"),
        ("Variables con mayor porcentaje de valores nulos", "fig_missing.json"),
        ("Matriz de correlación numérica", "fig_corr.json"),
        ("Correlación entre variables categóricas (Cramér's V)", "fig_cramers.json"),
        ("Distribución ORGANIZATION_TYPE", "organization_type.json"),
        ("Distribución NAME_INCOME_TYPE", "name_income_type.json"),
        ("Distribución OCCUPATION_TYPE", "occupation_type.json"),
        ("Distribución NAME_CONTRACT_STATUS", "name_contract_status.json"),
        ("Distribución CODE_REJECT_REASON", "code_reject_reason.json")
    ]
    
    content = []
    for titulo, archivo in graficos:
        try:
            with open(archivo, "r") as f:
                fig = pio.from_json(f.read())
                
            content.append(html.H4(titulo, style=estilo_subtitulo))
            content.append(dcc.Graph(figure=fig))
        
        except Exception as e:
            content.append(html.P(f"No se pudo cargar {archivo}: {e}"))
    
    return html.Div(style={'width': '90%', 'maxWidth': '1000px'}, children=content)

# Ejecutar servidor
if __name__ == '__main__':
    app.run_server(debug=True)
