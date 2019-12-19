const btnsLista = document.querySelectorAll('button.lista');
const btnsProducto = document.querySelectorAll('button.producto');

function activarLista(btn) {
    // console.log(JSON.parse(btn.dataset.list));
    console.log(btn);
    // localStorage.setItem('lista-activa', lista);
}


btnsLista.forEach( function(btn) {
    btn.addEventListener("click", function(e) {
        var id = e.toElement.dataset.id;
        // var pk = e.toElement.dataset.id;
        // var lista = JSON.parse(e.toElement.dataset);      
        // lista['id'] = id;
        // console.log(list);
        // localStorage.setItem('lista-activa', JSON.stringify(lista));
        localStorage.setItem('lista', id);
    });
});

btnsProducto.forEach( function(btn) {
    btn.addEventListener("click", function(e) {
        id = e.toElement.dataset.id;
        producto = JSON.parse(e.toElement.dataset.list)[id-1].fields;
        // console.log(id); console.log(producto);
        // localStorage.setItem('lista-activa', JSON.stringify(producto));
        // console.log(lista);
        lista = JSON.parse(localStorage.getItem('lista-activa'));
        productos = lista.productos;
        productos.push(producto);
        lista.productos = productos
        console.log(lista);
    });
});

