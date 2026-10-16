::: {align="center"}
# 🛣️ RoadSentinel Nexus

### Local-First Traffic Intelligence & Monitoring Platform

**Analyze traffic videos. Monitor system health. Manage modular tools
--- from one clean dashboard.**

```{=html}
<p>
```
`<img src="https://img.shields.io/badge/Status-Early%20Development-orange?style=for-the-badge" alt="Project status: Early Development">`{=html}
`<img src="https://img.shields.io/badge/Processing-Local--First-2563EB?style=for-the-badge" alt="Local-first processing">`{=html}
`<img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Web-475569?style=for-the-badge" alt="Platform">`{=html}
```{=html}
</p>
```
```{=html}
<!-- Replace the image path below with your own project screenshot. -->
```
`<img src="docs/images/dashboard.png" alt="RoadSentinel Nexus dashboard preview" width="900">`{=html}

*Your dashboard screenshot goes above. Add the image to
`docs/images/dashboard.png`, or change the path to match your file.*
:::

------------------------------------------------------------------------

## 👋 About the Project

**RoadSentinel Nexus** is a modular, local-first project that aims to
bring traffic-video analysis, system monitoring, network utilities, and
evidence/report workflows into one dashboard.

The project is under active development. The current starter version
includes a FastAPI backend, a React dashboard, persistent feature
settings, and a basic system monitor. Many advanced traffic and network
modules are still planned and are **not yet fully implemented**.

## 🖼️ Screenshots & Demo

Add your own screenshots, example images, or a short GIF to this
section.

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center" width="50%">
```
`<strong>`{=html}📊
Dashboard`</strong>`{=html}`<br>`{=html}`<br>`{=html}
`<img src="docs/images/dashboard.png" alt="Main dashboard screenshot" width="100%">`{=html}`<br>`{=html}
`<sub>`{=html}Replace with your main dashboard
screenshot.`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="50%">
```
`<strong>`{=html}🚦 Traffic
Analysis`</strong>`{=html}`<br>`{=html}`<br>`{=html}
`<img src="docs/images/traffic-analysis.png" alt="Traffic analysis screenshot" width="100%">`{=html}`<br>`{=html}
`<sub>`{=html}Replace with a traffic analysis screenshot when
available.`</sub>`{=html}
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td align="center" colspan="2">
```
`<strong>`{=html}🎬 Demo GIF / Video
Preview`</strong>`{=html}`<br>`{=html}`<br>`{=html}
`<img src="docs/images/demo.gif" alt="Project demo GIF" width="80%">`{=html}`<br>`{=html}
`<sub>`{=html}Optional: add a short GIF showing the app in
action.`</sub>`{=html}
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
### How to add your own images

1.  In your repository, create this folder: `docs/images/`
2.  Copy your screenshots into that folder.
3.  Use these suggested filenames, or edit the image paths above:
    -   `dashboard.png`
    -   `traffic-analysis.png`
    -   `demo.gif`
4.  Commit and push the changes to GitHub.

> **Tip:** GitHub README images can be stored in the repository. You do
> not need to upload them to a separate image-hosting website.

## ✨ Current Features

-   🧩 **Modular feature controls** --- enable or disable available
    modules from the dashboard.
-   🖥️ **System monitoring** --- view basic CPU, memory, and disk
    information.
-   ⚙️ **FastAPI backend** --- a local API for the dashboard.
-   💾 **SQLite persistence** --- saves feature settings locally.
-   ⏳ **Background job foundation** --- starter job-management
    structure for future long-running work.
-   🌙 **Dark dashboard UI** --- a clean interface built with React and
    TypeScript.
-   🔒 **Local-first design** --- the backend binds to `127.0.0.1` by
    default.

## 🗺️ Planned Modules

