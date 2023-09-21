from django.test import TestCase

from promptpage.models import Category, SubCategory, Prompt


# Create your tests here.
class CategoryModelTest(TestCase):
    # Set up the test data
    @classmethod
    def setUpTestData(cls):
        # Create a category object
        Category.objects.create(name='Fiction')

    # Test the name field
    def test_name_field(self):
        # Get the category object
        category = Category.objects.get(id=1)
        # Get the name field label
        field_label = category._meta.get_field('name').verbose_name
        # Assert that the label is equal to 'name'
        self.assertEqual(field_label, 'name')

    # Test the name field max length
    def test_name_max_length(self):
        # Get the category object
        category = Category.objects.get(id=1)
        # Get the max length of the name field
        max_length = category._meta.get_field('name').max_length
        # Assert that the max length is equal to 100
        self.assertEqual(max_length, 100)

    # Test the string representation of the category object
    def test_object_name_is_name(self):
        # Get the category object
        category = Category.objects.get(id=1)
        # Assert that the string representation is equal to its name
        self.assertEqual(str(category), category.name)


class SubCategoryModelTest(TestCase):
    # Set up the test data
    @classmethod
    def setUpTestData(cls):
        # Create a category object
        category = Category.objects.create(name='Fiction')
        # Create a subcategory object under that category
        SubCategory.objects.create(name='Fantasy', category=category)

    # Test the name field
    def test_name_field(self):
        # Get the subcategory object
        subcategory = SubCategory.objects.get(id=1)
        # Get the name field label
        field_label = subcategory._meta.get_field('name').verbose_name
        # Assert that the label is equal to 'name'
        self.assertEqual(field_label, 'name')

    # Test the name field max length
    def test_name_max_length(self):
        # Get the subcategory object
        subcategory = SubCategory.objects.get(id=1)
        # Get the max length of the name field
        max_length = subcategory._meta.get_field('name').max_length
        # Assert that the max length is equal to 100
        self.assertEqual(max_length, 100)

    # Test the category field
    def test_category_field(self):
        # Get the subcategory object
        subcategory = SubCategory.objects.get(id=1)
        # Get the category field label
        field_label = subcategory._meta.get_field('category').verbose_name
        # Assert that the label is equal to 'category'
        self.assertEqual(field_label, 'category')

    # Test the string representation of the subcategory object
    def test_object_name_is_name(self):
        # Get the subcategory object
        subcategory = SubCategory.objects.get(id=1)
        # Assert that the string representation is equal to its name
        self.assertEqual(str(subcategory), subcategory.name)

class PromptModelTest(TestCase):
    # Set up the test data
    @classmethod
    def setUpTestData(cls):
        # Create a category object
        category = Category.objects.create(name='Fiction')
        # Create a subcategory object under that category
        subcategory = SubCategory.objects.create(name='Fantasy', category=category)
        # Create a prompt object under that subcategory
        Prompt.objects.create(name='A dragon and a knight', prompt='Write a story about a dragon and a knight who become friends.', notes='The story should be set in a medieval fantasy world.', subcategory=subcategory)

    # Test the name field
    def test_name_field(self):
        # Get the prompt object
        prompt = Prompt.objects.get(id=1)
        # Get the name field label
        field_label = prompt._meta.get_field('name').verbose_name
        # Assert that the label is equal to 'name'
        self.assertEqual(field_label, 'name')

    # Test the name field max length
    def test_name_max_length(self):
        # Get the prompt object
        prompt = Prompt.objects.get(id=1)
        # Get the max length of the name field
        max_length = prompt._meta.get_field('name').max_length
        # Assert that the max length is equal to 100
        self.assertEqual(max_length, 100)

    # Test the prompt field
    def test_prompt_field(self):
        # Get the prompt object
        prompt = Prompt.objects.get(id=1)
        # Get the prompt field label
        field_label = prompt._meta.get_field('prompt').verbose_name
        # Assert that the label is equal to 'prompt'
        self.assertEqual(field_label, 'prompt')

    # Test the notes field
    def test_notes_field(self):
        # Get the prompt object
        prompt = Prompt.objects.get(id=1)
        # Get the notes field label
        field_label = prompt._meta.get_field('notes').verbose_name
        # Assert that the label is equal to 'notes'
        self.assertEqual(field_label, 'notes')

    # Test the subcategory field
    def test_subcategory_field(self):
        # Get the prompt object
        prompt = Prompt.objects.get(id=1)
        # Get the subcategory field label
        field_label = prompt._meta.get_field('subcategory').verbose_name
        # Assert that the label is equal to 'subcategory'
        self.assertEqual(field_label, 'subcategory')

    # Test the string representation of the prompt object
    def test_object_name_is_name(self):
        # Get the prompt object
        prompt = Prompt.objects.get(id=1)
        # Assert that the string representation is equal to its name
        self.assertEqual(str(prompt), prompt.name)
