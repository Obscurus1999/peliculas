from django.shortcuts import render, redirect

# Data que se envía a los templates
GENEROS_DATA = {
    'accion': {
        'nombre': 'Acción',
        'descripcion': 'Películas con secuencias de persecución, combate y gran dinamismo.',
        'peliculas': [
            {'nombre': 'Mad Max: Fury Road', 'edad': '16+', 'imagen': 'images/mad_max_fury_road.png'},
            {'nombre': 'John Wick', 'edad': '18+', 'imagen': 'images/john wick.png'},
            {'nombre': 'Top Gun: Maverick', 'edad': '13+', 'imagen': 'images/top_gun_maverick.png'},
        ]
    },
    'animacion': {
        'nombre': 'Animación',
        'descripcion': 'Historias ilustradas y animadas por computadora para toda la familia.',
        'peliculas': [
            {'nombre': 'Spider-Man: Into the Spider-Verse', 'edad': '7+', 'imagen': 'images/spiderman.png'},
            {'nombre': 'Toy Story', 'edad': 'Todos', 'imagen': 'images/toy story.png'},
            {'nombre': 'Coco', 'edad': 'Todos', 'imagen': 'images/coco.png'},
            {'nombre': 'Shrek', 'edad': 'Todos', 'imagen': 'images/shrek.png'},
        ]
    },
    'terror': {
            'nombre': 'Terror',
            'descripcion': 'Historias llenas de suspenso, misterio y situaciones escalofriantes.',
            'peliculas': [
                {'nombre': 'El conjuro', 'edad': '16+', 'imagen': 'images/el_conjuro.png'},
                {'nombre': 'Un Lugar en Silencio', 'edad': '13+', 'imagen': 'images/un_lugar_en_silencio.png'},
                {'nombre': 'IT (Eso)', 'edad': '16+', 'imagen': 'images/it.png'},
                {'nombre': 'Hereditary', 'edad': '18+', 'imagen': 'images/hereditary.png'},
                {'nombre': 'Scream', 'edad': '16+', 'imagen': 'images/scream.png'},
            ]
        }
}

def inicio(request):
    """Vista inicial: Muestra la lista de los links de géneros."""
    context = {'generos': GENEROS_DATA}
    return render(request, 'home_emmanuel/inicio.html', context)

def ver_peliculas(request, slug):
    """Vista secundaria: Muestra las películas del género seleccionado."""
    genero = GENEROS_DATA.get(slug)
    if not genero:
        return redirect('home:inicio')
    
    context = {'genero': genero}
    return render(request, 'home_emmanuel/peliculas.html', context)