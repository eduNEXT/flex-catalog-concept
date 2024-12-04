# Generated by Django 4.2.16 on 2024-12-04 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flex_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicCatalog',
            fields=[
                ('flexiblecatalogmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='flex_catalog.flexiblecatalogmodel')),
                ('query_string', models.TextField(blank=True, help_text='Dynamic query string to filter course_runs.', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('flex_catalog.flexiblecatalogmodel',),
        ),
    ]
