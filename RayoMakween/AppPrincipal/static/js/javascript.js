var vnombre = false, vsnombre = true, vappaterno = false, vapmaterno = true, vmail = false, vrut = false, vtelefono = false, vpass = false, vcpass = false

$(document).ready(function(){
  $("#btnRegistrarId").attr('disabled', true)
});

/*validar rut*/
$("#rutId, #dvrutId").keyup(function() {
  var rut = $("#rutId").val().replace(/\./g, '');
  var dv = $("#dvrutId").val();
  
  if (rut.length < 7) {
    $("#idrut").text("Ingrese un RUT válido");
    $("#idrut").css("color", "white");
    vrut = false;
  } else if (dv.length == 0) {
    $("#idrut").text("Ingrese un dígito verificador");
    $("#idrut").css("color", "white");
    vrut = false;
  } else {
    var suma = 0;
    var multiplo = 2;
    for (var i = rut.length - 1; i >= 0; i--) {
      suma += rut.charAt(i) * multiplo;
      if (multiplo < 7) {
        multiplo += 1;
      } else {
        multiplo = 2;
      }
    }
    var dvEsperado = 11 - (suma % 11);
    dv = (dv == 'K') ? 10 : dv;
    dv = (dv == 0) ? 11 : dv;
    if (dvEsperado != dv) {
      $("#idrut").text("RUT inválido");
      $("#idrut").css("color", "white");
      vrut = false;
    } else {
      $("#idrut").text("RUT válido");
      vrut = true;
    }
  }

  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar P nombre*/
$("#PnomId").keyup(function(){
  var caracteres = $("#PnomId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#PnomId").val().length;
  
  if(largo < 3 || largo > 15){
      $("#PnombreId").text("El nombre no puede ser menor a 3 caractéres o mayor a 15.");
      vnombre = false;
  }else if(!patronNombre.test(caracteres)){
      $("#PnombreId").text("Sólo puede ingresar letras");
      vnombre = false;
  }else{
      $("#PnombreId").text("Ingreso correcto");
      vnombre = true;
  }
  
  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar S nombre*/
$("#SnomId").keyup(function(){
  var caracteres = $("#SnomId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#SnomId").val().length;
  if(largo == 0){
    $("#SnombreId").text("No ingresará nada");
    vsnombre = true;
  }else if(largo < 3 || largo > 15){
      $("#SnombreId").text("El nombre no puede ser menor a 3 caractéres o mayor a 15.");
      vsnombre = false;
  }else if(!patronNombre.test(caracteres)){
      $("#SnombreId").text("Sólo puede ingresar letras");
      vsnombre = false;
  }else{
      $("#SnombreId").text("Ingreso correcto");
      vsnombre = true;
  }
  
  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar P apellido*/
$("#PapelId").keyup(function(){
  var caracteres = $("#PapelId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#PapelId").val().length;
  if(largo < 3 || largo > 15){
      $("#PapellidoId").text("El apellido no puede ser menor a 3 caractéres o mayor a 15.");
      vappaterno = false;
  }else if(!patronNombre.test(caracteres)){
      $("#PapellidoId").text("Sólo puede ingresar letras");
      vappaterno = false;
  }else{
      $("#PapellidoId").text("Ingreso correcto");
      vappaterno = true;
  }
  
  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar S apellido*/
$("#SapelId").keyup(function(){
  var caracteres = $("#SapelId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#SapelId").val().length;
  if(largo == 0){
    $("#MappellidoId").text("No ingresará nada.");
    vapmaterno = true;
  }else if(largo < 3 || largo > 15){
      $("#MappellidoId").text("El apellido no puede ser menor a 3 caractéres o mayor a 15.");
      vapmaterno = false;
  }else if(!patronNombre.test(caracteres)){
      $("#MappellidoId").text("Sólo puede ingresar letras");
      vapmaterno = false;
  }else{
      $("#MappellidoId").text("Ingreso correcto");
      vapmaterno = true;
  }
  
  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar Email*/
$("#EmailId").keyup(function(){
  var patronCorreo = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
  var correo = $.trim($("#EmailId").val());
  if(correo === ""){
      $("#EId").text("Este campo no puede quedar vacío");
      vmail = false;
  }else if(!patronCorreo.test(correo)){
      $("#EId").text("Formato de correo electrónico incorrecto");
      vmail = false;
  }else{
      $("#EId").text("Ingreso Correcto");
      vmail = true;
  }

  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar telefono*/
$("#TelId").keyup(function() {
  var telefono = $("#TelId").val();
  var regexNumeros = /^[0-9]+$/;

  if (!regexNumeros.test(telefono)) {
    $("#teleId").text("Ingresa solo números");
    vtelefono = false;
  } else {
    if (telefono < 900000000 || telefono > 999999999) {
      $("#teleId").text("Número inválido");
      vtelefono = false;
    } else {
      $("#teleId").text("Ingreso correcto");
      vtelefono = true;
    }
  }

  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});


/*validar contraseña*/
$("#passId").keyup(function(){
  var password = $("#passId").val();
  var patronpass = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]+$/;
  var largopass = $("#passId").val().length;

  if(largopass < 8){
    $("#passid").text("Contraseña muy corta. Al menos 8 caractéres.")
    vpass = false;
  }else if(!patronpass.test(password)){
    $("#passid").text("Contraseña inválida. Asegúrate de incluir al menos una letra mayúscula, dos números y un carácter especial.")
    vpass = false;
  }else{
    $("#passid").text("Contraseña válida.")
    vpass = true;
  }

  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});

$("#RepId").keyup(function(){
  var password = $("#passId").val();
  var confirmarpass = $("#RepId").val();

  if(password == confirmarpass){
    $("#repId").text("Ambas contraseñas coinciden.");
    vcpass = true;
  }else{
    $("#prepId").text("Las contraseñas no coinciden.");
    vcpass = false;
  }

  if(vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass){
    $("#btnRegistrarId").attr("disabled", false);
  }else{
    $("#btnRegistrarId").attr("disabled", true);
  }
});



/*

validar contraseña y repetir contraseña
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
  });*/
