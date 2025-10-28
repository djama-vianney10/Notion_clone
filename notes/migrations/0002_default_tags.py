from django.db import migrations

def create_default_tags(apps, schema_editor):
    Tag = apps.get_model('notes', 'Tag')
    default_tags = ['Personnel', 'Travail', 'Urgent', 'Important', 'Projet']
    for tag_name in default_tags:
        Tag.objects.get_or_create(name=tag_name)

def remove_default_tags(apps, schema_editor):
    Tag = apps.get_model('notes', 'Tag')
    Tag.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_tags, remove_default_tags),
    ]