// script.js
// Create a module for the prompt generator
const promptGenerator = (function () {
    // Define the private variables and functions
    let categories, subcategories, prompts;
    let categorySelect, subcategorySelect, promptSelect;
    let promptName, promptText, promptNotes;
    let createCategoryButton, createSubcategoryButton;
    let savePromptButton, deletePromptButton;

    // Fetch the categories from the backend and display them
    async function fetchCategories() {
        try {
            let response = await fetch('/promptpage/api/categories');
            let data = await response.json();
            categories = data;
            categorySelect.innerHTML = '<option value="">Select a category</option>';
            // Check if the data array is not empty
            if (data.length > 0) {
                // Loop over the data array and create option elements
                for (let category of data) {
                    let option = document.createElement('option');
                    option.textContent = category.name;
                    option.value = category.id;
                    categorySelect.appendChild(option);
                }
            } else {
                // Display a message that there are no categories available
                let option = document.createElement('option');
                option.textContent = 'No categories available';
                option.disabled = true;
                categorySelect.appendChild(option);
            }
        } catch (error) {
            // Handle the error here
            console.error(error);
            alert('Something went wrong while fetching the categories');
        }
    }


    // Fetch the subcategories of a given category and display them
    async function fetchSubcategories() {
        try {
            let category_id = categorySelect.value;
            let response = await fetch(`/promptpage/api/subcategories/${category_id}`);
            let data = await response.json();
            subcategories = data;
            subcategorySelect.innerHTML = '<option value="">Select a subcategory</option>';
            for (let subcategory of subcategories) {
                let option = document.createElement('option');
                option.textContent = subcategory.name;
                option.value = subcategory.id;
                subcategorySelect.appendChild(option);
            }
        } catch (error) {
            console.error(error);
        } finally {
            // Clear the prompts and prompt detail when changing the category
            prompts = null;
            promptSelect.innerHTML = '<option value="">Select a prompt</option>';
            clearPromptDetail();
        }
    }

    // Fetch the prompts of a given subcategory and display them
    async function fetchPrompts() {
        try {
            let subcategory_id = subcategorySelect.value;
            let response = await fetch(`/promptpage/api/prompts/${subcategory_id}`);
            let data = await response.json();
            prompts = data;
            promptSelect.innerHTML = '<option value="">Select a prompt</option>';
            for (let prompt of prompts) {
                let option = document.createElement('option');
                option.textContent = prompt.name;
                option.value = prompt.id;
                promptSelect.appendChild(option);
            }
        } catch (error) {
            console.error(error);
        } finally {
            // Clear the prompt detail when changing the subcategory
            clearPromptDetail();
        }
    }

    // Display the details of a given prompt in the input and textarea elements
    async function displayPromptDetail() {
        try {
            let prompt_id = promptSelect.value;
            if (prompt_id) {
                // Get the prompt details from the backend
                let response = await fetch(`/promptpage/api/prompt/${prompt_id}`);
                let data = await response.json();
                // Set the input and textarea values to the prompt details
                promptName.value = data.name;
                promptText.value = data.prompt;
                promptNotes.value = data.notes;
            } else {
                // Clear the input and textarea values
                clearPromptDetail();
            }
        } catch (error) {
            console.error(error);
        }
    }

    // Clear the input and textarea elements
    function clearPromptDetail() {
        promptName.value = '';
        promptText.value = '';
        promptNotes.value = '';
    }

    // Create a new category and add it to the database and the select element
    async function createCategory() {
        try {
            // Prompt the user to enter a category name
            let name = prompt('Enter a category name');
            if (name) {
                // Check if the category name already exists
                let existing = categories.find(category => category.name === name);
                if (existing) {
                    alert('This category already exists');
                } else {
                    // Send a post request to the backend with the category name
                    let response = await fetch('/promptpage/api/categories/create', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ name: name })
                    });
                    let data = await response.json();
                    // Add the new category to the categories array and the select element
                    categories.push(data);
                    let option = document.createElement('option');
                    option.textContent = data.name;
                    option.value = data.id;
                    option.selected = true;
                    categorySelect.appendChild(option);
                    // Fetch the subcategories for the new category
                    fetchSubcategories();
                }
            }
        } catch (error) {
            console.error(error);
        }
    }

    // Create a new subcategory and add it to the database and the select element
    async function createSubcategory() {
        try {
            // Check if a category is selected
            let category_id = categorySelect.value;
            if (category_id) {
                // Prompt the user to enter a subcategory name
                let name = prompt('Enter a subcategory name');
                if (name) {
                    // Check if the subcategory name already exists under the selected category
                    let existing = subcategories.find(subcategory => subcategory.name === name);
                    if (existing) {
                        alert('This subcategory already exists');
                    } else {
                        // Send a post request to the backend with the subcategory name and category id
                        let response = await fetch('/promptpage/api/subcategories', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ name: name, category: category_id })
                        });
                        let data = await response.json();
                        // Add the new subcategory to the subcategories array and the select element
                        subcategories.push(data);
                        let option = document.createElement('option');
                        option.textContent = data.name;
                        option.value = data.id;
                        option.selected = true;
                        subcategorySelect.appendChild(option);
                        // Fetch the prompts for the new subcategory
                        fetchPrompts();
                    }
                }
            } else {
                alert('Please select a category first');
            }
        } catch (error) {
            console.error(error);
        }
    }

    // Save or create a new prompt detail and update it in the database and the select element
    async function savePrompt() {
        try {
            // Get the input and textarea values
            let name = promptName.value;
            let text = promptText.value;
            let notes = promptNotes.value;
            // Check if a subcategory is selected
            let subcategory_id = subcategorySelect.value;
            if (subcategory_id) {
                // Check if a prompt is selected or a new one is being created
                let prompt_id = promptSelect.value;
                if (prompt_id) {
                    // Update an existing prompt in the database with a put request
                    let response = await fetch(`/promptpage/api/prompt/${prompt_id}`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ name: name, prompt: text, notes: notes })
                    });
                    let data = await response.json();
                    // Update the prompts array and the select element with the updated prompt details
                    let index = prompts.findIndex(prompt => prompt.id === data.id);
                    prompts[index] = data;
                    let option = promptSelect.querySelector(`option[value="${data.id}"]`);
                    option.textContent = data.name;
                } else {
                    // Create a new prompt in the database with a post request
                    let response = await fetch('/promptpage/api/prompts/save', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },

                        body: JSON.stringify({ name: name, prompt: text, notes: notes, subcategory: subcategory_id })
                    });
                    let data = await response.json();
                    // Add the new prompt to the prompts array and the select element 
                    prompts.push(data);
                    let option = document.createElement('option');
                    option.textContent = data.name;
                    option.value = data.id;
                    option.selected = true;
                    promptSelect.appendChild(option);
                }
                alert('Prompt saved successfully');
            } else { alert('Please select a subcategory first'); }
        }
        catch (error) { console.error(error); }
    }

    // Delete an existing prompt detail and remove it from the database and the select element
