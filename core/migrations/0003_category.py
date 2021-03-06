# Generated by Django 3.0.3 on 2020-02-10 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_playlist_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('movies', models.ManyToManyField(to='core.Movie')),
            ],
            bases=('core.basemodel',),
        ),
    ]
