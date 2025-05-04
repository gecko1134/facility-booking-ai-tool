# 🏟️ AI Booking Optimizer for Sports Complexes

This web app uses an AI-assisted engine to recommend conflict-free, revenue-optimized booking slots for sports facilities.

Built using **Streamlit** and **Pandas**, this tool allows staff to:
- Upload historical booking data
- Upload new booking requests
- Automatically detect conflicts
- Suggest best-fit time slots
- Download optimized schedules

---

## 📁 Project Files

- `app.py` – Streamlit dashboard interface
- `optimizer.py` – AI conflict detection & slot suggestion engine
- `requirements.txt` – Required Python packages
- `historical_data.csv` – Sample existing bookings
- `new_requests.csv` – Sample new booking requests

---

## 🚀 Deploy on Streamlit Cloud

1. Fork or clone this repo to your GitHub account.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud).
3. Click “Deploy an app”, and connect your repo.
4. Choose `app.py` as the entry point.
5. Done! Your app will be live in minutes.

---

## 🧠 Example

Uploads:
- Historical Data: Existing bookings by time, resource, and user group
- New Requests: Preferred slots for new users

The app outputs:
- Availability status for each request
- Recommended non-conflicting times
- Downloadable CSV with optimized assignments

---

## 🔧 Requirements

```bash
pip install -r requirements.txt
```

---

Made for smart scheduling at regional and national sports parks.