async function deletePrompt() {
    try {
        // Check if a prompt is selected
        let prompt_id = promptSelect.value;
        if (prompt_id) {
            // Confirm with the user before deleting the prompt
            let confirm = window.confirm('Are you sure you want to delete this prompt?');
            if (confirm) {
                // Delete the prompt from the database with a delete request
                // Pass the prompt id as a JSON object in the request body
                let response = await fetch(`/promptpage/api/prompt`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({id: prompt_id})
                });
                let data = await response.json();
                // Remove the prompt from the prompts array and the select element
                let index = prompts.findIndex(prompt => prompt.id === data.id);
                prompts.splice(index, 1);
                let option = promptSelect.querySelector(`option[value="${data.id}"]`);
                option.remove();
                // Clear the input and textarea values
                clearPromptDetail();
                alert('Prompt deleted successfully');
            }
        } else {
            alert('Please select a prompt first');
        }
    } catch (error) {
        console.error(error);
    }
}


    // Initialize the module by getting the DOM elements and adding event listeners
    function init() {
        categorySelect = document.getElementById('categories');
        subcategorySelect = document.getElementById('subcategories');
        promptSelect = document.getElementById('prompts');
        promptName = document.getElementById('prompt-name');
        promptText = document.getElementById('prompt-text');
        promptNotes = document.getElementById('prompt-notes');
        createCategoryButton = document.getElementById('create-category');
        createSubcategoryButton = document.getElementById('create-subcategory');
        savePromptButton = document.getElementById('save-prompt');
        deletePromptButton = document.getElementById('delete-prompt');

        categorySelect.addEventListener('change', fetchSubcategories);
        subcategorySelect.addEventListener('change', fetchPrompts);
        promptSelect.addEventListener('change', displayPromptDetail);
        createCategoryButton.addEventListener('click', createCategory);
        createSubcategoryButton.addEventListener('click', createSubcategory);
        savePromptButton.addEventListener('click', savePrompt);
        deletePromptButton.addEventListener('click', deletePrompt);

        fetchCategories();
    }

    // Return the public methods of the module
    return {
        init: init
    };
})();

// Call the init method of the module when the page loads 
window.addEventListener('load', promptGenerator.init);


