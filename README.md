# promptmanager

I'm glad you have added your project to GitHub. Here is a possible README file content for your project:

# Prompt Generator

This is a web application that allows users to store and organise their prompts for various categories and subcategories. A prompt is a text that can be used to generate creative content such as stories, poems, essays, etc. Users can also add notes to their prompts for further reference.

## Features

- Users can create categories and subcategories for their prompts.
- Users can enter the name, prompt, and notes for each prompt.
- Users can view the prompts by selecting a category and a subcategory.

## Technologies

- Backend: Django, PostgreSQL
- Frontend: HTML, CSS, JS ES 6+

## Installation

To run this project locally, you need to have Python 3, pip, and PostgreSQL installed on your system. Then follow these steps:

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Create a PostgreSQL database and user for this project.
5. Set the environment variables `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, and `DATABASE_HOST` with the appropriate values.
6. Run `python manage.py migrate` to create the database tables.
7. Run `python manage.py runserver` to start the development server.
8. Visit `http://localhost:8000` to see the web application.

## Usage

To use this web application, follow these steps:

1. On the home page, you will see a list of categories. Click on any category card to see the subcategories under it.
2. On the subcategory page, you will see a list of subcategories. Click on any subcategory item to see the prompts under it.
3. On the prompt page, you will see a list of prompts. Click on any prompt item to see the prompt detail in a modal window.
4. To create a new category, click on the `Create Category` button on the home page. Enter the name of the category and click on `Submit`.
5. To create a new subcategory, click on the `Create Subcategory` button on the subcategory page. Select the category from the dropdown menu, enter the name of the subcategory, and click on `Submit`.
6. To create a new prompt, click on the `Create Prompt` button on the prompt page. Select the subcategory from the dropdown menu, enter the name, prompt, and notes of the prompt, and click on `Submit`.

## License

This project is licensed under the MIT License.
