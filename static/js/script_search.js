
var item = document.getElementById('id_departamento');
var itemMun = document.getElementById('id_municipio');

item.addEventListener('change', (event) => {
  var baseUrl = 'https://bestpreicfes.com/lista-colegios/depts/';
  var deptpk = event.target.value;
  var url = baseUrl + deptpk;
  //var cad = '<option value="volvo">Volvo</option>';
  var cad = document.createElement('option');
  cad.setAttribute('name', 'Guateque');
  cad.innerText = 'Guateque';
  fetch(url)
    .then(response => response.json()) // converts the response to JSON
    .then(data => {
      //console.log(data['municipio_set']);
      var lista = data['municipio_set'];
      addOption(lista, itemMun);
      //itemMun.appendChild(cad);
      //console.log(cad);
      // do something (like update the DOM with the data)
  });
  console.log(deptpk);
});

function addOption(lista, nodo) {
  nodo.innerHTML = '';
  for (let mun of lista) {
    var cad = document.createElement('option');
    cad.setAttribute('name', mun);
    cad.innerText = mun;
    nodo.appendChild(cad);
  }
}
