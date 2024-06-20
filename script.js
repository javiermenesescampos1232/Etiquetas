// Función para mostrar la vista previa del logo seleccionado
document.getElementById('school-logo').onchange = function(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('logo-preview');
        output.src = reader.result;
        output.style.display = 'block';
    };
    reader.readAsDataURL(event.target.files[0]);
};

document.getElementById('label-form').onsubmit = function() {
    setTimeout(function() {
        window.print();
    }, 1000);  // Espera 1 segundo para asegurarse de que la imagen se haya cargado
};
function previewLogo(event, previewId) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById(previewId);
        output.src = reader.result;
        output.style.display = 'block';
    };
    reader.readAsDataURL(event.target.files[0]);
}
