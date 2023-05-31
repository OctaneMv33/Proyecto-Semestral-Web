$("#PnomId").keyup(function(){
    var caracteres = $("#PnomId").val();
    var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    var largo = $("#PnomId").val().length;
    if(largo < 3 || largo > 15){
        $("#PnombreId").text("El nombre no puede ser menor a 3 caractéres o mayor a 15.");
        var vnombre = false;
    }else if(!patronNombre.test(caracteres)){
        $("#PnombreId").text("Sólo puede ingresar letras");
        var vnombre = false;
    }else{
        $("#PnombreId").text("");
        var vnombre = false;
    }
    
});

$("#SnomId").keyup(function(){
    var caracteres = $("#SnomId").val();
    var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    var largo = $("#SnomId").val().length;
    if(largo < 3 || largo > 15){
        $("#SnombreId").text("El nombre no puede ser menor a 3 caractéres o mayor a 15.");
        var vnombre = false;
    }else if(!patronNombre.test(caracteres)){
        $("#SnombreId").text("Sólo puede ingresar letras");
        var vnombre = false;
    }else{
        $("#SnombreId").text("");
        var vnombre = false;
    }
    
});


$("#PapelId").keyup(function(){
    var caracteres = $("#PapelId").val();
    var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    var largo = $("#PapelId").val().length;
    if(largo < 3 || largo > 15){
        $("#PapellidoId").text("El apellido no puede ser menor a 3 caractéres o mayor a 15.");
        var vnombre = false;
    }else if(!patronNombre.test(caracteres)){
        $("#PapellidoId").text("Sólo puede ingresar letras");
        var vnombre = false;
    }else{
        $("#PapellidoId").text("");
        var vnombre = false;
    }
    
});


$("#SapelId").keyup(function(){
    var caracteres = $("#SapelId").val();
    var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    var largo = $("#SapelId").val().length;
    if(largo < 3 || largo > 15){
        $("#MapellidoId").text("El apellido no puede ser menor a 3 caractéres o mayor a 15.");
        var vnombre = false;
    }else if(!patronNombre.test(caracteres)){
        $("#MapellidoId").text("Sólo puede ingresar letras");
        var vnombre = false;
    }else{
        $("#MapellidoId").text("");
        var vnombre = false;
    }
    
});


$("#EmailId").keyup(function(){
    var patronCorreo = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
    var correo = $.trim($("#EmailId").val());
    if(correo === ""){
        $("#EId").text("Este campo no puede quedar vacío");
        
        email = false;
    }else if(!patronCorreo.test(correo)){
        $("#EId").text("Este campo no puede quedar vacío");
    
        email= false;
    }else{
        $("#EId").text("Ingreso Correcto");
       
        email = true;
    }

});

$("#TelId").keyup(function() {
    var telefono = $("#TelId").val();
    var regexNumeros = /^[0-9]+$/;
  
    if (!regexNumeros.test(telefono)) {
      $("#teleId").text("ingresa solo números");
      vtelefono = false;
    } else {
      var cantidad = telefono.length;
      if (cantidad < 3 || cantidad > 12) {
        $("#teleId").text("cantidad de caracteres inválida");
        vtelefono = false;
      } else {
        $("#teleId").text("BIEN, ingreso correctamente");
        vtelefono = true;
      }
    }
  });


  $(document).ready(function() {
    $('#passId').keyup(function() {
      var password = $('#passId').val();
      var confirmPassword = $('#confirmPasswordId').val();
  
      if (validatePassword(password)) {
        $('#passid').text('Contraseña válida.');
      } else {
        $('#passid').text('Contraseña inválida. Asegúrate de incluir al menos una letra mayúscula, dos números y un carácter especial.');
      }
  
      if (password === confirmPassword) {
        $('#confirmMessage').text('Las contraseñas coinciden.');
      } else {
        $('#confirmMessage').text('Las contraseñas no coinciden.');
      }
    });
  
    $('#RepId').keyup(function() {
      var password = $('#passId').val();
      var confirmPassword = $('#RepId').val();
  
      if (password === confirmPassword) {
        $('#repId').text('Las contraseñas coinciden.');
      } else {
        $('#repId').text('Las contraseñas no coinciden.');
      }
    });
  
    function validatePassword(password) {
      var passwordRegex = /^(?=.*[A-Z])(?=.*\d.*\d)(?=.*[$@#&!]).{8,}$/;
      return passwordRegex.test(password);
    }
  });
