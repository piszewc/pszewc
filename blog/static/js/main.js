$(document).ready(function () {
    $('#check_chances').on('click',function() {
        var sex = $( "#form_sex" ).val();
        var title = $("#form_title").val();
        var age = $("#form_age").val();
        var p_class = $("#form_class").val();
        var fare_band = $("#form_fband").val();
        var is_alone = $("#form_siblings").val();
        var embarked = $("#form_location").val();
        var age_class = age*p_class;

        var i = p_class+","+sex+","+age+","+fare_band+","+embarked+","+title+","+is_alone+","+age_class

        url = "http://127.0.0.1:8000/api/predict/?review="+i;
        window.open(url);
        
    });
});
