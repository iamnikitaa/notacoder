# notacoder 🐙

<p align="center">
  <img src="https://img.shields.io/badge/status-under%20construction%20🚧-yellow?style=for-the-badge" alt="Status: Under Construction">
  <img src="https://img.shields.io/badge/python-3.12-blue?style=for-the-badge&logo=python" alt="Python 3.12">
  <img src="https://img.shields.io/badge/django-5.1-092E20?style=for-the-badge&logo=django" alt="Django 5.1">
</p>

> "We don’t do boring syntax lectures here. Just you, some missing code, and the mild existential crisis that comes with debugging."

**notacoder** is a vibe. It's a hands-on, fill-in-the-blank coding playground built with Django, designed for beginners who want to learn Python without the yawn-inducing theory. The goal is to build logic and confidence, one challenge at a time. Slay your first `print()` statement and level up from there.

**⚠️ Heads up:** This project is a major work-in-progress. Things might break, look weird, or randomly change. It's all part of the process. ✨

## The Vibe (Features)

*   **🧠 Learn by Doing:** Progressive, fill-in-the-blank challenges that guide you from "Hello, World!" to understanding classes.
*   **🎮 Gamified Progression:** Earn points for each correct solution and track your completed challenges.
*   **💅 Guest Mode:** Hop in and try challenges without an account. Create a "guest user" with just a name and a magic word to save your progress.
*   **✨ Confetti Confirmed:** Get that sweet, sweet confetti validation when you get an answer right. Because you deserve it.

---

## Peep the Look 👀

A quick look at what we're building.

#### The Login Page: Who Dis?

*The entry point. Just pick a name and a magic word to get started.*

`![image](https://github.com/user-attachments/assets/ac53adca-31eb-410d-9860-95e84e370443)
`

---

#### The Challenge List: Choose Your Fighter

*Your dashboard of quests. Completed challenges get a nice little checkmark so you know what you've conquered.*

`![image](https://github.com/user-attachments/assets/356f9954-7735-4b38-bf87-21cf1e667080)
`

---

#### The Challenge Detail: The Main Event

*This is where the magic happens. Read the description, fill in the blanks, and smash that submit button.*

`![image](https://github.com/user-attachments/assets/9ba42bbd-9329-43e0-9f89-4cdcba74ca07)
`

---

## Tech Stack & Setup

This project is built on a simple but powerful stack.

*   **Backend:** Python 3.12, Django 5.1
*   **Database:** SQLite3 (perfect for development and simple hosting)
*   **Frontend:** HTML, CSS, a sprinkle of JavaScript
*   **Frameworks/Libs:** Bootstrap 5 (for layout), Confetti.js (for the vibes)

### Getting it Running Locally

Wanna run this on your own machine? Bet.

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/your-github-username/iamnikitaa-notacoder.git
    cd iamnikitaa-notacoder
    ```

2.  **Set up a virtual environment (you should, for real):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the good stuff:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the migrations to set up your database:**
    ```bash
    python manage.py migrate
    ```

5.  **Populate the database with the starter challenges:**
    ```bash
    python manage.py add_challenges
    ```

6.  **Fire up the server:**
    ```bash
    python manage.py runserver
    ```

    Now you can open your browser and go to `http://127.0.0.1:8000` to see the site live.

---

## The Roadmap (aka The To-Do List)

This is what's on the vision board for the future. No promises on timelines. ✌️

*   [ ] More advanced challenge topics (APIs, file handling).
*   [ ] A real user profile page to see stats.
*   [ ] Leaderboard to see who's slaying the most.
*   [ ] Prettier UI animations and transitions.
*   [ ] The ability to filter challenges by difficulty or topic.

---

<p align="center">
  Built with 💖 and a lot of `print("is this working?")`.
</p>
