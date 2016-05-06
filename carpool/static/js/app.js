$(document).ready(function() {

    $('select').material_select();

    $('#mast_head').delay(600).fadeIn( "slow" );
    $('#login_btn').delay(1200).fadeIn( "slow" );

    $("#login_video").YTPlayer();

    $("input[name='tipo']").val('irregular')

    $("input[name='tipo_show']").change(function(e) {

        if(e.currentTarget.checked){
            $("#fecha").fadeOut( "slow" );
            $("#dias").delay(700).fadeIn( "slow" );
            $("input[name='tipo']").val('regular')
        }else{
            $("#dias").fadeOut( "slow" );
            $("#fecha").delay(700).fadeIn( "slow" );
            $("input[name='tipo']").val('irregular')
        }
    });

     $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year
        monthsFull: ['Enero', 'Febrero', 'Mazo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        weekdaysFull: ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
        weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
        showMonthsShort: false,
        today: 'Hoy',
        clear: 'Borrar',
        close: 'Cerrar',
        labelMonthNext: 'Siguiente mes',
        labelMonthPrev: 'Mes anterior',
        labelMonthSelect: 'Selecciona un mex',
        labelYearSelect: 'Selecciona un año',
        min: new Date(),
        formatSubmit: 'dd/mm/yyyy',
        hiddenName: true
      });


    $("input[name='tipo_show']").change(function(e) {

        if(e.currentTarget.checked){
            $("#fecha").fadeOut( "slow" );
            $("#dias").delay(700).fadeIn( "slow" );
            $("input[name='tipo']").val('regular')
        }else{
            $("#dias").fadeOut( "slow" );
            $("#fecha").delay(700).fadeIn( "slow" );
            $("input[name='tipo']").val('irregular')
        }
    });

    $(".button-collapse").sideNav();

  });