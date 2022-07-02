const detalle = [
    {
      "Nombre": " Alimento Premium Dog ",
      "Precio": "30000",
      "Imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh5DqlGZGhemcW3EzHdzRDIP2wIeri2FT34A&usqp=CAU",
      "Fecha" : "13/5/2021"
    },  
    {
      "Nombre": " Alimento Premium Dog ",
      "Precio": "30000",
      "Imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh5DqlGZGhemcW3EzHdzRDIP2wIeri2FT34A&usqp=CAU",
      "Fecha" : "13/5/2021"
      },  
      {
      "Nombre": " Alimento Pets sin glúten  ",
      "Precio": "30000",
      "Imagen": "https://www.zaunk.com/wp-content/uploads/2022/04/thumb-facebook2.jpg",
      "Fecha" : "13/5/2021"
      },  
    {
      "Nombre": "Plato Doble Pets",
      "Precio": "13990",
      "Imagen": "https://fernapetcl.vtexassets.com/arquivos/ids/186280-800-auto?v=637715522886970000&width=800&height=auto&aspect=true",
      "Fecha" : "18/05/2021"
    },
    {
      "Nombre": "Mantita Pets   ",
      "Precio": "1200",
      "Imagen": "https://www.hogarmania.com/archivos/202011/mantitas-economicas-perros-gatos-6-XxXx80.jpg",
      "Fecha" : "18/05/2021"
      },

    {
      "Nombre": "Plato Doble Pets",
      "Precio": "13990",
      "Imagen": "https://fernapetcl.vtexassets.com/arquivos/ids/186280-800-auto?v=637715522886970000&width=800&height=auto&aspect=true",
      "Fecha" : "24/05/2021"
    },
    {
      "Nombre": "Plato Doble Pets",
      "Precio": "13990",
      "Imagen": "https://fernapetcl.vtexassets.com/arquivos/ids/186280-800-auto?v=637715522886970000&width=800&height=auto&aspect=true",
      "Fecha" : "24/05/2021"
      },
    {
      "Nombre": "Salsa Premium",
      "Precio": "1000 ",
      "Imagen": "https://www.almacendemascotas.cl/1024-home_default/three-dogs-carne-en-salsa-sachet-adulto-raza-med-grande-100g.jpg",
      "Fecha" : "24/05/2021"
    },

    {
      "Nombre": "Snack Pets",
      "Precio": "2000 ",
      "Imagen": "https://superpet.pe/blog/wp-content/uploads/2018/07/julio_BLOG_snacks-750x450.jpg",
      "Fecha" : "25/05/2021"
    },
    {
        "Nombre": "Guante Rascador Pets",
        "Precio": "6000 ",
        "Imagen": "https://angelsport.cl/Guante-de-aseo-para-gatos-de-goma-suave-pelo-de-las/pictures-2673_images/5.jpeg",
        "Fecha" : "01/06/2021"
      },
    {
      "Nombre": "Alimento Sabro Can Variedades ",
      "Precio": "45000   ",
      "Imagen": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1136803403.png?crop=1.00xw:0.752xh;0,0.0817xh&resize=1200:*",
      "Fecha" : "01/06/2021"
    },
    {
        "Nombre": "Banano Pets",
        "Precio": "20000",
        "Imagen": "https://http2.mlstatic.com/D_NQ_NP_735161-MLC42466610452_072020-O.jpg",
        "Fecha" : "01/06/2022"
      }
]


var texto_iterable=""

detalle.forEach((element) => {

    var tarjetita_html = `<div class="col">
    <div class="card" style="width: 18rem;">
        <img src="${element.Imagen}" class="card-img-top" alt="foto">
        <div class="card-body">
          <h5 class="card-title">${element.Nombre}</h5>
          <p class="card-text">Marca: ${element.Marca}</p>
          <p class="card-text">Precio: $${element.Precio}</p>
          <p class="card-text">Fecha venta: ${element.Fecha}</p>
        </div>
      </div>
    </div>`
    
    texto_iterable += tarjetita_html
    $("#productos").html( texto_iterable )
});