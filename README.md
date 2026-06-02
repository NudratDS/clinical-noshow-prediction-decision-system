

#  Patient No-Show Prediction: A Clinical AI Approach
###  Transforming 110,000+ Medical Appointment Records into Proactive Inpatient Interventions

<p align="center">
  <a href="https://www.linkedin.com/in/nudrat-abbas-664378324/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin"/>
  </a>
  <a href="https://www.kaggle.com/nudratabbas">
    <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle"/>
  </a>
  <a href="mailto:contact@nudratabbas.com">
    <img src="https://img.shields.io/badge/Email-C9A227?style=for-the-badge&logo=gmail"/>
  </a>
  <a href="https://wa.me/message/X2LUPKGE7KJYE1">
    <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp"/>
  </a>
  <a href="https://nudratabbas.com">
    <img src="https://img.shields.io/badge/Website-black?style=for-the-badge"/>
  </a>
</p>

---
<div align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2Fjcjg0bWFzaDc0bDlmaTNrcTRrdzR6NWV5dzN0NTdoZ3A0ZG9mayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gVnUxsQAqjLAyjgboq/giphy.gif" width="50%" alt="Header GIF">
</div>

## The Business Challenge & Clinical Impact

Missed medical appointments disrupt entire health systems. They result in wasted clinical resources, severe revenue leakage for practice operators, and compromised patient care timelines. 

Instead of reactive dashboarding, this project implements **The Clinical Clarity System™** approach—turning messy administrative and medical scheduling logs into an active, upstream **predictive infrastructure**. By analyzing over 110,000 global appointment data records, this system identifies high-risk no-show patients *before* the clinical day begins, enabling strategic automated interventions (SMS, predictive overbooking, or manual care-team triage).

### Key Technical Highlights
* **Comprehensive Feature Pipeline:** Label encoding, time-delta extractions (booking vs. appointment date), and multi-categorical health marker tracking (Hypertension, Diabetes, Alcoholism, Handcap).
* **Advanced Gradient Boosting:** Comparative model benchmarking leveraging optimized **LightGBM** and **XGBoost** pipelines.
* **Explainable AI (XAI):** Full **SHAP (SHapley Additive exPlanations)** integration to provide clinicians with transparent, case-by-case feature attributions explaining *why* a model flags a patient.

---

##  Repository Architecture

This codebase is organized to support clean production drops and enterprise modularity:

```bash 
├── data/
│   └── README.md           # Instructions to pull down the source 110k patient record set
├── notebooks/
│   └── patient-no-show-prediction.ipynb  # Comprehensive exploratory data analysis & R&D notebook
├── src/                    # Modular, production-ready enterprise scripts
│   ├── __init__.py
│   ├── data_processor.py   # Engineering class for pipeline transformations and feature splits
│   ├── model.py            # High-performance LightGBM and XGBoost training/inference loops
│   └── explainability.py   # SHAP explainer configurations for clinical visual interpretations
├── requirements.txt        # Package dependencies (pandas, scikit-learn, lightgbm, xgboost, shap)
├── LICENSE                 # Open-source MIT License
└── README.md               # Interactive Project Landing Page
```

---

## Step-by-Step Installation & Setup

### 1. Clone the Infrastructure

```bash
git clone [https://github.com/NudratDS/clinical-noshow-prediction-decision-system.git](https://github.com/NudratDS/clinical-noshow-prediction-decision-system.git)
cd clinical-noshow-prediction-decision-system

```

### 2. Configure Your Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

```

### 3. Execution

To run the end-to-end engineered production pipeline, execute:

```bash
python src/data_processor.py
python src/model.py

```

---

##  Evaluation & Clinical Transparency

The pipeline benchmarks multiple tree-based ensembles, evaluating accuracy alongside clinical recall parameters to minimize missed true-positives.

### Model Transparency via SHAP

To ensure clinical buy-in, we avoid "black-box" decisions. Global feature impacts highlight key driving vectors—including wait-time duration distributions and automated SMS notification histories.

*Add your generated SHAP Summary plots or performance charts directly beneath this section to optimize engagement and pull immediate **Stars** from technical visitors.*

---

##  About the Developer

**Nudrat Abbas** *Healthcare Data Scientist & Founder of Third Decimal* **Ranked #12 out of 9,206 globally as a Kaggle Datasets Grandmaster.** I specialized in architectural pipelines that translate clinical data into measurable system outcomes. Certified in HIPAA compliance with a footprint of 30+ successfully deployed data products worldwide.

---

##  Technical Partnerships & Consulting

Are you a clinic owner, digital health agency executive,a student need cosultancy or hospital clinical operations director looking to build out customized predictive analytics infrastructures?

I engineer white-label decision frameworks, readmission mitigation suites, fraud monitoring mechanisms, and automated clinical NLP data products. Let's maximize your system metrics:

 * **Schedule a Consultation:** [Click to WhatsApp Me](https://wa.me/message/X2LUPKGE7KJYE1)
 * **Direct Inquiry Email:** contact@nudratabbas.com
 * **Portfolio & Methods:** [nudratabbas.com](https://nudratabbas.com)

*"Strategy Sharpened to the Third Decimal"*

# Clinical Dataset Source

The raw medical appointment dataset containing over 110,000+ patient records is hosted directly on Kaggle. 

📥 **[Download the Dataset from Kaggle Here](https://www.kaggle.com/datasets/joniarroba/noshowappointments)**


