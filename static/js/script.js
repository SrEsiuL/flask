function guardar(){
    if (document.getElementById("name").value != ''){
            var _nom = document.getElementById("name").value;
            if (document.getElementById("goals").value != ''){
                var _age = document.getElementById("goals").value;
                if (document.getElementById("pg").value){
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
