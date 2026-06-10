<div align="center">

# 🦅 INTERNAL CAASM PORTAL
### `Cyber Asset Attack Surface Management`

*A stealth, internal footprinting and defensive operational awareness platform.*

<br>

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/UI-Vanilla_JS_+_Tailwind-20232A.svg?style=for-the-badge&logo=javascript&logoColor=61DAFB)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-RESTRICTED-red.svg?style=for-the-badge)](#)

<br>

</div>

---

## ⚠️ MANDATORY DISCLAIMER & RULES OF ENGAGEMENT

> [!CAUTION]
> **Defensive Operational Use Only:** This software is designed **exclusively** for visualizing, managing, and hardening the attack surface of proprietary, authorized network infrastructure.
>
> 1. **No Offensive Operations:** You are strictly prohibited from using this tool to scan, probe, or fingerprint external networks, IP ranges, or third-party assets without explicit, written legal authorization.
> 2. **No Exploitation:** This tool does not facilitate exploitation or unauthorized access. Attempting to modify it for such purposes violates its core defensive design.
> 3. **Liability:** The creator assumes zero responsibility for the misuse of this software. By running this application, you accept full legal accountability for your actions and confirm you are the owner or authorized auditor of the target networks.

---

## ⚙️ ARCHITECTURE OVERVIEW

The Internal CAASM Portal operates as a standalone, zero-container service focusing on rapid deployment:

- **Core Engine:** FastAPI (Async Python)
- **Database:** Local SQLite (via SQLAlchemy)
- **Scanner:** Background `nmap` engine (`python-nmap`)
- **Intelligence:** Placeholders for Hugging Face `transformers` (ViT Vision Models) and integrations for Analyst Copilots (LLMs).
- **Frontend:** Glassmorphism UI built with Tailwind CSS via CDN and Vanilla JS (Served directly by FastAPI).

---

## 🛠️ INSTALLATION & QUICKSTART

### Prerequisites
1. **Windows OS** (or Linux/macOS with appropriate Python adjustments)
2. **Python 3.11+** installed and added to PATH.
3. **Nmap** installed and added to the system `Environment Variables (PATH)`. This is strictly required for the discovery engine to function. [Download Nmap here](https://nmap.org/download).

### Setup Instructions

1. **Clone/Download the repository** to your local machine (e.g., `C:\Users\USUARIO\Desktop\Inteligencia\caasm-portal`).
2. **Launch the Engine:**
   Double-click the included `start.bat` file in the root directory.

   *What `start.bat` does automatically:*
   - Activates the local Python virtual environment (`venv`).
   - Verifies SQLite structure based on `models.py`.
   - Starts the `uvicorn` web server serving both the REST API and the Frontend.

3. **Access the Command Center:**
   Open your browser and navigate to:
   ```url
   http://127.0.0.1:8000
   ```

---

## 🎯 USAGE GUIDE

### 1. The Dashboard 
Provides a realtime statistical overview of your authorized footprint. It indicates the total assets discovered, exposed services, and active scanning jobs in the background queue. Keep an eye on the *Analyst Copilot* panel for future AI-driven hardening insights.

### 2. Launching Scans
Navigate to **`+ New Scan`** in the top navigation bar.
Provide an internal loopback, IP, or CIDR range.
- *Valid Target Examples:* `127.0.0.1`, `192.168.1.0/24`, `10.0.0.0/8`
- The system will dispatch an asynchronous background task to perform discovery (Ping sweep -> Top 100 Port Scan -> Banner Grabbing) and populate the local SQLite database.

### 3. Service Discovery (Shodan-Style Search)
Navigate to the **`Search Map`**.
Use the filter syntax to hunt for specific internal exposures:
- `port:80` (Finds all assets with HTTP port open)
- `service:ssh` (Finds all assets with SSH service running)

---

<br>
<br>

<div align="center">

## 💀 SUPPORT THE DEVELOPMENT 💀

*If this tool helps secure your perimeter, consider fueling future R&D.*
*Privacy respected. BTC Accepted.*

```text
       .---.
      /_____\
      ( '.' )
       \_-_/
    .-"`'v'`"-.
   /           \
  /  /       \  \
 /  /         \  \

```

> **Bitcoin (BTC) Network:**
> ### `bc1qqphwht25vjzlptwzjyjt3sex7e3p8twn390fkw`

</div>

---

## 🎖️ CENTRO DE COMUNICACIONES Y REPORTES OFICIALES
**NIVEL DE ACCESO:** AUTORIZADO | **DESTINATARIO:** COMANDANCIA DE DESARROLLO (gustavolobatoclara@gmail.com)

A través del siguiente portal de comunicaciones, el personal autorizado puede emitir reportes de incidencias, fallas críticas en despliegue (compilación) o solicitudes de mejoras estratégicas. Seleccione la directiva correspondiente para visualizar los protocolos de envío:

<details>
<summary><b>🚨 REPORTAR QUEJA O INCIDENCIA DISCIPLINARIA / OPERATIVA</b></summary>
<br>
Para tramitar una queja sobre el funcionamiento, estructura o contenido del sistema, envíe un mensaje a <b>gustavolobatoclara@gmail.com</b> siguiendo este protocolo:
<ol>
  <li><b>Asunto:</b> [QUEJA] - Nombre del Sistema - Breve descripción.</li>
  <li><b>Cuerpo del mensaje:</b> Detallar claramente la incidencia, impacto operativo y, si es posible, la evidencia (capturas o logs).</li>
  <li><b>Prioridad:</b> Indicar si es de atención inmediata o diferida.</li>
</ol>
</details>

<details>
<summary><b>🛠️ REPORTE DE PROBLEMAS DE COMPILACIÓN O DESPLIEGUE</b></summary>
<br>
Si experimenta fallos durante la fase de compilación o instalación del sistema, reporte a <b>gustavolobatoclara@gmail.com</b> con la siguiente estructura técnica:
<ol>
  <li><b>Asunto:</b> [COMPILACIÓN] - Falla en entorno &lt;Entorno/OS&gt;.</li>
  <li><b>Especificaciones:</b> Sistema Operativo, versión de dependencias y herramientas de compilación utilizadas.</li>
  <li><b>Traza de Error (Logs):</b> Adjunte el log completo de errores proporcionado por la terminal (en formato texto o captura legible).</li>
  <li><b>Pasos de Reproducción:</b> Secuencia exacta de comandos ejecutados antes del fallo crítico.</li>
</ol>
</details>

<details>
<summary><b>💡 SUGERENCIAS O SOLICITUDES DE DESARROLLO</b></summary>
<br>
Para proponer nuevas capacidades tácticas, módulos de inteligencia o mejoras de arquitectura, envíe su solicitud a <b>gustavolobatoclara@gmail.com</b>:
<ol>
  <li><b>Asunto:</b> [PROPUESTA] - Mejora o Nuevo Módulo.</li>
  <li><b>Objetivo Táctico:</b> ¿Qué problema resuelve o qué ventaja proporciona esta nueva característica?</li>
  <li><b>Viabilidad:</b> (Opcional) Posible enfoque técnico o herramientas recomendadas para su implementación.</li>
</ol>
</details>

---

---

## Support / Apoya este proyecto

I build open-source projects focused on applied AI, automation, and data intelligence.
Over on my GitHub you'll find things like AI-powered analysis engines, OSINT platforms for open-source research, Windows automation tools, and experiments with language models.
Everything is public and free, so anyone can use it, study it, or build on top of it. github.com/murdok1982

Keeping these projects alive takes a lot of hours. If any of them have helped you out or you just like what I'm doing, you can support me with a coffee: ko-fi.com/murdok1982

Every contribution goes straight back into shipping more open-source code.
