from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', models.FileField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])])),
                ('tag', multiselectfield.db.fields.MultiSelectField(choices=[('캐주얼룩', '캐주얼룩'), ('데이트룩', '데이트룩'), ('포멀룩', '포멀룩'), ('스트릿룩', '스트릿룩'), ('걸리쉬룩', '걸리쉬룩')], max_length=23)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
