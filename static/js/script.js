function guardar(){
    if (document.getElementById("name").value != ''){
            var _nom = document.getElementById("name").value;
            if (document.getElementById("goals").value != ''){
                var _age = document.getElementById("goals").value;
                if (document.getElementById("pg").value){
                    var _mail = document.getElementById("pg").value;	
                    var fila="<tr><td>"+_nom+"</td><td>"+_age+"</td><td>"+_mail+"</td><td><input type='image' title='Ver' id='btn_mostrar' src='https://cdn.icon-icons.com/icons2/2406/PNG/512/eye_visible_hide_hidden_show_icon_145988.png' onclick='mostrar();' width='30' height='30'/><input type='image' title='Editar' id='btn_editar' src='https://cdn.icon-icons.com/icons2/1883/PNG/512/twocirclingarrows1_120592.png' onclick='actualizar();' width='30' height='30'/><input type='image' title='Eliminar' id='btn_eliminar' src='https://cdn.icon-icons.com/icons2/868/PNG/512/trash_bin_icon-icons.com_67981.png' onclick='eliminar();' width='30' height='30'/></td>";
                    var btn = document.createElement("TR");
                    btn.innerHTML=fila;
                    document.getElementById("tablita").appendChild(btn);
                    limpiar();
                }else{
                    alert('Llene todos los campos');
                }
            }else{
                alert('Llene todos los campos');
            }
        }else{
            alert('Llene todos los campos');
        }
    }
    function limpiar(){
        document.getElementById("name").value = "";
        document.getElementById("goals").value = "";
        document.getElementById("pg").value = "";
    }
    function eliminar(){
        alert("eliminar registro.")
    }
    function actualizar(){
        alert("actualizar registro.")
    }
    function mostrar(){
        alert("ver registro.")
    }
