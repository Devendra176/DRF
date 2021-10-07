
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
      if (Otp){
        data=mydata;
      }
    else{
    
        $.ajax({
          url: url,
          type: 'POST',
          data: mydata,
          dataType: 'json',
          success:function(data){ 
            console.log(data);
            if(data.status==1003){
              
            //   window.location.href=data.url;
              console.log(data);
            }else if(data.status!=1003){
              console.log(data);
                $('#login_error').show();
                // $('#login_error').text(data.msg)
            }
            },
          
       
      });
    }
    });
    });
    