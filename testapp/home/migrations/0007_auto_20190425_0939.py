# Generated by Django 2.1.8 on 2019-04-25 09:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailnhsukfrontend.forms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_formpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='body',
            field=wagtail.core.fields.StreamField([('form', wagtail.core.blocks.StructBlock([('form_fields', wagtail.core.blocks.StreamBlock([('text_input', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=True)), ('hint', wagtail.core.blocks.CharBlock(required=False)), ('name', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'Valid characters: A-Z, a-z, 0-9, - and _'}, regex='^[A-Za-z0-9-_]+$', required=False)), ('required', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('disabled', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('validator', wagtail.core.blocks.CharBlock(required=False)), ('missing_field_error_message', wagtail.core.blocks.CharBlock(default='This field is required', required=False)), ('validation_error_message', wagtail.core.blocks.CharBlock(default='Validation error', required=False)), ('width', wagtail.core.blocks.ChoiceBlock(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('10', '10'), ('20', '20')], required=False))])), ('select', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=True)), ('hint', wagtail.core.blocks.CharBlock(required=False)), ('name', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'Valid characters: A-Z, a-z, 0-9, - and _'}, regex='^[A-Za-z0-9-_]+$', required=False)), ('required', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('disabled', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('validator', wagtail.core.blocks.CharBlock(required=False)), ('missing_field_error_message', wagtail.core.blocks.CharBlock(default='This field is required', required=False)), ('validation_error_message', wagtail.core.blocks.CharBlock(default='Validation error', required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.forms.blocks.FormFieldChoiceBlock, required=True))])), ('textarea', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=True)), ('hint', wagtail.core.blocks.CharBlock(required=False)), ('name', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'Valid characters: A-Z, a-z, 0-9, - and _'}, regex='^[A-Za-z0-9-_]+$', required=False)), ('required', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('disabled', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('validator', wagtail.core.blocks.CharBlock(required=False)), ('missing_field_error_message', wagtail.core.blocks.CharBlock(default='This field is required', required=False)), ('validation_error_message', wagtail.core.blocks.CharBlock(default='Validation error', required=False)), ('rows', wagtail.core.blocks.IntegerBlock(default=5, min_value=1, required=False))])), ('checkbox', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=True)), ('hint', wagtail.core.blocks.CharBlock(required=False)), ('name', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'Valid characters: A-Z, a-z, 0-9, - and _'}, regex='^[A-Za-z0-9-_]+$', required=False)), ('required', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('disabled', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('validator', wagtail.core.blocks.CharBlock(required=False)), ('missing_field_error_message', wagtail.core.blocks.CharBlock(default='This field is required', required=False)), ('validation_error_message', wagtail.core.blocks.CharBlock(default='Validation error', required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.forms.blocks.FormFieldChoiceBlock, required=True))])), ('radio', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=True)), ('hint', wagtail.core.blocks.CharBlock(required=False)), ('name', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'Valid characters: A-Z, a-z, 0-9, - and _'}, regex='^[A-Za-z0-9-_]+$', required=False)), ('required', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('disabled', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('validator', wagtail.core.blocks.CharBlock(required=False)), ('missing_field_error_message', wagtail.core.blocks.CharBlock(default='This field is required', required=False)), ('validation_error_message', wagtail.core.blocks.CharBlock(default='Validation error', required=False)), ('choices', wagtail.core.blocks.StreamBlock([('choice_groups', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(required=True)), ('value', wagtail.core.blocks.CharBlock(required=True))])))])), ('inline', wagtail.core.blocks.BooleanBlock(required=False))]))]))])), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='external URL', required=True))]))], default=[]),
        ),
    ]