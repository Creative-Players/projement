# Generated by Django 4.2.2 on 2023-07-25 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_alter_company_id_alter_project_id_alter_tag_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="actual_design",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=6,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999.99),
                ],
                verbose_name="Actual design hours",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="actual_development",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=6,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999.99),
                ],
                verbose_name="Actual development hours",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="actual_testing",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=6,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999.99),
                ],
                verbose_name="Actual testing hours",
            ),
        ),
    ]
