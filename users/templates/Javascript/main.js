//obtener contenedor de los usuarios
const contenedorUsuarios = document.getElementById('contenedor-usuarios');
const URL ="https://jsonplaceholder.typicode.com/users"
//solicitud GET a la API
axios.get(URL)
    .then(response=>{
        const usuarios = response.data;
//generar HTML para cada usuario
    const htmlUsuarios = usuarios.map(usuario =>{
        return`
        <tr> class="usuarios">
        <td>${usuario.name}</td>
        <td>Teléfono:${usuario.phone}</td>
        </tr>
        `;
    }).join('');
//insertar el HTML en el contenedor
contenedorUsuarios.innerHTML = htmlUsuarios;
    })

    .catch(error =>{
        console.error('error',error);
    });