function DeleteCategoria()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-categoria/"+id)
    })
}
function DeleteUnidad()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_unidad").setAttribute("href","/eliminar-unidad/"+id)
    })
}
function DeleteMaterial()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_materiales").setAttribute("href","/eliminar-materiales/"+id)
    })
}
function DeleteIngreso()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-ingreso/"+id)
    })
}
function DeleteStock()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-stock/"+id)
    })
}
function DeleteCategoria()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-categoria/"+id)
    })
}
function DeleteTipos()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_tipos").setAttribute("href","/eliminar-tipos/"+id)
    })
}
function DeleteSalida()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_salida").setAttribute("href","/eliminar-salida/"+id)
    })
}

function DeleteEmpleado()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-empleado/"+id)
    })
}

function DeleteUser()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-usuario/"+id)
    })
}