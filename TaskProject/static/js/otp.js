
$(document).ready(function(){
  $("#login_button_otp",).click(function (e) {
      e.preventDefault();
    var url =$(this).attr('href_url');
    let Otp=$('#Otp').val();
    let csrf=window.CSRF_TOKEN;
  
    mydata={Otp:Otp,csrf:csrf};
    // console.log(mydata);
    if (Otp==""){
      console.log("Please enter Otp ")
    }
  if(Otp){
          data = mydata;
    }
  
      $.ajax({
        url: url,
        type: 'POST',
        data:data,
        dataType: 'json',
        success:function(data){ 
          if(data.status==1001){
            
            window.location.href=data.url;
            // console.log(localStorage.getItem("url"));
          }else if(data.status==400){
              $('#login_error').show();
              // $('#login_error').text(data.msg)
          }
          },
        
     
    });
  });
  });
  