# 💡 SignalRGB Effects

A collection of modular custom lighting effects, development tools, and seamless meta-rotators for SignalRGB.

---

## 🌍 Overview

**SignalRGB Effects** is a dedicated workspace for developing, tuning, and deploying custom Canvas 2D lighting effects. The repository includes standalone visual effects, integrated browser-based testing tools, and **Random Pack** — a flagship meta-rotator that endlessly chains multiple scenes with smooth crossfade blending.

---

## 🌟 Key Features

*   **Local Effect Tester (`index.html`):** Instant browser preview environment to test and debug effects without launching SignalRGB *(open via VS Code **Live Server** extension)*.
*   **Visual Curve Editor (`curve_editor.html`):** Interactive tool for designing, tweaking, and visualizing 7-point CDF probability curves used for dynamic parameter animation *(open via VS Code **Live Server** extension)*.
*   **Meta-Rotator Engine (`Random Pack`):** Seamlessly crossfades N native-grade effects using continuous frame loops, CDF mathematics, and a gamma-corrected night mode.
*   **One-click Deployment (`deploy.py`):** Automatically detects SignalRGB directories on any Windows system and syncs ready-to-use effects.

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Quazzy23/SignalRGB-Effects.git
```

### 2. Local Preview & Testing (Optional)
To test effects or edit probability curves in your browser:
*   Open the project in VS Code.
*   Right-click `index.html` (for effect preview) or `curve_editor.html` (for curve design).
*   Select **Open with Live Server**.

### 3. Deploy to SignalRGB
Run the script `deploy.py` to automatically copy effects to your SignalRGB directory:
*(Or copy the `Effects/Random_Pack` folder manually into `Documents\WhirlwindFX\Effects\`)*.

### 4. Activate in SignalRGB
1. Open or restart **SignalRGB**.
2. Go to **Lighting**.
3. Select **Random Pack** (or other effect) and adjust settings to your preference.

---

## 👥 Authors & Credits

*   **Project Lead:** Quazzy ([@Quazzy23](https://github.com/Quazzy23))
*   **Development:** Created with the support of Google AI Gemini.