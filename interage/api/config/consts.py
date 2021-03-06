import os

# API General
VERSION = os.getenv('INTERAGE_API_VERSION', 'v1')
API_URL = os.getenv('INTERAGE_API_URL', 'https://api.interage.intmed.com.br')
AUTH_KEYS = ['username', 'password']

# URIs
METADATA              = 'metadados/'
INTERACTIONS_URI      = 'interacoes/'
MEDICINES_URI         = 'medicamentos/'
ACTIVE_PRINCIPLES_URI = 'principios-ativos/'
OBTAIN_TOKEN_URI      = 'obter-chave/'

# Interaction metadata
INTERACTION_EVIDENCES  = ['Caso', 'Estudo', 'Teórica', 'Extensa']
INTERACTION_ACTIONS    = ['Nenhuma', 'Informar', 'Monitorar', 'Ajustar', 'Evitar']
INTERACTION_SEVERITIES = ['Grave', 'Moderada', 'Leve', 'Nada esperado', 'Gravidade desconhecida']
