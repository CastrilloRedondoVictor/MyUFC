from django.db import models
from bases.models import BaseModel


GUARDIA_CHOICES = [
        ('diestra', 'Diestra'),
        ('zurda', 'Zurda'),
]

PAISES_CHOICES = [
    ('afghanistan', 'Afganistán'),
    ('albania', 'Albania'),
    ('algeria', 'Argelia'),
    ('andorra', 'Andorra'),
    ('angola', 'Angola'),
    ('antigua_and_barbuda', 'Antigua y Barbuda'),
    ('argentina', 'Argentina'),
    ('armenia', 'Armenia'),
    ('australia', 'Australia'),
    ('austria', 'Austria'),
    ('azerbaijan', 'Azerbaiyán'),
    ('bahamas', 'Bahamas'),
    ('bahrain', 'Baréin'),
    ('bangladesh', 'Bangladesh'),
    ('barbados', 'Barbados'),
    ('belarus', 'Belarús'),
    ('belgium', 'Bélgica'),
    ('belize', 'Belice'),
    ('benin', 'Benin'),
    ('bhutan', 'Bután'),
    ('bolivia', 'Bolivia'),
    ('bosnia_and_herzegovina', 'Bosnia y Herzegovina'),
    ('botswana', 'Botswana'),
    ('brazil', 'Brasil'),
    ('brunei', 'Brunei'),
    ('bulgaria', 'Bulgaria'),
    ('burkina_faso', 'Burkina Faso'),
    ('burundi', 'Burundi'),
    ('cabo_verde', 'Cabo Verde'),
    ('cambodia', 'Camboya'),
    ('cameroon', 'Camerún'),
    ('canada', 'Canadá'),
    ('central_african_republic', 'República Centroafricana'),
    ('chad', 'Chad'),
    ('chile', 'Chile'),
    ('china', 'China'),
    ('colombia', 'Colombia'),
    ('comoros', 'Comoras'),
    ('congo', 'Congo'),
    ('costa_rica', 'Costa Rica'),
    ('cote_divoire', 'Costa de Marfil'),
    ('croatia', 'Croacia'),
    ('cuba', 'Cuba'),
    ('cyprus', 'Chipre'),
    ('czech_republic', 'República Checa'),
    ('denmark', 'Dinamarca'),
    ('djibouti', 'Yibuti'),
    ('dominica', 'Dominica'),
    ('dominican_republic', 'República Dominicana'),
    ('ecuador', 'Ecuador'),
    ('egypt', 'Egipto'),
    ('el_salvador', 'El Salvador'),
    ('equatorial_guinea', 'Guinea Ecuatorial'),
    ('eritrea', 'Eritrea'),
    ('estonia', 'Estonia'),
    ('eswatini', 'Eswatini'),
    ('ethiopia', 'Etiopía'),
    ('fiji', 'Fiji'),
    ('finland', 'Finlandia'),
    ('france', 'Francia'),
    ('gabon', 'Gabón'),
    ('gambia', 'Gambia'),
    ('georgia', 'Georgia'),
    ('germany', 'Alemania'),
    ('ghana', 'Ghana'),
    ('greece', 'Grecia'),
    ('grenada', 'Granada'),
    ('guatemala', 'Guatemala'),
    ('guinea', 'Guinea'),
    ('guinea-bissau', 'Guinea-Bisáu'),
    ('guyana', 'Guyana'),
    ('haiti', 'Haití'),
    ('honduras', 'Honduras'),
    ('hungary', 'Hungría'),
    ('iceland', 'Islandia'),
    ('india', 'India'),
    ('indonesia', 'Indonesia'),
    ('iran', 'Irán'),
    ('iraq', 'Irak'),
    ('ireland', 'Irlanda'),
    ('israel', 'Israel'),
    ('italy', 'Italia'),
    ('jamaica', 'Jamaica'),
    ('japan', 'Japón'),
    ('jordan', 'Jordania'),
    ('kazakhstan', 'Kazajistán'),
    ('kenya', 'Kenia'),
    ('kiribati', 'Kiribati'),
    ('kosovo', 'Kosovo'),
    ('kuwait', 'Kuwait'),
    ('kyrgyzstan', 'Kirguistán'),
    ('laos', 'Laos'),
    ('latvia', 'Letonia'),
    ('lebanon', 'Líbano'),
    ('lesotho', 'Lesoto'),
    ('liberia', 'Liberia'),
    ('libya', 'Libia'),
    ('liechtenstein', 'Liechtenstein'),
    ('lithuania', 'Lituania'),
    ('luxembourg', 'Luxemburgo'),
    ('madagascar', 'Madagascar'),
    ('malawi', 'Malaui'),
    ('malaysia', 'Malasia'),
    ('maldives', 'Maldivas'),
    ('mali', 'Mali'),
    ('malta', 'Malta'),
    ('marshall_islands', 'Islas Marshall'),
    ('mauritania', 'Mauritania'),
    ('mauritius', 'Mauricio'),
    ('mexico', 'México'),
    ('micronesia', 'Micronesia'),
    ('moldova', 'Moldavia'),
    ('monaco', 'Mónaco'),
    ('mongolia', 'Mongolia'),
    ('montenegro', 'Montenegro'),
    ('morocco', 'Marruecos'),
    ('mozambique', 'Mozambique'),
    ('myanmar', 'Myanmar (Birmania)'),
    ('namibia', 'Namibia'),
    ('nauru', 'Nauru'),
    ('nepal', 'Nepal'),
    ('netherlands', 'Países Bajos'),
    ('new_zealand', 'Nueva Zelanda'),
    ('nicaragua', 'Nicaragua'),
    ('niger', 'Níger'),
    ('nigeria', 'Nigeria'),
    ('north_korea', 'Corea del Norte'),
    ('north_macedonia', 'Macedonia del Norte'),
    ('norway', 'Noruega'),
    ('oman', 'Omán'),
    ('pakistan', 'Pakistán'),
    ('palau', 'Palaos'),
    ('panama', 'Panamá'),
    ('papua_new_guinea', 'Papúa Nueva Guinea'),
    ('paraguay', 'Paraguay'),
    ('peru', 'Perú'),
    ('philippines', 'Filipinas'),
    ('poland', 'Polonia'),
    ('portugal', 'Portugal'),
    ('qatar', 'Catar'),
    ('romania', 'Rumania'),
    ('russia', 'Rusia'),
    ('rwanda', 'Ruanda'),
    ('monaco', 'Mónaco'),
    ('mongolia', 'Mongolia'),
    ('montenegro', 'Montenegro'),
    ('morocco', 'Marruecos'),
    ('mozambique', 'Mozambique'),
    ('myanmar', 'Myanmar'),
    ('namibia', 'Namibia'),
    ('nauru', 'Nauru'),
    ('nepal', 'Nepal'),
    ('netherlands', 'Países Bajos'),
    ('new_zealand', 'Nueva Zelanda'),
    ('nicaragua', 'Nicaragua'),
    ('niger', 'Níger'),
    ('nigeria', 'Nigeria'),
    ('north_korea', 'Corea del Norte'),
    ('north_macedonia', 'Macedonia del Norte'),
    ('norway', 'Noruega'),
    ('oman', 'Omán'),
    ('pakistan', 'Pakistán'),
    ('palau', 'Palaos'),
    ('panama', 'Panamá'),
    ('papua_new_guinea', 'Papúa Nueva Guinea'),
    ('paraguay', 'Paraguay'),
    ('peru', 'Perú'),
    ('philippines', 'Filipinas'),
    ('poland', 'Polonia'),
    ('portugal', 'Portugal'),
    ('qatar', 'Catar'),
    ('romania', 'Rumania'),
    ('russia', 'Rusia'),
    ('rwanda', 'Ruanda'),
    ('saint_kitts_and_nevis', 'San Cristóbal y Nieves'),
    ('saint_lucia', 'Santa Lucía'),
    ('saint_vincent_and_the_grenadines', 'San Vicente y las Granadinas'),
    ('samoa', 'Samoa'),
    ('san_marino', 'San Marino'),
    ('sao_tome_and_principe', 'Santo Tomé y Príncipe'),
    ('saudi_arabia', 'Arabia Saudita'),
    ('senegal', 'Senegal'),
    ('serbia', 'Serbia'),
    ('seychelles', 'Seychelles'),
    ('sierra_leone', 'Sierra Leona'),
    ('singapore', 'Singapur'),
    ('slovakia', 'Eslovaquia'),
    ('slovenia', 'Eslovenia'),
    ('solomon_islands', 'Islas Salomón'),
    ('somalia', 'Somalia'),
    ('south_africa', 'Sudáfrica'),
    ('south_korea', 'Corea del Sur'),
    ('south_sudan', 'Sudán del Sur'),
    ('spain', 'España'),
    ('sri_lanka', 'Sri Lanka'),
    ('sudan', 'Sudán'),
    ('suriname', 'Surinam'),
    ('sweden', 'Suecia'),
    ('switzerland', 'Suiza'),
    ('syria', 'Siria'),
    ('taiwan', 'Taiwán'),
    ('tajikistan', 'Tayikistán'),
    ('tanzania', 'Tanzania'),
    ('thailand', 'Tailandia'),
    ('timor-leste', 'Timor Oriental'),
    ('togo', 'Togo'),
    ('tonga', 'Tonga'),
    ('trinidad_and_tobago', 'Trinidad y Tobago'),
    ('tunisia', 'Túnez'),
    ('turkey', 'Turquía'),
    ('turkmenistan', 'Turkmenistán'),
    ('tuvalu', 'Tuvalu'),
    ('uganda', 'Uganda'),
    ('ukraine', 'Ucrania'),
    ('united_arab_emirates', 'Emiratos Árabes Unidos'),
    ('united_kingdom', 'Reino Unido'),
    ('united_states', 'Estados Unidos'),
    ('uruguay', 'Uruguay'),
    ('uzbekistan', 'Uzbekistán'),
    ('vanuatu', 'Vanuatu'),
    ('vatican_city', 'Ciudad del Vaticano'),
    ('venezuela', 'Venezuela'),
    ('vietnam', 'Vietnam'),
    ('yemen', 'Yemen'),
    ('zambia', 'Zambia'),
    ('zimbabwe', 'Zimbabue')
]

