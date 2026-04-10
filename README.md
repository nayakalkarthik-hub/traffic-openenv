# 🚦 Traffic Light RL Environment (OpenEnv API)

This project implements a reinforcement learning environment for traffic signal control, exposed via a simple OpenEnv-compatible API.

## 🔧 Endpoints

### POST /reset

Resets the environment.

**Response:**

```json
{
  "state": [10, 15, 8, 12]
}
```

### POST /step

Takes an action.

**Request:**

```json
{
  "action": 0
}
```

**Response:**

```json
{
  "state": [9, 16, 9, 13],
  "reward": 5,
  "done": false,
  "info": {}
}
```

## 📁 Files

* `env.py` → Environment logic
* `inference.py` → FastAPI server
* `Dockerfile` → Deployment config
* `requirements.txt` → Dependencies

## 🚀 Deployment

Runs on Hugging Face Spaces using Docker.

## 📌 Notes

* Designed for automated evaluation (Scalar OpenEnv checks)
* Minimal implementation for reliability and correctness
