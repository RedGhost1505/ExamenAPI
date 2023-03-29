from flask import Flask, render_template, jsonify, abort, request

#---------------------------------------------------
# Examen 2do parcial - Alex / Andrea 
# 27/03/2023
#---------------------------------------------------

uri='/api/videojuegos/'

app=Flask(__name__)

videojuegos=[{

        'id':1, 
        'titulo':'Super Mario Bros', 
        'desarrollador': 'Nintendo',
        'anio_lanzamiento': 1985,
        'plataforma':'Nintendo Entertainment',
        'clasificacion': 'E (Everyone)',
        'imagen':'https://www.google.com/url?sa=i&url=https%3A%2F%2Fhipertextual.com%2Ftag%2Fsuper-mario-bros&psig=AOvVaw0vKugVvqnT7rkh9JI9BG2m&ust=1680207069806000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLjapp75gf4CFQAAAAAdAAAAABAJ '
        }, 

        {
    
        'id':2, 
        'titulo':'The Legend of Zelda', 
        'desarrollador': 'Nintendo',
        'anio_lanzamiento': 1986,
        'plataforma':'Nintendo Entertainment',
        'clasificacion': 'E (Everyone)',
        'imagen':'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.nintendo.com%2Fes-mx%2Fstore%2Fproducts%2Fthe-legend-of-zelda-breath-of-the-wild-switch%2F&psig=AOvVaw2Nr50k2-5QhhdnN7Qdmad6&ust=1680207713599000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCJCEp9H7gf4CFQAAAAAdAAAAABAE'
        }, 

        {
        
        'id':3, 
        'titulo':'Halo', 
        'desarrollador': 'Bungie',
        'anio_lanzamiento': 2001,
        'plataforma':'Xbox',
        'clasificacion': 'B',
        'imagen':'https://i.blogs.es/72ace2/halo-infinite-3/840_560.jpeg'

    
        },


         {
        
        'id':4, 
        'titulo':'Cyberpunk', 
        'desarrollador': 'CD projekt RED',
        'anio_lanzamiento': 2020,
        'plataforma':'Varias',
        'clasificacion': 'B',
        'imagen':'https://image.api.playstation.com/vulcan/ap/rnd/202111/3013/cKZ4tKNFj9C00giTzYtH8PF1.png'
    
        },


        {
        
        'id':5, 
        'titulo':'Minecraft', 
        'desarrollador': 'Mojang Studios',
        'anio_lanzamiento': 2011,
        'plataforma':'Varias',
        'clasificacion': 'E (Everyone)',
        'imagen':'https://image.api.playstation.com/vulcan/img/cfn/11307uYG0CXzRuA9aryByTHYrQLFz-HVQ3VVl7aAysxK15HMpqjkAIcC_R5vdfZt52hAXQNHoYhSuoSq_46_MT_tDBcLu49I.png'
    
        },


        {
        
        'id':6, 
        'titulo':'Forza Horizon 5', 
        'desarrollador': 'Playground Games',
        'anio_lanzamiento': 2021,
        'plataforma':'Xbox',
        'clasificacion': 'E (Everyone)',
        'imagen':'https://media.vandal.net/m/11-2021/20211131553541_1.jpg'
    
        },
]

@app.route("/")
def hello_world():
    return "Bienvenido a nuestra API de videojuegos"

#GET

@app.route(uri, methods=['GET'])
def getVideogames():
    return jsonify({'videojuegos':videojuegos})


#GET 1 Videojuego

@app.route(uri + '<string:titulo>', methods=['GET'])
def get_task(id):
    
    game = [key for key in videojuegos if key['id']==id]
    if len(game)==0:
        abort(404)
    return jsonify({'Videojuego': game[0]})
   

#POST

@app.route(uri, methods =['POST'])
def create_videojuego():
    if not request.json:
        abort(404)

     
    videojuego = {
        'id': len(videojuegos)+1,
        'titulo': request.json['titulo'],
        'desarrollador': request.json['desarrollador'],
        'anio_lanzamiento': request.json['anio_lanzamiento'],
        'plataforma': request.json['plataforma'],
        'clasificacion': request.json['clasificacion']
    }

    videojuegos.append(videojuego)
    return jsonify({'videojuegos':videojuego}), 201


#UPDATE

@app.route(uri+'/<int:id>', methods= ['PUT'])
def update_juego(id):

    if request.json:
        this_game = [key for key in videojuegos if key['id'] == id]
        if len(this_game) == 0:
            abort(404)
        if not request.json:
            abort(404)
        if 'titulo' in request.json and type (request.json['titulo']) is not str:
            abort(400)
        if 'desarrollador' in request.json and type (request.json['desarrollador']) is not str:
            abort(400)
        if 'anio_lanzamiento' in request.json and type (request.json['anio_lanzamiento']) is not int:
            abort(400)
        if 'plataforma' in request.json and type (request.json['plataforma']) is not str:
            abort(400)
        if 'clasificacion' in request.json and type (request.json['clasificacion']) is not str:
            abort(400)


        this_game[0]['titulo'] = request.json.get ('titulo',this_game[0]['titulo'])
        this_game[0]['desarrollador']= request.json.get ('desarrollador',this_game[0]['desarrollador'])
        this_game[0]['anio_lanzamiento']= request.json.get ('anio_lanzamiento',this_game[0]['anio_lanzamiento'])
        this_game[0]['plataforma']= request.json.get ('plataforma',this_game[0]['plataforma'])
        this_game[0]['clasificacion']= request.json.get ('clasificacion',this_game[0]['clasificacion'])

        return jsonify ({'Game': this_game[0]}) 



#REMOVE

@app.route(uri+'/<int:id>', methods= ['DELETE'])
def delete_task(id):
    dele = [key for key in videojuegos if key['id']==id]
    if len(dele) == 0:
        abort(404)
    videojuegos.remove(dele[0])
    return jsonify({'result': True})


if __name__=='__main__':
    app.run(debug=True)


