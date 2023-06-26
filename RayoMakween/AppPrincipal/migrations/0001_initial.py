
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaTrabajo',
            fields=[
                ('id_categtrabajo', models.IntegerField(db_column='id_categtrabajo', primary_key=True, serialize=False)),
                ('nombre_categtrabajo', models.CharField(db_column='nombre_categtrabajo', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id_contacto', models.AutoField(db_column='id_contacto', primary_key=True, serialize=False)),
                ('correo', models.CharField(db_column='correo', max_length=100)),
                ('telefono', models.IntegerField(db_column='telefono')),
                ('descripcion', models.CharField(db_column='descripcion', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPublicacion',
            fields=[
                ('id_estpub', models.IntegerField(db_column='id_estpub', primary_key=True, serialize=False)),
                ('nombre_estpub', models.CharField(db_column='nombre_estpub', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id_material', models.AutoField(db_column='id_material', primary_key=True, serialize=False)),
                ('nombre_material', models.CharField(db_column='nombre_material', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id_publicacion', models.AutoField(db_column='id_publicacion', primary_key=True, serialize=False)),
                ('titulo_publicacion', models.CharField(db_column='titulo_publicacion', max_length=80)),
                ('diagnostico_publicacion', models.CharField(db_column='diagnostico_publicacion', max_length=500)),
                ('fecha_publicacion', models.DateField(db_column='fecha_publicacion')),
                ('descripcion_publicacion', models.CharField(db_column='descripcion_publicacion', max_length=1000)),
                ('foto1', models.ImageField(upload_to='foto_publicacion/')),
                ('foto2', models.ImageField(blank=True, null=True, upload_to='foto_publicacion/')),
                ('foto3', models.ImageField(blank=True, null=True, upload_to='foto_publicacion/')),
                ('foto4', models.ImageField(blank=True, null=True, upload_to='foto_publicacion/')),
                ('foto5', models.ImageField(blank=True, null=True, upload_to='foto_publicacion/')),
                ('foto6', models.ImageField(blank=True, null=True, upload_to='foto_publicacion/')),
                ('cant_rechaz', models.IntegerField(db_column='cantidad_rechazos')),
                ('motivo_rechazo', models.CharField(blank=True, db_column='motivo_rechazo', max_length=500, null=True)),
                ('id_categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.CASCADE, to='AppPrincipal.categoriatrabajo')),
                ('id_estpub', models.ForeignKey(db_column='id_estpub', on_delete=django.db.models.deletion.CASCADE, to='AppPrincipal.estadopublicacion')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('second_name', models.CharField(max_length=40, null=True)),
                ('second_last_name', models.CharField(max_length=40, null=True)),
                ('run', models.IntegerField(null=True)),
                ('dv_run', models.CharField(max_length=1)),
                ('phone', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PublicacionMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPrincipal.material')),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPrincipal.publicacion')),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
