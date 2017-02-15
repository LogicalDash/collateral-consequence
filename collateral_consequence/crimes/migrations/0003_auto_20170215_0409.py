# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 04:09
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crimes', '0002_auto_20170215_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consequence',
            name='consequence_cat',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('---', 'Choose a Category'), ('edu', 'Education'), ('family', 'Family/domestic rights'), ('govnt_bens', 'Government benefits'), ('govnt_contract', 'Government contracting and program participation'), ('govnt_loans', 'Government loans and grants'), ('housing', 'Housing'), ('jobs', 'Employment'), ('judicial', 'Judicial Rights'), ('prof_lic', 'Occupational and professional license and certification'), ('relief', 'General Relief Provision'), ('registration_lims', 'Registration, notification, and residency restrictions'), ('rec_weapons_lic', 'Recreational license, including firearms'), ('business_lic', 'Business license and other property rights'), ('driving_lic', 'Motor vehicle licensure'), ('voting', 'Political and civic participation')], default='---', max_length=255),
        ),
        migrations.AlterField(
            model_name='consequence',
            name='consequence_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('---', 'Choose some consequence types'), ('bkg', 'Background Check'), ('disc', 'Discretionary'), ('waiv', 'Discretionary (waiver)'), ('auto', 'Mandatory/Automatic')], default='---', max_length=255),
        ),
        migrations.AlterField(
            model_name='consequence',
            name='offense_cat',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('---', 'Choose a Category'), ('corruption', 'Public corruption offense'), ('misdem', 'Any misdemeanor'), ('moral', 'Crime of moral turpitude'), ('child_supp', 'Child Support offense'), ('driving', 'Motor vehicle offense'), ('drugs', 'Controlled substances offense'), ('sex', 'Sex offense'), ('violence', 'Crime of violence'), ('rec_license', 'Recreational license offense'), ('fraud', 'Crime involving fraud'), ('any', 'Any offense (including felony, misdemeanor, and lesser offense)'), ('felony', 'Any felony'), ('weapons', 'Weapons offense'), ('misc', 'Other')], default='---', max_length=255),
        ),
    ]
