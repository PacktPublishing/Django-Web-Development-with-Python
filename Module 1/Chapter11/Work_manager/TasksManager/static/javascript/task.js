function task_delete(id, url){
  $.ajax({
    type: 'POST', 
    // Here, we define the used method to send data to the Django views. Other values are possible as POST, GET, and other HTTP request methods.
    url: url, 
    // This line is used to specify the URL that will process the request.
    data: {task: id}, 
    // The data property is used to define the data that will be sent with the AJAX request.
    dataType:'json', 
    // This line defines the type of data that we are expecting back from the server. We do not necessarily need JSON in this example, but when the response is more complete, we use this kind of data type.
    success: task_delete_confirm,
    // The success property allows to define a function that will be executed when the AJAX request works. This function receives as a parameter the AJAX response.
    error: function () {alert('AJAX error.');} 
    // The error property can define a function when the AJAX request does not work. We defined in the previous code an anonymous function that displays AJAX error to the user.
  });
}
function task_delete_confirm(response) {
  task_id = JSON.parse(response); 
  // This line is in the function that receives the AJAX response when the request was successful. This line allows deserializing the JSON response returned by Django views.
  if (task_id>0) {
    $('#task_'+task_id).remove(); 
    // This line will delete the <tr> tag containing the task we have just removed
  }
  else {
    alert('Error');
  }
}
