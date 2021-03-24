function ExcluirIngrediente(){
    swal({
      title: "Você tem certeza?",
      text: "Uma vez deletado, não será possível recupera-lo!",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {
        swal("Poof! O ingrediente foi deletado com sucesso!", {
          icon: "success",
        });
      } 
    });
}

function EditarIngrediente(){
  swal("Digite o novo nome do ingrediente:", {
    content: {
      element: "input",
      attributes:{
        type: "input",
        id: "txtNome"
      }
    },
    buttons: {
      cancel: "Cancelar",
      confirm: true
    },
  })
  .then((value) => {

    if(value){
      var Nome = document.getElementById("txtNome").value;
      var txt = "Seu ingrediente agora se chama: "+ Nome;
      if(Nome != "")
        swal("Salvo!", txt, "success");
    }
    
  });
}

function AdicionarIngrediente(){
  swal("Digite o nome do ingrediente:", {
    content: {
      element: "input",
      attributes:{
        type: "input",
        id: "txtNome"
      }
    },
    buttons: {
      cancel: "Cancelar",
      confirm: true
    },
  })
  .then((value) => {

    if(value){
      var Nome = document.getElementById("txtNome").value;
      var txt = Nome + " adicionado com sucesso";
      if(Nome != "")
        swal("Adicionado!", txt, "success");
    }
    
  });
}

function AdicionarListaIngrediente(){
  swal({
      title:"Lista Adicionada!",
      icon: "success",
      closeOnClickOutside: false,
      buttons:{
          sim:{
              text:"Confirmar",
              value: true
          }
      },
  }).then(value => {
    location.reload();
  })
}

function AdicionarCampoIngrediente(){
    const dvIngredientes = document.getElementById("dvIngredientes");
  
    let campo = document.createElement("input");
    campo.name = "ingredientes[]";
    campo.placeholder = "Ex: Sal";
    dvIngredientes.appendChild(campo);
}