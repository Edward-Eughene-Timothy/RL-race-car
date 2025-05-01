
## 🚗 System Approach

The **System Approach** outlines the overall strategy and methodology adopted for the development and implementation of the **Self-Driving Car using Reinforcement Learning**. This includes defining system requirements, preparing the environment, selecting suitable libraries, and providing hassle-free steps for training and evaluation.

---

### 1. 📋 Overall Strategy

- **Goal**: Train a reinforcement learning agent to autonomously drive a car on a procedurally generated track in the CarRacing-v3 environment from Gymnasium.
- **Learning Method**: The agent uses visual observations (96x96 RGB images) as input and learns through interaction with the environment using a reward-based feedback loop.
- **Model Used**: Proximal Policy Optimization (PPO) algorithm from the `stable-baselines3` library.

---

### 2. 🧰 System Requirements

To develop and run the project smoothly, the following system specifications are recommended:

- **Operating System**: Fedora Linux  
- **Python Version**: 3.7.12  
- **Processor**: Intel Core i7 (13th Gen)  
- **RAM**: Minimum 16 GB  
- **GPU (Optional)**: For faster training, though CPU is sufficient for testing and evaluation

---

### 3. 📦 Required Libraries

The following Python libraries and system packages are necessary:

- `gymnasium` (for the CarRacing-v3 environment)  
- `stable-baselines3` (for RL algorithms like PPO)  
- `numpy` (for numerical operations)  
- `box2d-py` (physics engine required by CarRacing)  
- `matplotlib` (for visualization)  
- `swig` (required to compile Box2D; install via system package manager)

> 🛠️ **Install SWIG on Fedora**:
```bash
sudo dnf install swig
```

---

### 4. 🛠️ Environment Setup

To avoid dependency issues, a virtual environment setup is recommended. You can use either `conda` or `venv`.

#### 📌 Using Conda (Recommended)
```bash
conda create -n selfdrivingcar python=3.7.12
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

### 5. 🧠 Model Development Methodology

- **Data Source**: The agent receives pixel-based visual input (RGB image).
- **Action Space**: Continuous or discrete depending on configuration. Common actions include steering, acceleration, and braking.
- **Training**: Conducted using `train.py`, where PPO learns from episodes by interacting with the environment.
- **Evaluation**: Using `evaluate.py`, the trained agent is tested on unseen tracks to measure performance and visualize behavior.

---

### 6. 🚦 Usage Instructions

- To **train the model**:
```bash
python train.py
```

- To **evaluate a pre-trained model**:
```bash
python evaluate.py
```

> 🎯 Make sure the correct mode is selected based on whether you're training a new agent or testing an existing one.

---
