# Multimodal AI Safety Assistant

## Overview

The Multimodal AI Safety Assistant is an AI-powered application that analyzes uploaded images and identifies potential safety hazards using Google's Gemini Vision model.

The system accepts an image and a user question, then provides:

- Hazard Identification
- Risk Explanation
- Safety Recommendations

This project was developed as part of the Edxso AI Engineer Internship Assignment.

---

## Features

- Upload Images
- Multimodal Image Understanding
- Hazard Detection
- Risk Assessment
- Safety Recommendations
- Streamlit User Interface
- Google Gemini Integration

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Pillow
- Python Dotenv

---

## Project Structure

```text
multimodal-ai-safety-assistant/
│
├── assets/
│   ├── sample_image.jpg
│   └── screenshots/
│
├── src/
│   ├── assistant.py
│   ├── config.py
│   ├── image_processor.py
│   └── prompts.py
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .env
```

---

## Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## Example Query

```text
What is the primary danger shown in this image?
```

---

## Sample Output

Primary Hazard:
Electrocution Hazard

Why It Is Dangerous:
- Exposed electrical wires are in contact with water.
- Water conducts electricity.
- High risk of electric shock and injury.

Safety Recommendations:
- Turn off power immediately.
- Keep people away from the area.
- Replace damaged cables.
- Dry the area before restoring power.

---

## Future Improvements

- Real-time Video Analysis
- Multiple Hazard Detection
- Severity Scoring
- Workplace Compliance Checks
- Safety Report Generation

---

## Author

Vidya Bag
