import webbrowser

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Feliz Día de la Mujer</title>
    <style>
        body {
            background-color: #FFCCCB;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            max-width: 100%;
            overflow-x: hidden;
        }
        h1 {
            color: #FF69B4;
            font-size: 36px;
        }
        h2 {
            color: rgb(0, 0, 0);
            font-size: 20px;
        }
         h3 {
            color: rgb(0, 0, 0);
            font-size: 15px;
            margin: 20px 0; /* Agregar márgenes superior e inferior */
        }
        img {
            width: 20%; /* Incrementar el tamaño de la imagen */
            margin: 30px 0;
            height: auto;
            cursor: pointer;
            max-width: 100%;
        }
        .acrostic-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 30px;
            flex-wrap: wrap;
            gap: 0px; /* Eliminar espacio entre elementos */
        }
        .acrostic-image {
            margin: 100px; /* Reducir margen entre imágenes y acróstico */
        }
        .acrostic {
            margin: 100px; /* Reducir margen para acercar las imágenes */
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 50px;
            font-weight: bold;
            perspective: 1000px;
        }
        .acrostic span {
            margin: 10px 0;
            transform: rotateY(20deg); /* Efecto 3D */
            cursor: pointer;
        }
        .acrostic .letter {
            transform: perspective(500px) rotateY(30deg);
        }
        .letter-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 5px;
        }
        .letter-container .letter {
            font-size: 20px;
            font-weight: bold;
        }
        .letter-content {
            display: none;
            margin: 20px auto;
            text-align: left;
            font-size: 18px;
            max-width: 600px;
        }
        .letter-content img {
            display: block;
            margin: 20px auto;
            width: 50%;
        }
        .corner-image {
            position: fixed;
            width: 100px;
            height: 100px;
        }
        .top-left {
            top: 0;
            left: 0;
        }
        .top-right {
            top: 10px;
            right: 10px;
        }
        .bottom-left {
            bottom: 10px;
            left: 10px;
        }
        .bottom-right {
            bottom: 10px;
            right: 10px;
        }
        .back-button {
            position: fixed;
            top: 10px;
            left: 120px;
            padding: 10px 20px;
            background-color: #FF69B4;
            color: #FFF;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <audio autoplay loop>
        <source src="mi_archivo.mp3" type="audio/mpeg">
    </audio>
    <h1>❤Feliz Día de la Mujer❤</h1>
    <h3>🌹Le deseo lo mejor en su día, sublime y valiosa mujer. Mi querida y estimada brigadier Milenka. Quiero deserarle un excelente dia lleno de bendiciones.🌹</h3>
    <h3>🌹Es una mujer maravillosa y admirable, le agradezco a Dios por su vida y su existencia, no hay mujer que logre compararse con usted, es unica entre los casi 8000 millones de habitantes del mundo🌹
    <img src="https://depor.com/resizer/v2/24QD42JCZRGLPBT65CZFLAX7ZQ.jpg?auth=c559c5b5dc227a591a0408071e647de8c79da2b64e4dcf9d7bf3b4e59bf3183b&width=1200&height=900&quality=75&smart=true" alt="Imagen Principal" onclick="showAcrostic()">
    <h3>Porfavor, de click en la imagen que esta arriba para empezar👆👆.</h3>
    <h3>🥰Luego observe lo que aparece a continuación y de click en la letras y corazones en negrita para ver el contenido.🥰</h3>
    <h2>👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇 <h2>
    <div class="acrostic-container" id="acrostic-container" style="display: none;">
        <img src="https://i.pinimg.com/originals/d2/f7/90/d2f790978f11b5bb2f1ff38124a9a47a.gif" alt="Imagen 1" class="acrostic-image" style="width: 25%;">
        <div class="acrostic" id="acrostic">
            <div class="letter-container">
                <h2>🌹Dale click🌹</h2>
                <span class="letter" onclick="showLetter('M')">M - Maravillosa</span> 
                <span class="letter" onclick="showLetter('U')">U - Única </span> 
                <span class="letter" onclick="showLetter('J')">J - Joven</span> 
                <span class="letter" onclick="showLetter('E')">E - Especial</span> 
                <span class="letter" onclick="showLetter('R')">R - Radiante</span> 
                <span class="letter" onclick="showLetter('❤')">❤ - ❤❤❤</span> 
            </div>
        </div>
        <img src="mi_foto.jpg" alt="Imagen 2" class="acrostic-image" style="width: 20%;">
    </div>
    <div id="M" class="letter-content">
        <h2>🌹Carta con M🌹</h2>
         <h3>Maravillosa, una mujer que ilumina la vida de todos a su alrededor. Tu bondad y dedicación son ejemplos de amor y entrega. Eres alguien incomparable, y siempre estaré agradecido por todo lo que has hecho por nosotros.</h3>
        <img src="https://img.freepik.com/fotos-premium/doctora-gafas-esta-leyendo-libro_604472-21810.jpg" alt="Imagen M">
        <button class="back-button" onclick="hideLetter()">Regresar</button>
    </div>
    <div id="U" class="letter-content">
        <h2>🌹Carta con U🌹</h2>
         <h3>Única, en cada sentido de la palabra. Tu presencia deja una huella imborrable en quienes tienen la suerte de conocerte. Tu alegría y carisma son contagiosos, y tu belleza, tanto interior como exterior, es incomparable.</h3>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrCWJwuEHmsTIdxykRW48S1hyVaq5N9yTv2w&s" alt="Imagen U">
        <button class="back-button" onclick="hideLetter()">Regresar</button>
    </div>
    <div id="J" class="letter-content">
        <h2>🌹Carta con J🌹</h2>
         <h3>Joya en espíritu, cuerpo y alma. Tu juventud no se mide en años, sino en la pasión y el cariño que pones en todo lo que haces. Eres invaluable para todos los que te conocen, y estoy agradecido de tenerte en mi vida.</h3>
        <img src="https://img.freepik.com/vector-premium/mujer-joven-dibujos-animados-abrazando-corazon-rojo-gigante_74855-19951.jpg" alt="Imagen J">
        <button class="back-button" onclick="hideLetter()">Regresar</button>
    </div>
    <div id="E" class="letter-content">
        <h2>🌹Carta con E🌹</h2>
         <h3>Especial, esa es la palabra que mejor te describe. Tu alegría ilumina cualquier lugar, y tu sonrisa es capaz de alegrar el día de cualquiera. Siempre estaré aquí para apoyarte incondicionalmente.</h3>
        <img src="https://img.freepik.com/vector-premium/doctora-amable-gran-corazon-rojo-cuida-tu-corazon-diseno-concepto_36358-2359.jpg" alt="Imagen E">
        <button class="back-button" onclick="hideLetter()">Regresar</button>
    </div>
    <div id="R" class="letter-content">
        <h2>🌹Carta con R🌹</h2>
         <h3>Radiante, tu belleza es única y incomparable. No hay mujer más hermosa que tú, tanto por dentro como por fuera. Eres una persona muy valiosa y una gran mujer. Que tu día esté lleno de bendiciones.</h3>
        <img src="https://img1.picmix.com/output/stamp/normal/9/6/4/1/421469_22d3e.gif" alt="Imagen R">
        <button class="back-button" onclick="hideLetter()">Regresar</button>
    </div>
    <div id="❤" class="letter-content">
        <h2>💌Acrosticos💌</h2>
        <div style="display: flex; justify-content: center; align-items: center;">
            <div style="margin: 20px;">
                <p>💖M - Maravillosa como un amanecer💖</p>
                <p>💖U - Única en su ser💖</p>
                <p>💖J - Joven en su corazón💖</p>
                <p>💖E - Especial sin razón💖</p>
                <p>💖R - Radiante con su luz y pasión💖</p>
            </div>
            <div style="margin: 20px;">
                
                <p>💖M - Maravillosa en cada detalle💖</p>
                <p>💖I - Inteligente y llena de sabiduría💖</p>
                <p>💖L - Luminosa, siempre irradiando alegría💖</p>
                <p>💖E - Encantadora en su esencia💖</p>
                <p>💖N - Noble de corazón y espíritu💖</p>
                <p>💖K - Cariñosa, siempre atenta a los demás💖</p>
                <p>💖A - Admirable en cada aspecto de su vida💖</p>
            </div>
        </div>
        <img src="https://st3.depositphotos.com/7358190/14972/v/450/depositphotos_149726324-stock-illustration-we-can-do-it-woman.jpg" alt="Imagen ❤">
        <button class="back-button" onclick="hideLetter()">Regresar</button>
    </div>
    <img src="https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f493.gif" class="corner-image top-left">
    <img src="https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f493.gif" class="corner-image top-right">
    <img src="https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f493.gif" class="corner-image bottom-left">
    <img src="https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f493.gif" class="corner-image bottom-right">
    <script>
        function showAcrostic() {
            document.getElementById('acrostic-container').style.display = 'flex';
        }
        function showLetter(letter) {
            document.querySelectorAll('.letter-content').forEach(function(content) {
                content.style.display = 'none';
            });
            document.getElementById(letter).style.display = 'block';
        }
        function hideLetter() {
            document.querySelectorAll('.letter-content').forEach(function(content) {
                content.style.display = 'none';
            });
            document.getElementById('acrostic-container').style.display = 'flex';
        }
    </script>
</body>
</html>
"""

# Guardar el contenido HTML en un archivo
file_path = "feliz_dia_de_la_mujer.html"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

# Abrir el archivo HTML en el navegador web predeterminado
webbrowser.open(file_path)

print("El archivo HTML ha sido creado y abierto exitosamente en tu navegador.")