PAISES = {
'afghanistan': 'Afganistán',
'albania': 'Albania',
'algeria': 'Argelia',
'andorra': 'Andorra',
'angola': 'Angola',
'antigua_and_barbuda': 'Antigua y Barbuda',
'argentina': 'Argentina',
'armenia': 'Armenia',
'australia': 'Australia',
'austria': 'Austria',
'azerbaijan': 'Azerbaiyán',
'bahamas': 'Bahamas',
'bahrain': 'Baréin',
'bangladesh': 'Bangladesh',
'barbados': 'Barbados',
'belarus': 'Belarús',
'belgium': 'Bélgica',
'belize': 'Belice',
'benin': 'Benin',
'bhutan': 'Bután',
'bolivia': 'Bolivia',
'bosnia_and_herzegovina': 'Bosnia y Herzegovina',
'botswana': 'Botswana',
'brazil': 'Brasil',
'brunei': 'Brunei',
'bulgaria': 'Bulgaria',
'burkina_faso': 'Burkina Faso',
'burundi': 'Burundi',
'cabo_verde': 'Cabo Verde',
'cambodia': 'Camboya',
'cameroon': 'Camerún',
'canada': 'Canadá',
'central_african_republic': 'República Centroafricana',
'chad': 'Chad',
'chile': 'Chile',
'china': 'China',
'colombia': 'Colombia',
'comoros': 'Comoras',
'congo': 'Congo',
'costa_rica': 'Costa Rica',
'cote_divoire': 'Costa de Marfil',
'croatia': 'Croacia',
'cuba': 'Cuba',
'cyprus': 'Chipre',
'czech_republic': 'República Checa',
'denmark': 'Dinamarca',
'djibouti': 'Yibuti',
'dominica': 'Dominica',
'dominican_republic': 'República Dominicana',
'ecuador': 'Ecuador',
'egypt': 'Egipto',
'el_salvador': 'El Salvador',
'equatorial_guinea': 'Guinea Ecuatorial',
'eritrea': 'Eritrea',
'estonia': 'Estonia',
'eswatini': 'Eswatini',
'ethiopia': 'Etiopía',
'fiji': 'Fiji',
'finland': 'Finlandia',
'france': 'Francia',
'gabon': 'Gabón',
'gambia': 'Gambia',
'georgia': 'Georgia',
'germany': 'Alemania',
'ghana': 'Ghana',
'greece': 'Grecia',
'grenada': 'Granada',
'guatemala': 'Guatemala',
'guinea': 'Guinea',
'guinea_bissau': 'Guinea-Bissau',
'guyana': 'Guyana',
'haiti': 'Haití',
'honduras': 'Honduras',
'hungary': 'Hungría',
'iceland': 'Islandia',
'india': 'India',
'indonesia': 'Indonesia',
'iran': 'Irán',
'iraq': 'Irak',
'ireland': 'Irlanda',
'israel': 'Israel',
'italy': 'Italia',
'jamaica': 'Jamaica',
'japan': 'Japón',
'jordan': 'Jordania',
'kazakhstan': 'Kazajistán',
'kenya': 'Kenia',
'kiribati': 'Kiribati',
'kosovo': 'Kosovo',
'kuwait': 'Kuwait',
'kyrgyzstan': 'Kirguistán',
'laos': 'Laos',
'latvia': 'Letonia',
'lebanon': 'Líbano',
'lesotho': 'Lesotho',
'liberia': 'Liberia',
'libya': 'Libia',
'liechtenstein': 'Liechtenstein',
'lithuania': 'Lituania',
'luxembourg': 'Luxemburgo',
'madagascar': 'Madagascar',
'malawi': 'Malawi',
'malaysia': 'Malasia',
'maldives': 'Maldivas',
'mali': 'Mali',
'malta': 'Malta',
'marshall_islands': 'Islas Marshall',
'mauritania': 'Mauritania',
'mauritius': 'Mauricio',
'mexico': 'México',
'micronesia': 'Micronesia',
'moldova': 'Moldavia',
'monaco': 'Mónaco',
'mongolia': 'Mongolia',
'montenegro': 'Montenegro',
'morocco': 'Marruecos',
'mozambique': 'Mozambique',
'myanmar': 'Myanmar',
'namibia': 'Namibia',
'nauru': 'Nauru',
'nepal': 'Nepal',
'netherlands': 'Países Bajos',
'new_zealand': 'Nueva Zelanda',
'nicaragua': 'Nicaragua',
'niger': 'Níger',
'nigeria': 'Nigeria',
'north_korea': 'Corea del Norte',
'north_macedonia': 'Macedonia del Norte',
'norway': 'Noruega',
'oman': 'Omán',
'pakistan': 'Pakistán',
'palau': 'Palau',
'panama': 'Panamá',
'papua_new_guinea': 'Papúa Nueva Guinea',
'paraguay': 'Paraguay',
'peru': 'Perú',
'philippines': 'Filipinas',
'poland': 'Polonia',
'portugal': 'Portugal',
'qatar': 'Catar',
'rwanda': 'Ruanda',
'mongolia': 'Mongolia',
'monaco': 'Mónaco',
'montenegro': 'Montenegro',
'morocco': 'Marruecos',
'mozambique': 'Mozambique',
'myanmar': 'Myanmar',
'namibia': 'Namibia',
'nauru': 'Nauru',
'nepal': 'Nepal',
'netherlands': 'Países Bajos',
'new_zealand': 'Nueva Zelanda',
'nicaragua': 'Nicaragua',
'niger': 'Níger',
'nigeria': 'Nigeria',
'north_korea': 'Corea del Norte',
'north_macedonia': 'Macedonia del Norte',
'norway': 'Noruega',
'oman': 'Omán',
'pakistan': 'Pakistán',
'palau': 'Palau',
'panama': 'Panamá',
'papua_new_guinea': 'Papúa Nueva Guinea',
'paraguay': 'Paraguay',
'peru': 'Perú',
'philippines': 'Filipinas',
'poland': 'Polonia',
'portugal': 'Portugal',
'qatar': 'Catar',
'romania': 'Rumanía',
'russia': 'Rusia',
'rwanda': 'Ruanda',
'saint_kitts_and_nevis': 'San Cristóbal y Nieves',
'saint_lucia': 'Santa Lucía',
'saint_vincent_and_the_grenadines': 'San Vicente y las Granadinas',
'samoa': 'Samoa',
'san_marino': 'San Marino',
'sao_tome_and_principe': 'Santo Tomé y Príncipe',
'saudi_arabia': 'Arabia Saudita',
'senegal': 'Senegal',
'serbia': 'Serbia',
'seychelles': 'Seychelles',
'sierra_leone': 'Sierra Leona',
'singapore': 'Singapur',
'slovakia': 'Eslovaquia',
'slovenia': 'Eslovenia',
'solomon_islands': 'Islas Salomón',
'somalia': 'Somalia',
'south_africa': 'Sudáfrica',
'south_korea': 'Corea del Sur',
'south_sudan': 'Sudán del Sur',
'spain': 'España',
'sri_lanka': 'Sri Lanka',
'sudan': 'Sudán',
'suriname': 'Surinam',
'sweden': 'Suecia',
'switzerland': 'Suiza',
'syria': 'Siria',
'taiwan': 'Taiwán',
'tajikistan': 'Tayikistán',
'tanzania': 'Tanzania',
'thailand': 'Tailandia',
'timor_leste': 'Timor Oriental',
'togo': 'Togo',
'tonga': 'Tonga',
'trinidad_and_tobago': 'Trinidad y Tobago',
'tunisia': 'Túnez',
'turkey': 'Turquía',
'turkmenistan': 'Turkmenistán',
'tuvalu': 'Tuvalu',
'uganda': 'Uganda',
'ukraine': 'Ucrania',
'united_arab_emirates': 'Emiratos Árabes Unidos',
'united_kingdom': 'Reino Unido',
'united_states': 'Estados Unidos',
'uruguay': 'Uruguay',
'uzbekistan': 'Uzbekistán',
'vanuatu': 'Vanuatu',
'vatican_city': 'Ciudad del Vaticano',
'venezuela': 'Venezuela',
'vietnam': 'Vietnam',
'yemen': 'Yemen',
'zambia': 'Zambia',
'zimbabwe': 'Zimbabue'
}

# Create your models here.

class Luchador(BaseModel):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    pais = models.CharField(choices=PAISES_CHOICES, default='spain')
    guardia = models.CharField(choices=GUARDIA_CHOICES)
    alcance = models.DecimalField(max_digits=4, decimal_places=2)
    empates = models.PositiveIntegerField(null=True, blank=True, default=0)
    victorias = models.PositiveIntegerField(null=True, blank=True, default=0)
    derrotas = models.PositiveIntegerField(null=True, blank=True, default=0)
    nacimiento = models.DateField()
    edad = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_totales = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_acertados = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_fallados = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_recibidos = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_encajados = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_evitados = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
    

