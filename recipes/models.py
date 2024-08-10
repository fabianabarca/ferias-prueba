from django.db import models
from django.utils.text import slugify
from products.models import Variety


class AllergyType(models.TextChoices):
    GLUTEN = "gluten", "Gluten"
    DAIRY = "dairy", "Lácteos"
    EGG = "egg", "Huevo"
    NUTS = "nuts", "Nueces"
    SOYA = (
        "soy",
        "Soya",
    )
    FISH = "fish", "Pescado"


class Ingredient(models.Model):
    """
    Data model: https://schema.org/recipeIngredient
    """

    ingredient_name = models.CharField(max_length=100, unique=True)
    ingredient_description = models.TextField(blank=True, null=True)
    # TODO: Evaluar cómo vincular con variedades de productos.
    ingredient_product = models.ForeignKey(Variety, blank=True, null=True, on_delete=models.SET_NULL)
    # Si no tenemos algún producto, puede quedar blank. Si sí está, vincular con el existente.
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    # allergies = models.CharField(max_length=100, blank=True, null=True, choices=AllergyType.choices)
    
    is_gluten_free = models.BooleanField(default=False)
    is_dairy_free = models.BooleanField(default=False)
    is_nut_free = models.BooleanField(default=False)
    is_soy_free = models.BooleanField(default=False)
    

    def __str__(self):
        return self.ingredient_name


class Category(models.Model):
    """
    Recipe category. Examples: breakfast, lunch, dinner, dessert.
    Data model: https://schema.org/category
    """

    category_name = models.CharField(max_length=100, unique=True)
    category_description = models.TextField(blank=True, null=True)
    category_slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    """
    Keywords or tags for recipes. Examples: vegan, gluten-free, low-carb.
    Data model: https://schema.org/DefinedTerm
    """

    tag_name = models.CharField(max_length=50, unique=True)
    tag_slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.tag_slug:
            self.tag_slug = slugify(self.tag_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag_name


class Recipe(models.Model):
    """
    Data model: https://schema.org/Recipe
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    # TODO: image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """
    Data model: https://schema.org/recipeIngredient
    """

    UNIT_CHOICES = [
        ("g", "gramos"),
        ("kg", "kilogramos"),
        ("ml", "mililitros"),
        ("l", "litros"),
        ("tsp", "cucharadita"),
        ("tbsp", "cucharada"),
        ("cup", "taza"),
        ("unit", "unidad"),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, default="unit")
    # TODO: Que la cantidad mínima sea 0 y no pueda ser negativa.
    quantity = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        unique_together = ("recipe", "ingredient")

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.name} for {self.recipe.name}"


class Step(models.Model):
    """
    Data model: https://schema.org/HowToStep
    """

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_sequence = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="steps/", blank=True, null=True)

    class Meta:
        ordering = ["step_sequence"]

    def __str__(self):
        return f"Step {self.step_sequence} for {self.recipe.name}"
