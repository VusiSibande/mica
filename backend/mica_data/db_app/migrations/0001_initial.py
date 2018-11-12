# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-12 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LevyComponets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex_water', models.FloatField()),
                ('complex_power', models.FloatField()),
                ('reserve_fund', models.FloatField()),
                ('csos_levy', models.FloatField()),
                ('regular_insurance', models.FloatField()),
                ('fidelity_insurance', models.FloatField()),
                ('admin_salary', models.FloatField()),
                ('admin_stationary', models.FloatField()),
                ('bank_charges', models.FloatField()),
                ('audit', models.FloatField()),
                ('landscaping', models.FloatField()),
                ('water_reader', models.FloatField()),
                ('firequip', models.FloatField()),
                ('fy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_app.FinancialYear')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('water_reading', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('cell_number', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('id_number_one', models.CharField(blank=True, max_length=14, null=True)),
                ('id_number_two', models.CharField(blank=True, max_length=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unitID', models.IntegerField(primary_key=True, serialize=False)),
                ('square_meters', models.FloatField(blank=True, null=True)),
                ('title_deed', models.CharField(blank=True, max_length=12, null=True)),
                ('registation_date', models.DateField(blank=True, null=True)),
                ('purchase_price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='unit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='db_app.Unit'),
        ),
        migrations.AddField(
            model_name='monthlywater',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_app.Unit'),
        ),
        migrations.AddField(
            model_name='levycomponets',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_app.Unit'),
        ),
        migrations.AlterUniqueTogether(
            name='financialyear',
            unique_together=set([('start', 'end')]),
        ),
    ]