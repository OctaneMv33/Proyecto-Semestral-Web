var vnombre = false, vsnombre = true, vappaterno = false, vapmaterno = true, vmail = false, vrut = false, vtelefono = false, vpass = false, vcpass = false

$(document).ready(function () {
  $("#btnRegistrarId").attr('disabled', true)
});

/*------------ Validacion para registro -----------------*/

/*validar rut*/
$("#rutId, #dvrutId").keyup(function () {
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

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar P nombre*/
$("#PnomId").keyup(function () {
  var caracteres = $("#PnomId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#PnomId").val().length;

  if (largo < 3 || largo > 15) {
    $("#PnombreId").text("El nombre no puede ser menor a 3 caractéres o mayor a 15.");
    vnombre = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#PnombreId").text("Sólo puede ingresar letras");
    vnombre = false;
  } else {
    $("#PnombreId").text("Ingreso correcto");
    vnombre = true;
  }

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar S nombre*/
$("#SnomId").keyup(function () {
  var caracteres = $("#SnomId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#SnomId").val().length;
  if (largo == 0) {
    $("#SnombreId").text("No ingresará nada");
    vsnombre = true;
  } else if (largo < 3 || largo > 15) {
    $("#SnombreId").text("El nombre no puede ser menor a 3 caractéres o mayor a 15.");
    vsnombre = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#SnombreId").text("Sólo puede ingresar letras");
    vsnombre = false;
  } else {
    $("#SnombreId").text("Ingreso correcto");
    vsnombre = true;
  }

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar P apellido*/
$("#PapelId").keyup(function () {
  var caracteres = $("#PapelId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#PapelId").val().length;
  if (largo < 3 || largo > 15) {
    $("#PappellidoId").text("El apellido no puede ser menor a 3 caractéres o mayor a 15.");
    vappaterno = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#PappellidoId").text("Sólo puede ingresar letras");
    vappaterno = false;
  } else {
    $("#PappellidoId").text("Ingreso correcto");
    vappaterno = true;
  }

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar S apellido*/
$("#SapelId").keyup(function () {
  var caracteres = $("#SapelId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#SapelId").val().length;
  if (largo == 0) {
    $("#MappellidoId").text("No ingresará nada.");
    vapmaterno = true;
  } else if (largo < 3 || largo > 15) {
    $("#MappellidoId").text("El apellido no puede ser menor a 3 caractéres o mayor a 15.");
    vapmaterno = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#MappellidoId").text("Sólo puede ingresar letras");
    vapmaterno = false;
  } else {
    $("#MappellidoId").text("Ingreso correcto");
    vapmaterno = true;
  }

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar Email*/
$("#EmailId").keyup(function () {
  var patronCorreo = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
  var correo = $.trim($("#EmailId").val());
  if (correo === "") {
    $("#EId").text("Este campo no puede quedar vacío");
    vmail = false;
  } else if (!patronCorreo.test(correo)) {
    $("#EId").text("Formato de correo electrónico incorrecto");
    vmail = false;
  } else {
    $("#EId").text("Ingreso Correcto");
    vmail = true;
  }

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/*validar telefono*/
$("#TelId").keyup(function () {
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

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});


/*validar contraseña*/
$("#passId").keyup(function () {
  var password = $("#passId").val();
  var patronpass = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]+$/;
  var largopass = $("#passId").val().length;

  if (largopass < 8) {
    $("#passid").text("Contraseña muy corta. Al menos 8 caractéres.")
    vpass = false;
  } else if (!patronpass.test(password)) {
    $("#passid").text("Contraseña inválida. Asegúrate de incluir al menos una letra mayúscula, dos números y un carácter especial.")
    vpass = false;
  } else {
    $("#passid").text("Contraseña válida.")
    vpass = true;
  }

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});

$("#RepId").keyup(function () {
  var password = $("#passId").val();
  var confirmarpass = $("#RepId").val();

  if (password == confirmarpass) {
    $("#repId").text("Ambas contraseñas coinciden.");
    vcpass = true;
  } else {
    $("#prepId").text("Las contraseñas no coinciden.");
    vcpass = false;
  }

  if (vnombre && vsnombre && vappaterno && vapmaterno && vmail && vrut && vtelefono && vpass && vcpass) {
    $("#btnRegistrarId").attr("disabled", false);
  } else {
    $("#btnRegistrarId").attr("disabled", true);
  }
});

/* ------------------- Validación de Formulario de Contacto ---------------------*/
$(document).ready(function () {
  $("#enviarContactoId").attr('disabled', true);
});

/* validar email */
$("#EmailId").keyup(function () {
  var patronCorreo = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
  var correo = $.trim($("#EmailId").val());
  if (correo === "") {
    $("#EId").text("Este campo no puede quedar vacío");
    vmail = false;
  } else if (!patronCorreo.test(correo)) {
    $("#EId").text("Formato de correo electrónico incorrecto");
    vmail = false;
  } else {
    $("#EId").text("Ingreso Correcto");
    vmail = true;
  }

  if (vmail && vtelefono) {
    $("#enviarContactoId").attr("disabled", false);
  } else {
    $("#enviarContactoId").attr("disabled", true);
  }
});

/* validar telefono */
$("#TelId").keyup(function () {
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

  if (vmail && vtelefono) {
    $("#enviarContactoId").attr("disabled", false);
  } else {
    $("#enviarContactoId").attr("disabled", true);
  }
});

/* -------------- Validacion de Formulario de solicitud -------------- */
var vfecha = false, vdescripcion = false
/* Deshabilitando botón */
$(document).ready(function () {
  $("#enviarId").attr('disabled', true)
});

/* Validando Fecha válida */

$("#fechaId").change(function () {
  var fecha = $("#fechaId").val();
  const dia = new Date();
  dia.setDate(dia.getDate() - 1);
  const fecha2 = new Date(fecha);

  if (fecha2 >= dia) {
    $("#mensajeFechaId").text("Ingreso correcto");
    vfecha = true;
  } else {
    $("#mensajeFechaId").text("Debes seleccionar una fecha adecuada");
    vfecha = false;
  }

  if (vfecha && vdescripcion) {
    $("#enviarId").attr('disabled', false)
  } else {
    $("#enviarId").attr('disabled', true)
  }
});


/* Validando descripción de mínimo 20 caractéres y máximo 500*/
$("#descripcionId").keyup(function () {
  var largo = $("#descripcionId").val().length

  if (largo < 20 || largo > 500) {
    $("#mensajeDescripcionId").text("Tiene que ingresar una descripción entre 20 y 500 caracteres")
    vdescripcion = false
  } else {
    $("#mensajeDescripcionId").text("Descripción mínima completada")
    vdescripcion = true
  }

  if (vfecha && vdescripcion) {
    $("#enviarId").attr('disabled', false)
  } else {
    $("#enviarId").attr('disabled', true)
  }
});

/* -------------- Validacion de Formulario de Crear Trabajo/Publicación -------------- */
var vdescripcion = false, vtitulo = false, vdiagnostico = false, vcategoriatrabajo = false, vfoto = false
/* Deshabilitando botón */
$(document).ready(function () {
  $("#publicarId").attr('disabled', true)
});

/* Validando título del/la trabajo/publicación */
$("#tituloId").keyup(function () {
  var largo = $("#tituloId").val().length
  var patroncaracteres = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]+$/
  var caracteres = $("#tituloId").val()

  if (largo < 20 || largo > 80) {
    $("#mensajeTituloId").text('El largo mínimo es de 20 caractéres y el máximo de 80')
    vtitulo = false
  } else if (!patroncaracteres.test(caracteres)) {
    $("#mensajeTituloId").text('Sólo puede ingresar letras y números')
    vtitulo = false
  } else {
    $("#mensajeTituloId").text('Ingreso correcto')
    vtitulo = true
  }

  if (vdescripcion && vtitulo && vdiagnostico && vcategoriatrabajo && vfoto) {
    $("#publicarId").attr('disabled', false)
  } else {
    $("#publicarId").attr('disabled', true)
  }
});

/* Validando diagnóstico de mínimo 50 caractéres y máximo 500*/
$("#diagId").keyup(function () {
  var largo = $("#diagId").val().length

  if (largo < 50 || largo > 500) {
    $("#mensajeDiagnosticoTrabajoId").text("Tiene que ingresar un diagnóstico entre 50 y 500 caracteres")
    vdiagnostico = false
  } else {
    $("#mensajeDiagnosticoTrabajoId").text("Diagnóstico mínimo completado")
    vdiagnostico = true
  }

  if (vdescripcion && vtitulo && vdiagnostico && vcategoriatrabajo && vfoto) {
    $("#publicarId").attr('disabled', false)
  } else {
    $("#publicarId").attr('disabled', true)
  }
});

/* Validando descripción de mínimo 100 caractéres y máximo 1000*/
$("#DesId").keyup(function () {
  var largo = $("#DesId").val().length

  if (largo < 100 || largo > 1000) {
    $("#mensajeDescripcionTrabajoId").text("Tiene que ingresar una descripción entre 100 y 1000 caracteres")
    vdescripcion = false
  } else {
    $("#mensajeDescripcionTrabajoId").text("Descripción mínima completada")
    vdescripcion = true
  }

  if (vdescripcion && vtitulo && vdiagnostico && vcategoriatrabajo && vfoto) {
    $("#publicarId").attr('disabled', false)
  } else {
    $("#publicarId").attr('disabled', true)
  }
});

/* Validando cantidad de fotos */
$('#formFile').on('change', function () {
  var files = $(this)[0].files;
  if (files.length > 6) {
    $("#mensajeFotosTrabajoId").text('Sólo se permiten como máximo 6 fotos')
    $(this).val('');
    vfoto = false
  } else {
    $("#mensajeFotosTrabajoId").text('Ingreso correcto')
    vfoto = true
  }

  if (vdescripcion && vtitulo && vdiagnostico && vcategoriatrabajo && vfoto) {
    $("#publicarId").attr('disabled', false)
  } else {
    $("#publicarId").attr('disabled', true)
  }
});

/* Validando que se elija una categoría de trabajo */
$("#categoriaId").change(function () {
  if (this.value == "") {
    $("#mensajeCategoriaTrabajoId").text('Debe elegir una categoría para el trabajo')
    vcategoriatrabajo = true
  } else {
    $("#mensajeCategoriaTrabajoId").text('Ingreso correcto')
    vcategoriatrabajo = true
  }

  if (vdescripcion && vtitulo && vdiagnostico && vcategoriatrabajo && vfoto) {
    $("#publicarId").attr('disabled', false)
  } else {
    $("#publicarId").attr('disabled', true)
  }
});

/*Validando material */
var grupo = "2";
var materiales = [];

$(document).ready(function () {
  cargarMaterialesSeleccionados();

  $("#agregarID").click(function () {
    var sel = $("#MaterialesID :selected");
    var val = $(sel).val();
    var text = $(sel).text();
    var idPadre = sel.parent().prop("id");
    grupo = "#" + idPadre.substr(0, idPadre.length - 1) + "2";
    $(grupo).append('<option value="' + val + '">' + text + '</option>');
    materiales.push(val);
    actualizarOcultoID();
    $(sel).remove();
  });

  $("#eliminarID").click(function () {
    var sel = $("#eliminadoID :selected");
    var val = $(sel).val();
    var text = $(sel).text();
    var idPadre = sel.parent().prop("id");
    grupo = "#" + idPadre.substr(0, idPadre.length - 1) + "1";
    $(grupo).append('<option value="' + val + '">' + text + '</option>');

    var index = materiales.indexOf(val);
    if (index > -1) {
      materiales.splice(index, 1);
    }
    actualizarOcultoID();
    $(sel).remove();
  });
});

function cargarMaterialesSeleccionados() {
  var materialesSeleccionados = [];
  $("#eliminadoID option").each(function () {
    materialesSeleccionados.push($(this).val());
  });
  materiales = materialesSeleccionados.filter(function (material) {
    return material.trim() !== "";
  });
  actualizarOcultoID();
}

function actualizarOcultoID() {
  $("#ocultoID").val(materiales.join(","));
}

var vmotivo = false, vestado = false
/* Validaciones Revision de Trabajo */
$(document).ready(function () {
  $("#btnRevisionId").attr('disabled', true)
  $("#motivoId").attr('disabled', true)
});

$("#motivoId").keyup(function () {
  cantidadCaracteres = $("#motivoId").val().length
  if (cantidadCaracteres < 50 || cantidadCaracteres > 500) {
    $("#mensajeMotivoId").text('El motivo de rechazo debe tener al menos 50 caracteres de largo y máximo 500');
    vmotivo = false
  } else {
    $("#mensajeMotivoId").text('Ingreso correcto');
    vmotivo = true
    vestado = true
  }

  if ((vmotivo && vestado) || vestado) {
    $("#btnRevisionId").attr('disabled', false)
  } else {
    $("#btnRevisionId").attr('disabled', true)
  }
});

$("#estadoRevisionId").change(function () {
  opcion = $("#estadoRevisionId").val();
  fechaRevision = new Date()
  var fechaRevisionFormateada = fechaRevision.toISOString().slice(0, 19).replace('T', ' ');

  if (opcion === "") {
    $("#mensajeEstadoMotivoId").text('Debe seleccionar un estado de revisión.')
    vestado = false
  } else if (opcion === "20") {
    $("#mensajeEstadoMotivoId").text('Escriba el motivo de rechazo.')
    vestado = false
    $("#fechaRevisionId").val(fechaRevisionFormateada)
    console.log($("#fechaRevisionId").val())
    $("#motivoId").attr('disabled', false)
  } else {
    $("#mensajeEstadoMotivoId").text('Ingreso correcto')
    $("#mensajeMotivoId").text('');
    $("#motivoId").val("");
    $("#fechaRevisionId").val(fechaRevisionFormateada)
    console.log($("#fechaRevisionId").val())
    vestado = true
    $("#motivoId").attr('disabled', true)
  }

  if ((vmotivo && vestado) || vestado) {
    $("#btnRevisionId").attr('disabled', false)
  } else {
    $("#btnRevisionId").attr('disabled', true)
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var checkboxCambiarImagenes = document.getElementById("checkbox_cambiar_imagenes");
  var inputImagenes = document.getElementById("input_imagenes");

  checkboxCambiarImagenes.addEventListener("change", function () {
    if (checkboxCambiarImagenes.checked) {
      inputImagenes.style.display = "block";
    } else {
      inputImagenes.style.display = "none";
    }
  });
});

/* Mostrar mensaje por pantalla o poner una alerta visual en el ver publicaciones rechazadas, o ver estado publicación 
   cuando le revisen el trabajo para cumplir con un punto del requerimiento 11
*/

/* -------------- Validacion de Formulario de Editar Trabajo/Publicación -------------- */
var vdescripcion = false, vtitulo = false, vdiagnostico = false, vfoto = true

/* Validando título del/la trabajo/publicación */
$(document).ready(function () {
  var largo = $("#tituloId").val().length
  var patroncaracteres = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]+$/
  var caracteres = $("#tituloId").val()

  if (largo < 20 || largo > 80) {
    $("#mensajeTituloId").text('El largo mínimo es de 20 caractéres y el máximo de 80')
    vtitulo = false
  } else if (!patroncaracteres.test(caracteres)) {
    $("#mensajeTituloId").text('Sólo puede ingresar letras y números')
    vtitulo = false
  } else {
    $("#mensajeTituloId").text('Ingreso correcto')
    vtitulo = true
  }
  $("#tituloId").keyup(function () {
    var largo = $("#tituloId").val().length
    var patroncaracteres = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]+$/
    var caracteres = $("#tituloId").val()

    if (largo < 20 || largo > 80) {
      $("#mensajeTituloId").text('El largo mínimo es de 20 caractéres y el máximo de 80')
      vtitulo = false
    } else if (!patroncaracteres.test(caracteres)) {
      $("#mensajeTituloId").text('Sólo puede ingresar letras y números')
      vtitulo = false
    } else {
      $("#mensajeTituloId").text('Ingreso correcto')
      vtitulo = true
    }

    if (vdescripcion && vtitulo && vdiagnostico && vfoto) {
      $("#Editarid").attr('disabled', false)
    } else {
      $("#Editarid").attr('disabled', true)
    }
  });
});

/* Validando diagnóstico de mínimo 50 caractéres y máximo 500*/
$(document).ready(function () {
  var largo = $("#diagId").val().length

  if (largo < 50 || largo > 500) {
    $("#mensajeDiagnosticoTrabajoId").text("Tiene que ingresar un diagnóstico entre 50 y 500 caracteres")
    vdiagnostico = false
  } else {
    $("#mensajeDiagnosticoTrabajoId").text("Diagnóstico mínimo completado")
    vdiagnostico = true
  }
  $("#diagId").keyup(function () {
    var largo = $("#diagId").val().length

    if (largo < 50 || largo > 500) {
      $("#mensajeDiagnosticoTrabajoId").text("Tiene que ingresar un diagnóstico entre 50 y 500 caracteres")
      vdiagnostico = false
    } else {
      $("#mensajeDiagnosticoTrabajoId").text("Diagnóstico mínimo completado")
      vdiagnostico = true
    }

    if (vdescripcion && vtitulo && vdiagnostico && vfoto) {
      $("#Editarid").attr('disabled', false)
    } else {
      $("#Editarid").attr('disabled', true)
    }
  });
});

/* Validando descripción de mínimo 100 caractéres y máximo 1000*/
$(document).ready(function () {
  var largo = $("#DesId").val().length

  if (largo < 100 || largo > 1000) {
    $("#mensajeDescripcionTrabajoId").text("Tiene que ingresar una descripción entre 100 y 1000 caracteres")
    vdescripcion = false
  } else {
    $("#mensajeDescripcionTrabajoId").text("Descripción mínima completada")
    vdescripcion = true
  }
  $("#DesId").keyup(function () {
    var largo = $("#DesId").val().length

    if (largo < 100 || largo > 1000) {
      $("#mensajeDescripcionTrabajoId").text("Tiene que ingresar una descripción entre 100 y 1000 caracteres")
      vdescripcion = false
    } else {
      $("#mensajeDescripcionTrabajoId").text("Descripción mínima completada")
      vdescripcion = true
    }

    if (vdescripcion && vtitulo && vdiagnostico && vfoto) {
      $("#Editarid").attr('disabled', false)
    } else {
      $("#Editarid").attr('disabled', true)
    }
  });
});

/* Validando cantidad de fotos */
$('#input_imagenes').on('change', function () {
  var files = $(this)[0].files;
  if (files.length > 6) {
    $("#mensajeFotosTrabajoId").text('Sólo se permiten como máximo 6 fotos')
    $(this).val('');
    vfoto = false
  } else {
    $("#mensajeFotosTrabajoId").text('Ingreso correcto')
    vfoto = true
  }

  if (vdescripcion && vtitulo && vdiagnostico && vfoto) {
    $("#Editarid").attr('disabled', false)
  } else {
    $("#Editarid").attr('disabled', true)
  }
});
