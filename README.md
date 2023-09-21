# Prompt Manager

This is a web application that allows users to create, store and organise their prompts for various categories and subcategories. A prompt is a text that can be used to generate creative content such as stories, poems, essays, etc. Users can also add some notes to each prompt to provide more context or guidance.

## Features

- Users can browse their existing categories and subcategories of prompts, or create new ones.
- Users can select a subcategory and see the prompts that belong to it, or create a new one.
- Users can enter the name, prompt, and notes for each prompt.
- Users can view the details of each prompt, such as its name, text, and notes.
- Users can edit or delete the existing prompts, or save a new one.

## Technologies

- Backend: Python 3.11, Django 4.2, PostgreSQL 13
- Frontend: HTML, CSS, JS ES6+

## Installation

To run this project locally, you need to have Python 3, Django, and PostgreSQL installed on your system. Then follow these steps:

1. Navigate to the project directory and clone this repository to your local machine using `git clone https://github.com/v-s-dev/promptmanager.git`.
2. Create a virtual environment using `python -m venv venv` and activate the virtual environment using `source venv/bin/activate` on Linux or `venv\Scripts\activate` on Windows
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Create a PostgreSQL database and user for this project.
5. Set the environment variables `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, and `DATABASE_HOST` with the appropriate values.
6. Run `python manage.py migrate` to create the database tables.
7. Run `python manage.py runserver` to start the development server.
8. Visit `http://localhost:8000` to see the web application.

## Usage

To use this web application, follow these steps:

1. On the homepage, you will see a list of categories and a button to create a new category. You can select a category or create your own one by clicking the button and entering a name.
2. After selecting a category, you will see a list of subcategories and a button to create a new subcategory. You can select a subcategory or create your own one by clicking the button and entering a name.
3. After selecting a subcategory, you will see a list of prompts and a button to save a new prompt. You can select a prompt or create your own one by clicking the button and entering the details.
4. After selecting or creating a prompt, you will see its details on the screen. You can edit or delete the prompt by clicking the corresponding buttons.

## License

This project is licensed under the MIT License.
