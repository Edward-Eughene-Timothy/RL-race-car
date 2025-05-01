



# 🚗 Self-Driving Car using Reinforcement Learning

This project focuses on training an autonomous driving agent using **Reinforcement Learning** in the **CarRacing-v3** environment provided by Gymnasium. The agent learns to drive a car using visual inputs and the **Proximal Policy Optimization (PPO)** algorithm.



### 1.  Overall Strategy

- **Goal**: Train a reinforcement learning agent to drive autonomously on randomly generated tracks.
- **Input**: Visual observations (96x96 RGB frames).
- **Algorithm**: PPO (Proximal Policy Optimization) from `stable-baselines3`.
- **Output**: Trained model that can navigate tracks efficiently.

---

### 2.  System Requirements

| Component      | Specification                 |
|----------------|-------------------------------|
| OS             | Linux/Windows/Mac             |
| Python         | 3.10.0                        |
| Processor      | Intel Core i7 (13th Gen)      |
| RAM            | Minimum 16 GB                 |
| GPU (Optional) | For faster training           |

---

### 3.  Required Libraries

Install the following libraries before starting:

- `gymnasium`
- `stable-baselines3`
- `box2d-py`
- `numpy`
- `matplotlib`
- `swig` (system package, for Box2D)

####  Install SWIG (Fedora):
```bash
sudo dnf install swig
```

---

### 4.  Environment Setup

Set up a virtual environment using either Conda or venv to manage dependencies.

#### 📌 Using Conda (Recommended)
```bash
conda create -n selfdrivingcar python=3.10.0
conda activate selfdrivingcar
pip install -r requirements.txt
```

#### 📌 Using venv
```bash
python3 -m venv selfdrivingcar
source selfdrivingcar/bin/activate
pip install -r requirements.txt
```

---

### 5.  Model Development Methodology

- **Data**: Agent uses pixel data from CarRacing-v3.
- **Action Space**: Continuous or discrete actions (steer, gas, brake).
- **Training Script**: `train.ipynb`
- **Evaluation Script**: `evaluate.py`

---

### 6.  Usage Instructions

To **train the model**:
```bash
python train.ipynb
```

To **evaluate a pre-trained model**:
```bash
python evaluate.py
```

> ✅ Make sure you configure `train.ipynb` and `evaluate.py` according to your model paths and environment settings.

---