These are planned or in-progress areas, not promises that they already
work.

  -----------------------------------------------------------------------
  Module                  Purpose                 Status
  ----------------------- ----------------------- -----------------------
  🚘 Vehicle detection &  Detect and track        Planned
  tracking                vehicles in video       

  🔢 Number-plate OCR     Read plate text from    Planned
                          supported footage       

  📏 Speed estimation     Estimate speed after    Planned
                          camera calibration      

  🚦 Traffic-event review Flag possible red-light Planned
                          or lane events for      
                          human review            

  🅿️ Parking analysis     Estimate parking-space  Planned
                          occupancy               

  🌐 Network tools        Local network discovery Planned
                          and diagnostics         

  🧰 Windows diagnostics  Useful local system     Planned
                          information             

  📄 Reports & evidence   Organize analysis       Planned
                          outputs for review      
  -----------------------------------------------------------------------

**Important:** Feature toggles are not the same as completed engines. In
this starter build, most advanced modules are placeholders.
Traffic-event results should be treated as candidates for human review,
not as automatic legal decisions or fines.

## 🧰 Tech Stack

  Area             Technology
  ---------------- -------------------------
  Backend API      Python, FastAPI
  Dashboard        React, TypeScript, Vite
  Local storage    SQLite
  System metrics   `psutil`
  Tests            `pytest`

## 🚀 Quick Start --- Windows

### 1. Requirements

Install these first:

-   [Python](https://www.python.org/downloads/) --- use a version
    compatible with `backend/requirements.txt`
-   [Node.js](https://nodejs.org/) --- includes npm
-   [Git](https://git-scm.com/downloads/) --- optional, but useful for
    cloning the repository

### 2. Start the backend

Open **PowerShell** in the project folder and run:

``` powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

Keep this terminal open. The local API should be available at:

-   API: `http://127.0.0.1:8765`
-   API documentation: `http://127.0.0.1:8765/docs`

### 3. Start the dashboard

Open a **second PowerShell** window in the project folder:

``` powershell
cd apps\dashboard
npm install
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173`.

### 4. Stop the app

Press `Ctrl + C` in each terminal window.

## 📁 Project Structure

``` text
roadsentinel-nexus/
├── apps/
│   └── dashboard/       # React + TypeScript web dashboard
├── backend/
│   ├── app/
│   │   ├── database/    # SQLite storage
│   │   ├── feature_control/
│   │   ├── job_manager/
│   │   └── main.py      # FastAPI entry point
│   ├── tests/
│   └── requirements.txt
├── data/                # Local data directory
├── docs/
│   ├── images/          # Add README screenshots here
│   ├── ARCHITECTURE.md
│   └── ROADMAP.md
├── .gitignore
├── LICENSE
└── README.md
```

## 🧪 Run Tests

From the `backend` directory, with the virtual environment activated:

``` powershell
pytest
```

If a test fails, check that dependencies were installed and that you are
running the command from the correct directory.

## 🔐 Privacy & Safety Notes

-   The backend is configured to listen on the local machine
    (`127.0.0.1`) by default.
-   Do not expose the API to a public network unless you have added
    suitable authentication and security controls.
-   Keep private footage, plate images, logs, and generated reports out
    of public commits unless you have permission to share them.
-   Speed estimates and traffic-event detections can be inaccurate.
    Review results before relying on them.
-   The project does not automatically issue official fines or legal
    decisions.

## 🛣️ Roadmap

-   [x] Starter API and dashboard
-   [x] Local feature-setting persistence
-   [x] Basic system metrics
-   [ ] Improve module dependency handling
-   [ ] Add recorded-video import and job progress
-   [ ] Implement and test vehicle detection
-   [ ] Add plate OCR with configurable privacy controls
-   [ ] Add calibrated speed estimation
-   [ ] Build reviewable evidence and report export
-   [ ] Package a native desktop application

## 🤝 Contributing

Contributions, bug reports, ideas, and UI feedback are welcome.

1.  Fork the repository.
2.  Create a branch for your change.
3.  Make a focused change and test it.
4.  Open a pull request with a clear description and screenshots when
    useful.

## 📌 Project Status

RoadSentinel Nexus is an **early-development starter project**. Please
check the current implementation before relying on any feature in a
real-world environment.

## 📄 License

This project is distributed under the MIT License. See
[`LICENSE`](LICENSE) for details.

------------------------------------------------------------------------

::: {align="center"}
**Built for practical, local-first experimentation.** 🛣️
:::
