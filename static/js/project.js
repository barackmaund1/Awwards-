$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
      form = $("form")
  
      $.ajax({
        'url':'/ajax/projectsearch/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_project search').val('')
     
    }) // End of submit event
  
  }) // End of document ready function