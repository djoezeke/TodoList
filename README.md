<p align="center">
  <h1 align="center"> To-Do List App </h1>
</p>

<p align="center">
	<em>
    <code>Task Organizer and Manager App</code>
  </em>
</p>

<p align="center">
	<img src="https://img.shields.io/github/license/djoezeke/TodoList?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/djoezeke/TodoList?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/djoezeke/TodoList?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/djoezeke/TodoList?style=default&color=0080ff" alt="repo-language-count">
</p>

<p align="center">
  <img src="images/to-do-list.jpg" alt="To-Do List"/>
</p>

<details>
  <summary>Table of Contents</summary>

- [📍 Overview](#📍-overview)
- [🚀 Features](#🚀-features)
- [📁 Project Structure](#📁-project-structure)
- [📌 Getting Started](#📌-getting-started)
  - [☑️ Prerequisites](#☑️-prerequisites)
  - [⚙️ Installation](#⚙️-installation)
  - [🤖 Usage](#🤖-usage)
  - [🚀 Deploying on Vercel](#🚀-deploying-on-vercel)
- [🔰 Contributing](#🔰-contributing)
- [🙌 Acknowledgments](#🙌-acknowledgments)
- [📚 References](#📚-references)
- [📝 License](#📝-license)

</details>

## 📍 Overview

**To-Do List** is a web based application made predominantly with Django that allows the user to create and keep track of _Tasks_ and complete them with a single click.
The **To-Do List Application** enables users to manage and organize their tasks effectively. Create, track, complete and organize tasks between lists with fast modern interface.

## Kilobytes Group Project: Web Application

### Instructions

1. Join a group of 5 people and select any web application project of your choice, build it and upload it to your github account.
   Share the github repo link as your answer.

2. Find a free webhosting and domain online and publish your web application

### Group Members

- Hagan Eshun Ebenezer **01243192B**
- Sackey Ezekiel Etrue **01243101B**
- Nathaniel Okyere **01241217B**

<!-- #### Example Screenshots

<p align="center">
   <img src="images/to-do-list.jpg" alt="To-Do List UI" width="600"/>
</p> -->

## 🚀 Features

- 📝 **Create, edit, and delete tasks** with a modern, responsive UI
- ✅ **Mark tasks as complete/incomplete** with a single click
- 🗂️ **Organize tasks into lists** for better management
- 🔍 **Search, filter, and sort** tasks by title, date, or completion
- 🎨 **Modern UI** with Bootstrap 5 and Font Awesome icons
- 📱 **Mobile-friendly** and fully responsive
- 💾 **Posgressql database** for easy setup and persistence
- ⚡ **Fast and intuitive** user experience
- 🛡️ **Secure** with CSRF protection and Django best practices

<!--
✔️ Complete Tasks
🌠 Move Task
❌ Delete Task
🌟 Select Tasks
💼 Create Folders
📁 Open Folder
❌ Delete Folder
-->

## 📁 Project Structure

```
TodoList
├── images                 # Documentation images.
├── static                 # Stores static files like CSS, JavaScript, and images.
├── tasks                  # This directory contains the main application.
├── todolist               # Directory contains the core settings and configurations.
├── manage.py              # Command-line utility for interacting with the project.
├── .python-version        # Contains python version.
├── pyproject.toml         # Project config setups.
├── requirements.txt       # Lists the Python dependencies of your project.
├── .gitignore             # Specifies files and directories to be ignored by Git.
├── LICENSE                # Project License.
└── README.md              # Project Documentation.
```

## 📌 Getting Started

### 📜 Technologies & Tools

- **Django** (backend framework)
- **Supabase** (PostgreSQL database & authentication)
- **Bootstrap 5 & Tailwind CSS** (UI/UX)
- **Vercel** (deployment)

#### ☑️ Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Supabase account](https://supabase.com/) (free tier is fine)
- [Vercel account](https://vercel.com/) (for deployment)

#### 🧰 Additionals

- [Git](https://git-scm.com/) – (Optional) Version control

- [Node.js](https://nodejs.org/) (Optional) for Tailwind CSS

### ⚙️ Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/djoezeke/TodoList.git
   cd TodoList
   ```
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Supabase:**
   - Create a new project at [Supabase](https://app.supabase.com/).
   - Get your database connection string from the Supabase dashboard.
   - In your project root, create a `.env` file and add:
     ```env
     DATABASE_URL=your_supabase_postgres_connection_string
     SUPABASE_URL=your_supabase_url
     SUPABASE_KEY=your_supabase_anon_key
     ```
   - Update `settings.py` to use `os.environ['DATABASE_URL']` for `DATABASES`.
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
6. **(Optional) Install Tailwind CSS:**
   ```bash
   npm install -D tailwindcss
   npx tailwindcss init
   # Configure tailwind.config.js and build CSS as needed
   ```

### 🤖 Usage

1. Open your browser and go to `http://127.0.0.1:8000/`
2. Create a new list and start adding tasks!
3. Use the navigation bar to view all lists, all tasks, or return to the home page.
4. Edit, complete, or delete tasks and lists as needed.

### 🚀 Deploying on Vercel

1. **Push your code to GitHub.**
2. **Sign in to [Vercel](https://vercel.com/) and import your repo.**
3. **Set environment variables in Vercel dashboard:**
   - `DATABASE_URL`, `SUPABASE_URL`, `SUPABASE_KEY` (from your Supabase project)
4. **Configure Vercel for Django:**
   - Use [Vercel's Python template](https://vercel.com/templates/python/django) or add a `vercel.json` and `requirements.txt`.
   - Set the build command to `python manage.py collectstatic --noinput` and `python manage.py migrate` as needed.
5. **Deploy!**

For more, see [Deploying Django on Vercel](https://vercel.com/guides/deploying-django-with-vercel).

## 🔰 Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the game.

- **💬 [Join the Discussions](https://github.com/djoezeke/TodoList/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/djoezeke/TodoList/issues)**: Submit bugs found or log feature requests for the `TodoList` project.
- **💡 [Submit Pull Requests](https://github.com/djoezeke/TodoList/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone --recursive https://github.com/djoezeke/TodoList
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/djoezeke/TodoList/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=djoezeke/TodoList">
   </a>
</p>
</details>

## 🙌 Acknowledgments

We would like to express our gratitude to the following projects and individuals whose work made this project possible:

- [Django](https://www.github.com/django/django/) – The Web framework for perfectionists with deadlines.
- [Supabase](https://supabase.com/) – Open source Firebase alternative for backend and database.
- [Vercel](https://vercel.com/) – Effortless cloud deployment platform.
- [Bootstrap](https://getbootstrap.com/) & [Tailwind CSS](https://tailwindcss.com/) – For modern, responsive UI.
- [Font Awesome](https://fontawesome.com/) – For beautiful icons.
- The open-source community for their invaluable libraries, tutorials, and support.
- Special thanks to all contributors, testers, and users who provided feedback and suggestions.

If you feel your work should be acknowledged here, please open an issue or pull request.

---

## 📚 References

- [Django Documentation](https://docs.djangoproject.com/)
- [Supabase Docs](https://supabase.com/docs)
- [Vercel Docs](https://vercel.com/docs)
- [Bootstrap 5](https://getbootstrap.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Font Awesome](https://fontawesome.com/)

## 📝 License

This project is protected under the [MIT](LICENSE) License.
For more details, refer to the [LICENSE](LICENSE) file.
