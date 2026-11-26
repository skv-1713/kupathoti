# CLEAN MADURAI
## Intelligent Waste Collection & Demand Mapping System
### Municipal Waste Intelligence Platform for Madurai City Corporation

Clean Madurai is a unified municipal intelligence platform combining:
- **IoT Smart Bins**: Real-time fill-level telemetry via ESP32 microcontrollers, HC-SR04 ultrasonic sensors (with safe 3.3V logic interfacing), and ESP32-CAM visual monitoring.
- **Citizen Waste Reporting**: Direct community participation for proposing new collection points and reporting waste issues.
- **Geographic Demand Clustering**: DBSCAN algorithm grouping citizen requests into explainable municipal demand hotspots.
- **AI/ML Fill-Level Prediction**: Linear & cyclical regression models predicting critical fill milestones for pre-emptive truck dispatch.
- **Unified Role-Based Architecture**: Single web application and single backend serving Citizens, Municipal Operations Staff, and Sanitation Crew Workers through role-based access.

---

## Directory Architecture

```
clean-madurai/
│
├── frontend/               # React + TypeScript + Vite + Tailwind CSS + Three.js + Leaflet
│   ├── src/
│   │   ├── components/     # 3D Digital Twin, UI cards, Navbar, Footer, Simulator
│   │   ├── layouts/        # MainLayout, CitizenLayout, AdminLayout
│   │   ├── pages/          # Public landing, Live Map, How it works, Login, Dashboards
│   │   ├── types/          # Core TypeScript definitions
│   │   └── router/         # React Router v6 unified role routing
│   ├── index.html
│   └── package.json
│
├── backend/                # Python + Flask REST API (Phase 3)
│   ├── app.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── auth/
│   └── config/
│
├── database/               # Relational MySQL Schema (Phase 3)
│   └── schema.sql
│
├── iot-simulator/          # Multi-bin ESP32 telemetry simulator daemon (Phase 7)
│   └── simulator.py
│
└── ai/                     # scikit-learn fill forecasting & DBSCAN clustering (Phase 8)
    ├── fill_prediction.py
    └── demand_clustering.py
```

---

## Phase 1 Completed Milestones

- [x] Full Project Structure with clean separation (`/frontend`, `/backend`, `/database`, `/iot-simulator`, `/ai`)
- [x] React 19 + TypeScript + Vite 8 + Tailwind CSS modern design system setup
- [x] Clean Madurai Visual Identity: Deep navy/purple primary, mint green accent, light lavender/blue-white contrast
- [x] Real Interactive 3D Hero Experience built with Three.js (Smart Bin MD-017, HC-SR04 dual transducer, ESP32 enclosure with status LED, ESP32-CAM lens, internal waste fill level, animated sonar rings, ascending IoT telemetry particles, mouse parallax, raycaster hover & click inspection zoom, WebGL fallback)
- [x] Scroll-based 4-stage municipal storytelling ("Waste becomes data", "Citizens part of the solution", "Data becomes action", "See Madurai in real time")
- [x] Interactive On-Page Ultrasonic Sensor Simulator widget with real HC-SR04 mathematical distance computation
- [x] Interactive Live Madurai Waste Grid GIS Map Teaser with demo bins in Anna Nagar, KK Nagar, Sellur, Mattuthavani, and Simmakkal
- [x] Global Navigation Bar with mobile drawer, status indicators, and distinct dual entry portal ("Citizen Portal" vs "Municipality Staff")
- [x] Unified Authentication Page with separate Citizen and Staff login entry points (no role dropdown!) and Citizen Registration
- [x] Public Dedicated Leaflet GIS Waste Map Page (`/waste-map`)
- [x] Technical Architecture Documentation Page (`/how-it-works`) with mandatory HC-SR04 3.3V logic hardware safety notice
- [x] About Page (`/about`) highlighting Madurai Smart City Mission objectives
- [x] Protected Role Route Shells (`/citizen`, `/admin`, `/worker`) prepared for Phase 2 authentication and backend integration
