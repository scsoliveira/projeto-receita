function ExcluirIngrediente(id){
    swal({
      title: "Você tem certeza?",
      text: "Uma vez deletado, não será possível recupera-lo!",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {

        $.ajax({
          data:{
            id : id
          },
          type : 'POST',
          url : '/GerenciarIngrediente/Excluir'
        })
        .done(function(data){
  
          if(data.error){
            swal({
              title: "Atenção!",
              text: "Erro ao excluir ingrediente",
              icon: "error"
            })
          }else{
            swal("Poof!", "O ingrediente foi deletado com sucesso", "success").then(value =>{
              console.log(data.nome)
              location.reload()
            });
            
          }
  
        });
      } 
    });
}

function EditarIngrediente(id){
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

      $.ajax({
        data:{
          id : id,
          nome: $('#txtNome').val()
        },
        type : 'POST',
        url : '/GerenciarIngrediente/Editar'
      })
      .done(function(data){

        if(data.error){
          swal({
            title: "Atenção!",
            text: "Erro ao editar ingrediente",
            icon: "error"
          })
        }else{
          var txt = "Seu ingrediente agora se chama: "+ data.nome;
          swal("Salvo!", txt, "success").then(value =>{
            location.reload()
          });
          
        }

      });
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

      $.ajax({
        data:{
          nome : $('#txtNome').val()
        },
        type : 'POST',
        url : '/GerenciarIngrediente/Cadastrar'
      })
      .done(function(data){

        if(data.error){
          swal({
            title: "Atenção!",
            text: "Erro ao inserir ingrediente",
            icon: "error"
          })
        }else{
          var txt = data.nome + " adicionado com sucesso";
          swal("Adicionado!", txt, "success").then(value =>{
            location.reload()
          });
          
        }

      });
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

function LimparCampos(){
  document.getElementById('txtQtd').value='';
  document.getElementById('txtNome').value='';

  var textarea = document.getElementById('txtListaI')
  var textarea2 = document.getElementById('txtListaP')
  var textarea3 = document.getElementById('txtListaI2')

  textarea.value = "";
  textarea2.value = "";
  textarea3.value = "";
}

function AdicionarIngredienteReceita(){
  var textarea = document.getElementById('txtListaI');
  if(textarea.value == "")
    var txt = $('#txtQtd').val() + " - " + $('#slcIngrediente option:selected').text() + ";";
  else
    var txt = "\n"+$('#txtQtd').val() + " - " + $('#slcIngrediente option:selected').text() + ";";

  textarea.value += txt;

  //PARA PEGAR NO BANCO

  var textarea2 = document.getElementById('txtListaI2');
  if(textarea2.value == "")
    var txt = $('#txtQtd').val() + "-" + $('#slcIngrediente').val() + ";";
  else
    var txt = "\n"+$('#txtQtd').val() + "-" + $('#slcIngrediente').val() + ";";

  document.getElementById('txtQtd').value='';
  
  textarea2.value += txt;

}

function SalvarReceita(){

  var vingredientes = $("#txtListaI2").val();
  vingredientes = vingredientes.replace("\n", "");
  vingredientes = vingredientes.replace(" ", "");

  var lIngrediente = vingredientes.split(";");
  lIngrediente.pop();

  console.log(lIngrediente)

  $.ajax({
    data:{
      nome : $('#txtNome').val(),
      modo : $('#txtListaP').val(),
      ingredientes : lIngrediente
    },
    type : 'POST',
    url : '/GerenciarReceitas/Cadastrar'
  })
  .done(function(data){

    if(data.error){
      swal({
        title: "Atenção!",
        text: "Erro ao inserir receita",
        icon: "error"
      })
    }else{
      
      swal({
        title:"Salvo!",
        text: "Nova receita registrada!",
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

  });
}

function ExcluirReceita(id){
  swal({
    title: "Você tem certeza?",
    text: "Uma vez deletado, não será possível recupera-la!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {

      $.ajax({
        data:{
          id : id
        },
        type : 'POST',
        url : '/GerenciarReceita/Excluir'
      })
      .done(function(data){

        if(data.error){
          swal({
            title: "Atenção!",
            text: "Erro ao excluir receita",
            icon: "error"
          })
        }else{
          swal("Poof!", "A receita foi deletado com sucesso", "success").then(value =>{
            location.reload()
          });
          
        }

      });
    } 
  });
}