from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from catalog.models import Author, Book


class AuthorCreationForm(UserCreationForm):
    class Meta:
        model = Author
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "psedonimo",)


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Book
        fields = "__all__"


class BookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Pesquisar por título"})
    )