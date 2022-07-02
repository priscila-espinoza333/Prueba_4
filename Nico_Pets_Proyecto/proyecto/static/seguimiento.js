var ordenes= [
    {nombre:"Alimento Premium Dog " , estado:"Enviado", clase:"estadoVerde", imagen: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh5DqlGZGhemcW3EzHdzRDIP2wIeri2FT34A&usqp=CAU"},
    {nombre:"Mordedor Pets" , estado:"En ruta",clase:"estadoAzul", imagen: "https://m.media-amazon.com/images/I/91ev6M-vNxL._AC_UL320_.jpg"},
    {nombre:"Alimento Pets sin glúten " , estado:"Entregado",clase:"estadoPurpura", imagen: "https://www.zaunk.com/wp-content/uploads/2022/04/thumb-facebook2.jpg"},
  ]
  
  
  var acomulador_texto=""
  
  ordenes.forEach((element, index) => {
  
      var html_producto = `
      <tr>
        <th scope="row">${index}</th>
        <td>  <img src="${element.imagen} class="card-img-top" alt="imagen" width="50" height="50">  ${element.nombre}</td>
        <td class="${element.clase}">${element.estado}</td>
      </tr>`
      
      acomulador_texto += html_producto
      $("#seguimiento").html( acomulador_texto )
  });

  