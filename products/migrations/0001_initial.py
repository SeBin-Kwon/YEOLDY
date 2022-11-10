from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
                ('category', models.CharField(choices=[('상의', '상의'), ('하의', '하의'), ('아우터', '아우터'), ('신발', '신발'), ('악세사리', '악세사리')], max_length=10)),
                ('color', multiselectfield.db.fields.MultiSelectField(choices=[('white', 'white'), ('black', 'black'), ('beige', 'beige'), ('khaki', 'khaki'), ('charcoal', 'charcoal'), ('gray', 'gray'), ('green', 'green'), ('yellow', 'yellow'), ('red', 'red'), ('pink', 'pink'), ('blue', 'blue')], max_length=64)),
                ('size', multiselectfield.db.fields.MultiSelectField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('FREE', 'FREE')], max_length=20)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('save_users', models.ManyToManyField(related_name='save_movies', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]