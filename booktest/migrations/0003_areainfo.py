# Generated by Django 2.0.3 on 2018-11-03 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20181102_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booktest.AreaInfo')),
            ],
        ),
    ]