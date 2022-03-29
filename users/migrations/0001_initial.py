# Generated by Django 4.0.3 on 2022-03-29 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('code', models.CharField(max_length=150, null=True)),
                ('name', models.CharField(max_length=150, null=True)),
                ('price_sale', models.DecimalField(decimal_places=4, max_digits=11)),
                ('stock', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('Condition', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('description', models.CharField(max_length=500)),
                ('Condition', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_voucher', models.CharField(max_length=300)),
                ('serial_voucher', models.CharField(max_length=500, null=True)),
                ('num_voucher', models.CharField(max_length=200, null=True)),
                ('date_hour', models.DateTimeField()),
                ('tax', models.DecimalField(decimal_places=2, max_digits=4)),
                ('total', models.DecimalField(decimal_places=2, max_digits=11)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_person', models.CharField(max_length=125, null=True)),
                ('name', models.CharField(max_length=150, null=True, unique=True)),
                ('type_id', models.CharField(max_length=100, null=True)),
                ('num_document', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=400, null=True)),
                ('email', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Nombre')),
                ('description', models.CharField(max_length=500)),
                ('Condition', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('users_id', models.IntegerField()),
                ('type_voucher', models.CharField(max_length=200, null=True)),
                ('serial_voucher', models.CharField(max_length=300, null=True)),
                ('mun_voucher', models.IntegerField(null=True)),
                ('date_hour', models.DateTimeField()),
                ('tax', models.DecimalField(decimal_places=2, max_digits=4)),
                ('total', models.DecimalField(decimal_places=2, max_digits=11)),
                ('state', models.CharField(max_length=100)),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.person')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_id', models.IntegerField()),
                ('first_names', models.CharField(max_length=255, unique=True, verbose_name='Nombres')),
                ('last_names', models.CharField(max_length=255, unique=True)),
                ('type_id', models.CharField(max_length=125)),
                ('num_document', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=300)),
                ('Password', models.CharField(max_length=10)),
                ('Condition', models.BooleanField()),
                ('Rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Sale_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_id', models.IntegerField()),
                ('article_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=11)),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.article')),
                ('Sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.sale')),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='Users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users'),
        ),
        migrations.CreateModel(
            name='Income_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.IntegerField(null=True)),
                ('article_id', models.IntegerField(null=True)),
                ('amont', models.IntegerField(null=True)),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.article')),
                ('Entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.entry')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='supplierid_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.person'),
        ),
        migrations.AddField(
            model_name='entry',
            name='users_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users'),
        ),
        migrations.AddField(
            model_name='article',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.category'),
        ),
    ]
