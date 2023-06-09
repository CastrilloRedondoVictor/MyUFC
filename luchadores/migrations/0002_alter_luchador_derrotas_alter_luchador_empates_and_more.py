# Generated by Django 4.2 on 2023-05-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luchadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luchador',
            name='derrotas',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='luchador',
            name='empates',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='luchador',
            name='guardia',
            field=models.CharField(choices=[('diestra', 'Diestra'), ('zurda', 'Zurda')]),
        ),
        migrations.AlterField(
            model_name='luchador',
            name='pais',
            field=models.CharField(choices=[('afghanistan', 'Afganistán'), ('albania', 'Albania'), ('algeria', 'Argelia'), ('andorra', 'Andorra'), ('angola', 'Angola'), ('antigua_and_barbuda', 'Antigua y Barbuda'), ('argentina', 'Argentina'), ('armenia', 'Armenia'), ('australia', 'Australia'), ('austria', 'Austria'), ('azerbaijan', 'Azerbaiyán'), ('bahamas', 'Bahamas'), ('bahrain', 'Baréin'), ('bangladesh', 'Bangladesh'), ('barbados', 'Barbados'), ('belarus', 'Belarús'), ('belgium', 'Bélgica'), ('belize', 'Belice'), ('benin', 'Benin'), ('bhutan', 'Bután'), ('bolivia', 'Bolivia'), ('bosnia_and_herzegovina', 'Bosnia y Herzegovina'), ('botswana', 'Botswana'), ('brazil', 'Brasil'), ('brunei', 'Brunei'), ('bulgaria', 'Bulgaria'), ('burkina_faso', 'Burkina Faso'), ('burundi', 'Burundi'), ('cabo_verde', 'Cabo Verde'), ('cambodia', 'Camboya'), ('cameroon', 'Camerún'), ('canada', 'Canadá'), ('central_african_republic', 'República Centroafricana'), ('chad', 'Chad'), ('chile', 'Chile'), ('china', 'China'), ('colombia', 'Colombia'), ('comoros', 'Comoras'), ('congo', 'Congo'), ('costa_rica', 'Costa Rica'), ('cote_divoire', 'Costa de Marfil'), ('croatia', 'Croacia'), ('cuba', 'Cuba'), ('cyprus', 'Chipre'), ('czech_republic', 'República Checa'), ('denmark', 'Dinamarca'), ('djibouti', 'Yibuti'), ('dominica', 'Dominica'), ('dominican_republic', 'República Dominicana'), ('ecuador', 'Ecuador'), ('egypt', 'Egipto'), ('el_salvador', 'El Salvador'), ('equatorial_guinea', 'Guinea Ecuatorial'), ('eritrea', 'Eritrea'), ('estonia', 'Estonia'), ('eswatini', 'Eswatini'), ('ethiopia', 'Etiopía'), ('fiji', 'Fiji'), ('finland', 'Finlandia'), ('france', 'Francia'), ('gabon', 'Gabón'), ('gambia', 'Gambia'), ('georgia', 'Georgia'), ('germany', 'Alemania'), ('ghana', 'Ghana'), ('greece', 'Grecia'), ('grenada', 'Granada'), ('guatemala', 'Guatemala'), ('guinea', 'Guinea'), ('guinea-bissau', 'Guinea-Bisáu'), ('guyana', 'Guyana'), ('haiti', 'Haití'), ('honduras', 'Honduras'), ('hungary', 'Hungría'), ('iceland', 'Islandia'), ('india', 'India'), ('indonesia', 'Indonesia'), ('iran', 'Irán'), ('iraq', 'Irak'), ('ireland', 'Irlanda'), ('israel', 'Israel'), ('italy', 'Italia'), ('jamaica', 'Jamaica'), ('japan', 'Japón'), ('jordan', 'Jordania'), ('kazakhstan', 'Kazajistán'), ('kenya', 'Kenia'), ('kiribati', 'Kiribati'), ('kosovo', 'Kosovo'), ('kuwait', 'Kuwait'), ('kyrgyzstan', 'Kirguistán'), ('laos', 'Laos'), ('latvia', 'Letonia'), ('lebanon', 'Líbano'), ('lesotho', 'Lesoto'), ('liberia', 'Liberia'), ('libya', 'Libia'), ('liechtenstein', 'Liechtenstein'), ('lithuania', 'Lituania'), ('luxembourg', 'Luxemburgo'), ('madagascar', 'Madagascar'), ('malawi', 'Malaui'), ('malaysia', 'Malasia'), ('maldives', 'Maldivas'), ('mali', 'Mali'), ('malta', 'Malta'), ('marshall_islands', 'Islas Marshall'), ('mauritania', 'Mauritania'), ('mauritius', 'Mauricio'), ('mexico', 'México'), ('micronesia', 'Micronesia'), ('moldova', 'Moldavia'), ('monaco', 'Mónaco'), ('mongolia', 'Mongolia'), ('montenegro', 'Montenegro'), ('morocco', 'Marruecos'), ('mozambique', 'Mozambique'), ('myanmar', 'Myanmar (Birmania)'), ('namibia', 'Namibia'), ('nauru', 'Nauru'), ('nepal', 'Nepal'), ('netherlands', 'Países Bajos'), ('new_zealand', 'Nueva Zelanda'), ('nicaragua', 'Nicaragua'), ('niger', 'Níger'), ('nigeria', 'Nigeria'), ('north_korea', 'Corea del Norte'), ('north_macedonia', 'Macedonia del Norte'), ('norway', 'Noruega'), ('oman', 'Omán'), ('pakistan', 'Pakistán'), ('palau', 'Palaos'), ('panama', 'Panamá'), ('papua_new_guinea', 'Papúa Nueva Guinea'), ('paraguay', 'Paraguay'), ('peru', 'Perú'), ('philippines', 'Filipinas'), ('poland', 'Polonia'), ('portugal', 'Portugal'), ('qatar', 'Catar'), ('romania', 'Rumania'), ('russia', 'Rusia'), ('rwanda', 'Ruanda'), ('monaco', 'Mónaco'), ('mongolia', 'Mongolia'), ('montenegro', 'Montenegro'), ('morocco', 'Marruecos'), ('mozambique', 'Mozambique'), ('myanmar', 'Myanmar'), ('namibia', 'Namibia'), ('nauru', 'Nauru'), ('nepal', 'Nepal'), ('netherlands', 'Países Bajos'), ('new_zealand', 'Nueva Zelanda'), ('nicaragua', 'Nicaragua'), ('niger', 'Níger'), ('nigeria', 'Nigeria'), ('north_korea', 'Corea del Norte'), ('north_macedonia', 'Macedonia del Norte'), ('norway', 'Noruega'), ('oman', 'Omán'), ('pakistan', 'Pakistán'), ('palau', 'Palaos'), ('panama', 'Panamá'), ('papua_new_guinea', 'Papúa Nueva Guinea'), ('paraguay', 'Paraguay'), ('peru', 'Perú'), ('philippines', 'Filipinas'), ('poland', 'Polonia'), ('portugal', 'Portugal'), ('qatar', 'Catar'), ('romania', 'Rumania'), ('russia', 'Rusia'), ('rwanda', 'Ruanda'), ('saint_kitts_and_nevis', 'San Cristóbal y Nieves'), ('saint_lucia', 'Santa Lucía'), ('saint_vincent_and_the_grenadines', 'San Vicente y las Granadinas'), ('samoa', 'Samoa'), ('san_marino', 'San Marino'), ('sao_tome_and_principe', 'Santo Tomé y Príncipe'), ('saudi_arabia', 'Arabia Saudita'), ('senegal', 'Senegal'), ('serbia', 'Serbia'), ('seychelles', 'Seychelles'), ('sierra_leone', 'Sierra Leona'), ('singapore', 'Singapur'), ('slovakia', 'Eslovaquia'), ('slovenia', 'Eslovenia'), ('solomon_islands', 'Islas Salomón'), ('somalia', 'Somalia'), ('south_africa', 'Sudáfrica'), ('south_korea', 'Corea del Sur'), ('south_sudan', 'Sudán del Sur'), ('spain', 'España'), ('sri_lanka', 'Sri Lanka'), ('sudan', 'Sudán'), ('suriname', 'Surinam'), ('sweden', 'Suecia'), ('switzerland', 'Suiza'), ('syria', 'Siria'), ('taiwan', 'Taiwán'), ('tajikistan', 'Tayikistán'), ('tanzania', 'Tanzania'), ('thailand', 'Tailandia'), ('timor-leste', 'Timor Oriental'), ('togo', 'Togo'), ('tonga', 'Tonga'), ('trinidad_and_tobago', 'Trinidad y Tobago'), ('tunisia', 'Túnez'), ('turkey', 'Turquía'), ('turkmenistan', 'Turkmenistán'), ('tuvalu', 'Tuvalu'), ('uganda', 'Uganda'), ('ukraine', 'Ucrania'), ('united_arab_emirates', 'Emiratos Árabes Unidos'), ('united_kingdom', 'Reino Unido'), ('united_states', 'Estados Unidos'), ('uruguay', 'Uruguay'), ('uzbekistan', 'Uzbekistán'), ('vanuatu', 'Vanuatu'), ('vatican_city', 'Ciudad del Vaticano'), ('venezuela', 'Venezuela'), ('vietnam', 'Vietnam'), ('yemen', 'Yemen'), ('zambia', 'Zambia'), ('zimbabwe', 'Zimbabue')], default='spain'),
        ),
        migrations.AlterField(
            model_name='luchador',
            name='victorias',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
