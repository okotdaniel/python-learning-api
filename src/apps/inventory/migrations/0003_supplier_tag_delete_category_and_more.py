# Generated by Django 5.1.6 on 2025-02-25 14:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_image_url_alter_product_product_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='bar_code',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_url',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='qr_code',
            new_name='warehouse_location',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='bundle_products',
            field=models.ManyToManyField(blank=True, related_name='bundles', to='inventory.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='inventory.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='cost_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(default='USD', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_returnable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_tax_included',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_variant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='lead_time',
            field=models.IntegerField(default=7, help_text='Lead time in days'),
        ),
        migrations.AddField(
            model_name='product',
            name='manual',
            field=models.FileField(blank=True, null=True, upload_to='product_manuals/'),
        ),
        migrations.AddField(
            model_name='product',
            name='parent_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variants', to='inventory.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='reorder_level',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_alert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_status',
            field=models.CharField(choices=[('in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock'), ('low_stock', 'Low Stock')], default='in_stock', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='tax_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='product_videos/'),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='inventory.supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='inventory.tag'),
        ),
    ]
