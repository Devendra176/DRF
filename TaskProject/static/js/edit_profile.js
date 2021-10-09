$(document).ready(function(){
$("#save_profile",).click(function (e) {
    e.preventDefault();
  var url =$(this).attr('href_url');
  let email_address=$('#email_address').val();
  let customer_name=$('#customer_name').val();
  let mobile_number=$('#mobile_number').val();
  let date_of_birth=$('#date_of_birth').val();
  let status=true;
  let csrf=window.CSRF_TOKEN;
  
  mydata={email_address:email_address,customer_name:customer_name,csrf:csrf,mobile_number:mobile_number,date_of_birth:date_of_birth,status:status}


    $.ajax({
      url: url,
      type: 'POST',
      data:mydata,
      dataType: 'json',
      success:function(data){ 
        if (data.status==1001){
          window.location.reload(true);
            }else if(data.status!=1001){
                window.location.reload(true);
            }else{
              console.log(" sever failed  ")
            }
          },
        });
   
  });
});


$(document).ready(function(){
  $("#save_profile_pic",).click(function (e) {
      e.preventDefault();
    var url =$(this).attr('href_url');
    formdata = new FormData();
    var imagepath=$('input[name=imagepath]')[0].files[0];
    let customer_id = $('#customer_id').val();
    let status=true;
    let csrf=window.CSRF_TOKEN;
    
    formdata.append("imagepath", imagepath);
    formdata.append("csrf", csrf);
    formdata.append("status", status);
    formdata.append("customer_id", customer_id);
      $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        data:formdata,
        processData: false,
        contentType: false,
        success:function(data){ 
          if (data.status==1001){
            window.location.reload(true);
              }else if(data.status!=1001){
                  window.location.reload(true);
              }else{
                console.log(" sever failed  ")
              }
            },
          });
     
    });
  });