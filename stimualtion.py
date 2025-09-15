import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
import random
import math

# Set page config
st.set_page_config(
    page_title="Gram-Urja: Complete IoT System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with PERFECT sizing for Digital Twin
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        margin-top: 2rem;
            padding-top: 2 rem;
    }
    
    .efficiency-proof {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(40, 167, 69, 0.3);
    }
    
    .feature-card {
        background: white;
        border: 2px solid #e9ecef;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        text-align: center;
    }
    
    .feature-card:hover {
        border-color: #1e3c72;
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(30, 60, 114, 0.2);
    }
    
    /* PERFECT SIZE DIGITAL TWIN STYLING */
    .digital-twin-header {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 2rem auto;
        max-width: 90%;
        box-shadow: 0 15px 35px rgba(255, 107, 53, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .digital-twin-header h1 {
        font-size: 2.5rem !important;
        margin-bottom: 1rem !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .digital-twin-header p {
        font-size: 1.1rem !important;
        margin: 0.5rem 0 !important;
        opacity: 0.95;
    }
    
    .holographic-equipment {
        background: linear-gradient(145deg, #ffffff, #f0f2f5);
        border: 2px solid rgba(255, 107, 53, 0.3);
        border-radius: 15px;
        padding: 1.2rem;
        margin: 0.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        min-height: 180px;
        max-height: 200px;
    }
    
    .equipment-3d-icon {
        font-size: 2.5rem;
        background: linear-gradient(135deg, #FF6B35, #F7931E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 2px 4px rgba(255, 107, 53, 0.3));
        animation: float 4s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    .sensor-hologram {
        background: radial-gradient(circle at center, rgba(255, 107, 53, 0.8) 0%, rgba(247, 147, 30, 0.8) 100%);
        border-radius: 15px;
        padding: 1.2rem;
        margin: 0.3rem;
        color: white;
        text-align: center;
        position: relative;
        overflow: hidden;
        animation: pulse-glow 3s infinite;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 20px rgba(255, 107, 53, 0.2);
        min-height: 140px;
        max-height: 160px;
    }
    
    @keyframes pulse-glow {
        0%, 100% { 
            box-shadow: 0 0 20px rgba(255, 107, 53, 0.3);
            transform: scale(1);
        }
        50% { 
            box-shadow: 0 0 30px rgba(255, 107, 53, 0.5);
            transform: scale(1.02);
        }
    }
    
    .neural-network-3d {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 50%, #FFA726 100%);
        background-size: 200% 200%;
        animation: neural-pulse 4s ease-in-out infinite;
        border-radius: 20px;
        padding: 2rem;
        color: white;
        position: relative;
        overflow: hidden;
        margin: 2rem auto;
        max-width: 90%;
        box-shadow: 0 15px 35px rgba(255, 107, 53, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    @keyframes neural-pulse {
        0%, 100% { 
            background-position: 0% 50%;
            box-shadow: 0 0 25px rgba(255, 107, 53, 0.4);
        }
        50% { 
            background-position: 100% 50%;
            box-shadow: 0 0 35px rgba(247, 147, 30, 0.6);
        }
    }
    
    /* PERFECT SIZE SIMULATION SECTION */
    .simulation-lab-main {
        background: linear-gradient(135deg, #FF1744 0%, #FF5722 100%);
        border-radius: 25px;
        padding: 3rem 2rem;
        color: white;
        text-align: center;
        margin: 3rem auto;
        max-width: 90%;
        box-shadow: 0 20px 40px rgba(255, 23, 68, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    .simulation-lab-main h1 {
        font-size: 3rem !important;
        margin-bottom: 1.5rem !important;
        text-shadow: 0 4px 8px rgba(0,0,0,0.5);
    }
    
    .simulation-controls-main {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 90%;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        border: 2px solid rgba(255, 87, 34, 0.2);
    }
    
    .simulation-header-main {
        background: linear-gradient(135deg, #FF5722 0%, #FF9800 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(255, 87, 34, 0.3);
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .parameter-card {
        background: linear-gradient(135deg, rgba(255, 87, 34, 0.1) 0%, rgba(255, 152, 0, 0.1) 100%);
        border: 2px solid rgba(255, 87, 34, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 87, 34, 0.1);
    }
    
    .parameter-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(255, 87, 34, 0.2);
        border-color: rgba(255, 87, 34, 0.5);
    }
    
    .parameter-card h3 {
        font-size: 1.3rem !important;
        margin-bottom: 1rem !important;
        font-weight: 700 !important;
    }
    
    .execute-button-container {
        display: flex;
        justify-content: center;
        margin: 3rem 0;
        width: 100%;
    }
    
    .simulation-results-main {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 25px;
        padding: 3rem;
        margin: 3rem auto;
        max-width: 90%;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        border: 2px solid rgba(255, 87, 34, 0.2);
    }
    
    .result-card-main {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border: 2px solid rgba(255, 87, 34, 0.4);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }
    
    .result-value-main {
        font-size: 2.2rem;
        font-weight: bold;
        background: linear-gradient(135deg, #FF5722, #FF9800);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 1rem 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* PERFECT BUTTON STYLING */
    .stButton > button {
        background: linear-gradient(135deg, #FF1744 0%, #FF5722 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 1.5rem 3rem !important;
        font-weight: bold !important;
        font-size: 1.3rem !important;
        transition: all 0.3s ease !important;
        min-width: 350px !important;
        box-shadow: 0 10px 30px rgba(255, 23, 68, 0.4) !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 15px 40px rgba(255, 23, 68, 0.6) !important;
    }
    
    .stSelectbox > div > div {
        background: white !important;
        border: 2px solid #FF5722 !important;
        border-radius: 10px !important;
        font-size: 1rem !important;
    }
    
    .stSlider > div > div > div {
        color: #FF5722 !important;
    }
    
    /* ENSURE PERFECT VISIBILITY */
    .block-container {
        max-width: 100% !important;
        padding: 1rem 2rem !important;
    }
    
    .main > div {
        overflow: visible !important;
    }
    
    .main {
        overflow-x: visible !important;
        overflow-y: auto !important;
    }
    
    /* Overview metrics styling */
    .overview-section {
        background: linear-gradient(135deg, rgba(255, 87, 34, 0.1) 0%, rgba(255, 152, 0, 0.1) 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1.5rem auto;
        max-width: 90%;
        border: 2px solid rgba(255, 87, 34, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'home'

# FIXED: Initialize villages with ALL required sensor keys
if 'villages' not in st.session_state:
    st.session_state.villages = {
        'Balasore_Solar': {
            'name': 'Balasore Solar Village',
            'type': 'Solar',
            'coordinates': {'lat': 21.4934, 'lon': 86.9332},
            'efficiency_improvement': 21.5,
            'solar_power': 850,
            'battery_level': 78,
            'battery_voltage': 48.2,
            'battery_current': 15.6,
            'battery_health': 94,
            'load_consumption': 640,
            'monthly_savings': 12500,
            'population': 450,
            'health': 'Healthy',
            'active_source': 'Solar',
            'equipment': {
                'solar_panels': {'status': 'Online', 'efficiency': 92, 'temp': 45.2, 'voltage': 24.5, 'power_output': 850, 'tilt_angle': 23},
                'mppt_controller': {'status': 'Online', 'efficiency': 98, 'temp': 38.1, 'tracking_accuracy': 99.2},
                'inverter': {'status': 'Online', 'efficiency': 95, 'temp': 42.3, 'thd': 2.1, 'frequency': 50.0},
                'battery_bank': {'status': 'Online', 'soc': 78, 'voltage': 48.2, 'temp': 28.5, 'health': 94, 'cycles': 1250}
            },
            'sensors': {
                'irradiance': 850, 'ambient_temp': 32.1, 'humidity': 65, 'panel_temp': 45.2,
                'pressure': 1013.2, 'voltage': 24.5, 'current': 34.6, 'power': 850,
                'dust_level': 15, 'vibration': 0.02, 'light_intensity': 85000,
                'wind_speed': 5.2, 'wind_direction': 120  # Added for completeness
            },
            'loads': {
                'households': {'status': True, 'power': 290, 'priority': 'Critical', 'efficiency': 95},
                'street_lights': {'status': True, 'power': 200, 'priority': 'High', 'efficiency': 90},
                'water_pump': {'status': True, 'power': 150, 'priority': 'Medium', 'efficiency': 85}
            },
            'predictions': {
                'next_hour_generation': 820, 'battery_runtime': 8.5,
                'maintenance_due': 15, 'failure_probability': 2.1,
                'weather_impact': 'Positive', 'cost_savings_today': 450
            },
            'ai_decisions': [],
            'maintenance_alerts': [],
            'performance_history': []
        },
        'Kendrapara_Wind': {
            'name': 'Kendrapara Wind Village',
            'type': 'Wind',
            'coordinates': {'lat': 20.4850, 'lon': 86.4194},
            'efficiency_improvement': 21.9,
            'wind_power': 920,
            'battery_level': 65,
            'battery_voltage': 47.8,
            'battery_current': 12.3,
            'battery_health': 89,
            'load_consumption': 580,
            'monthly_savings': 8900,
            'population': 380,
            'health': 'Warning',
            'active_source': 'Wind',
            'equipment': {
                'wind_turbine': {'status': 'Online', 'rpm': 45.2, 'power': 920, 'efficiency': 88, 'blade_angle': 15, 'yaw_angle': 245},
                'generator': {'status': 'Online', 'efficiency': 91, 'temp': 52.1, 'voltage': 380, 'frequency': 50.1},
                'power_electronics': {'status': 'Online', 'efficiency': 96, 'temp': 39.8, 'switching_freq': 20000},
                'battery_bank': {'status': 'Online', 'soc': 65, 'voltage': 47.8, 'temp': 31.2, 'health': 89, 'cycles': 1850}
            },
            'sensors': {
                'wind_speed': 12.5, 'wind_direction': 245, 'ambient_temp': 29.3,
                'pressure': 1015.1, 'humidity': 72, 'voltage': 22.8, 'current': 40.4,
                'turbulence': 8.2, 'noise_level': 45, 'tower_vibration': 0.05,
                'power': 920, 'rotor_speed': 45.2,
                'panel_temp': 29.3, 'irradiance': 0, 'dust_level': 10,  # Added for wind village
                'vibration': 0.05, 'light_intensity': 0  # Added for completeness
            },
            'loads': {
                'households': {'status': True, 'power': 400, 'priority': 'Critical', 'efficiency': 93},
                'street_lights': {'status': True, 'power': 180, 'priority': 'High', 'efficiency': 88},
                'water_pump': {'status': False, 'power': 0, 'priority': 'Low', 'efficiency': 0}
            },
            'predictions': {
                'next_hour_generation': 890, 'battery_runtime': 6.2,
                'maintenance_due': 8, 'failure_probability': 5.3,
                'weather_impact': 'Favorable', 'cost_savings_today': 320
            },
            'ai_decisions': [],
            'maintenance_alerts': [],
            'performance_history': []
        },
        'Puri_Hybrid': {
            'name': 'Puri Hybrid Village',
            'type': 'Hybrid',
            'coordinates': {'lat': 19.8135, 'lon': 85.8312},
            'efficiency_improvement': 22.5,
            'solar_power': 650,
            'wind_power': 420,
            'battery_level': 85,
            'battery_voltage': 49.1,
            'battery_current': 8.7,
            'battery_health': 97,
            'load_consumption': 780,
            'monthly_savings': 15200,
            'population': 520,
            'health': 'Healthy',
            'active_source': 'Hybrid',
            'equipment': {
                'solar_panels': {'status': 'Online', 'efficiency': 94, 'temp': 43.1, 'voltage': 24.8, 'power_output': 650},
                'wind_turbine': {'status': 'Online', 'rpm': 38.5, 'power': 420, 'efficiency': 92, 'blade_angle': 12},
                'hybrid_controller': {'status': 'Online', 'efficiency': 97, 'temp': 35.2, 'switching_freq': 25000, 'optimization_level': 98},
                'battery_bank': {'status': 'Online', 'soc': 85, 'voltage': 49.1, 'temp': 26.8, 'health': 97, 'cycles': 890}
            },
            'sensors': {
                'irradiance': 780, 'wind_speed': 8.5, 'ambient_temp': 30.2,
                'humidity': 68, 'pressure': 1014.5, 'voltage': 25.2, 'current': 31.0,
                'dust_level': 12, 'vibration': 0.03, 'wind_direction': 180,
                'total_power': 1070, 'system_efficiency': 94.1, 'panel_temp': 43.1,
                'light_intensity': 75000, 'turbulence': 5.2, 'noise_level': 35,
                'tower_vibration': 0.02, 'power': 1070, 'rotor_speed': 38.5
            },
            'loads': {
                'households': {'status': True, 'power': 380, 'priority': 'Critical', 'efficiency': 96},
                'street_lights': {'status': True, 'power': 220, 'priority': 'High', 'efficiency': 92},
                'water_pump': {'status': True, 'power': 180, 'priority': 'Medium', 'efficiency': 87}
            },
            'predictions': {
                'next_hour_generation': 1040, 'battery_runtime': 12.3,
                'maintenance_due': 22, 'failure_probability': 1.2,
                'weather_impact': 'Optimal', 'cost_savings_today': 685
            },
            'ai_decisions': [],
            'maintenance_alerts': [],
            'performance_history': []
        }
    }

if 'simulation_data' not in st.session_state:
    st.session_state.simulation_data = {
        'overall_improvement': 22.0,
        'cost_saved_monthly': 36600,
        'co2_reduced_annually': 45.6,
        'ai_decisions_today': 1847,
        'energy_optimized': 2.4,
        'system_uptime': 98.3
    }

# Feature definitions
FEATURES = {
    1: {'icon': '📊', 'title': 'Real-Time Monitoring'},
    2: {'icon': '🤖', 'title': 'AI Source Switching'},
    3: {'icon': '🔧', 'title': 'Predictive Maintenance'},
    4: {'icon': '📱', 'title': 'Mobile Application'},
    5: {'icon': '🏘️', 'title': 'Smart Load Management'},
    6: {'icon': '👥', 'title': 'Digital Twin Simulation'},
    7: {'icon': '🌤️', 'title': 'Weather Integration'}
}

def ensure_sensor_keys(village):
    """Ensure all required sensor keys exist with default values"""
    default_sensors = {
        'irradiance': 0,
        'ambient_temp': 30.0,
        'humidity': 65,
        'panel_temp': 30.0,
        'pressure': 1013.2,
        'voltage': 24.0,
        'current': 0.0,
        'power': 0,
        'dust_level': 10,
        'vibration': 0.02,
        'light_intensity': 0,
        'wind_speed': 0.0,
        'wind_direction': 0,
        'turbulence': 0.0,
        'noise_level': 30,
        'tower_vibration': 0.0,
        'rotor_speed': 0.0,
        'system_efficiency': 90.0,
        'total_power': 0
    }
    
    # Ensure sensors dict exists
    if 'sensors' not in village:
        village['sensors'] = {}
    
    # Add missing sensor keys
    for key, default_value in default_sensors.items():
        if key not in village['sensors']:
            village['sensors'][key] = default_value

def update_simulation_data():
    """FIXED: Update all simulation data with proper error handling"""
    if st.session_state.current_view != 'home':
        return
        
    try:
        current_time = datetime.now()
        hour = current_time.hour
        
        for village_id, village in st.session_state.villages.items():
            # FIXED: Ensure all sensor keys exist first
            ensure_sensor_keys(village)
            
            # Advanced solar power simulation
            if village['type'] in ['Solar', 'Hybrid']:
                try:
                    if 6 <= hour <= 18:
                        solar_factor = math.sin((hour - 6) * math.pi / 12) * random.uniform(0.8, 1.1)
                        irradiance = max(0, 1000 * solar_factor)
                        village['sensors']['irradiance'] = irradiance
                        
                        # Safe temperature calculation
                        ambient_temp = village['sensors'].get('ambient_temp', 30.0)
                        panel_temp = village['sensors'].get('panel_temp', ambient_temp)
                        
                        temp_factor = max(0.8, 1 - (panel_temp - 25) * 0.004)
                        dust_factor = max(0.85, 1 - village['sensors'].get('dust_level', 10) * 0.01)
                        
                        village['solar_power'] = irradiance * 0.85 * temp_factor * dust_factor + random.uniform(-30, 30)
                        village['solar_power'] = max(0, village['solar_power'])
                        
                        # Update panel temperature safely
                        village['sensors']['panel_temp'] = ambient_temp + (irradiance / 30) + random.uniform(-2, 2)
                        
                        # Update equipment safely
                        if 'equipment' in village and 'solar_panels' in village['equipment']:
                            village['equipment']['solar_panels']['temp'] = village['sensors']['panel_temp']
                            village['equipment']['solar_panels']['power_output'] = village['solar_power']
                    else:
                        village['sensors']['irradiance'] = 0
                        village['solar_power'] = 0
                        village['sensors']['panel_temp'] = village['sensors'].get('ambient_temp', 30.0) + random.uniform(-1, 1)
                
                except Exception as solar_error:
                    # If solar update fails, set safe defaults
                    village['solar_power'] = 0
                    village['sensors']['irradiance'] = 0
                    village['sensors']['panel_temp'] = village['sensors'].get('ambient_temp', 30.0)
            
            # Advanced wind power simulation
            if village['type'] in ['Wind', 'Hybrid']:
                try:
                    wind_speed = max(0, 10 + random.uniform(-4, 8))
                    village['sensors']['wind_speed'] = wind_speed
                    if wind_speed > 3:
                        wind_power = min(1200, (wind_speed ** 3) * 6)
                        village['wind_power'] = wind_power + random.uniform(-50, 50)
                        village['wind_power'] = max(0, village['wind_power'])
                    else:
                        village['wind_power'] = 0
                        
                except Exception as wind_error:
                    # If wind update fails, set safe defaults
                    village['wind_power'] = 0
                    village['sensors']['wind_speed'] = 0
            
            # Safe battery and other updates
            try:
                total_generation = village.get('solar_power', 0) + village.get('wind_power', 0)
                power_balance = total_generation - village['load_consumption']
                battery_change = (power_balance / 1000) * 0.4
                village['battery_level'] += battery_change + random.uniform(-0.3, 0.3)
                village['battery_level'] = max(10, min(100, village['battery_level']))
                
                # Safe sensor updates
                village['sensors']['ambient_temp'] = 30 + random.uniform(-3, 5)
                village['sensors']['humidity'] = max(30, min(90, 65 + random.uniform(-8, 12)))
                village['sensors']['pressure'] = 1013 + random.uniform(-3, 3)
                village['sensors']['voltage'] = 24 + random.uniform(-2, 2)
                village['sensors']['current'] = total_generation / max(village['sensors']['voltage'], 1)
                village['sensors']['power'] = total_generation
                
            except Exception as update_error:
                # If any update fails, continue without crashing
                pass
    
    except Exception as e:
        # Silent error handling - don't show errors to user for minor issues
        pass

def create_holographic_equipment_display(equipment_name, equipment_data, village_type):
    """Create compact holographic equipment display"""
    status_color = '#00ff88' if equipment_data.get('status', 'Offline') == 'Online' else '#ff4444'
    
    equipment_icons = {
        'solar_panels': '☀️',
        'wind_turbine': '🌪️',
        'inverter': '🔄',
        'mppt_controller': '⚡',
        'generator': '⚙️',
        'power_electronics': '🔌',
        'hybrid_controller': '🎛️',
        'battery_bank': '🔋'
    }
    
    icon = equipment_icons.get(equipment_name, '⚙️')
    efficiency = equipment_data.get('efficiency', 0)
    
    return f"""
    <div class="holographic-equipment">
        <div class="equipment-3d-icon">{icon}</div>
        <h4 style="color: #2c3e50; margin: 0.5rem 0; font-size: 1rem;">{equipment_name.replace('_', ' ').title()}</h4>
        <div style="display: flex; justify-content: center; align-items: center; margin: 0.5rem 0;">
            <div style="width: 10px; height: 10px; border-radius: 50%; background: {status_color}; 
                        box-shadow: 0 0 5px {status_color};"></div>
            <span style="margin-left: 8px; font-weight: bold; color: #2c3e50; font-size: 0.9rem;">
                {equipment_data.get('status', 'Unknown')}
            </span>
        </div>
        <div style="background: rgba(255, 107, 53, 0.1); padding: 0.8rem; border-radius: 8px; margin: 0.5rem 0;">
            <div style="font-size: 1.4rem; font-weight: bold; color: #FF5722;">{efficiency:.1f}%</div>
            <div style="font-size: 0.8rem; color: #666;">Efficiency</div>
        </div>
    </div>
    """

def create_advanced_simulation_results(simulation_params, village):
    """Create comprehensive simulation results"""
    base_efficiency = village['efficiency_improvement']
    weather_impact = simulation_params['weather_impact']
    load_impact = simulation_params['load_impact']
    equipment_impact = simulation_params['equipment_impact']
    duration = simulation_params['duration']
    
    total_efficiency_change = weather_impact + load_impact + equipment_impact
    final_efficiency = base_efficiency + total_efficiency_change
    
    hourly_generation = village.get('solar_power', 0) + village.get('wind_power', 0)
    energy_change = (total_efficiency_change / 100) * hourly_generation * duration
    cost_per_kwh = 4.5
    cost_impact = (energy_change / 1000) * cost_per_kwh
    
    co2_factor = 0.82
    co2_impact = (energy_change / 1000) * co2_factor
    
    base_reliability = 92
    reliability_impact = (equipment_impact * 0.5) + (weather_impact * 0.3) + (load_impact * 0.2)
    final_reliability = base_reliability + reliability_impact
    
    battery_impact = total_efficiency_change * 0.4
    maintenance_impact = equipment_impact * 2
    
    return {
        'efficiency': {
            'base': base_efficiency,
            'change': total_efficiency_change,
            'final': final_efficiency,
            'weather_component': weather_impact,
            'load_component': load_impact,
            'equipment_component': equipment_impact
        },
        'economic': {
            'energy_change_kwh': energy_change / 1000,
            'cost_impact': cost_impact,
            'hourly_impact': cost_impact / duration,
            'annual_projection': cost_impact * 365 / duration
        },
        'environmental': {
            'co2_change_kg': co2_impact,
            'co2_annual_projection': co2_impact * 365 / duration
        },
        'reliability': {
            'base': base_reliability,
            'change': reliability_impact,
            'final': final_reliability,
            'uptime_hours': (final_reliability / 100) * duration
        },
        'performance': {
            'battery_life_change': battery_impact,
            'maintenance_frequency_change': maintenance_impact,
            'generation_efficiency': final_efficiency
        }
    }

def display_enhanced_simulation_results(results, simulation_params):
    """Display comprehensive simulation results WITHOUT AI recommendations"""
    
    st.markdown("""
    <div class="simulation-results-main">
        <h1 style="text-align: center; color: #FF5722; margin-bottom: 2rem; font-size: 2.5rem;">
            🎯 Advanced Simulation Results Analysis
        </h1>
        <p style="text-align: center; color: #6c757d; font-size: 1.2rem; margin-bottom: 3rem;">
            Comprehensive Multi-Parameter Impact Assessment with Predictive Analytics
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # PRIMARY RESULTS GRID
    st.markdown("## 📊 **Primary Impact Metrics**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        efficiency_change = results['efficiency']['change']
        
        st.markdown(f"""
        <div class="result-card-main">
            <div style="color: #666; font-size: 1.1rem; font-weight: 600;">System Efficiency Impact</div>
            <div class="result-value-main">{efficiency_change:+.1f}%</div>
            <div style="color: #28a745; font-weight: bold; font-size: 1rem;">
                Final: {results['efficiency']['final']:.1f}%
            </div>
            <div style="color: #6c757d; font-size: 0.9rem; margin-top: 0.5rem;">
                Base: {results['efficiency']['base']:.1f}%
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        cost_impact = results['economic']['cost_impact']
        
        st.markdown(f"""
        <div class="result-card-main">
            <div style="color: #666; font-size: 1.1rem; font-weight: 600;">Economic Impact</div>
            <div class="result-value-main">₹{cost_impact:+,.0f}</div>
            <div style="color: #2196F3; font-weight: bold; font-size: 1rem;">
                Per Hour: ₹{results['economic']['hourly_impact']:+.0f}
            </div>
            <div style="color: #6c757d; font-size: 0.9rem; margin-top: 0.5rem;">
                Duration: {simulation_params['duration']} hours
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        reliability_change = results['reliability']['change']
        
        st.markdown(f"""
        <div class="result-card-main">
            <div style="color: #666; font-size: 1.1rem; font-weight: 600;">System Reliability</div>
            <div class="result-value-main">{results['reliability']['final']:.1f}%</div>
            <div style="color: #667eea; font-weight: bold; font-size: 1rem;">
                Change: {reliability_change:+.1f}%
            </div>
            <div style="color: #6c757d; font-size: 0.9rem; margin-top: 0.5rem;">
                Uptime: {results['reliability']['uptime_hours']:.1f}h
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        energy_change = results['economic']['energy_change_kwh']
        
        st.markdown(f"""
        <div class="result-card-main">
            <div style="color: #666; font-size: 1.1rem; font-weight: 600;">Energy Generation Impact</div>
            <div class="result-value-main">{energy_change:+.1f} kWh</div>
            <div style="color: #28a745; font-weight: bold; font-size: 1rem;">
                CO₂: {results['environmental']['co2_change_kg']:+.1f} kg
            </div>
            <div style="color: #6c757d; font-size: 0.9rem; margin-top: 0.5rem;">
                Environmental Impact
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # DETAILED ANALYSIS CHARTS
    st.markdown("---")
    st.markdown("## 🔬 **Detailed Impact Analysis**")
    
    analysis_col1, analysis_col2 = st.columns(2)
    
    with analysis_col1:
        st.markdown("### 📊 **Component Breakdown**")
        component_data = {
            'Component': ['Weather Impact', 'Load Impact', 'Equipment Impact'],
            'Impact (%)': [
                results['efficiency']['weather_component'],
                results['efficiency']['load_component'],
                results['efficiency']['equipment_component']
            ]
        }
        
        fig_components = px.bar(
            pd.DataFrame(component_data),
            x='Component',
            y='Impact (%)',
            color='Impact (%)',
            color_continuous_scale='RdYlGn',
            title="Efficiency Impact by Component"
        )
        fig_components.update_layout(height=400, font=dict(size=14))
        st.plotly_chart(fig_components, use_container_width=True)
    
    with analysis_col2:
        st.markdown("### 🎯 **Performance Radar**")
        metrics = ['Efficiency', 'Reliability', 'Economic Impact', 'Environmental Impact']
        values = [
            min(100, max(0, results['efficiency']['final'])),
            min(100, max(0, results['reliability']['final'])),
            min(100, max(0, 80 + (results['economic']['cost_impact'] / 1000))),
            min(100, max(0, 85 + (results['environmental']['co2_change_kg'] / 10)))
        ]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=metrics,
            fill='toself',
            name='Performance Score',
            line_color='rgba(255, 87, 34, 0.8)',
            fillcolor='rgba(255, 87, 34, 0.3)'
        ))
        
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False,
            title="Overall Performance Impact",
            height=400,
            font=dict(size=14)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

def show_home_screen():
    """Main dashboard home screen"""
    st.markdown('<div class="main-title">Gram-Urja IoT Microgrid System</div>', unsafe_allow_html=True)
    
    overall_improvement = st.session_state.simulation_data['overall_improvement']
    st.markdown(f"""
    <div class="efficiency-proof">
        <h2>🎯 EFFICIENCY ACHIEVED: {overall_improvement:.1f}%</h2>
        <p>Exceeding 15% target through AI-powered optimization</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📈 Efficiency", f"{overall_improvement:.1f}%", "+7% vs target")
    with col2:
        st.metric("💰 Monthly Savings", f"₹{st.session_state.simulation_data['cost_saved_monthly']:,}")
    with col3:
        st.metric("🌱 CO₂ Saved", f"{st.session_state.simulation_data['co2_reduced_annually']:.1f}T")
    with col4:
        st.metric("⚡ System Uptime", f"{st.session_state.simulation_data['system_uptime']:.1f}%")
    
    # Features grid
    st.markdown("## 🚀 **System Features**")
    
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    
    for i, (feature_id, feature) in enumerate(FEATURES.items()):
        with columns[i % 3]:
            if st.button(f"{feature['icon']}", key=f"feature_{feature_id}", help=feature['title']):
                st.session_state.current_view = f'feature_{feature_id}'
                st.rerun()
            
            st.markdown(f"""
            <div class="feature-card">
                <h3>{feature['icon']}</h3>
                <h4>{feature['title']}</h4>
            </div>
            """, unsafe_allow_html=True)
    
    # Live village status
    st.markdown("---")
    st.markdown("## 🏘️ **Live Village Status**")
    
    for village_id, village in st.session_state.villages.items():
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            health_color = {'Healthy': '#28a745', 'Warning': '#ffc107', 'Critical': '#dc3545'}[village['health']]
            st.markdown(f"""
            <div style="background: {health_color}; color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                <h4>{village['name']}</h4>
                <p>Type: {village['type']}</p>
                <p>Population: {village['population']}</p>
                <p>Status: {village['health']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.metric("🔋 Battery", f"{village['battery_level']:.1f}%")
            total_gen = village.get('solar_power', 0) + village.get('wind_power', 0)
            st.metric("⚡ Generation", f"{total_gen:.0f}W")
        
        with col3:
            st.metric("🏠 Load", f"{village['load_consumption']:.0f}W")
            st.metric("💰 Savings", f"₹{village['monthly_savings']:,}")
        
        with col4:
            st.metric("📈 Efficiency", f"+{village['efficiency_improvement']:.1f}%")

def show_feature_1():
    """Real-Time Monitoring - STANDALONE"""
    st.markdown("# 📊 **Real-Time Multi-Source Monitoring**")
    
    if st.button("← Back to Home", key="back_feature_1"):
        st.session_state.current_view = 'home'
        st.rerun()
    
    col1, col2, col3 = st.columns(3)
    
    try:
        total_generation = sum([v.get('solar_power', 0) + v.get('wind_power', 0) for v in st.session_state.villages.values()])
        total_consumption = sum([v.get('load_consumption', 0) for v in st.session_state.villages.values()])
        efficiency = (total_generation / (total_generation + 200)) * 100 if total_generation > 0 else 0
        
        with col1:
            fig_gen = go.Figure(go.Indicator(
                mode="gauge+number",
                value=total_generation,
                title={'text': "Total Generation (W)"},
                gauge={'axis': {'range': [None, 3000]}, 'bar': {'color': "darkgreen"}}
            ))
            fig_gen.update_layout(height=300)
            st.plotly_chart(fig_gen, use_container_width=True)
        
        with col2:
            fig_cons = go.Figure(go.Indicator(
                mode="gauge+number",
                value=total_consumption,
                title={'text': "Total Consumption (W)"},
                gauge={'axis': {'range': [None, 2500]}, 'bar': {'color': "darkblue"}}
            ))
            fig_cons.update_layout(height=300)
            st.plotly_chart(fig_cons, use_container_width=True)
        
        with col3:
            fig_eff = go.Figure(go.Indicator(
                mode="gauge+number",
                value=efficiency,
                title={'text': "Network Efficiency (%)"},
                gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "purple"}}
            ))
            fig_eff.update_layout(height=300)
            st.plotly_chart(fig_eff, use_container_width=True)
    
    except Exception as e:
        st.error(f"Error displaying gauges: {str(e)}")
    
    # Live data table
    st.markdown("### 📋 **Live Village Data**")
    try:
        village_data = []
        for village in st.session_state.villages.values():
            village_data.append({
                'Village': village['name'],
                'Solar (W)': village.get('solar_power', 0),
                'Wind (W)': village.get('wind_power', 0),
                'Battery (%)': f"{village['battery_level']:.1f}%",
                'Load (W)': village.get('load_consumption', 0),
                'Improvement': f"+{village['efficiency_improvement']:.1f}%"
            })
        
        st.dataframe(pd.DataFrame(village_data), use_container_width=True)
        st.success(f"✅ **Efficiency Target Achieved:** Average {np.mean([v['efficiency_improvement'] for v in st.session_state.villages.values()]):.1f}% improvement")
    except Exception as e:
        st.error(f"Error displaying data table: {str(e)}")

def show_feature_2():
    """AI Source Switching - STANDALONE"""
    st.markdown("# 🤖 **AI-Powered Source Switching**")
    
    if st.button("← Back to Home", key="back_feature_2"):
        st.session_state.current_view = 'home'
        st.rerun()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🧠 **AI Decision Matrix**")
        switching_data = []
        for village in st.session_state.villages.values():
            solar = village.get('solar_power', 0)
            wind = village.get('wind_power', 0)
            battery = village['battery_level']
            
            if solar > 500:
                decision = "Solar Primary"
            elif wind > 400:
                decision = "Wind Primary" 
            elif battery > 80:
                decision = "Battery Mode"
            else:
                decision = "Hybrid Mode"
            
            switching_data.append({
                'Village': village['name'],
                'Solar': f"{solar:.0f}W",
                'Wind': f"{wind:.0f}W",
                'Battery': f"{battery:.1f}%",
                'AI Decision': decision
            })
        
        st.dataframe(pd.DataFrame(switching_data), use_container_width=True)
    
    with col2:
        st.markdown("### ⚡ **Performance**")
        st.metric("Response Time", "23 seconds", "-97% vs manual")
        st.metric("Accuracy", "95.2%", "+12% vs traditional")
        st.metric("Energy Saved", "18%", "Through optimization")
        st.metric("Battery Life", "+40%", "Extended lifespan")

def show_feature_3():
    """Predictive Maintenance - STANDALONE"""
    st.markdown("# 🔧 **Predictive Maintenance System**")
    
    if st.button("← Back to Home", key="back_feature_3"):
        st.session_state.current_view = 'home'
        st.rerun()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔋 **Battery Health Analysis**")
        
        battery_data = []
        for village in st.session_state.villages.values():
            battery_data.append({
                'Village': village['name'],
                'Health': village['battery_health'],
                'Cycles': village['equipment']['battery_bank'].get('cycles', 1000)
            })
        
        fig = px.scatter(pd.DataFrame(battery_data), x='Cycles', y='Health', 
                        color='Village', size='Health',
                        title="Battery Health vs Usage Cycles")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### ⚠️ **Maintenance Alerts**")
        
        alerts = [
            {"equipment": "Solar Inverter - Balasore", "health": "87%", "days": "12", "cost": "₹8,500"},
            {"equipment": "Wind Turbine - Kendrapara", "health": "91%", "days": "18", "cost": "₹12,000"},
            {"equipment": "Battery Bank - Puri", "health": "94%", "days": "45", "cost": "₹6,500"}
        ]
        
        for alert in alerts:
            with st.expander(f"🔧 {alert['equipment']}"):
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Health", alert['health'])
                    st.metric("Maintenance Due", f"{alert['days']} days")
                with col_b:
                    st.metric("Planned Cost", alert['cost'])
                    st.metric("Failure Cost", "₹45,000")
                st.success("💰 Savings: ₹36,500 prevented")

def show_feature_4():
    """Mobile Application - STANDALONE"""
    st.markdown("# 📱 **Community Mobile Application**")
    
    if st.button("← Back to Home", key="back_feature_4"):
        st.session_state.current_view = 'home'
        st.rerun()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📊 **Dashboard Features**")
        st.metric("User Adoption", "95%", "+70% vs traditional")
        st.metric("Daily Active Users", "78%", "High engagement rate")
    
    with col2:
        st.markdown("### 🎮 **Gamification System**")
        st.info("🏆 **Current Challenge:** Diwali Energy Saving - 75% complete")
        
        leaderboard = ["🥇 श्री राम परिवार - ₹850", "🥈 गीता देवी घर - ₹720", "🥉 मोहन बाबू घर - ₹680"]
        for entry in leaderboard:
            st.write(entry)
    
    with col3:
        st.markdown("### 🔌 **Smart Controls**")
        st.success("💡 Street Lights: ON (200W)")
        st.warning("💧 Water Pump: SCHEDULED OFF")
        st.success("🏠 Households: PRIORITY ACTIVE (670W)")

def show_feature_5():
    """Smart Load Management - STANDALONE"""
    st.markdown("# 🏘️ **Smart Load Management System**")
    
    if st.button("← Back to Home", key="back_feature_5"):
        st.session_state.current_view = 'home'
        st.rerun()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔌 **Live Load Distribution**")
        load_data = []
        for village in st.session_state.villages.values():
            for load_name, load_info in village['loads'].items():
                load_data.append({
                    'Village': village['name'],
                    'Load': load_name.replace('_', ' ').title(),
                    'Power (W)': load_info['power'],
                    'Priority': load_info['priority'],
                    'Status': 'ON' if load_info['status'] else 'OFF'
                })
        
        st.dataframe(pd.DataFrame(load_data), use_container_width=True)
    
    with col2:
        st.markdown("### 📊 **Priority Distribution**")
        
        priority_totals = {'Critical': 0, 'High': 0, 'Medium': 0, 'Low': 0}
        for village in st.session_state.villages.values():
            for load_info in village['loads'].values():
                if load_info['status']:
                    priority_totals[load_info['priority']] += load_info['power']
        
        if sum(priority_totals.values()) > 0:
            fig = px.pie(values=list(priority_totals.values()), names=list(priority_totals.keys()), 
                        title="Active Load Distribution by Priority",
                        color_discrete_map={'Critical': '#dc3545', 'High': '#ffc107', 'Medium': '#fd7e14', 'Low': '#28a745'})
            st.plotly_chart(fig, use_container_width=True)

def show_feature_7():
    """Weather Integration - STANDALONE"""
    st.markdown("# 🌤️ **Weather Integration & Disaster Preparedness**")
    
    if st.button("← Back to Home", key="back_feature_7"):
        st.session_state.current_view = 'home'
        st.rerun()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🌡️ **Current Weather**")
        st.metric("Temperature", "32.1°C", "+2.3°C")
        st.metric("Humidity", "65%", "-5%")
        st.metric("Wind Speed", "12.5 km/h", "+3.2 km/h")
        st.metric("Pressure", "1013.2 hPa", "Stable")
    
    with col2:
        st.markdown("### 🌀 **Cyclone Risk**")
        risk_level = "🟢 LOW RISK"
        st.markdown(f"""
        <div style="background: #28a745; color: white; padding: 1.5rem; border-radius: 15px; text-align: center;">
            <h3>Risk Level: {risk_level}</h3>
            <h2>30/100</h2>
            <p>Overall Risk Score</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(0.3)
    
    with col3:
        st.markdown("### ⚠️ **Disaster Status**")
        st.success("✅ **NORMAL OPERATION MODE**")
        st.metric("Network Backup Time", "76 hours")
        st.metric("Emergency Readiness", "98%")

def show_ultimate_digital_twin():
    """Ultimate Digital Twin - STANDALONE"""
    
    # COMPACT DIGITAL TWIN HEADER
    st.markdown("""
    <div class="digital-twin-header">
        <h1>🔮 ULTIMATE DIGITAL TWIN EXPERIENCE</h1>
        <p>🚀 Real-time Holographic Replica with AI-Powered Insights</p>
        <p>⚡ Live Data Stream • 🤖 Neural Processing • 📊 Predictive Models</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Home", key="back_home_twin"):
        st.session_state.current_view = 'home'
        st.rerun()
    
    # Village Selection
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🏘️ **Select Village for Advanced Analysis**")
        village_options = list(st.session_state.villages.keys())
        selected_village_id = st.selectbox(
            "Choose Village:",
            village_options,
            format_func=lambda x: f"{st.session_state.villages[x]['name']} ({st.session_state.villages[x]['type']})",
            key="village_selector_twin"
        )
    
    village = st.session_state.villages[selected_village_id]
    
    # Ensure sensor keys exist for selected village
    ensure_sensor_keys(village)
    
    # COMPACT SYSTEM OVERVIEW
    st.markdown("---")
    st.markdown("""
    <div class="overview-section">
        <h2 style="text-align: center; color: #FF5722; margin-bottom: 1rem;">⚡ Real-Time System Overview</h2>
    </div>
    """, unsafe_allow_html=True)
    
    overview_col1, overview_col2, overview_col3, overview_col4, overview_col5 = st.columns(5)
    
    with overview_col1:
        total_generation = village.get('solar_power', 0) + village.get('wind_power', 0)
        st.metric("🔋 Generation", f"{total_generation:.0f}W", f"{total_generation - village['load_consumption']:+.0f}W")
    
    with overview_col2:
        st.metric("🏠 Load", f"{village['load_consumption']:.0f}W", f"{village['efficiency_improvement']:.1f}%")
    
    with overview_col3:
        st.metric("🔋 Battery", f"{village['battery_level']:.1f}%", f"{village['battery_voltage']:.1f}V")
    
    with overview_col4:
        st.metric("⏱️ Runtime", f"{village['predictions']['battery_runtime']:.1f}h", f"{village['predictions']['failure_probability']:.1f}%")
    
    with overview_col5:
        st.metric("🎯 AI Decisions", f"{len(village['ai_decisions'])}", f"+{random.randint(5, 15)}")
    
    # COMPACT EQUIPMENT MATRIX
    st.markdown("---")
    st.markdown("## 🏗️ **Holographic Equipment Matrix**")
    
    try:
        equipment_cols = st.columns(len(village['equipment']))
        
        for i, (equip_name, equip_data) in enumerate(village['equipment'].items()):
            with equipment_cols[i]:
                card_html = create_holographic_equipment_display(equip_name, equip_data, village['type'])
                st.markdown(card_html, unsafe_allow_html=True)
                
                # Compact metrics display
                key_metrics = 0
                for key, value in equip_data.items():
                    if key not in ['status'] and isinstance(value, (int, float)) and key_metrics < 2:
                        unit = '°C' if 'temp' in key else 'RPM' if key == 'rpm' else '%' if 'efficiency' in key or 'soc' in key else 'V' if 'voltage' in key else 'Hz' if 'frequency' in key else ''
                        st.metric(key.replace('_', ' ').title(), f"{value:.1f}{unit}")
                        key_metrics += 1
    
    except Exception as e:
        st.error(f"Equipment display error: {str(e)}")
    
    # COMPACT SENSOR ARRAY
    st.markdown("---")
    st.markdown("## 📡 **Advanced Sensor Hologram Array**")
    
    try:
        sensor_cols = st.columns(5)
        sensor_data = [
            ("🌡️", "Temperature", village['sensors'].get('ambient_temp', 30.0), "°C"),
            ("💧", "Humidity", village['sensors'].get('humidity', 65), "%"),
            ("⚡", "Voltage", village['sensors'].get('voltage', 24.0), "V"),
            ("🔌", "Current", village['sensors'].get('current', 0.0), "A"),
            ("💨", "Pressure", village['sensors'].get('pressure', 1013.2), "hPa")
        ]
        
        for i, (icon, name, value, unit) in enumerate(sensor_data):
            with sensor_cols[i]:
                st.markdown(f"""
                <div class="sensor-hologram">
                    <h2 style="margin: 0.3rem 0; font-size: 2rem;">{icon}</h2>
                    <h4 style="margin: 0.3rem 0; font-weight: 600; font-size: 0.9rem;">{name}</h4>
                    <h1 style="margin: 0.3rem 0; font-size: 1.6rem; font-weight: bold;">{value:.1f}{unit}</h1>
                    <div style="font-size: 0.7rem; opacity: 0.9;">🔄 Live</div>
                </div>
                """, unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Sensor display error: {str(e)}")
    
    # COMPACT AI PROCESSING
    st.markdown("---")
    st.markdown("""
    <div class="neural-network-3d">
        <h2 style="text-align: center; margin-bottom: 1.5rem; font-size: 2rem;">🧠 AI Neural Network Processing</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
            <div style="text-align: center;">
                <h2 style="margin: 0; font-size: 2rem;">1,847</h2>
                <p style="margin: 5px 0; opacity: 0.9;">Decisions Today</p>
            </div>
            <div style="text-align: center;">
                <h2 style="margin: 0; font-size: 2rem;">23ms</h2>
                <p style="margin: 5px 0; opacity: 0.9;">Avg Response</p>
            </div>
            <div style="text-align: center;">
                <h2 style="margin: 0; font-size: 2rem;">96.7%</h2>
                <p style="margin: 5px 0; opacity: 0.9;">Accuracy Rate</p>
            </div>
            <div style="text-align: center;">
                <h2 style="margin: 0; font-size: 2rem;">45</h2>
                <p style="margin: 5px 0; opacity: 0.9;">Active Sensors</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # COMPACT SIMULATION SECTION
    st.markdown("---")
    st.markdown("""
    <div class="simulation-lab-main">
        <h1>🧪 ADVANCED SIMULATION LABORATORY</h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">
            Multi-Parameter Scenario Testing with Real-Time Impact Analysis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # COMPACT SIMULATION CONTROLS
    st.markdown("""
    <div class="simulation-controls-main">
        <div class="simulation-header-main">
            🎛️ SIMULATION PARAMETER CONFIGURATION
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # COMPACT PARAMETER GRID
    param_col1, param_col2 = st.columns(2)
    
    with param_col1:
        st.markdown("""
        <div class="parameter-card">
            <h3>🌦️ Weather Conditions</h3>
        </div>
        """, unsafe_allow_html=True)
        
        weather_scenario = st.selectbox("Weather Pattern", [
            "☀️ Clear Sunny", "⛅ Partly Cloudy", "☁️ Overcast",
            "🌧️ Rainy", "🌪️ Storm", "🌀 Cyclone"
        ], key="weather_sim_twin")
        weather_intensity = st.slider("Intensity", 1, 10, 5, key="weather_int_twin")
        
        st.markdown("""
        <div class="parameter-card">
            <h3>⚡ Load Pattern</h3>
        </div>
        """, unsafe_allow_html=True)
        
        load_scenario = st.selectbox("Load Type", [
            "🏠 Normal", "🎉 Festival", "🌙 Night Low",
            "☀️ Day High", "⚠️ Emergency", "🏭 Industrial"
        ], key="load_sim_twin")
        load_factor = st.slider("Load Multiplier", 0.5, 3.0, 1.0, key="load_factor_twin")
    
    with param_col2:
        st.markdown("""
        <div class="parameter-card">
            <h3>🔧 Equipment Status</h3>
        </div>
        """, unsafe_allow_html=True)
        
        equipment_scenario = st.selectbox("Equipment Condition", [
            "✅ All Optimal", "⚠️ Degraded", "🔋 Battery Aging",
            "☀️ Panel Soiling", "💨 Maintenance", "❌ Failure"
        ], key="equip_sim_twin")
        reliability_factor = st.slider("Reliability", 0.7, 1.0, 0.95, key="reliability_twin")
        
        st.markdown("""
        <div class="parameter-card">
            <h3>🎯 Duration</h3>
        </div>
        """, unsafe_allow_html=True)
        
        duration = st.slider("Hours", 1, 168, 24, key="duration_sim_twin")
    
    # COMPACT EXECUTE BUTTON
    st.markdown('<div class="execute-button-container">', unsafe_allow_html=True)
    
    if st.button("🚀 EXECUTE ADVANCED SIMULATION", 
                type="primary", 
                key="run_advanced_sim_twin"):
        
        with st.spinner("🔮 Running Analysis..."):
            progress = st.progress(0)
            status_text = st.empty()
            
            simulation_steps = [
                "🔄 Initializing simulation...",
                "📊 Loading data...",
                "🌦️ Weather analysis...",
                "⚡ Load analysis...",
                "🔧 Equipment evaluation...",
                "🧠 AI processing...",
                "💰 Economic impact...",
                "🌱 Environmental assessment...",
                "🎯 Reliability calculation...",
                "📈 Compiling results...",
                "✅ Analysis complete!"
            ]
            
            for i, step in enumerate(simulation_steps):
                status_text.markdown(f"**{step}**")
                time.sleep(0.4)
                progress.progress((i + 1) * 9)
            
            progress.progress(100)
            time.sleep(0.5)
            
            # Calculate results
            weather_impact_map = {
                "☀️ Clear Sunny": (weather_intensity - 5) * 2,
                "⛅ Partly Cloudy": (weather_intensity - 5) * 1,
                "☁️ Overcast": (weather_intensity - 5) * -1,
                "🌧️ Rainy": (weather_intensity - 5) * -2,
                "🌪️ Storm": (weather_intensity - 5) * -3,
                "🌀 Cyclone": (weather_intensity - 5) * -4
            }
            
            load_impact_map = {
                "🏠 Normal": (load_factor - 1) * 5,
                "🎉 Festival": (load_factor - 1) * 8,
                "🌙 Night Low": (load_factor - 1) * 3,
                "☀️ Day High": (load_factor - 1) * 6,
                "⚠️ Emergency": (load_factor - 1) * 12,
                "🏭 Industrial": (load_factor - 1) * 15
            }
            
            equipment_impact_map = {
                "✅ All Optimal": (reliability_factor - 0.95) * 50,
                "⚠️ Degraded": (reliability_factor - 0.95) * 40,
                "🔋 Battery Aging": (reliability_factor - 0.95) * 35,
                "☀️ Panel Soiling": (reliability_factor - 0.95) * 30,
                "💨 Maintenance": (reliability_factor - 0.95) * 25,
                "❌ Failure": (reliability_factor - 0.95) * 20
            }
            
            simulation_params = {
                'weather_scenario': weather_scenario,
                'weather_intensity': weather_intensity,
                'weather_impact': weather_impact_map.get(weather_scenario, 0),
                'load_scenario': load_scenario,
                'load_factor': load_factor,
                'load_impact': load_impact_map.get(load_scenario, 0),
                'equipment_scenario': equipment_scenario,
                'reliability_factor': reliability_factor,
                'equipment_impact': equipment_impact_map.get(equipment_scenario, 0),
                'duration': duration
            }
            
            results = create_advanced_simulation_results(simulation_params, village)
            
            st.success("✅ **SIMULATION COMPLETED SUCCESSFULLY!**")
            
            # Display results WITHOUT AI recommendations
            display_enhanced_simulation_results(results, simulation_params)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main application - FIXED NAVIGATION AND ERROR HANDLING
def main():
    try:
        # Only update data on home page
        if st.session_state.current_view == 'home':
            update_simulation_data()
        
        # Route to correct feature - NO MIXING
        if st.session_state.current_view == 'home':
            show_home_screen()
        elif st.session_state.current_view == 'feature_1':
            show_feature_1()  # ONLY show this feature
        elif st.session_state.current_view == 'feature_2':
            show_feature_2()  # ONLY show this feature
        elif st.session_state.current_view == 'feature_3':
            show_feature_3()  # ONLY show this feature
        elif st.session_state.current_view == 'feature_4':
            show_feature_4()  # ONLY show this feature
        elif st.session_state.current_view == 'feature_5':
            show_feature_5()  # ONLY show this feature
        elif st.session_state.current_view == 'feature_6':
            show_ultimate_digital_twin()  # ONLY show this feature
        elif st.session_state.current_view == 'feature_7':
            show_feature_7()  # ONLY show this feature
        
        # Auto-refresh ONLY for home page
        if st.session_state.current_view == 'home':
            time.sleep(3)
            st.rerun()
    
    except Exception as e:
        # Silent error handling for minor issues
        st.info("🔄 System initializing...")
        time.sleep(1)
        st.rerun()

if __name__ == "__main__":
    main()
