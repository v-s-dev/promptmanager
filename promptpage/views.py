# views.py
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Category, SubCategory, Prompt
import json

def index(request):
    return render(request, 'promptpage/index.html')

# Get all the categories as a list of dictionaries
@csrf_exempt
def get_categories(request):
    categories = Category.objects.all()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(data, safe=False)

# Get all the subcategories of a given category as a list of dictionaries
@csrf_exempt
def get_subcategories(request, category_id):
    subcategories = SubCategory.objects.filter(category_id=category_id)
    data = [{'id': subcategory.id, 'name': subcategory.name} for subcategory in subcategories]
    return JsonResponse(data, safe=False)

# Get all the prompts of a given subcategory as a list of dictionaries
@csrf_exempt
def get_prompts(request, subcategory_id):
    prompts = Prompt.objects.filter(subcategory_id=subcategory_id)
    data = [{'id': prompt.id, 'name': prompt.name} for prompt in prompts]
    return JsonResponse(data, safe=False)

# Get the details of a given prompt as a dictionary
@csrf_exempt
def get_prompt(request, prompt_id):
    prompt = Prompt.objects.get(id=prompt_id)
    data = {'id': prompt.id, 'name': prompt.name, 'prompt': prompt.prompt, 'notes': prompt.notes}
    return JsonResponse(data)

# Create a new category and return it as a dictionary
@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        print('name: ', name)
        category = Category.objects.create(name=name)
        data = {'id': category.id, 'name': category.name}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'})

# Create a new subcategory and return it as a dictionary
@csrf_exempt
def create_subcategory(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        print('name: ', name)
        category_id = payload['category']
        print('category: ', category_id)
        subcategory = SubCategory.objects.create(name=name, category_id=category_id)
        data = {'id': subcategory.id, 'name': subcategory.name}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'})

# Save or create a new prompt and return it as a dictionary
@csrf_exempt
def save_prompt(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        text = payload['prompt']
        notes = payload['notes']
        subcategory_id = payload['subcategory']
        # Check if the prompt id is provided or not
        if 'id' in payload:
            prompt_id = payload['id']
        else:
            prompt_id = None
        
        if prompt_id:
            # Update an existing prompt with the given id
            prompt = Prompt.objects.get(id=prompt_id)
            prompt.name = name
            prompt.prompt = text
            prompt.notes = notes
            prompt.save()
            data = {'id': prompt.id, 'name': prompt.name, 'prompt': prompt.prompt, 'notes': prompt.notes}
            return JsonResponse(data)
        else:
            # Create a new prompt with the given details
            prompt = Prompt.objects.create(name=name, prompt=text, notes=notes, subcategory_id=subcategory_id)
            data = {'id': prompt.id, 'name': prompt.name, 'prompt': prompt.prompt, 'notes': prompt.notes}
            return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'})

# Delete an existing prompt and return it as a dictionary
@csrf_exempt
def delete_prompt(request):
    if request.method == 'DELETE':
        # Get the prompt id from the request body
        body = json.loads(request.body)
        prompt_id = body.get('id')
        if prompt_id:
            # Delete the prompt with the given id
            prompt = Prompt.objects.get(id=prompt_id)
            data = {'id': prompt.id, 'name': prompt.name, 'prompt': prompt.prompt, 'notes': prompt.notes}
            prompt.delete()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Missing id parameter'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
